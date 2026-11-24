"""Original Fairy Hills opening cue. Run with Python + NumPy. Writes WAV beside _src."""
from pathlib import Path
import wave
import numpy as np

SR = 44100
SECONDS = 27.4
rng = np.random.default_rng(1124)
mix = np.zeros((round(SR * SECONDS), 2))
send = np.zeros_like(mix)
def place(t, y, pan, room):
    start = round(t * SR)
    y = y[:len(mix)-start]
    stereo = y[:, None] * [np.cos((pan+1)*np.pi/4), np.sin((pan+1)*np.pi/4)]
    mix[start:start+len(y)] += stereo
    send[start:start+len(y)] += room * stereo

def axis(d):
    return np.arange(round(d*SR))/SR

def hz(note):
    return 440*2**((note-69)/12)

def harp(start,note,amp):
    t=axis(3.4)
    f=hz(note)
    y=np.zeros_like(t)
    for k in range(1,13):
        freq=f*k*np.sqrt(1+0.00009*k*k)
        tau=1.45*(220/f)**.20/(1+.40*(k-1))
        weight=(.45+.55*np.sin(k*.45)**2)/k**1.35
        y+=weight*np.sin(2*np.pi*freq*t)*np.exp(-t/tau)
    y*=np.minimum(t/.006,1)*np.clip((3.4-t)/.34,0,1)
    place(start,y*amp,-.26+.16*(note-50)/24,.20)

def whistle(start,note,length,amp,far=False):
    t=axis(length+.16)
    f=hz(note)
    pitch=1-.004*np.exp(-t/.035)+.0028*np.sin(2*np.pi*4.8*t)*np.clip((t-.20)/.4,0,1)
    phase=2*np.pi*np.cumsum(f*pitch)/SR
    breath=rng.normal(0,1,len(t))
    breath=np.convolve(breath,np.ones(13)/13,'same')
    tone=np.sin(phase)+.16*np.sin(2*phase+.18)+.044*np.sin(3*phase)+.09*breath
    env=np.minimum(t/.065,1)*np.clip((length+.16-t)/.18,0,1)
    place(start,tone*env*amp,.39 if far else .11,.65 if far else .22)

def pedal(start,note,length,amp):
    t=axis(length)
    f=hz(note)
    y=np.zeros_like(t)
    for detune in (.999,1.001):
        phase=2*np.pi*f*detune*t
        y+=.42*np.sin(phase)+.12*np.sin(phase*2+.4)+.045*np.sin(phase*3)
    env=np.minimum(t/.7,1)*np.clip((length-t)/1.1,0,1)
    place(start,y*env*amp,-.05,.23)

# Village and hill share a swaying three-beat phrase. The sixth degree B natural
# colours the G chord. The answering phrase in the middle belongs to the girls.
bars=[
 (.12, .78, [50,57,64,65], [0,1,1.5,2.05]),
 (2.46,.78, [53,60,65,69], [0,.98,1.52,2.10]),
 (4.80,.78, [43,55,62,71], [0,1,1.55,2.13]),
 (7.14,.78, [48,55,64], [0,1.10,2]),
 (9.48,.78, [50,57,65,69,67], [0,.50,1,1.52,2.35]),
 (11.82,.78,[55,62,71,69,67], [0,.50,1,1.55,2.15]),
 (14.16,.78,[57,64], [0,.50])]
for start,beat,notes,offsets in bars:
    for i,(note,offset) in enumerate(zip(notes,offsets)):
        harp(start+beat*offset+rng.uniform(-.007,.007), note, (.63 if i==0 else .40)*rng.uniform(.90,1.06))
for start,note,duration,level in [
 (9.66,69,.48,.18),(10.26,72,.25,.17),(10.64,74,.78,.20),
 (11.86,71,.46,.17),(12.52,69,.30,.15),(12.96,67,.65,.17),
 (13.80,69,.55,.16)]:
    whistle(start,note,duration,level)
pedal(.05,50,9.9,.065)
pedal(5.05,43,3.9,.041)
pedal(9.6,50,5.30,.058)
# Listening: the familiar plucks stop. A separated two-note call sounds farther right.
pedal(15.75,45,5.75,.082)
whistle(16.62,76,.94,.12,True)
whistle(18.20,71,1.42,.13,True)
harp(20.12,57,.27)
# Running: build a light eighth-note pulse and quote the call over the open fifth.
for j,(start,notes) in enumerate([(21.48,[50,57,62,64,65,69]),(23.30,[43,55,62,67,71,69]),(25.12,[45,57,64,69])]):
    for i,note in enumerate(notes):
        harp(start+i*.303+rng.uniform(-.006,.006),note,[.61,.30,.41,.31,.43,.30][i])
pedal(21.46,50,4.20,.075)
whistle(22.12,69,.42,.14)
whistle(22.74,72,.37,.14)
whistle(23.33,74,.72,.17)
whistle(24.42,71,.56,.15,True)
whistle(25.25,69,.83,.14,True)

# Diffuse stereo room plus early reflections, with finite tail at picture end.
t=axis(2.6)
for ch in range(2):
    ir=rng.normal(size=len(t))*np.exp(-t/.36)
    ir=np.convolve(ir,np.ones(10)/10,'same')
    ir/=np.sqrt(np.sum(ir*ir))
    ir[:round(SR*.032)]=0
    for delay,gain in [(.040,.22),(.071,.16),(.108,.10)]:
        ir[round((delay+ch*.003)*SR)]+=gain
    n=1<<(len(send)+len(ir)-2).bit_length()
    mix[:,ch]+=np.fft.irfft(np.fft.rfft(send[:,ch],n)*np.fft.rfft(ir,n),n)[:len(mix)]
mix*=np.clip((SECONDS-np.arange(len(mix))/SR)/.70,0,1)[:,None]**1.5
mix*=10**(-3/20)/np.max(np.abs(mix))
target=Path(__file__).resolve().parents[1]/'BGM_Opening_Five_Scenes_v1.wav'
with wave.open(str(target),'wb') as w:
    w.setparams((2,2,SR,0,'NONE','not compressed'))
    w.writeframes(np.rint(mix*32767).astype('<i2').tobytes())

