# 2026-11-01 森林 v4：荆棘丛 3u、荆棘墙 9u + 红光遮罩、草土边补满、前景纵向渐变、布局 v4
import numpy as np, cv2, json
from PIL import Image
B="TechArtAsset/Scenes/S1b_ForestPath"; P=f"{B}/props"; W_=f"{B}/_work"
# 荆棘丛 3u：用 v2 的处理结果（已去蓝影）按高度放大
br=Image.open(f"{P}/F_prop_bramble_v2.png"); br=br.resize((int(br.width*300/br.height),300),Image.LANCZOS); br.save(f"{P}/F_prop_bramble_v3.png")
# 荆棘墙 9u：从 Nano Banana 修边的源图放大
tw=Image.open(f"{P}/F_prop_thornwall_v3_src.png"); tw=tw.resize((int(tw.width*900/tw.height),900),Image.LANCZOS); tw.save(f"{P}/F_prop_thornwall_v3.png")
a=np.array(tw).astype(np.float32); rgb=a[:,:,:3]; al=a[:,:,3]/255
lum=rgb.mean(2); red=(rgb[:,:,0]-rgb[:,:,1:].max(2))
gaps=np.clip((35-lum)/35,0,1)**2*al   # v2：只取最深的缝                 # 枝条之间的暗缝
reds=np.clip((red-40)/60,0,1)*al                  # 原图的红点
g=np.maximum(cv2.GaussianBlur(gaps,(0,0),3)*0.45, cv2.GaussianBlur(reds,(0,0),2)*1.0)
g+=cv2.GaussianBlur(reds,(0,0),18)*0.6
g*=np.clip(1-(1-al)*3,0,1)
yy=np.linspace(0,1,g.shape[0])[:,None]; g*= (0.4+0.6*np.clip((yy-0.15)/0.5,0,1))   # 顶部稀疏枝条处少一些
g=np.clip(g/ max(g.max(),1e-3),0,1)
Image.fromarray(np.dstack([np.full_like(lum,255),np.full_like(lum,255),np.full_like(lum,255),g*255]).astype(np.uint8),"RGBA").save(f"{P}/F_prop_thornwall_v3_glow.png")
print("bramble",br.size,"wall",tw.size)
# 草土边补满：重跑 v1 生成但不留缺口
walk=np.array(Image.open(f"{W_}/S1b_ForestPath_L3_Walk_ditch_v2.png")); H2,W2=walk.shape[:2]
src=np.array(Image.open("MJ_ref/FOREST_KEY_01_pan.png").convert("RGB")).astype(np.float32)
band=src[1000:1040]; band=np.vstack([band[::-1],band,band[::-1]])
reps=int(np.ceil(W2/band.shape[1]))+1
row=np.hstack([band if i%2==0 else band[:,::-1] for i in range(reps)])[:,:W2]*0.85
Hs=row.shape[0]; edge=np.zeros((H2,W2,4),np.float32); TOPY=1036-Hs+8
rng=np.random.default_rng(3); noise=cv2.GaussianBlur(rng.random(W2).astype(np.float32).reshape(1,-1),(0,0),18).ravel()
noise=(noise-noise.min())/(noise.max()-noise.min()); crest=Hs*0.15+noise*Hs*0.45
alpha=np.clip((np.arange(Hs)[:,None]-crest[None,:])/10,0,1)
edge[TOPY:TOPY+Hs,:,:3]=row; edge[TOPY:TOPY+Hs,:,3]=cv2.GaussianBlur(alpha*255,(0,0),2)
Image.fromarray(np.clip(edge,0,255).astype(np.uint8),"RGBA").save(f"{W_}/S1b_ForestPath_L3b_GrassEdge.png")
# 前景纵向渐变
f=np.array(Image.open(f"{W_}/S1b_ForestPath_L4_Fore_wip.png")).astype(np.float32); Hf=f.shape[0]
ys,_=np.where(f[:,:,3]>10); top=ys.min()
t=np.clip((np.arange(Hf)-top)/((Hf-top)*0.7),0,1)[:,None]
f[:,:,3]*=t**1.3*0.9; f[:,:,:3]*=(1-0.35*t)[:,:,None]
Image.fromarray(f.astype(np.uint8),"RGBA").save(f"{W_}/S1b_ForestPath_L4_Fore_v2.png")
# 布局 v4
L=json.load(open(f"{B}/S1b_ForestPath_layout_v3.json",encoding="utf-8"))
for b in L["blocks"]:
    if b["kind"]=="deco": b.update({"x":45.6,"w":round(br.width/100,2),"h":3.0,"sprite":"props/F_prop_bramble_v3.png","sorting_order":12,"label":"荆棘丛（装饰，在妮芙前面，包住十字架）"})
    if b["kind"]=="thorn": b.update({"x":49.2,"w":round(tw.width/100,2),"h":9.0,"collider_x":52.2,"collider_w":6.6,"sprite":"props/F_prop_thornwall_v3.png","glow":"props/F_prop_thornwall_v3_glow.png","label":"受控荆棘墙 9u（红光；碰撞只取中间实心）"})
for it in L["interact"]:
    if it["type"]=="pickup_low": it.update({"sorting_order":11,"hint_trigger_x":44.6})
    if it["type"]=="exit": it["x"]=59.5
L["length"]=60.0; L["_note_v4"]="v4（2026-11-01）：荆棘丛 3u、荆棘墙 9u + 红光遮罩、草土边连续、前景 L4_Fore_v2 渐变、星星在 x>44.6 后触发、场景长 60u。"
json.dump(L,open(f"{B}/S1b_ForestPath_layout_v4.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); print([ (b["x"],b["w"]) for b in L["blocks"]])
