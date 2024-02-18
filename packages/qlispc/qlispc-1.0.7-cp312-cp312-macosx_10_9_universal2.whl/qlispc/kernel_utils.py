import re
from typing import Any, Iterable

import dill
import numpy as np
from waveforms.dicttree import NOTSET
from waveforms.waveform import Waveform, WaveVStack, step

from .base import Capture
from .commands import COMMAND, SYNC, WRITE
from .config import Config
from .library import Library


def qcompile(circuit: str | list | bytes,
             lib: Library,
             cfg: Config,
             signal,
             shots: int,
             context: dict,
             arch,
             align_right=False,
             waveform_length=98e-6):
    from qlispc import compile, get_arch

    if isinstance(circuit, bytes):
        circuit = dill.loads(circuit)

    code = compile(circuit, lib=lib, cfg=cfg)
    code.signal = signal
    code.shots = shots
    code.arch = arch

    if align_right:
        delay = waveform_length - code.end

        code.waveforms = {k: v >> delay for k, v in code.waveforms.items()}
        code.measures = {
            k:
            Capture(v.qubit, v.cbit, v.time + delay, v.signal, v.params,
                    v.hardware, v.shift + delay)
            for k, v in code.measures.items()
        }

    return code, get_arch(code.arch).assembly_code(code, context)


def is_feedable(cmd):
    if isinstance(cmd, WRITE):
        if cmd.address.startswith('gate.'):
            return False
        if re.match(r'[QCM]\d+\..+', cmd.address) and not re.match(
                r'[QCM]\d+\.(setting|waveform)\..+', cmd.address):
            return False
    return True


_window = step(0) << 1e-3


def _eq(a, b):
    if isinstance(a, WaveVStack) or isinstance(b, WaveVStack):
        return False
    if isinstance(a, Waveform) and isinstance(b, Waveform):
        return (a * _window) == (b * _window)
    try:
        return a == b
    except:
        return False


def pre_feed(
    cmds: list[COMMAND],
    state_caches: dict[str, Any] | None = None,
    active_suffixs: Iterable[str] = (),
    active_prefixs: Iterable[str] = ()
) -> dict[str, list[tuple[str, str, Any, str]]]:
    """format data required by feed api of quark

    Args:
        cmds (list): commands to be executed
    """
    commands = []

    writes = {}
    updates = {}
    others = []

    for cmd in cmds:
        if is_feedable(cmd):
            if isinstance(cmd, WRITE):
                if (state_caches is not None and cmd.address in state_caches
                        and not cmd.address.startswith(tuple(active_prefixs))
                        and not cmd.address.endswith(tuple(active_suffixs))):
                    try:
                        if _eq(state_caches[cmd.address], cmd.value):
                            continue
                    except:
                        print(cmd.address)
                        print(cmd.value.bounds)
                        print(cmd.value.seq)
                        print()
                        print(state_caches[cmd.address].bounds)
                        print(state_caches[cmd.address].seq)
                        raise
                state_caches[cmd.address] = cmd.value
                if not (isinstance(cmd.value, tuple)
                        and cmd.value[0] is NOTSET):
                    writes[cmd.address] = (type(cmd).__name__, cmd.value)
            # elif isinstance(cmd, SYNC):
            #     commands.extend(list(writes.items()))
            #     writes = {}
            #     commands.extend(others)
            #     others = []
            #     # commands.append(
            #     #     (cmd.address, (type(cmd).__name__, cmd.value)))
            else:
                others.append((cmd.address, (type(cmd).__name__, cmd.value)))
        else:
            updates[cmd.address] = ('UPDATE', cmd.value)
    commands.extend(list(writes.items()))
    commands.extend(others)

    if len(commands) == 0:
        raise ValueError('No commands to be executed')

    # cmds = {'INIT': [], 'WRITE': [], 'TRIG': [], 'READ': []}
    cmds = {'WRITE': [], 'TRIG': [], 'READ': []}

    # for address, (cmd, value) in updates.items():
    #     cmds['INIT'].append((cmd, address, value, ''))

    for address, (cmd, value) in commands:
        cmds[cmd].append((cmd, address, value, ''))
    """
        cmds: dict
            in the form of {
                'INIT': [('UPDATE', address, value, ''), ...],
                'step1': [('WRITE', address, value, ''), ...],
                'step2': [('WAIT', '', delay, '')],
                'step3': [('TRIG', address, 0, ''), ...],
                ...
                'READ': [('READ', address, 0, ''), ...]
            }
        """
    return cmds


