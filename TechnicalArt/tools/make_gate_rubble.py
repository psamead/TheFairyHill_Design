# 栅门石柱脚下的碎石堆：从矮石墙底部取石块，做成起伏的小土堆轮廓（遮住柱脚与地面的接缝）
import numpy as np
from PIL import Image, ImageFilter
P='TechArtAsset/Scenes/S1_Village/props/'
src=np.array(Image.open(P+'S1_prop_wall_low.png').convert('RGBA')).astype(np.float32)
def make(x0,w,h,seed,flip,name):
    rng=np.random.default_rng(seed)
    crop=src[120-h:120, x0:x0+w].copy()
    xs=np.linspace(0,1,w)
    top=h*(0.15+0.55*(1-(2*xs-1)**2))           # 中间高、两边低的土堆
    for k in range(4):                           # 加几块凸起的石头
        c=rng.uniform(0.15,0.85); r=rng.uniform(0.08,0.16); a=rng.uniform(0.1,0.25)*h
        top+=a*np.clip(1-((xs-c)/r)**2,0,None)
    yy=np.arange(h)[:,None]; mask=(yy>=h-top[None,:]).astype(np.float32)
    m=Image.fromarray((mask*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    crop[...,3]*=np.array(m)/255.0
    crop[...,:3]*=(1.0-0.25*(1-yy/h))[...,None]
    im=Image.fromarray(np.clip(crop,0,255).astype(np.uint8),'RGBA')
    if flip: im=im.transpose(Image.FLIP_LEFT_RIGHT)
    im.save(P+name); return im.size
import os; os.chdir(os.path.dirname(os.path.abspath(__file__))+'/../..')
print(make(20,150,46,3,False,'S1_prop_gate_rubble_L.png'), make(110,160,50,7,True,'S1_prop_gate_rubble_R.png'))
