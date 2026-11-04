# 在森林可行走层上挖出两条地沟（按灰盒：x=30u 宽 1.4u 深 1.6u；x=42u 宽 2.6u 深 1.8u）。
# 纹理全部取自原图路面（压暗、上下翻转），不另外出图。输出新文件，不覆盖原可行走层。
import numpy as np, cv2
from PIL import Image
D="TechArtAsset/Scenes/S1b_ForestPath/_work"
im=np.array(Image.open(f"{D}/S1b_ForestPath_L3_Walk_wip.png")).astype(np.float32)
H,W,_=im.shape; G=1065; OPEN=1036   # v2：从路面上沿就断开，读起来是「地面上的缺口」而不是一个箱子            # 脚底行；沟口从路面上沿稍下开始
path=im[1040:1098,:,:3].copy()                        # 路面纹理带
PITS=[(30.0,1.4,1.6),(42.0,2.6,1.8)]
for x,w,d in PITS:
    a,b=int(x*100),int((x+w)*100); floor=G+int(d*100)
    rows=np.arange(OPEN,H)
    tex=np.concatenate([path[::-1],path]*12,0)[:len(rows),a:b]
    k=np.clip((rows-OPEN)/(floor-OPEN),0,1)[:,None,None]
    shade=0.30-0.22*k   # v2：沟里更暗，像洞                           # 越深越暗
    fill=tex*shade
    fl=(rows>=floor)[:,None,None]               # 坑底：亮一点的泥土
    fill=np.where(fl,tex*0.30,fill)
    im[OPEN:,a:b,:3]=fill; im[OPEN:,a:b,3]=255
    # v4：沟内从路面上沿起一直到画面底都是近黑的深洞（背景层里也有路面，透明没用），两侧留出向内收的土唇
    top=1026; rr=np.arange(top,H)
    dark=np.concatenate([path[::-1],path]*12,0)[:len(rr),a:b]*np.clip(0.16-0.10*(rr-top)/200,0.04,0.16)[:,None,None]
    im[top:,a:b,:3]=dark; im[top:,a:b,3]=255
    for e,sgn in ((a,1),(b-1,-1)):
        for i in range(18):                        # 土唇：路面颜色沿斜线向内、向下收
            c=e+sgn*i; d=int(i*1.6)
            im[top:top+40+d,c,:3]=np.concatenate([path[:, c]]*3,0)[:40+d]*max(0.3,0.9-0.035*i)
    for e,sgn in ((a,1),(b-1,-1)):              # 两侧土壁：深色墨线 + 渐暗
        for i in range(26):                     # v2：土壁 = 断口处路面纹理往下延伸，越靠里越暗
            c=e+sgn*i; f=max(0.25,0.95-0.03*i)
            im[OPEN:floor,c,:3]=np.concatenate([path[:, c]]*12,0)[:floor-OPEN]*f
        im[OPEN:floor,e-2:e+3 if sgn>0 else e+2,:3]=[18,20,10]
Image.fromarray(np.clip(im,0,255).astype(np.uint8),"RGBA").save(f"{D}/S1b_ForestPath_L3_Walk_ditch_wip.png")
print("ok")
