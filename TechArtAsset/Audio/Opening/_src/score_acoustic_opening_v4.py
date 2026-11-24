"""The Fairy Hills opening, new original manuscript. Python, numpy and ffmpeg.
The sound sources are individual player recordings from VSCO 2 CE, CC0.
Rebuild downloads only the required samples from the pinned upstream revision."""
from pathlib import Path
import tempfile, urllib.request, urllib.parse, concurrent.futures
root_url='https://raw.githubusercontent.com/sgossner/VSCO-2-CE/440300901dfe9275fd84e0b7763af1f8443ae62e/'
cache=Path(tempfile.gettempdir())/'fh_opening_vsco_4403009'
cache.mkdir(exist_ok=True)
def fetch(path):
    target=cache/path.split('/')[-1]
    if not target.exists():
        raw=urllib.request.urlopen(root_url+urllib.parse.quote(path),timeout=45).read()
        if raw[:4]!=b'RIFF':raise ValueError(path)
        tmp=target.with_suffix('.part')
        tmp.write_bytes(raw)
        tmp.replace(target)
    return target
samples={'harp':{n:f'Strings/Harp/KSHarp_{n}_mf.wav' for n in ('D2','F2','A2','C3','E3','G3','B3','D4','F4','A4')},
         'flute':{n:f'Woodwinds/Flute/susNV/LDFlute_susNV_{n}_v1_1.wav' for n in ('C3','E3','A3','C4','E4')},
         'cello':{n:f'Strings/Cello Section/susvib/susvib_{n}_v1_1.wav' for n in ('G1','B1','D2','F2')}}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    list(pool.map(fetch,[p for files in samples.values() for p in files.values()]))

import re, wave, subprocess
import numpy as np
SR=44100
LENGTH=27.4
bus=np.zeros((round(SR*LENGTH),2))
bank={}
for instrument,paths in samples.items():
    for name,path in paths.items():
        label=int(name[1:])*12+{'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}[name[0]]
        root=label+(12 if instrument=='harp' else 24)  # library octave conventions differ
        raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(fetch(path)),'-ar',str(SR),'-ac','2','-f','f32le','-'])
        sample=np.frombuffer(raw,'<f4').reshape(-1,2)
        # Trim recording-room lead-in but retain the breath, bow or finger attack.
        threshold=np.max(abs(sample))*.012
        onset=np.flatnonzero(np.max(abs(sample),axis=1)>threshold)[0]
        bank[instrument,root]=sample[max(0,onset-round(SR*.022)):]
def play(inst,time,pitch,length,level):
    key=min((k for k in bank if k[0]==inst),key=lambda k: abs(k[1]-pitch))
    src=bank[key]
    # Connected flute notes enter on the sustained breath. The phrase opening
    # and the call retain the recorded tongue attack.
    connected = inst == 'flute' and time in (11.05,12.27,13.64,14.28,20.45,21.67,22.71,23.81,25.12)
    if connected:
        src=src[round(.18*SR):]
    n=min(round(SR*length),len(bus)-round(time*SR))
    idx=np.arange(n)*2**((pitch-key[1])/12)
    idx=idx[idx<len(src)-1]
    left=idx.astype(int); frac=(idx-left)[:,None]
    voice=src[left]*(1-frac)+src[left+1]*frac
    t=np.arange(len(idx))/SR
    if inst=='harp':
        reference=np.sqrt(np.mean(voice[:min(len(voice),round(.32*SR))]**2))
        release=min(.55,length*.28);attack=.003
    else:
        reference=np.sqrt(np.mean(voice[round(.16*SR):min(len(voice),round(.83*SR))]**2))
        release=min(.30,length*.31);attack=.035 if inst=='flute' else .23
    if connected:
        attack=.145
        release=.21
    # Taper with the player; leave stereo body and natural room in the recording.
    envelope=np.sin(np.pi/2*np.clip(t/attack,0,1))**2*np.sin(np.pi/2*np.clip((length-t)/release,0,1))**2
    balance={'harp':(.99,.85),'cello':(.86,.95),'flute':(.94,.99)}[inst]
    start=round(time*SR)
    bus[start:start+len(voice)]+=voice*(level/max(reference,.0001))*envelope[:,None]*balance
# Each entry is a played note: seconds, concert MIDI note, ringing length, dynamics.
# A falling third answered by an upward fifth binds the warm and cold shots.
harp=[
 (.12,55,3.10,.084),(.39,62,2.70,.052),(.86,71,1.85,.083),(1.48,67,2.10,.068),
 (2.39,74,2.26,.093),(3.61,69,1.56,.066),(4.42,62,2.2,.054),
 (5.04,48,3.2,.078),(5.74,55,2.3,.044),(6.15,64,2.5,.069),
 (7.32,69,1.71,.057),(8.17,67,1.83,.071),(8.93,62,1.76,.041),
 (9.53,55,2.3,.073),(10.20,62,2.0,.053),(10.69,71,1.58,.054),
 (11.20,67,1.72,.046),(11.85,52,2.7,.068),(12.28,59,2.04,.034),
 (12.76,67,2.04,.035),(13.48,64,2.00,.039),(14.19,62,1.91,.035),
 (17.36,59,2.45,.043),(19.48,66,2.15,.040),
 (20.68,59,2.23,.029),(21.48,52,2.68,.059),(22.18,67,2.18,.039),
 (22.94,55,2.41,.050),(23.54,62,2.08,.037),
 (24.07,50,2.48,.052),(24.78,64,2.05,.037),
 (25.50,59,1.85,.040),(26.02,66,1.37,.032)]
flute=[
 (5.44,67,1.01,.049),(6.62,64,.66,.040),(7.46,69,.88,.047),
 (9.57,71,.55,.069),(10.17,67,1.08,.062),(11.05,74,1.44,.069),(12.27,69,1.58,.061),
 (13.64,67,.86,.055),(14.28,71,1.13,.055),
 (16.38,74,1.35,.045),(18.52,69,2.13,.040),(20.45,67,1.42,.044),
 (21.67,71,1.25,.057),(22.71,67,1.34,.055),
 (23.81,74,1.54,.062),(25.12,69,1.98,.051)]
cello=[(1.38,43,3.90,.034),(5.10,48,3.98,.034),(9.40,43,2.55,.034),
       (11.78,52,3.54,.031),(15.70,47,5.23,.027),(20.58,52,3.80,.035),(24.07,50,3.14,.032)]
for inst,part in [('harp',harp),('flute',flute),('cello',cello)]:
    for note in part:play(inst,*note)
end=np.linspace(1,0,round(.68*SR))**1.6
bus[-len(end):]*=end[:,None]
meter=subprocess.run(['ffmpeg','-hide_banner','-nostats','-f','f32le','-ar',str(SR),'-ac','2','-i','pipe:0','-af','ebur128','-f','null','-'],input=bus.astype('<f4').tobytes(),stderr=subprocess.PIPE,check=True)
lufs=float(re.findall(r'I:\s+(-?\d+(?:\.\d+)?) LUFS',meter.stderr.decode(errors='replace'))[-1])
bus*=min(10**((-16.8-lufs)/20),10**(-2.6/20)/abs(bus).max())
target=Path(__file__).resolve().parents[1]/'BGM_Opening_Five_Scenes_v4.wav'
with wave.open(str(target),'wb') as f:
    f.setparams((2,2,SR,0,'NONE','not compressed'))
    f.writeframes(np.rint(bus*32767).astype('<i2').tobytes())

