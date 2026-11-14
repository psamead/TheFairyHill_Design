"""Deterministic Niamh motion SFX study. Run from the design repository root.

Creates mono 44.1 kHz WAV masters and OGG Unity trials. These sounds are
prototypes until reviewed with Chapter 1 music and gameplay timing.
"""

from pathlib import Path
import subprocess
import wave

import numpy as np


SR = 44100
OUT = Path("TechArtAsset/Audio/SFX/Niamh_Motion_v1")
OUT.mkdir(parents=True, exist_ok=True)
PEAK = 10 ** (-8.5 / 20)


def noise(n, seed, lo=30, hi=12000, slope=0.0):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(n)
    spectrum = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    mask = np.clip((f - lo) / max(lo * 0.3, 30), 0, 1)
    mask *= np.clip((hi - f) / max(hi * 0.2, 100), 0, 1)
    spectrum *= mask * np.maximum(f, 40) ** slope
    y = np.fft.irfft(spectrum, n)
    return y / (np.std(y) + 1e-8)


def burst(n, start, length, texture, strength, attack=0.004, release=4.0):
    a, b = int(start * SR), min(n, int((start + length) * SR))
    if b <= a:
        return np.zeros(n)
    u = np.arange(b - a) / SR
    env = np.minimum(1, u / attack) * np.exp(-release * u / length)
    out = np.zeros(n)
    out[a:b] = texture[a:b] * env * strength
    return out


def tone(n, start, hz, length, strength, decay):
    a, b = int(start * SR), min(n, int((start + length) * SR))
    out = np.zeros(n)
    if b <= a:
        return out
    t = np.arange(b - a) / SR
    env = (1 - np.exp(-t * 800)) * np.exp(-decay * t)
    out[a:b] = np.sin(2 * np.pi * hz * t) * env * strength
    return out


def fade(x):
    a = min(len(x) // 4, int(0.003 * SR))
    b = min(len(x) // 3, int(0.045 * SR))
    x[:a] *= np.linspace(0, 1, a)
    x[-b:] *= np.linspace(1, 0, b)
    return x


def step(material, take):
    seed = 20261114 + 101 * take + sum(ord(c) for c in material)
    rng = np.random.default_rng(seed)
    dur = {"dirt": 0.29, "grass": 0.34, "wood": 0.28,
           "stone": 0.25, "hay": 0.38}[material]
    n = int(SR * dur)
    x = np.zeros(n)
    jitter = rng.uniform(-0.009, 0.009)
    if material == "dirt":
        x += burst(n, 0.018, 0.17, noise(n, seed, 100, 2200, -0.25), 0.28)
        x += burst(n, 0.078 + jitter, 0.16, noise(n, seed + 1, 450, 4300), 0.10, release=3.2)
        x += tone(n, 0.019, 115 + 7 * take, 0.11, 0.14, 29)
    elif material == "grass":
        x += burst(n, 0.018, 0.16, noise(n, seed, 100, 2100, -0.25), 0.20)
        x += burst(n, 0.040, 0.25, noise(n, seed + 1, 1700, 9000), 0.115, release=2.8)
        x += burst(n, 0.145 + jitter, 0.13, noise(n, seed + 2, 2000, 8500), 0.07)
        x += tone(n, 0.017, 115 + 5 * take, 0.10, 0.085, 27)
    elif material == "wood":
        x += burst(n, 0.012, 0.105, noise(n, seed, 250, 6000), 0.16, release=5)
        x += tone(n, 0.014, 175 + 9 * take, 0.20, 0.40, 18)
        x += tone(n, 0.016, 390 + 14 * take, 0.16, 0.16, 27)
        x += burst(n, 0.10, 0.11, noise(n, seed + 1, 500, 4300), 0.075)
    elif material == "stone":
        x += burst(n, 0.009, 0.10, noise(n, seed, 400, 10500), 0.30, release=7)
        x += tone(n, 0.011, 245 + 16 * take, 0.13, 0.13, 40)
        for j in range(3):
            x += burst(n, 0.058 + j * 0.025 + jitter, 0.048,
                       noise(n, seed + j + 1, 2000, 12000), 0.060, release=7)
    else:  # hay: compressed dry straw plus a brief fibre brush
        x += burst(n, 0.021, 0.16, noise(n, seed, 200, 1800), 0.15)
        x += burst(n, 0.036, 0.28, noise(n, seed + 1, 2100, 11500), 0.16, release=2.8)
        x += burst(n, 0.14 + jitter, 0.13, noise(n, seed + 2, 3200, 13000), 0.09)
    return fade(x)


def jump(take):
    n = int(SR * 0.33)
    seed = 20262000 + take
    x = burst(n, 0.018, 0.15, noise(n, seed, 100, 2100, -0.25), 0.22)
    x += tone(n, 0.018, 105 + 8 * take, 0.15, 0.14, 24)
    x += burst(n, 0.082, 0.18, noise(n, seed + 1, 1700, 7000), 0.080, release=2.8)
    return fade(x)


def land(take, heavy):
    n = int(SR * (0.38 if heavy else 0.28))
    seed = 20263000 + take + 10 * heavy
    x = burst(n, 0.018, 0.19, noise(n, seed, 90, 2200, -0.28), 0.40 if heavy else 0.24)
    x += tone(n, 0.016, 98 + 6 * take, 0.19, 0.26 if heavy else 0.14, 20)
    x += burst(n, 0.094, 0.21, noise(n, seed + 1, 600, 6800), 0.14 if heavy else 0.07)
    return fade(x)


def brush(take):
    n = int(SR * 0.68)
    seed = 20264000 + take
    t = np.arange(n) / SR
    flutter = 0.58 + 0.42 * np.sin(2 * np.pi * (14 + take) * t) ** 2
    env = np.sin(np.pi * np.arange(n) / n) ** 1.4
    return fade(noise(n, seed, 2400, 12500) * flutter * env * 0.14)


def save(name, x):
    x = x / max(1e-8, np.max(np.abs(x))) * PEAK
    pcm = (x * 32767).astype("<i2")
    wav = OUT / f"{name}.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav),
                    "-c:a", "libvorbis", "-q:a", "6", str(wav.with_suffix(".ogg"))], check=True)
    print(f"{name}: {len(x)/SR:.2f}s")
    return x


def main():
    preview = []
    pause = np.zeros(int(SR * 0.18))
    for material in ("dirt", "grass", "wood", "stone", "hay"):
        for take in (1, 2, 3):
            x = save(f"SFX_Niamh_Step_{material}_{take:02d}_v1", step(material, take))
            preview += [x * 0.8, pause]
        preview.append(np.zeros(int(SR * 0.5)))
    for take in (1, 2):
        preview += [save(f"SFX_Niamh_Jump_{take:02d}_v1", jump(take)), pause]
    for heavy in (False, True):
        for take in (1, 2):
            preview += [save(f"SFX_Niamh_Land_{'heavy' if heavy else 'light'}_{take:02d}_v1",
                             land(take, heavy)), pause]
    for take in (1, 2):
        preview += [save(f"SFX_Niamh_HayBrush_{take:02d}_v1", brush(take)), pause]
    # Listening contact reel; intentionally not an individual Unity cue.
    save("Niamh_Motion_v1_listening_reel", np.concatenate(preview))


if __name__ == "__main__":
    main()
