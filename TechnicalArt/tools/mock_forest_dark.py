# 森林暗场（Deepnest 风格）效果预览：按 Unity 的层、视差、光照近似合成一帧
import numpy as np, sys
from PIL import Image
W='Scenes/S1b_ForestPath/_work/'
CX=float(sys.argv[1]) if len(sys.argv)>1 else 20.0   # 相机 / 妮芙 x
def load(f): return np.array(Image.open(f).convert('RGBA')).astype(np.float32)/255
def crop(img,f):
    H=img.shape[0]; left=int(round((CX*f-9.6)*100)); 
    out=np.zeros((1080,1920,4),np.float32)
    rows=img[H-1080:H]                       # 底部 1080 px = 视野 y -2.7..8.1
    for x0 in range(1920):
        pass
    xs=np.clip(np.arange(1920)+left,0,img.shape[1]-1)
    ok=(xs>=0)&(xs<img.shape[1]); out[:,ok]=rows[:,xs[ok]]
    return out
layers=[('L0',W+'S1b_ForestPath_L0_Sky_wip.png',0.05,'far0'),('L1',W+'S1b_ForestPath_L1_Far_wip.png',0.4,'far1'),
 ('L2',W+'S1b_ForestPath_L2_Undergrowth.png',0.65,'lit'),('L3',W+'S1b_ForestPath_L3_Walk_ditch_v2.png',1.0,'lit'),
 ('L3b',W+'S1b_ForestPath_L3b_GrassEdge.png',1.0,'lit'),('NIAMH',None,1.0,'lit'),('L4',W+'S1b_ForestPath_L4_Fore_v2.png',1.15,'fore')]
nia=Image.open('Characters/Niamh/Niamh_side_static_v3.png').convert('RGBA'); nia=nia.resize((int(nia.width*0.3),int(nia.height*0.3)),Image.LANCZOS)
yy,xx=np.mgrid[0:1080,0:1920]; wy=8.1-yy/100; wx=CX-9.6+xx/100
def hexc(h): return np.array([int(h[i:i+2],16)/255 for i in (1,3,5)],np.float32)
def render(cfg):
    out=np.zeros((1080,1920,3),np.float32)
    d=np.hypot(wx-CX, wy-1.2); R0,R1=cfg['inner'],cfg['outer']
    t=np.clip((d-R0)/(R1-R0),0,1); pl=(1-t)**cfg['fall']*cfg['li']
    light=hexc(cfg['amb'])*cfg['ai']+pl[...,None]*hexc(cfg['lc'])
    for name,f,par,mode in layers:
        if f is None:
            L=np.zeros((1080,1920,4),np.float32); a=np.array(nia).astype(np.float32)/255
            x0=960-a.shape[1]//2; y0=1080-270-a.shape[0]; L[y0:y0+a.shape[0],x0:x0+a.shape[1]]=a
        else: L=crop(load(f),par)
        rgb=L[...,:3]
        if mode=='lit': rgb=rgb*light
        elif mode in cfg: rgb=rgb*hexc(cfg[mode])
        a=L[...,3:]; out=rgb*a+out*(1-a)
    return np.clip(out,0,1)
cur=dict(amb='#FFFFFF',ai=1.0,lc='#000000',li=0,inner=1,outer=2,fall=1)
cool=dict(amb='#6878A0',ai=0.28,lc='#E4ECF6',li=1.2,inner=0.8,outer=5.5,fall=1.4,far0='#38445C',far1='#262F42',fore='#08090E')
warm=dict(cool,lc='#FFE2B8')
imgs=[render(c) for c in (cur,cool,warm)]
sm=[Image.fromarray((i*255).astype(np.uint8)).resize((960,540),Image.LANCZOS) for i in imgs]
s=Image.new('RGB',(960,540*3+20),(0,0,0))
for k,im in enumerate(sm): s.paste(im,(0,k*550))
s.save(f'../TechnicalArt/mock/forest_dark_x{int(CX)}.jpg',quality=88)
print('ok')
