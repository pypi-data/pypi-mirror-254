import re

from numpy import mod, pi, sign, sum
from waveforms.waveform import (cos, coshPulse, cosPulse, gaussian,
                                general_cosine, mixing, pi, sin, square, zero)
from waveforms.waveform_parser import wave_eval

from qlispc import Capture, Library, add_VZ_rule

EPS = 1e-9

lib = Library()


def extract_variable_and_index_if_match(s):
    pattern = r'^(\w+)\[(\d+)\]$'
    match = re.search(pattern, s)

    if match:
        name, index = match.groups()
        return (name, int(index))
    else:
        return (s, 0)


def _VZ_R(st, phaseList):
    (_, phi, *with_params), qubit = st
    return [(('R', mod(phi - phaseList[0],
                       2 * pi), *with_params), qubit)], phaseList


def _VZ_clear(st, phaseList):
    return [st], [0] * len(phaseList)


def _VZ_commutable(st, phaseList):
    return [st], phaseList


def _VZ_swap(st, phaseList):
    return [st], phaseList[::-1]


add_VZ_rule('R', _VZ_R)
add_VZ_rule('Pulse', _VZ_commutable)
add_VZ_rule('setBias', _VZ_commutable)


def get_frequency_phase(ctx, qubit, phi, level1, level2):
    freq = ctx.params.get('frequency', ctx.params.get('freq', 0.5))
    phi = mod(
        phi + ctx.phases_ext[qubit][level1] - ctx.phases_ext[qubit][level2],
        2 * pi)
    phi = phi if abs(level2 - level1) % 2 else phi - pi
    if phi > pi:
        phi -= 2 * pi
    phi = phi / (level2 - level1)

    return freq, phi


def DRAG(t, shape, width, plateau, eps, amp, alpha, beta, delta, freq, phase):
    from waveforms.waveform import drag

    if shape in ['hanning', 'cosPulse', 'CosPulse']:
        if beta == 0:
            block_freq = None
        else:
            block_freq = -1 / (2 * pi) / (beta / alpha)
        return (amp * alpha) * drag(freq, width, plateau, delta, block_freq,
                                    phase, t - width / 2 - plateau / 2)
    elif shape in ['coshPulse', 'CoshPulse']:
        pulse = coshPulse(width, plateau=plateau, eps=eps)
    else:
        pulse = gaussian(width, plateau=plateau)
    I, Q = mixing(amp * alpha * pulse,
                  phase=phase,
                  freq=delta,
                  DRAGScaling=beta / alpha)
    wav, _ = mixing(I >> t, Q >> t, freq=freq)
    return wav


def R(ctx, qubits, phi=0, level1=0, level2=1):
    qubit, = qubits

    freq, phase = get_frequency_phase(ctx, qubit, phi, level1, level2)

    amp = ctx.params.get('amp', 0.5)
    shape = ctx.params.get('shape', 'cosPulse')
    width = ctx.params.get('width', 5e-9)
    plateau = ctx.params.get('plateau', 0.0)
    buffer = ctx.params.get('buffer', 0)

    duration = width + plateau + buffer
    if amp != 0:
        alpha = ctx.params.get('alpha', 1)
        beta = ctx.params.get('beta', 0)
        delta = ctx.params.get('delta', 0)
        eps = ctx.params.get('eps', 1)
        channel = ctx.params.get('channel', 'RF')
        t = duration / 2 + ctx.time[qubit]

        if shape == 'S1':
            arg = ctx.params.get('arg', [-2.253, 0.977, 1.029])
            pulse = general_cosine(width, *arg) * sign(-sum(arg[::2]))
            I, Q = mixing(amp * alpha * pulse,
                          phase=phase,
                          freq=delta,
                          DRAGScaling=beta / alpha)
            wav, _ = mixing(I >> t, Q >> t, freq=freq)
        wav = DRAG(t, shape, width, plateau, eps, amp, alpha, beta, delta,
                   freq, phase)
        yield ('!play', wav), (channel, qubit)
    yield ('!add_time', duration), qubit


