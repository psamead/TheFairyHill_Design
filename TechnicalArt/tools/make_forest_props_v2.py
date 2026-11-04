# 2026-10-30 森林物件夸张放大（用户要求）：荆棘丛 1.0u→2.0u、荆棘墙 3u→6u、铁十字 0.4u→1.2u；从 _src 大图重新缩放，不放大小图
import numpy as np, cv2, json
from PIL import Image, ImageEnhance
P="TechArtAsset/Scenes/S1b_ForestPath/props"
def tone(im,k,sat):
    rgb=ImageEnhance.Color(ImageEnhance.Brightness(im.convert("RGB")).enhance(k)).enhance(sat).convert("RGBA"); rgb.putalpha(im.split()[3]); return rgb
br=Image.open(f"{P}/F_prop_bramble_src.png"); br=br.crop((0,0,br.width,int(br.height*0.9)))
a=np.array(br); h=cv2.cvtColor(a[:,:,:3],cv2.COLOR_RGB2HSV); a[(h[:,:,0]>75)&(h[:,:,0]<130)&(h[:,:,1]>25),3]=0
br=Image.fromarray(a,"RGBA"); br=br.crop(br.getbbox()); br=tone(br,0.75,0.85)
br=br.resize((int(br.width*200/br.height),200),Image.LANCZOS); br.save(f"{P}/F_prop_bramble_v2.png")
tw=Image.open(f"{P}/F_prop_thornwall_src.png"); w=tw.width
tw=tw.crop((int(w*0.25),0,int(w*0.75),int(tw.height*0.82))); tw=tone(tw,0.8,0.9).resize((440,600),Image.LANCZOS)
ta=np.array(tw).astype(np.float32); Hh,Ww=ta.shape[:2]                 # 左右两边改成不规则的枝条边缘（之前是直切口）
rng=np.random.default_rng(7); prof=cv2.GaussianBlur(rng.random(Hh).astype(np.float32).reshape(-1,1),(0,0),3).ravel()
prof=(prof-prof.min())/(prof.max()-prof.min())
xx=np.arange(Ww)[None,:]; inset=(10+prof*55)[:,None]
fade=np.clip(np.minimum(xx-inset, (Ww-1-xx)-inset[::-1])/18+0.5,0,1)
dark=(ta[:,:,:3].mean(2)<110)                                         # 边缘区只留深色枝条，像散开的刺
band=(np.minimum(xx-10, (Ww-1-xx)-10)<75)
fade=np.where(band&~dark,np.minimum(fade,np.clip((np.minimum(xx, Ww-1-xx)-40)/35,0,1)),fade)   # 边缘带里浅色块淡掉，只剩深色枝条伸出去
fade=np.where(band&dark,np.maximum(fade,0.9*(np.minimum(xx,Ww-1-xx)>4)),fade)
ta[:,:,3]*=fade; tw=Image.fromarray(ta.astype(np.uint8),"RGBA"); tw.save(f"{P}/F_prop_thornwall_v2.png")
cr=Image.open(f"{P}/F_prop_cross_full.png").rotate(-75,expand=True,resample=Image.BICUBIC)
cr=cr.resize((int(cr.width*120/cr.height),120),Image.LANCZOS); cr.save(f"{P}/F_prop_cross_v2.png")
print("bramble",br.size,"wall",tw.size,"cross",cr.size)
L=json.load(open("TechArtAsset/Scenes/S1b_ForestPath/S1b_ForestPath_layout_v2.json",encoding="utf-8"))
bw=round(br.width/100,2)
L["blocks"]=[{"x":47.0,"w":bw,"h":2.0,"base":0,"label":"荆棘丛（装饰，不挡路，夸张放大）","kind":"deco","sprite":"props/F_prop_bramble_v2.png","solid":False},
             {"x":52.2,"w":4.4,"h":6.0,"base":0,"label":"受控荆棘墙（挡路；IronPulse 驱散；夸张放大）","kind":"thorn","sprite":"props/F_prop_thornwall_v2.png","solid":True}]
for it in L["interact"]:
    if it["type"]=="pickup_low":
        it.update({"x":round(47.0+bw-0.9,2),"sprite":"props/F_prop_cross_v2.png","label":"家传铁十字（夸张放大约 1.2u；远处只显示闪光星星，走近 2.5u 内才显现）","reveal_radius":2.5,"hint_fx":"FX/FX_sparkle_star.png"})
    if it["type"]=="exit": it["x"]=57.2
L["_note_v3"]="v3（2026-10-30）：物件夸张放大；路面上沿加同速草土边 _work/S1b_ForestPath_L3b_GrassEdge.png；前景 L4 透明度 0.55、视差 1.15。"
json.dump(L,open("TechArtAsset/Scenes/S1b_ForestPath/S1b_ForestPath_layout_v3.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([ (b["x"],b["w"]) for b in L["blocks"]],[i for i in L["interact"]])
