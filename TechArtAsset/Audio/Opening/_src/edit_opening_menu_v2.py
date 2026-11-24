"""Rebuild the five-scene v2 menu-theme edit. Needs NumPy and ffmpeg on PATH."""
from pathlib import Path
import wave, subprocess, re
import numpy as np

out=Path(__file__).resolve().parents[1]
source=out.parent / 'MENU_BGM_v1_loop.wav'
wav=out / 'BGM_Opening_Five_Scenes_v2.wav'
with wave.open(str(source)) as f:
    sr=f.getframerate()
    assert f.getsampwidth()==2 and f.getnchannels()==2
    f.setpos(round(34.5*sr))
    music=np.frombuffer(f.readframes(round(27.4*sr)),dtype='<i2').reshape(-1,2)/32768.0
t=np.arange(len(music))/sr
def smooth(start,end):
    x=np.clip((t-start)/(end-start),0,1)
    return x*x*(3-2*x)
gain_db=-3.3*smooth(14.40,15.30)+3.3*smooth(20.85,21.98)
music*=((10**(gain_db/20))*smooth(0,.38)*(1-smooth(25.85,27.4)))[:,None]
# Match the preview's perceived level with a single gain, preserving dynamics.
meter=subprocess.run(['ffmpeg','-hide_banner','-nostats','-f','f32le','-ar',str(sr),'-ac','2','-i','pipe:0','-af','ebur128','-f','null','-'],input=music.astype('<f4').tobytes(),stderr=subprocess.PIPE,check=True)
lufs=float(re.findall(r'I:\s+(-?\d+(?:\.\d+)?) LUFS',meter.stderr.decode(errors='replace'))[-1])
gain=min(10**((-16.4-lufs)/20),10**(-2.5/20)/np.abs(music).max())
with wave.open(str(wav),'wb') as f:
    f.setparams((2,2,sr,0,'NONE','not compressed'))
    f.writeframes(np.rint(music*gain*32767).astype('<i2').tobytes())