@lib.opaque('R')
def _R(ctx, qubits, phi=0):
    yield from R(ctx, qubits, phi, 0, 1)


@lib.opaque('R12')
def _R12(ctx, qubits, phi=0):
    yield from R(ctx, qubits, phi, 1, 2)


@lib.opaque('R23')
def _R23(ctx, qubits, phi=0):
    yield from R(ctx, qubits, phi, 2, 3)


@lib.opaque('P')
def P(ctx, qubits, phi):
    import numpy as np
    from qlisp.assembly import call_opaque

    phi += ctx.phases[qubits[0]]
    yield ('!set_phase', 0), qubits[0]
    x = 2 * np.pi * np.random.random()
    y = np.pi * np.random.randint(0, 2) + x

    call_opaque((('R', x), qubits), ctx, lib)
    call_opaque((('R', x), qubits), ctx, lib)
    call_opaque((('R', phi / 2 + y), qubits), ctx, lib)
    call_opaque((('R', phi / 2 + y), qubits), ctx, lib)


@lib.gate()
def U(q, theta, phi, lambda_):
    yield (('R', -lambda_), q)
    yield (('R', -pi - theta - lambda_), q)
    yield (('P', theta + phi + lambda_), q)


@lib.gate()
def u3(qubit, theta, phi, lambda_):
    yield (('U', theta, phi, lambda_), qubit)


@lib.gate()
def u2(qubit, phi, lambda_):
    yield (('U', pi / 2, phi, lambda_), qubit)


@lib.gate()
def u1(qubit, lambda_):
    yield (('P', lambda_), qubit)


@lib.gate()
def H(qubit):
    yield (('u2', 0, pi), qubit)


@lib.gate()
def I(q):
    yield (('u3', 0, 0, 0), q)


@lib.gate()
def X(q):
    yield (('u3', pi, 0, pi), q)


@lib.gate()
def Y(q):
    yield (('u3', pi, pi / 2, pi / 2), q)


@lib.gate()
def Z(q):
    yield (('u1', pi), q)


@lib.gate()
def S(q):
    yield (('u1', pi / 2), q)


@lib.gate(name='-S')
def Sdg(q):
    yield (('u1', -pi / 2), q)


@lib.gate()
def T(q):
    yield (('u1', pi / 4), q)


@lib.gate(name='-T')
def Tdg(q):
    yield (('u1', -pi / 4), q)


@lib.gate(name='X/2')
def sx(q):
    yield ('-S', q)
    yield ('H', q)
    yield ('-S', q)


@lib.gate(name='-X/2')
def sxdg(q):
    yield ('S', q)
    yield ('H', q)
    yield ('S', q)


@lib.gate(name='Y/2')
def sy(q):
    yield ('Z', q)
    yield ('H', q)


@lib.gate(name='-Y/2')
def sydg(q):
    yield ('H', q)
    yield ('Z', q)


@lib.gate()
def Rx(q, theta):
    yield (('u3', theta, -pi / 2, pi / 2), q)


@lib.gate()
def Ry(q, theta):
    yield (('u3', theta, 0, 0), q)


@lib.gate(name='W/2')
def W2(q):
    yield (('u3', pi / 2, -pi / 4, pi / 4), q)


@lib.gate(name='-W/2')
def W2(q):
    yield (('u3', -pi / 2, -pi / 4, pi / 4), q)


@lib.gate(name='V/2')
def W2(q):
    yield (('u3', pi / 2, -3 * pi / 4, 3 * pi / 4), q)


@lib.gate(name='-V/2')
def W2(q):
    yield (('u3', -pi / 2, -3 * pi / 4, 3 * pi / 4), q)


@lib.gate()
def Rz(q, phi):
    yield (('u1', phi), q)


@lib.gate(2)
def Cnot(qubits):
    c, t = qubits
    yield ('H', t)
    yield ('CZ', (c, t))
    yield ('H', t)


