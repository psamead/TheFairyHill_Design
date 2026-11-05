# 栅门音效 v2：真实一点的木门合页「黏滑」吱呀 + 木门板撞击 + 门闩
# 原理：不规则间隔的摩擦脉冲（stick-slip）去激励几个木头共振峰，比 v1 的正弦谐波更像木头和铁合页
import numpy as np, wave, subprocess
SR=44100; rng=np.random.default_rng(11); OUT="TechArtAsset/Audio/SFX"
def reson(x,f,q):                      # 二阶共振滤波（带通）
    w=2*np.pi*f/SR; r=np.exp(-w/(2*q)); a1=-2*r*np.cos(w); a2=r*r; b=(1-r)
    y=np.zeros_like(x); y1=y2=0.
    for i,v in enumerate(x): y0=b*v-a1*y1-a2*y2; y[i]=y0; y2=y1; y1=y0
    return y
def wood(x,modes=((190,8),(420,10),(880,12),(1650,14),(2900,16)),gains=(1,.8,.6,.35,.2)):
    return sum(g*reson(x,f,q) for (f,q),g in zip(modes,gains))
def creak(d,p0,p1,density=1.0):
    n=int(SR*d); x=np.zeros(n); tpos=0.
    while True:
        frac=tpos/d; per=(p0+(p1-p0)*frac)*(1+0.35*rng.standard_normal())   # 脉冲周期（秒），越短音越高
        per*=1+0.6*max(0,np.sin(2*np.pi*2.3*tpos))                          # 一顿一顿
        tpos+=abs(per); i=int(tpos*SR)
        if i>=n: break
        x[i]+=rng.uniform(0.5,1.0)*density
    y=wood(x,((310,25),(640,30),(1180,28),(2300,20)),(1,.9,.6,.3))          # 合页金属+木头的尖细共振
    e=np.minimum(1,np.linspace(0,1,n)*12)*np.minimum(1,np.linspace(1,0,n)*5)
    return y*e
def thud(d=0.5,amp=1.):
    n=int(SR*d); x=np.zeros(n); x[0]=1; x[int(SR*0.012)]=0.5
    x+=rng.standard_normal(n)*np.exp(-np.arange(n)/SR*90)*0.15
    return amp*wood(x)*np.exp(-np.arange(n)/SR*9)
def latch(amp=0.6):
    n=int(SR*0.12); x=np.zeros(n); x[0]=1; x[int(SR*0.03)]=0.6
    return amp*reson(x,2600,20)+amp*0.5*reson(x,4100,25)
def reverb(x,mix=0.2,dec=0.7):
    ir=rng.standard_normal(int(SR*dec))*np.exp(-np.linspace(0,7,int(SR*dec))); ir/=np.sqrt((ir**2).sum())*3
    w=np.convolve(x,ir); y=np.zeros(len(w)); y[:len(x)]=x; return y*(1-mix)+w*mix
def save(name,x,pan=0.):
    x=x/np.max(np.abs(x))*0.89; L=x*(1-max(pan,0)); R=x*(1+min(pan,0))
    st=(np.stack([L,R],1)*32767).astype(np.int16); p=f"{OUT}/{name}.wav"
    w=wave.open(p,"wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
    subprocess.run(["ffmpeg","-v","error","-y","-i",p,"-c:a","libvorbis","-q:a","6",p[:-4]+".ogg"],check=True); print(name,round(len(x)/SR,2))
# 开门：门闩“咔” → 合页长吱呀（由低到高）→ 门板轻轻停住
g=np.zeros(int(SR*1.9)); g[:int(SR*0.12)]+=latch(0.7)
c=creak(1.2,0.009,0.0035); s=int(SR*0.15); g[s:s+len(c)]+=c*0.9
t=thud(0.4,0.35); s=int(SR*1.38); g[s:s+len(t)]+=t
save("SFX_gate_open_v2",reverb(g),0.1)
# 关门：短吱呀（由高到低）→ 门板撞上石柱的闷响 → 门闩落下
g=np.zeros(int(SR*1.3)); c=creak(0.5,0.004,0.008); g[:len(c)]+=c*0.8
t=thud(0.5,1.0); s=int(SR*0.5); g[s:s+len(t)]+=t
l=latch(0.5); s=int(SR*0.62); g[s:s+len(l)]+=l
save("SFX_gate_close_v2",reverb(g),-0.1)
