# 把 Nano Banana 修好的地沟（_ditch_fix/*_out.png）贴回森林可行走层：只取路面上沿（y≥1022）以下、沟两侧各 2u 范围，边缘羽化
import json, numpy as np, cv2
from PIL import Image
R="TechArtAsset/Scenes/S1b_ForestPath"; O=f"{R}/_ditch_fix"; D=f"{R}/_work"
info=json.load(open(f"{O}/_offsets.json"))
walk=np.array(Image.open(f"{D}/S1b_ForestPath_L3_Walk_wip.png")).astype(np.float32)   # 用没挖过的原可行走层做底
for name,(a,b) in {"ditch_A_1.4u":(3000,3140),"ditch_B_2.6u":(4200,4460)}.items():
    inf=info[name]; x0,y0=inf["walk_x0"],inf["walk_y0"]; bw=inf["box"][2]-inf["box"][0]; bh=inf["box"][3]-inf["box"][1]
    out=np.array(Image.open(f"{O}/{name}_out.png").convert("RGB").resize((bw,bh),Image.LANCZOS)).astype(np.float32)
    TOP=1022; m=np.zeros((bh,bw),np.float32)
    m[TOP-y0:, (a-200)-x0:(b+200)-x0]=1
    m=cv2.GaussianBlur(m,(0,0),18); m[:TOP-y0]=0
    reg=walk[y0:y0+bh,x0:x0+bw]
    reg[...,:3]=reg[...,:3]*(1-m[...,None])+out*m[...,None]
    reg[...,3]=np.maximum(reg[...,3],m*255)
Image.fromarray(np.clip(walk,0,255).astype(np.uint8),"RGBA").save(f"{D}/S1b_ForestPath_L3_Walk_ditch_v2.png"); print("ok")