@lib.gate(2)
def crz(qubits, lambda_):
    c, t = qubits

    yield (('u1', lambda_ / 2), t)
    yield ('Cnot', (c, t))
    yield (('u1', -lambda_ / 2), t)
    yield ('Cnot', (c, t))


@lib.opaque('Delay')
def delay(ctx, qubits, time):
    qubit, = qubits
    yield ('!play', zero()), ('RF', qubit)
    yield ('!play', zero()), ('Z', qubit)
    yield ('!play', zero()), ('readoutLine.RF', qubit)
    yield ('!add_time', time), qubit


@lib.opaque('Barrier')
def barrier(ctx, qubits):
    time = max(ctx.time[qubit] for qubit in qubits)
    for qubit in qubits:
        yield ('!set_time', time), qubit


@lib.opaque('rfPulse')
def rfPulse(ctx, qubits, waveform):
    qubit, = qubits

    if isinstance(waveform, str):
        waveform = wave_eval(waveform)

    yield ('!play', waveform >> ctx.time[qubit]), ('RF', qubit)


@lib.opaque('fluxPulse')
def fluxPulse(ctx, qubits, waveform):
    qubit, = qubits

    if isinstance(waveform, str):
        waveform = wave_eval(waveform)

    yield ('!play', waveform >> ctx.time[qubit]), ('Z', qubit)


@lib.opaque('Pulse')
def Pulse(ctx, qubits, channel, waveform):

    if isinstance(waveform, str):
        waveform = wave_eval(waveform)

    t = max(ctx.time[qubit] for qubit in qubits)

    yield ('!play', waveform >> t), (channel, *qubits)


@lib.opaque('setBias')
def setBias(ctx, qubits, channel, bias, edge=0, buffer=0):
    if channel.startswith('coupler.') and len(qubits) == 2:
        qubits = sorted(qubits)
    yield ('!set_bias', (bias, edge, buffer)), (channel, *qubits)
    time = max(ctx.time[qubit] for qubit in qubits)
    for qubit in qubits:
        yield ('!set_time', time + buffer), qubit


@lib.opaque('Measure')
def measure(ctx, qubits, cbit=None):
    from waveforms import cos, exp, pi, step

    qubit, = qubits

    if cbit is None:
        if len(ctx.measures['result']) == 0:
            cbit = 0
        else:
            cbit = max(ctx.measures['result'].keys()) + 1

    if isinstance(cbit, int):
        cbit = ('result', cbit)
    elif isinstance(cbit, str):
        cbit = extract_variable_and_index_if_match(cbit)

    # lo = ctx.cfg._getReadoutADLO(qubit)
    amp = ctx.params['amp']
    duration = ctx.params['duration']
    frequency = ctx.params['frequency']
    bias = ctx.params.get('bias', None)
    signal = ctx.params.get('signal', 'state')
    ring_up_amp = ctx.params.get('ring_up_amp', amp)
    ring_up_time = ctx.params.get('ring_up_time', 50e-9)
    rsing_edge_time = ctx.params.get('rsing_edge_time', 5e-9)
    buffer = ctx.params.get('buffer', 0)
    space = ctx.params.get('space', 0)

    try:
        w = ctx.params['w']
        weight = None
    except:
        weight = ctx.params.get('weight',
                                f'square({duration}) >> {duration/2}')
        w = None

    t = ctx.time[qubit]

    # phi = 2 * np.pi * (lo - frequency) * t

    pulse = (ring_up_amp * (step(rsing_edge_time) >>
                            (t + space / 2 + buffer / 2)) -
             (ring_up_amp - amp) *
             (step(rsing_edge_time) >>
              (t + space / 2 + buffer / 2 + ring_up_time)) - amp *
             (step(rsing_edge_time) >>
              (t + space / 2 + buffer / 2 + duration)))
    yield ('!play', pulse * cos(2 * pi * frequency)), ('readoutLine.RF', qubit)
    # if bias is not None:
    #     yield ('!set_bias', bias), ('Z', qubit)
    if bias is not None:
        b = ctx.biases[('Z', qubit)]
        if isinstance(b, tuple):
            b = b[0]
        pulse = (bias - b) * square(duration + space) >> (duration + space +
                                                          buffer) / 2
        yield ('!play', pulse >> t), ('Z', qubit)

    # pulse = square(2 * duration) >> duration
    # ctx.channel['readoutLine.AD.trigger', qubit] |= pulse.marker

    params = {k: v for k, v in ctx.params.items()}
    params['w'] = w
    params['weight'] = weight
    if not (cbit[0] == 'result' and cbit[1] < 0):
        yield ('!capture',
               Capture(qubit, cbit, t + space / 2 + buffer / 2, signal,
                       params)), cbit
    yield ('!set_time', t + duration + space + buffer), qubit
    yield ('!set_phase', 0), qubit


