# 2026-10-30 视差眩晕修正：
# (5) S1 前景 L4：去掉上沿碎草（每列从上往下，找到连续成片的草之前的部分全部透明，边缘羽化）
# (6) 森林：做一条与路面同速的草土边 L3b_GrassEdge，盖住背景层里树根的底部
import numpy as np, cv2
from PIL import Image
B="TechArtAsset/Scenes"
# ---- (5) ----
p=f"{B}/S1_Village/_work/S1_Village_L4_Fore_wip.png"
im=np.array(Image.open(p)).astype(np.float32); a=im[:,:,3]/255; H,W=a.shape
solid=cv2.erode((a>0.9).astype(np.uint8),np.ones((25,9),np.uint8))   # 只认「成片」的草
top=np.full(W,H)
for x in range(W):
    ys=np.where(solid[:,x])[0]
    if len(ys): top[x]=ys[0]
top=cv2.GaussianBlur(top.astype(np.float32).reshape(1,-1),(0,0),25).ravel()
yy=np.arange(H)[:,None]
keep=np.clip((yy-top[None,:]+6)/12,0,1)
im[:,:,3]=im[:,:,3]*keep
Image.fromarray(im.astype(np.uint8),"RGBA").save(f"{B}/S1_Village/_work/S1_Village_L4_Fore_v2.png")
print("S1 L4 top range",int(top.min()),int(top.max()))
# ---- (6) ----
walk=np.array(Image.open(f"{B}/S1b_ForestPath/_work/S1b_ForestPath_L3_Walk_ditch_v2.png")).astype(np.float32)
H2,W2=walk.shape[:2]
src=np.array(Image.open("MJ_ref/FOREST_KEY_01_pan.png").convert("RGB")).astype(np.float32)
band=src[1000:1040]                                # 原图路面上沿那一圈草与土
band=np.vstack([band[::-1],band,band[::-1]])        # 120 px 高
reps=int(np.ceil(W2/band.shape[1]))+1
row=np.hstack([band if i%2==0 else band[:,::-1] for i in range(reps)])[:,:W2]
row*=0.85
Hs=row.shape[0]; edge=np.zeros((H2,W2,4),np.float32)
TOPY=1036-Hs+8                                     # 草边底部压住路面上沿
rng=np.random.default_rng(3)
noise=cv2.GaussianBlur(rng.random(W2).astype(np.float32).reshape(1,-1),(0,0),18).ravel()
noise=(noise-noise.min())/(noise.max()-noise.min())
crest=(Hs*0.15+noise*Hs*0.45)                      # 起伏的上沿
yy=np.arange(Hs)[:,None]
alpha=np.clip((yy-crest[None,:])/10,0,1)
edge[TOPY:TOPY+Hs,:,:3]=row; edge[TOPY:TOPY+Hs,:,3]=alpha*255
# 地沟处不画草边（保持坑口可见）
for a_,b_ in ((3000,3140),(4200,4460)):
    edge[:, a_-30:b_+30, 3]*=0
    m=np.clip(np.abs(np.arange(W2)-((a_+b_)/2))/((b_-a_)/2+60),0,1)
edge[:,:,3]=cv2.GaussianBlur(edge[:,:,3],(0,0),2)
Image.fromarray(np.clip(edge,0,255).astype(np.uint8),"RGBA").save(f"{B}/S1b_ForestPath/_work/S1b_ForestPath_L3b_GrassEdge.png")
print("forest edge rows",TOPY,TOPY+Hs)
