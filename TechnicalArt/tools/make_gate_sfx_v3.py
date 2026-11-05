# 栅门音效 v3：拆成两段，像守灯人菜单音效那样由代码按事件播放
#   SFX_Gate_Creak_01~03_v3：门转动的合页吱呀（三个变体轮流，不连续重复）
#   SFX_Gate_Latch_v3：门转到头停住 / 扣上（开门停住和关门扣上共用）
import numpy as np, importlib.util, os
spec=importlib.util.spec_from_file_location('v2',os.path.join(os.path.dirname(__file__),'make_gate_sfx_v2.py'))
src=open(spec.origin,encoding='utf-8').read().split('# 开门：')[0]          # 只取 v2 的函数，不重跑 v2 输出
ns={}; exec(src,ns)
creak,thud,latch,reverb,save,SR=ns['creak'],ns['thud'],ns['latch'],ns['reverb'],ns['save'],ns['SR']
ns['rng'].__init__(21) if False else None
def fade(x,a=0.01,r=0.06):
    n=len(x); e=np.ones(n); A=int(SR*a); R=int(SR*r); e[:A]=np.linspace(0,1,A); e[-R:]=np.linspace(1,0,R); return x*e
variants=[(0.85,0.0085,0.0042),(0.75,0.0070,0.0038),(0.95,0.0095,0.0050)]   # 时长、起止脉冲周期
for i,(d,p0,p1) in enumerate(variants,1):
    c=creak(d,p0,p1); save(f"SFX_Gate_Creak_0{i}_v3",reverb(fade(c),0.15,0.5),0.05)
g=np.zeros(int(SR*0.55)); t=thud(0.5,1.0); g[:len(t)]+=t; l=latch(0.55); s=int(SR*0.04); g[s:s+len(l)]+=l
save("SFX_Gate_Latch_v3",reverb(fade(g,0.002,0.1),0.18,0.6),0.0)