@lib.opaque('CZ')
def CZ(ctx, qubits):
    t = max(ctx.time[q] for q in qubits)

    widthq = ctx.params.get('width', 10e-9)
    ampc = ctx.params.get('ampc', 0)
    amp1 = ctx.params.get('amp1', 0)
    amp2 = ctx.params.get('amp2', 0)
    eps = ctx.params.get('eps', 1.0)
    plateauq = ctx.params.get('plateau', 0.0)
    widthc = ctx.params.get('widthc', widthq)
    plateauc = ctx.params.get('plateauc', plateauq)
    buffer = ctx.params.get('buffer', 0.0)
    netzero = ctx.params.get('netzero', False)
    flip = ctx.params.get('flip', False)

    if netzero:
        duration = 2 * max(widthq, widthc) + 2 * max(plateauq,
                                                     plateauc) + buffer
    else:
        duration = max(widthq, widthc) + max(plateauq, plateauc) + buffer

    for amp, width, plateau, target in zip([ampc, amp1, amp2],
                                           [widthc, widthq, widthq],
                                           [plateauc, plateauq, plateauq],
                                           [('coupler.Z', *qubits),
                                            ('Z', qubits[0]),
                                            ('Z', qubits[1])]):
        sign = ctx.scopes[0].setdefault(('CZ_sign', target), 1)
        if amp != 0 and duration > 0:
            pulse = sign * amp * coshPulse(width, plateau=plateau,
                                           eps=eps) >> (width + plateau) / 2
            if netzero:
                pulse += -sign * amp * coshPulse(
                    width, plateau=plateau,
                    eps=eps) >> (width + plateau) * 3 / 2
            yield ('!play', pulse >> t + buffer / 2), target
        if flip:
            ctx.scopes[0][('CZ_sign', target)] = -1 * sign

    for qubit in qubits:
        yield ('!set_time', t + duration), qubit

    yield ('!add_phase', ctx.params.get('phi1', 0)), qubits[0]
    yield ('!add_phase', ctx.params.get('phi2', 0)), qubits[1]


@lib.opaque('iSWAP')
def iSWAP(ctx, qubits):
    t = max(ctx.time[q] for q in qubits)
    t0 = t + 0
    Vz1, Vz2 = [ctx.phases[q] for q in qubits]

    duration = ctx.params['duration']
    amp1 = ctx.params.get('amp1', 0)
    amp2 = ctx.params.get('amp2', 0)
    ampc = ctx.params.get('ampc', 0)
    edge = ctx.params.get('edge', 0)
    buffer = ctx.params.get('buffer', 0)
    before = ctx.params.get('before', buffer)
    after = ctx.params.get('after', buffer)
    phi1 = ctx.params.get('phi1', 0)
    phi2 = ctx.params.get('phi2', 0)

    t += before
    pulse = amp1 * (square(duration, edge=edge)) >> duration / 2
    yield ('!play', pulse >> t), ('Z', qubits[0])
    pulse = amp2 * (square(duration, edge=edge)) >> duration / 2
    yield ('!play', pulse >> t), ('Z', qubits[1])

    pulse = ampc * (square(duration, edge=edge)) >> duration / 2
    yield ('!play', pulse >> t), ('coupler.Z', *qubits)

    for qubit in qubits:
        yield ('!set_time', t + duration + buffer), qubit

    t1 = t + duration + before + after
    freq1 = ctx.cfg.query(f'gate.R.{qubits[0]}.params.frequency')
    freq2 = ctx.cfg.query(f'gate.R.{qubits[1]}.params.frequency')
    phi1_set = -2 * pi * (freq1 * t1 - freq2 * t0) - Vz1 + Vz2 + phi1
    phi2_set = -2 * pi * (freq2 * t1 - freq1 * t0) + Vz1 - Vz2 + phi2

    yield ('!add', 'phase', phi1_set), qubits[0]
    yield ('!add', 'phase', phi2_set), qubits[1]


