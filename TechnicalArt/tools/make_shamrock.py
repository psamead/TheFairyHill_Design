# 三叶草光点：从 Nano Banana 原图（米白底）抠图 → 去白边 → 128/256 px 图标 + Additive 光晕图
import numpy as np, cv2
from PIL import Image, ImageFilter
src=np.array(Image.open('MJ_ref/SHAMROCK_01.png').convert('RGB')).astype(np.float32)
H,W=src.shape[:2]
bg=np.median(np.concatenate([src[:20].reshape(-1,3),src[-20:].reshape(-1,3),src[:,:20].reshape(-1,3),src[:,-20:].reshape(-1,3)]),0)
d=np.linalg.norm(src-bg,axis=2)
fg=d>38
k=np.ones((5,5),np.uint8)
m=cv2.morphologyEx(fg.astype(np.uint8),cv2.MORPH_CLOSE,k,iterations=2)
n,lab,st,_=cv2.connectedComponentsWithStats(m); big=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); m=(lab==big).astype(np.uint8)  # 只留最大的一块
inv=(1-m).copy(); ff=np.zeros((H+2,W+2),np.uint8); cv2.floodFill(inv,ff,(0,0),2); fg=(m==1)|(inv==1)  # 填洞
alpha=cv2.GaussianBlur(fg.astype(np.float32),(0,0),1.5)
alpha=np.clip((alpha-0.15)/0.7,0,1)
# 去白边：边缘颜色用内部颜色外扩
core=cv2.erode(fg.astype(np.uint8),np.ones((3,3),np.uint8),iterations=6).astype(bool)
fill=src*core[...,None]; w=core.astype(np.float32); known=core.copy()
for _ in range(10):
    s=cv2.blur(fill,(7,7)); c=cv2.blur(w,(7,7)); new=(~known)&(c>0.01)
    fill[new]=s[new]/c[new][:,None]; w[new]=1; known|=new
rgb=np.where(core[...,None],src,fill)
ys,xs=np.where(alpha>0.02); y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max()
side=int(max(y1-y0,x1-x0)*1.08); cy,cx=(y0+y1)//2,(x0+x1)//2
rgba=np.dstack([np.clip(rgb,0,255),alpha*255]).astype(np.uint8)
im=Image.fromarray(rgba,'RGBA').crop((cx-side//2,cy-side//2,cx+side//2,cy+side//2))
out='TechArtAsset/FX/Shamrock/'
for s in (256,128): im.resize((s,s),Image.LANCZOS).save(out+f'FX_shamrock_{s}.png')
# 光晕：外形放大模糊，淡绿金，用于 Additive 叠在背后
a=np.array(im.resize((256,256),Image.LANCZOS))[...,3].astype(np.float32)/255
pad=np.zeros((384,384),np.float32); pad[64:320,64:320]=a
g=cv2.GaussianBlur(pad,(0,0),26); g=g/g.max()
yy,xx=np.mgrid[0:384,0:384]; r=np.hypot(yy-192,xx-192)/192; g=np.maximum(g*0.9,np.clip(1-r,0,1)**2.2*0.55)
col=np.array([207,240,160],np.float32)
glow=np.dstack([np.ones_like(g)[...,None]*col,(g*255)[...,None]]).reshape(384,384,4)
Image.fromarray(np.clip(glow,0,255).astype(np.uint8),'RGBA').save(out+'FX_shamrock_glow.png')
# 预览：暗场里的效果
prev=Image.new('RGBA',(768,384),(18,20,30,255))
gl=Image.open(out+'FX_shamrock_glow.png'); ic=Image.open(out+'FX_shamrock_256.png')
for i,(x,sc) in enumerate(((192,1.0),(576,0.5))):
    gg=gl.resize((int(384*sc),)*2); ii=ic.resize((int(256*sc),)*2)
    base=np.array(prev).astype(np.float32); ga=np.array(gg).astype(np.float32)
    ox,oy=x-gg.width//2,192-gg.height//2
    reg=base[oy:oy+gg.height,ox:ox+gg.width,:3]; reg+=ga[...,:3]*(ga[...,3:]/255)*0.8
    base[oy:oy+gg.height,ox:ox+gg.width,:3]=np.clip(reg,0,255); prev=Image.fromarray(base.astype(np.uint8),'RGBA')
    prev.alpha_composite(ii,(x-ii.width//2,192-ii.height//2))
prev.convert('RGB').save('TechnicalArt/mock/_shamrock_chk.jpg')
print('ok',im.size)
