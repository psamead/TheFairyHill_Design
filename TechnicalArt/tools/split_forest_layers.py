# 森林小径自动拆五层（WIP）。原尺度；路面在原图 y≈1065；层宽不足时水平镜像拼接（路面 / 前景草可无缝镜像）。
# 中景 = 与灌木带相连的深色前排树干 + 灌木根部带；远景 = 其余（光带、紫雾、细树），被中景挡住处按行左右插值（树干竖窄，背景是竖向光带，插值后接近真实画面）。
import sys, os, numpy as np, cv2
from scipy import ndimage
from PIL import Image
ROOT=sys.argv[1]; SRC=os.path.join(ROOT,"MJ_ref/FOREST_KEY_01_pan.png")
OUT=os.path.join(ROOT,"TechArtAsset/Scenes/S1b_ForestPath/_work"); os.makedirs(OUT,exist_ok=True)
img=np.array(Image.open(SRC).convert("RGB")); H,W,_=img.shape
CUT=1100; GROUND=1065; PAD=GROUND+270-CUT   # 底部补到脚底距画底 270 px
UND_TOP, PATH_TOP = 870, 1035
hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV); V=hsv[:,:,2]/255.0
yy=np.arange(H)[:,None]*np.ones((1,W))
# --- 中景遮罩 ---
dark=(V<0.42)&(yy<PATH_TOP)
dark=ndimage.binary_closing(dark,structure=np.ones((15,3)))
lab,n=ndimage.label(dark)
touch=set(np.unique(lab[UND_TOP:UND_TOP+40]))-{0}
sizes=ndimage.sum(dark,lab,range(1,n+1))
keep=[i for i in touch if sizes[i-1]>3000]
mid=np.isin(lab,keep)|((yy>=UND_TOP)&(yy<PATH_TOP))
mid=ndimage.binary_opening(mid,iterations=2); mid=ndimage.binary_fill_holes(mid)
# v4：粗树干上方的树冠一起归中景（之前树冠留在远景，树干移开后像悬空的树）
colfrac=mid[:UND_TOP].mean(0)
wide=ndimage.binary_dilation(colfrac>0.45,iterations=6)
pass  # v5 试过把粗树干留在远景，灌木带出现横向断层，已撤回
# --- 远景：中景处按行插值 ---
far=img.astype(np.float32).copy()
# v3：被前排树干挡住的地方，用单独生成的远景图 FOREST_FAR_01 垫底（调色到和原图背景一致、轻微模糊），
#     原图背景在没被挡住的地方照常保留，所以开场画面和原图一样；镜头一动，树干后面露出的是 FAR_01 的真实细树和光带。
FARSRC=os.path.join(ROOT,"MJ_ref/FOREST_FAR_01.png")
fb=np.array(Image.open(FARSRC).convert("RGB")); fh,fw,_=fb.shape
fb=fb[:int(fh*0.80), int(fw*0.08):]                       # 去掉左边的人形剪影和下面的草丛
fb=cv2.resize(fb,(W,UND_TOP),interpolation=cv2.INTER_AREA)
bg=~mid[:UND_TOP]
L1=cv2.cvtColor(fb,cv2.COLOR_RGB2LAB).astype(np.float32); L0=cv2.cvtColor(img[:UND_TOP],cv2.COLOR_RGB2LAB).astype(np.float32)
for c in range(3):                                        # 按列分块做均值 / 方差匹配，左金右紫的走向跟原图一致
    for x0 in range(0,W,256):
        sl=slice(x0,min(W,x0+256)); ws=slice(max(0,x0-640),min(W,x0+896))   # v3b：参考统计取左右各约 2.5 块的窗口，粗树干那几块不会因背景像素太少而跳过（之前出现蓝色色块）
        t=L0[:,ws,c][bg[:,ws]]; s_=L1[:,sl,c]
        L1[:,sl,c]=(s_-s_.mean())/(s_.std()+1e-3)*t.std()*0.9+t.mean()
