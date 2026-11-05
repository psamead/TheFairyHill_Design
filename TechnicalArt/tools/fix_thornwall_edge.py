# 荆棘墙去白边：半透明边缘像素原来是抠图残留的浅灰（约 146），改用内部实心颜色向外扩散填充，
# 再把最外一圈染成暗红，读起来像红光透出的光边，而不是没抠干净
import numpy as np, cv2
from PIL import Image
P='TechArtAsset/Scenes/S1b_ForestPath/props/'
a=np.array(Image.open(P+'F_prop_thornwall_v3.png').convert('RGBA')).astype(np.float32)
rgb=a[...,:3].copy(); al=a[...,3]
solid=al>=250
# 颜色外扩：反复用实心像素的邻域平均填充非实心像素
fill=rgb*solid[...,None]; w=solid.astype(np.float32); known=solid.copy()
for _ in range(12):
    s=cv2.blur(fill,(5,5)); c=cv2.blur(w,(5,5))
    new=(~known)&(c>0.01)
    fill[new]=s[new]/c[new][:,None]; w[new]=1; known|=new
edge=(al>0)&(~solid)
rgb[edge]=fill[edge]
# 外缘暗红光边：按透明度越低越红
t=np.clip(1-al/255,0,1)[...,None]*edge[...,None]
red=np.array([176,32,42],np.float32)
rgb=rgb*(1-0.55*t)+red*0.55*t
# 外缘 alpha 收紧一点，去掉最外一圈半透明雾边
al2=np.where(al<40,0,al)
out=np.dstack([np.clip(rgb,0,255),al2]).astype(np.uint8)
Image.fromarray(out,'RGBA').save(P+'F_prop_thornwall_v4.png')
for name,arr in (('v3',a.astype(np.uint8)),('v4',out)):
    c=Image.fromarray(arr,'RGBA').crop((0,0,400,400)); bg=Image.new('RGBA',c.size,(10,8,20,255)); bg.alpha_composite(c)
    bg.resize((600,600)).convert('RGB').save(f'TechnicalArt/mock/_tw_edge_{name}.jpg')
print('edge px',edge.sum(),'new edge mean',out[edge][:,:3].mean(0))
