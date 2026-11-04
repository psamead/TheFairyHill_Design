# 栅门两种状态共用同一对石柱（来自 Nano Banana 去门图），关门 = 石柱 + 原图门板
import numpy as np, cv2
from scipy import ndimage
from PIL import Image
P="TechArtAsset/Scenes/S1_Village/props"
src=np.array(Image.open(f"{P}/S1_prop_gate_src.png").convert("RGBA")).astype(np.float32); H,W=src.shape[:2]
op=np.array(Image.open("MJ_ref/S1_PROP_GATE_OPEN_01.png").convert("RGB").resize((W,H),Image.LANCZOS)).astype(np.float32)
dist=255-op.min(2); pa=np.clip((dist-14)/50,0,1)
lab,n=ndimage.label(pa>0.3); sz=ndimage.sum(pa>0.3,lab,range(1,n+1)); keep=np.isin(lab,[i+1 for i in np.argsort(sz)[::-1][:2]])
pa*=ndimage.binary_dilation(keep,iterations=3)
pa=cv2.GaussianBlur(pa,(3,3),0)
prgb=np.where(pa[...,None]>0.02,(op-255*(1-pa[...,None]))/np.maximum(pa[...,None],0.02),0)
posts=np.dstack([np.clip(prgb,0,255),pa*255])
# 门板 = 原图前景中位于两根柱子内侧之间的部分
xs=np.where(keep.any(0))[0]; lab2,_=ndimage.label(keep)
cols=[np.where((lab2==k).any(0))[0] for k in np.unique(lab2[lab2>0])]
cols.sort(key=lambda c:c.min()); inL=cols[0].max(); inR=cols[1].min()
boards=src.copy(); m=np.zeros(W,np.float32); m[inL-40:inR+40]=1; m=cv2.GaussianBlur(m.reshape(1,-1),(0,0),8).ravel()
boards[:,:,3]*=m[None,:]
boards[:,:,3]*=(1-np.clip(pa*1.2,0,1))          # 不盖住柱子
closed=posts.copy(); a1=boards[:,:,3:]/255; a0=closed[:,:,3:]/255
closed[:,:,:3]=boards[:,:,:3]*a1+closed[:,:,:3]*(1-a1); closed[:,:,3]=(a1+a0*(1-a1))[:,:,0]*255
ys,xs=np.where((closed[:,:,3]>20)|(posts[:,:,3]>20)); box=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
def out(arr,name):
    im=Image.fromarray(np.clip(arr,0,255).astype(np.uint8),"RGBA").crop(box)
    im=im.resize((int(im.width*240/im.height),240),Image.LANCZOS); im.save(f"{P}/{name}"); return im.size
print(out(closed,"S1_prop_gate.png"),out(posts,"S1_prop_gate_open.png"),"inner",inL,inR)
cl=Image.open(f"{P}/S1_prop_gate.png"); opn=Image.open(f"{P}/S1_prop_gate_open.png")
s=Image.new("RGBA",(cl.width*2+20,cl.height),(235,170,95,255)); s.alpha_composite(cl,(0,0)); s.alpha_composite(opn,(cl.width+20,0)); s.convert("RGB").save("deprecated/_gate_states_chk.jpg")