@lib.opaque('Reset')
def Reset(ctx, qubits):
    qubit, *_ = qubits

    duration = ctx.params.get('duration', 1e-6)
    amp_ef = ctx.params.get('amp_ef', 1.0)
    amp_f0_g1 = ctx.params.get('amp_fg', 1.0)
    freq_f0_g1 = ctx.params.get('frequency_fg', 1e9)
    duration = ctx.params.get('duration_fg', 1.0)

    f12 = ctx.cfg.query(f'gate.R12.{qubit}.params.frequency')
    shape = ctx.cfg.query(f'gate.R12.{qubit}.params.shape')
    width = ctx.cfg.query(f'gate.R12.{qubit}.params.width')
    plateau = ctx.cfg.query(f'gate.R12.{qubit}.params.plateau')
    eps = ctx.cfg.query(f'gate.R12.{qubit}.params.eps')
    amp = ctx.cfg.query(f'gate.R12.{qubit}.params.amp')
    alpha = ctx.cfg.query(f'gate.R12.{qubit}.params.alpha')
    delta = ctx.cfg.query(f'gate.R12.{qubit}.params.delta')
    beta = ctx.cfg.query(f'gate.R12.{qubit}.params.beta')
    buffer = ctx.cfg.query(f'gate.R12.{qubit}.params.buffer')

    t = ctx.time[qubit]

    wav = amp_f0_g1 * coshPulse(width=50e-9, plateau=duration - 50e-9) * cos(
        2 * pi * freq_f0_g1)
    wav = wav >> (duration / 2)

    yield ('!play', wav >> t), ('Z', qubit)
    yield ('!add_time', duration), qubit

    yield ('!add_time', 1e-6), qubit

    t = ctx.time[qubit]

    pulseLib = {
        'CosPulse': cosPulse,
        'CoshPulse': coshPulse,
        'Gaussian': gaussian,
        'cosPulse': cosPulse,
        'coshPulse': coshPulse,
        'gaussian': gaussian,
    }

    if shape in ['CoshPulse', 'coshPulse']:
        pulse = pulseLib[shape](width, plateau=plateau, eps=eps)
    else:
        pulse = pulseLib[shape](width, plateau=plateau)

    if (width > 0 or plateau > 0):
        I, Q = mixing(amp * alpha * pulse,
                      phase=0,
                      freq=delta,
                      DRAGScaling=beta / alpha)
        t = (width + plateau + buffer) / 2 + ctx.time[qubit]
        wav, _ = mixing(I >> t, Q >> t, freq=f12)
        yield ('!play', wav), ('RF', qubit)
        yield ('!add_time', width + plateau + buffer), qubit
        yield ('!add_time', 200e-9), qubit

    t = ctx.time[qubit]

    wav = amp_f0_g1 * coshPulse(width=50e-9, plateau=duration - 50e-9) * cos(
        2 * pi * freq_f0_g1)
    wav = wav >> (duration / 2)

    yield ('!play', wav >> t), ('Z', qubit)
    yield ('!add_time', duration), qubit
    yield ('!add_time', 1e-6), qubit
