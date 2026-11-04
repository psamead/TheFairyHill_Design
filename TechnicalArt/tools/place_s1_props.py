# S1 可行走物件：按灰盒尺寸缩放、写入布局 v2、合成进视差预览
import json, os, copy
import numpy as np
from PIL import Image
R="TechArtAsset/Scenes/S1_Village"; P=f"{R}/props"
def load(n, trim=0.0):
    im=Image.open(f"{P}/S1_prop_{n}_src.png")
    if trim: im=im.crop((0,0,im.width,int(im.height*(1-trim))))
    return im
def scale(im,h_u):
    h=int(h_u*100); return im.resize((int(im.width*h/im.height),h),Image.LANCZOS)
wall=load("wall",0.03); hay=load("hay",0.06); gate=load("gate",0.04)
items=[ # 名称, 图, 高(u), 左x(u)
 ("wall_low",  scale(wall,1.2), 1.2, 9.5),
 ("hay",       scale(hay,0.9),  0.9, 15.0),
 ("wall_tall", scale(wall,1.8), 1.8, 16.8),
 ("gate",      scale(gate,2.4), 2.4, 24.0)]
for n,im,h,x in items: im.save(f"{P}/S1_prop_{n}.png")
lay=json.load(open(f"{R}/S1_Village_layout_v1.json",encoding="utf-8")); L2=copy.deepcopy(lay)
L2["ground"]=[[[0,0],[38.4,0]]]
L2["blocks"]=[]
lab={"wall_low":"干石墙 1.2u（跳跃教学，可站上）","hay":"方草捆 0.9u（垫脚）","wall_tall":"石墙 1.8u（与低墙同图放大）"}
for n,im,h,x in items:
    w=round(im.width/100,2)
    if n=="gate":
        for it in L2["interact"]:
            if it["type"]=="reach": it["x"]=round(x+w/2,2); it["label"]="木栅门（伸手推开，宽 %.1fu）"%w
        continue
    L2["blocks"].append({"x":x,"w":w,"h":h,"base":0,"label":lab[n],"sprite":f"props/S1_prop_{n}.png"})
L2["_note_v2"]="v2（2026-10-29）：地面拉平；物件宽度按实际图片；高石墙用低石墙同一张图放大。"
L2["lights"]=[[6,1.0],[10.85,1.9],[12.5,1.2],[15.8,1.6],[18.8,2.5],[21.5,1.3],[27,1.0],[29,1.4],[31,1.0]]
json.dump(L2,open(f"{R}/S1_Village_layout_v2.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
for b in L2["blocks"]: print(b["label"], "x", b["x"], "w", b["w"])
# 检查间距
b=L2["blocks"]; print("hay→tall gap", round(b[2]["x"]-(b[1]["x"]+b[1]["w"]),2), "low wall→hay gap", round(b[1]["x"]-(b[0]["x"]+b[0]["w"]),2))
# 预览：物件叠在可行走层
D=f"{R}/_work"; PP={"L0_Sky":0.05,"L1_Far":0.2,"L2_Mid":0.5,"L3_Walk":1.0,"L4_Fore":1.3}
Ls={k:Image.open(f"{D}/S1_Village_{k}_wip.png").convert("RGBA") for k in PP}
props=Image.new("RGBA",Ls["L3_Walk"].size,(0,0,0,0)); GY=1000  # 原图路面行（与拆层一致）
for n,im,h,x in items: props.alpha_composite(im,(int(x*100),GY-im.height+8))
props.save(f"{P}/S1_props_layer_wip.png")
NI=Image.open("TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png").convert("RGBA"); ni=NI.resize((int(NI.width*210/NI.height),210),Image.LANCZOS)
fd=os.path.expanduser("~/s1p"); os.makedirs(fd,exist_ok=True)
for f in os.listdir(fd): os.remove(os.path.join(fd,f))
for i,c in enumerate(range(0,1921,12)):
    fr=Image.new("RGBA",(1920,1080),(0,0,0,255))
    for k,p in PP.items():
        fr.alpha_composite(Ls[k].crop((int(c*p),190,int(c*p)+1920,1270)))
        if k=="L3_Walk":
            fr.alpha_composite(props.crop((c,190,c+1920,1270)))
            fr.alpha_composite(ni,(900-ni.width//2,810-ni.height))
    if c in (720,1440): fr.convert("RGB").resize((960,540)).save(f"{P}/_chk_{c}.jpg",quality=80)
    fr.convert("RGB").resize((1280,720),Image.LANCZOS).save(f"{fd}/f{i:04d}.png")
