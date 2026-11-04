# 森林物件：荆棘丛（1.0u 高，x≈48.4，下面藏铁十字）、受控荆棘墙（3.0u 高，x=52.2）；叠到带地沟的可行走层上并出预览
import os, numpy as np
from PIL import Image, ImageEnhance
R="TechArtAsset/Scenes/S1b_ForestPath"; P=f"{R}/props"; D=f"{R}/_work"
def tone(im,k=0.8,sat=0.8):
    rgb=im.convert("RGB"); rgb=ImageEnhance.Brightness(rgb).enhance(k); rgb=ImageEnhance.Color(rgb).enhance(sat)
    out=rgb.convert("RGBA"); out.putalpha(im.split()[3]); return out
br=Image.open(f"{P}/F_prop_bramble_src.png"); br=br.crop((0,0,br.width,int(br.height*0.9)))
import numpy as _np, cv2 as _cv
_a=_np.array(br); _h=_cv.cvtColor(_a[:,:,:3],_cv.COLOR_RGB2HSV)
_blue=(_h[:,:,0]>75)&(_h[:,:,0]<130)&(_h[:,:,1]>25)          # 去掉底部残留的蓝灰影子
_a[_blue,3]=0; br=Image.fromarray(_a,"RGBA"); br=br.crop(br.getbbox()); br=tone(br,0.75,0.85)
br=br.resize((int(br.width*100/br.height),100),Image.LANCZOS); br.save(f"{P}/F_prop_bramble.png")
tw=Image.open(f"{P}/F_prop_thornwall_src.png"); w=tw.width
tw=tw.crop((int(w*0.3),0,int(w*0.7),int(tw.height*0.82)))   # 去掉底部蓝色地面       # 取中段，竖向拉成 3u 高的墙
tw=tone(tw,0.8,0.9).resize((220,300),Image.LANCZOS); tw.save(f"{P}/F_prop_thornwall.png")
walk=Image.open(f"{D}/S1b_ForestPath_L3_Walk_ditch_v2.png").convert("RGBA")
G=1065; layer=Image.new("RGBA",walk.size,(0,0,0,0))
layer.alpha_composite(br,(4840,G-br.height+6));
cr=Image.open(f"{P}/F_prop_cross.png"); layer.alpha_composite(cr,(4840+br.width-34,G-cr.height+2))   # 铁十字掉在荆棘丛底下（先画，荆棘压在上面一点）   # 露出一半在荆棘丛右下 layer.alpha_composite(tw,(5220,G-tw.height+8))
layer.save(f"{P}/F_props_layer_wip.png")
S="S1b_ForestPath"; PP={"L0_Sky":0.05,"L1_Far":0.4,"L2_Mid":0.5,"L3_Walk":1.0,"L4_Fore":1.3}
L={k:Image.open(f"{D}/{S}_{k}_wip.png").convert("RGBA") for k in PP}; L["L3_Walk"]=walk
NI=Image.open("TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png").convert("RGBA"); ni=NI.resize((int(NI.width*210/NI.height),210),Image.LANCZOS)
fd=os.path.expanduser("~/ffp"); os.makedirs(fd,exist_ok=True)
for f in os.listdir(fd): os.remove(os.path.join(fd,f))
shots=[]
for i,c in enumerate(range(0,3841,16)):
    fr=Image.new("RGBA",(1920,1080),(0,0,0,255))
    for k,p in PP.items():
        fr.alpha_composite(L[k].crop((int(c*p),255,int(c*p)+1920,1335)))
        if k=="L3_Walk":
            fr.alpha_composite(layer.crop((c,255,c+1920,1335)))
            fr.alpha_composite(ni,(900-ni.width//2,810-ni.height))
    if c in (2400,3500): shots.append(fr.convert("RGB").resize((960,540)))
    fr.convert("RGB").resize((1280,720),Image.LANCZOS).save(f"{fd}/f{i:04d}.png")
s=Image.new("RGB",(960,1090));[s.paste(im,(0,i*550)) for i,im in enumerate(shots)];s.save(f"{D}/_chk_props.jpg",quality=80)