def get_raw_channel_info(address: str, mapping: dict[str, str],
                         cfg: Config) -> str | dict | None:
    for k, v in mapping.items():
        if address.endswith(k):
            break
    else:
        return address

    prefix = address[:-len(k)]
    channel_type, property = v.split('.')
    config = cfg.query(prefix)
    channel = config['channel'][channel_type]
    if channel is None:
        return None
    calibration = config['calibration'][channel_type]
    if not isinstance(calibration, dict):
        calibration = {}
    sample_rate = cfg.query('dev.' + channel.split('.')[0] + '.srate')
    if not isinstance(sample_rate, (int, float)):
        sample_rate = None
    return {
        'channel': channel,
        'property': property,
        'calibration': calibration,
        'sample_rate': sample_rate,
        'LEN': config['waveform'].get('LEN', 99e-6)
    }


def get_all_channels(cfg):
    d = cfg.export()
    mapping = {}
    ch_types = set()
    for k, v in d['etc']['mapping'].items():
        mapping['.' + '.'.join(k.split('_'))] = v
        if k.startswith('waveform_'):
            ch_types.add(k.split('_')[-1])
    channels = set()
    for k, v in d.items():
        if isinstance(v, dict) and 'channel' in v and 'waveform' in v:
            for ch in ch_types:
                try:
                    info = get_raw_channel_info(f'{k}.waveform.{ch}', mapping,
                                                cfg)
                    if isinstance(info, dict):
                        ins = info['channel'].split('.')[0]
                        if ins in d['dev']:
                            channels.add(
                                cfg._map_repetitive_channel(
                                    f'{k}.waveform.{ch}'))
                except:
                    pass
    return channels


def sample_waveform(waveform,
                    calibration,
                    sample_rate,
                    start=0,
                    stop=100e-6,
                    support_waveform_object=False,
                    with_x=False):
    """
    Sample a waveform with calibration parameters.

    Parameters
    ----------
    waveform : Waveform
        The waveform to be sampled.
    calibration : dict
        Calibration parameters. It should contain 'delay' and 'distortion'.
        Example:
        ```
            {
                'delay': 0.0,
                'distortion': {
                    'decay': [(0.1, 1e-6), (0.2, 2e-6)]
                }
            }
        ```
        'decay' is a list of (amplitude, decay time) or
                (amplitude list, decay time list) pairs.
    sample_rate : int | float
        Sample rate.
    start : int | float
        Start time of the sampled waveform.
    stop : int | float
        Stop time of the sampled waveform.
    support_waveform_object : bool
        Whether to return a Waveform object. Some AWG drivers support sending
        Waveform object rather than ndarray.
    with_x : bool
        Whether to return the x axis (used for plotting).
    """
    from waveforms.math.signal import (correct_reflection, exp_decay_filter,
                                       predistort)

    waveform >>= calibration.get('delay', 0)
    waveform.start = start
    waveform.stop = stop
    waveform.sample_rate = sample_rate

    if support_waveform_object:
        return waveform

    distortion_params = calibration.get('distortion', {})
    if not isinstance(distortion_params, dict):
        distortion_params = {}

    points = waveform.sample()

    filters = []
    ker = None
    if 'decay' in distortion_params and isinstance(distortion_params['decay'],
                                                   list):
        for amp, tau in distortion_params.get('decay', []):
            a, b = exp_decay_filter(amp, tau, sample_rate)
            filters.append((b, a))

    length = len(points)
    if length > 0:
        last = points[-1]
        try:
            points = predistort(points, filters, ker, initial=last)
        except:
            points = np.hstack([np.full((length, ), last), points])
            points = predistort(points, filters, ker)[length:]
        points[-1] = last

    if with_x:
        return np.linspace(start, stop, len(points), endpoint=False), points
    else:
        return points


def try_to_call(x, args, kwds):
    from waveforms.scan.base import _try_to_call

    return _try_to_call(x, args, kwds)
