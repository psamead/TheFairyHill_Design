# 荆棘墙“从边缘向中心灼烧”的溶解遮罩：灰度 0 = 最先烧掉（外缘），1 = 最后烧掉（中心）
# = 到透明边缘的距离（归一化）+ 两层噪声，让火线不规则、有枝条感
import numpy as np, cv2
from PIL import Image
P='TechArtAsset/Scenes/S1b_ForestPath/props/'
a=np.array(Image.open(P+'F_prop_thornwall_v4.png'))[...,3]
solid=(a>40).astype(np.uint8)
d=cv2.distanceTransform(cv2.copyMakeBorder(solid,1,1,1,1,cv2.BORDER_CONSTANT,0),cv2.DIST_L2,5)[1:-1,1:-1]
d=cv2.GaussianBlur(d,(0,0),18)          # 先把细枝条的距离抹平，整体从外往里
d=d/d.max(); d=d**0.8
rng=np.random.default_rng(3); H,W=a.shape
def noise(s):
    n=rng.random((H//s+2,W//s+2)).astype(np.float32); return cv2.resize(n,(W,H),interpolation=cv2.INTER_CUBIC)
m=0.72*d+0.18*noise(60)+0.10*noise(14)
m=(m-m[solid>0].min())/(m[solid>0].max()-m[solid>0].min()); m=np.clip(m,0,1)
Image.fromarray((m*255).astype(np.uint8),'L').save(P+'F_prop_thornwall_v4_burnmask.png')
# 预览：5 个阶段
w=np.array(Image.open(P+'F_prop_thornwall_v4.png').convert('RGBA')).astype(np.float32)
frames=[]
for t in (0.0,0.25,0.5,0.75,0.92):
    keep=m>=t; band=(m>=t)&(m<t+0.06)
    f=w.copy(); f[...,3]*=keep
    f[band,:3]=f[band,:3]*0.2+np.array([255,150,60])*0.8
    bg=np.zeros_like(f); bg[...,:3]=[14,14,22]; bg[...,3]=255
    al=f[...,3:]/255; out=f[...,:3]*al+bg[...,:3]*(1-al)
    frames.append(cv2.resize(out,(W//3,H//3)))
Image.fromarray(np.concatenate(frames,1).astype(np.uint8)).save('TechnicalArt/mock/_thornwall_burn_stages.jpg')
print('ok')
