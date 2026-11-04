# 程序合成第一章四个音效（44.1 kHz 立体声），输出 .wav 母带 + .ogg
import numpy as np, wave, subprocess, os
SR=44100; rng=np.random.default_rng(7); OUT="TechArtAsset/Audio/SFX"
def t(d): return np.arange(int(SR*d))/SR
def env(n,a,r): e=np.ones(n); A=int(SR*a); R=int(SR*r); e[:A]=np.linspace(0,1,A); e[n-R:]*=np.linspace(1,0,R)**2; return e
def lp(x,c):  # 一阶低通
    a=np.exp(-2*np.pi*c/SR); y=np.zeros_like(x); s=0.
    for i,v in enumerate(x): s=(1-a)*v+a*s; y[i]=s
    return y
def bp(x,lo,hi): return lp(x,hi)-lp(x,lo)
def reverb(x,mix=0.25,dec=1.2):
    ir=rng.standard_normal(int(SR*dec))*np.exp(-np.linspace(0,6,int(SR*dec))); ir/=np.abs(ir).sum()**0.5*8
    w=np.convolve(x,ir)[:len(x)+int(SR*dec)]; y=np.zeros(len(w)); y[:len(x)]=x; return y*(1-mix)+w*mix
def save(name,x,pan=0.0):
    x=x/np.max(np.abs(x))*0.89; L=x*(1-max(pan,0)); R=x*(1+min(pan,0))
    st=(np.stack([L,R],1)*32767).astype(np.int16)
    p=f"{OUT}/{name}.wav"; w=wave.open(p,"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
    subprocess.run(["ffmpeg","-v","error","-y","-i",p,"-c:a","libvorbis","-q:a","6",p[:-4]+".ogg"],check=True); print(name,round(len(x)/SR,2))
def knock(f=140,d=0.18,amp=1.):
    tt=t(d); return amp*(np.sin(2*np.pi*f*tt)+0.5*np.sin(2*np.pi*f*2.3*tt)+0.3*bp(rng.standard_normal(len(tt)),300,2000)*4)*np.exp(-tt*28)
def creak(d,f0,f1,rough=0.6):
    tt=t(d); f=np.linspace(f0,f1,len(tt))+25*np.sin(2*np.pi*3.1*tt)
    jit=np.cumsum(rng.standard_normal(len(tt)))*0.002; ph=np.cumsum(2*np.pi*f/SR)+jit
    # 摩擦：脉冲串 + 谐波，按不规则「黏滑」调幅
    stick=np.clip(np.sin(2*np.pi*rng.uniform(9,14)*tt+rng.uniform(0,6))*0.5+0.6,0,1)**3
    x=sum(np.sin(ph*k)/k for k in range(1,9))*stick
    x+=rough*bp(rng.standard_normal(len(tt)),800,3000)*stick*2
    return x*env(len(tt),0.05,0.25)
# 1 开门：吱呀上滑 + 尾端木头轻敲
g=np.zeros(int(SR*1.6)); c=creak(1.15,330,520); g[:len(c)]+=c*0.8
k=knock(120,0.25); s=int(SR*1.22); g[s:s+len(k)]+=k*0.9
save("SFX_gate_open",reverb(g,0.18,0.6),0.1)
# 2 关门：短吱呀下滑 + 撞石柱闷响
g=np.zeros(int(SR*1.1)); c=creak(0.45,480,300); g[:len(c)]+=c*0.7
k=knock(90,0.35,1.3); k[:int(SR*0.12)]+=knock(210,0.12,0.4); s=int(SR*0.48); g[s:s+len(k)]+=k
save("SFX_gate_close",reverb(g,0.18,0.6),-0.1)
# 3 拾起十字架：落叶沙沙 + 金属叮 + 上行铃声闪光
tt=t(2.2); x=np.zeros(len(tt))
rus=bp(rng.standard_normal(int(SR*0.35)),1500,6000)*env(int(SR*0.35),0.05,0.2)*0.5; x[:len(rus)]+=rus
ct=t(0.6); clink=sum(np.sin(2*np.pi*f*ct)*np.exp(-ct*a) for f,a in ((2350,9),(3720,12),(5130,16)))*0.45; s=int(SR*0.28); x[s:s+len(ct)]+=clink
notes=[587.33,739.99,880.0,1174.66,1479.98]   # D 大调琶音，上行
for i,f in enumerate(notes):
    bt=t(1.2); b=(np.sin(2*np.pi*f*bt)+0.35*np.sin(2*np.pi*f*2.76*bt)+0.15*np.sin(2*np.pi*f*5.4*bt))*np.exp(-bt*3.2)*0.35
    s=int(SR*(0.55+i*0.12)); n=min(len(b),len(x)-s); x[s:s+n]+=b[:n]
sh=bp(rng.standard_normal(len(tt)),5000,11000)*np.clip((tt-0.5)/0.3,0,1)*np.exp(-np.clip(tt-0.8,0,9)*2.5)*0.12; x+=sh
save("SFX_cross_pickup",reverb(x,0.35,1.6))
# 4 荆棘墙湮灭：低沉冷呼啸 + 枝条噼啪 + 黑烟嘶声 + 渐弱低语
d=3.0; tt=t(d); n=len(tt); x=np.zeros(n)
wh=lp(rng.standard_normal(n),220)*8; wh=bp(rng.standard_normal(n),120,900)*3+wh
wenv=np.clip(tt/0.25,0,1)*np.exp(-np.clip(tt-0.4,0,9)*1.1); x+=wh*wenv*0.9
sweep=np.sin(2*np.pi*np.cumsum(np.linspace(70,38,n))/SR)*np.exp(-tt*0.9)*0.6; x+=sweep
for _ in range(70):   # 噼啪
    s=int(SR*rng.uniform(0.05,1.6)); L=int(SR*rng.uniform(0.004,0.02)); 
    if s+L<n: x[s:s+L]+=bp(rng.standard_normal(L),1200,7000)*rng.uniform(0.6,2.0)*np.exp(-np.linspace(0,5,L))
hiss=bp(rng.standard_normal(n),3000,9000)*np.clip((tt-0.3)/0.4,0,1)*np.exp(-np.clip(tt-1.0,0,9)*1.0)*0.5; x+=hiss
wt=t(1.6); vow=bp(rng.standard_normal(len(wt)),300,1200)*(0.5+0.5*np.sin(2*np.pi*4.5*wt))*np.sin(np.pi*wt/1.6)*0.35
s=int(SR*1.0); x[s:s+len(wt)]+=vow
x*=env(n,0.01,0.6)
save("SFX_thornwall_banish",reverb(x,0.4,2.0))
