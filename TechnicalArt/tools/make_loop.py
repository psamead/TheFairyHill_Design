"""make_loop.py — 把一首 AI 生成的音乐处理成无缝循环（妖精丘陵音频流程）。

用法：
    python make_loop.py 输入.mp3 输出名前缀 [--start 11.7 --end 78.95] [--xfade 3.0]

不给 --start / --end 时，自动在 [3, 30] 秒里找起点、在 [曲长*0.5, 曲长-6] 秒里找终点，
挑和声（12 音级色度）与音量最接近的一对。
输出：<前缀>.wav（母带）和 <前缀>.ogg（给 Unity）。需要 ffmpeg 与 numpy。
"""
import argparse, subprocess, wave, tempfile, os
import numpy as np

SR = 44100

def load(path):
    tmp = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ar", str(SR), "-ac", "2", tmp], check=True)
    w = wave.open(tmp); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).reshape(-1, 2).astype(float) / 32768
    w.close(); os.remove(tmp); return a

def save(path, x):
    x = np.clip(x, -1, 1); w = wave.open(path, "wb")
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x * 32767).astype(np.int16).tobytes()); w.close()

def features(m, hop=2205, win=8192):
    f = np.fft.rfftfreq(win, 1 / SR); mask = (f > 60) & (f < 4000)
    pc = (np.round(12 * np.log2(f[mask] / 440)) % 12).astype(int); out = []
    for i in range(0, len(m) - win, hop):
        seg = m[i:i + win]; X = np.abs(np.fft.rfft(seg * np.hanning(win)))[mask]
        c = np.bincount(pc, X, 12); out.append(np.concatenate([c / (np.linalg.norm(c) + 1e-9), [np.sqrt((seg ** 2).mean())]]))
    return np.array(out), SR / hop

def find_points(a):
    F, fps = features(a.mean(1)); dur = len(a) / SR; L = int(4 * fps); best = None
    for s in range(int(3 * fps), int(30 * fps)):
        for e in range(int(dur * 0.5 * fps), int((dur - 6) * fps) - L):
            sim = (F[s:s + L, :12] * F[e:e + L, :12]).sum(1).mean()
            lr = abs(np.log(F[s:s + L, 12].mean() / F[e:e + L, 12].mean()))
            sc = sim - 0.5 * lr
            if best is None or sc > best[0]: best = (sc, s / fps, e / fps)
    return best[1], best[2]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--start", type=float); ap.add_argument("--end", type=float); ap.add_argument("--xfade", type=float, default=3.0)
    o = ap.parse_args(); a = load(o.src)
    st, en = (o.start, o.end) if o.start is not None else find_points(a)
    s, e, X = int(st * SR), int(en * SR), int(o.xfade * SR)
    loop = a[s:e].copy(); t = np.linspace(0, np.pi / 2, X)[:, None]
    loop[-X:] = a[e - X:e] * np.cos(t) + a[s - X:s] * np.sin(t)   # 等功率交叉淡入：尾部淡出 + 起点之前的音频淡入
    save(o.out + ".wav", loop)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", o.out + ".wav", "-c:a", "libvorbis", "-q:a", "6", o.out + ".ogg"], check=True)
    print(f"loop {st:.2f}s -> {en:.2f}s, length {len(loop)/SR:.2f}s")

if __name__ == "__main__":
    main()
