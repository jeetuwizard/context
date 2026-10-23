"""Synthesizes the promo soundtrack (no samples, no copyright issues).

Event times match the timeline constants in promo.html.
Usage: python -I sound.py <output.wav>
"""
import math
import random
import struct
import sys
import wave

SR = 44100
DUR = 18.0
N = int(SR * DUR)
buf = [0.0] * N
rnd = random.Random(7)

BEATS = [0.15, 0.45, 1.35, 1.65, 2.55, 2.85]
STAMPS = [3.9, 4.6, 5.3, 6.0]
COUNT = [6.9, 7.8, 8.7]
T_SILENCE, T_HIT, T_END = 9.6, 10.1, 14.2
T_TYPE, TYPE_STEP, TYPE_CHARS = 12.4, 0.043, 28
END_ITEMS = [14.7, 15.1, 15.6, 16.2]


def boom(t0, f0, f1, dur, amp, k):
    """Sine whose pitch drops from f0 to f1: kicks, impacts, heartbeats."""
    start, n, ph = int(t0 * SR), int(dur * SR), 0.0
    for i in range(n):
        idx = start + i
        if idx >= N:
            break
        tt = i / SR
        f = f1 + (f0 - f1) * math.exp(-tt * k)
        ph += 2 * math.pi * f / SR
        env = math.exp(-tt * 4.0 / dur) * min(1.0, i / (0.002 * SR))
        buf[idx] += amp * env * math.sin(ph)


def noise(t0, dur, amp, decay=0.0, lp=0.3, rise=False):
    """Low-passed noise: gunshots and crashes (decay) or whooshes (rise)."""
    start, n, y = int(t0 * SR), int(dur * SR), 0.0
    for i in range(n):
        idx = start + i
        if idx >= N or idx < 0:
            continue
        tt = i / SR
        env = (tt / dur) ** 2 if rise else math.exp(-tt * decay) * min(1.0, i / (0.001 * SR))
        y += lp * (rnd.uniform(-1, 1) - y)
        buf[idx] += amp * env * y


def tone(t0, freq, dur, amp, decay):
    start, n = int(t0 * SR), int(dur * SR)
    for i in range(n):
        idx = start + i
        if idx >= N:
            break
        tt = i / SR
        buf[idx] += amp * math.exp(-tt * decay) * math.sin(2 * math.pi * freq * tt)


def drone():
    for i in range(N):
        t = i / SR
        if T_SILENCE <= t < T_HIT:
            continue
        if t < T_SILENCE:
            env = 0.16 * min(1.0, t / 1.0) + 0.12 * max(0.0, min(1.0, (t - 6.6) / 3.0))
        else:
            env = 0.20 + 0.14 * math.exp(-(t - T_HIT) * 0.8)
        env *= 1.0 - max(0.0, min(1.0, (t - 17.0) / 1.0))
        env *= 0.8 + 0.2 * math.sin(2 * math.pi * 0.5 * t)
        s = math.sin(2 * math.pi * 41.2 * t) + 0.7 * math.sin(2 * math.pi * 55.0 * t)
        if t >= T_HIT:
            s += 0.5 * math.sin(2 * math.pi * 82.4 * t)
        buf[i] += env * s


def riser(t0, t1):
    start, end, ph, y = int(t0 * SR), int(t1 * SR), 0.0, 0.0
    for i in range(start, end):
        p = (i - start) / (end - start)
        f = 120 * (1100 / 120) ** p
        ph += 2 * math.pi * f / SR
        y += (0.03 + 0.4 * p) * (rnd.uniform(-1, 1) - y)
        buf[i] += (0.03 + 0.55 * p * p) * math.sin(ph) + 0.50 * p * p * y


drone()
for b in BEATS:
    boom(b, 95, 45, 0.25, 0.9, 18)
for w in (0.3, 1.5):
    noise(w - 0.25, 0.3, 0.25, rise=True, lp=0.08)
for _ in range(12):
    noise(2.7 + rnd.random() * 0.4, 0.02, 0.5, decay=80, lp=0.6)
for s in STAMPS:
    boom(s, 140, 38, 0.6, 1.0, 12)
    noise(s, 0.25, 0.75, decay=25, lp=0.35)
for c in COUNT:
    tone(c, 1760, 0.08, 0.25, 50)
    tone(c, 2640, 0.06, 0.15, 60)
    boom(c, 80, 40, 0.3, 0.5, 15)
riser(6.6, T_SILENCE)
boom(9.75, 90, 45, 0.3, 0.6, 18)
boom(T_HIT, 110, 30, 2.0, 1.2, 4)
boom(T_HIT, 50, 28, 2.5, 0.6, 2)
noise(T_HIT, 1.5, 0.8, decay=3.5, lp=0.15)
noise(T_HIT, 0.08, 0.9, decay=40, lp=0.7)
for h in (10.6, 11.0):
    boom(h, 130, 45, 0.5, 0.7, 12)
    noise(h, 0.15, 0.4, decay=30, lp=0.4)
for k in range(TYPE_CHARS):
    tone(T_TYPE + k * TYPE_STEP, 3000, 0.015, 0.10, 200)
noise(T_END - 0.3, 0.35, 0.3, rise=True, lp=0.1)
for e in END_ITEMS:
    boom(e, 200, 90, 0.2, 0.4, 25)
    tone(e, 880, 0.12, 0.12, 25)

# a little space: two quiet echoes
for delay, gain in ((0.11, 0.18), (0.37, 0.10)):
    d = int(delay * SR)
    for i in range(N - 1, d - 1, -1):
        buf[i] += gain * buf[i - d]

peak = max(abs(x) for x in buf) or 1.0
k = 2.6
left = [math.tanh(k * x / peak) / math.tanh(k) * 0.92 for x in buf]
w = int(0.012 * SR)
right = [0.0] * w + left[:-w]

with wave.open(sys.argv[1], 'wb') as f:
    f.setnchannels(2)
    f.setsampwidth(2)
    f.setframerate(SR)
    f.writeframes(b''.join(struct.pack('<hh', int(l * 32767), int(r * 32767)) for l, r in zip(left, right)))
print(f'wrote {sys.argv[1]} ({DUR}s)')