fb=cv2.cvtColor(np.clip(L1,0,255).astype(np.uint8),cv2.COLOR_LAB2RGB)
fb=cv2.GaussianBlur(fb,(0,0),1.4)
haze=np.median(img[:UND_TOP][bg].reshape(-1,3),0)
fb=(fb*0.82+haze*0.18).astype(np.float32)
alpha=cv2.GaussianBlur(bg.astype(np.float32),(0,0),3)[...,None]
far[:UND_TOP]=far[:UND_TOP]*alpha+fb*(1-alpha)
far[UND_TOP:]=far[UND_TOP-1]
far=far.astype(np.uint8)
# --- 天空：顶部几行的纵向渐变（在远景后面，基本看不到） ---
sky=np.repeat(cv2.resize(img[:60].mean(1,keepdims=True).astype(np.uint8),(1,H)).reshape(H,1,3),W,1)
# --- 可行走层：路面 + 底部补地面色 ---
walk=img[:CUT].copy(); ground_col=np.median(img[1080:1098].reshape(-1,3),0).astype(np.uint8)*0+np.array([46,52,22],np.uint8)
und=img[UND_TOP:PATH_TOP][::-1]            # v2：路面以下用灌木带上下翻转、压暗，代替纯色色块
und=cv2.resize(und,(W,PAD),interpolation=cv2.INTER_AREA)
und=(und*np.linspace(0.55,0.3,PAD)[:,None,None]).astype(np.uint8)
walk=np.vstack([walk,und])
walk_a=np.zeros(walk.shape[:2],np.float32); walk_a[PATH_TOP-6:]=1
# --- 前景：灌木带深色剪影，压在画面最底 ---
strip=img[940:PATH_TOP]; sv=cv2.cvtColor(strip,cv2.COLOR_RGB2HSV)[:,:,2]/255.0
fa=np.clip((0.45-sv)/0.2,0,1).astype(np.float32); fa=cv2.GaussianBlur(fa,(3,3),0)
fore_rgb=(strip*0.35).astype(np.uint8)
Hh=CUT+PAD; fore=np.zeros((Hh,W,3),np.uint8); fore_a=np.zeros((Hh,W),np.float32)
fore[Hh-strip.shape[0]:]=fore_rgb; fore_a[Hh-strip.shape[0]:]=fa
fore_a[Hh-60:]=np.maximum(fore_a[Hh-60:],1.0); fore[Hh-60:]=np.minimum(fore[Hh-60:],np.array([20,28,12],np.uint8)+fore[Hh-60:]*0)
def padto(a,alpha=False):
    if a.shape[0]>=Hh: return a[:Hh]
    extra=np.repeat(a[-1:],Hh-a.shape[0],0); return np.concatenate([a,extra],0)
def dusk(rgb,p):
    # 越往右越暗、越紫（用户要求过渡到 S2 暮紫）
    w=rgb.shape[1]; t=(np.arange(w)/w)[None,:,None]**1.3
    tint=np.array([70,50,110],np.float32)
    return np.clip(rgb*(1-0.38*t)+tint*0.18*t,0,255).astype(np.uint8)
P={"L0_Sky":0.05,"L1_Far":0.4,"L2_Mid":0.5,"L3_Walk":1.0,"L4_Fore":1.3}
LEVEL=5760; SCREEN=1920
layers={"L0_Sky":(padto(sky),np.ones((Hh,W),np.float32)),
        "L1_Far":(padto(img[:CUT]),np.ones((Hh,W),np.float32)),   # v6：整张原图（树干 + 灌木带）一起作背景层
        "L2_Mid":(padto(img[:CUT]),np.zeros((Hh,W),np.float32)),  # v6：留空（之后放地沟、荆棘等中景物件）
        "L3_Walk":(walk,walk_a),
        "L4_Fore":(fore,fore_a)}
for k,(rgb,a) in layers.items():
    need=int((SCREEN+(LEVEL-SCREEN)*P[k])*1.05)+1
    while rgb.shape[1]<need: rgb=np.hstack([rgb,rgb[:,::-1]]); a=np.hstack([a,a[:,::-1]])
    rgb=dusk(rgb[:,:need].astype(np.float32),P[k]); a=a[:,:need]
    Image.fromarray(np.dstack([rgb,(np.clip(a,0,1)*255).astype(np.uint8)]),"RGBA").save(f"{OUT}/S1b_ForestPath_{k}_wip.png")
    print(k,rgb.shape)
