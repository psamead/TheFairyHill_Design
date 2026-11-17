from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import math,json
ROOT=Path(__file__).resolve().parent.parent
def rgba(n):return Image.open(ROOT/'parts'/n).convert('RGBA')
body=rgba('body.png');chest=rgba('chest_arms.png')
def ref_arm(n,anchor,target,scale=.18):
    im=rgba(n);box=im.getbbox();im=im.crop(box);im=ImageOps.mirror(im)
    im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
    layer=Image.new('RGBA',body.size)
    x=target[0]+(anchor[0]-box[2])*scale;y=target[1]+(box[1]-anchor[1])*scale
    layer.alpha_composite(im,(round(x),round(y)));return layer
far=ref_arm('raise_U1_cut.png',(600,1000),(216,287))
near=ref_arm('raise_U2_cut.png',(600,900),(216,280))
crosspath=ROOT.parents[5]/'TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_cross_v2.png'
cross=Image.open(crosspath).convert('RGBA').rotate(70,Image.Resampling.BICUBIC,expand=True)
cross=cross.crop(cross.getbbox());cross.thumbnail((92,140),Image.Resampling.LANCZOS)
def cross_at(grip):
    layer=Image.new('RGBA',body.size)
    layer.alpha_composite(cross,(round(grip[0]-cross.width*.5),round(grip[1]-cross.height*.78)))
    return layer
def shifted(im,dx,dy):
    l=Image.new('RGBA',body.size);l.alpha_composite(im,(round(dx),round(dy)));return l
def alpha(im,a):
    out=im.copy();out.putalpha(out.getchannel('A').point(lambda x:round(x*a)));return out
FPS=20;frames=[];poses=[]
for i in range(90):
    t=i/FPS
    if t<.8:u=0
    elif t<2:u=(t-.8)/1.2
    elif t<3:u=1
    elif t<4.2:u=1-(t-3)/1.2
    else:u=0
    u=u*u*(3-2*u)
    out=body.copy()
    # A pose study crossfade; the source cutouts stay intact.
    if u<.5:
        arm=shifted(chest,0,-u*35)
        grip=(282-14*u,260-65*u)
        out.alpha_composite(cross_at(grip));out.alpha_composite(arm)
    else:
        dy=(1-u)*65
        out.alpha_composite(shifted(far,0,dy))
        out.alpha_composite(cross_at((267,227+dy)))
        out.alpha_composite(shifted(near,0,dy))
    canvas=Image.new('RGB',(540,840),'#263141');d=ImageDraw.Draw(canvas)
    d.text((24,18),'NIAMH | CROSS RAISE | POSE / TIMING TEST v1',fill='#f3e7cc')
    d.text((24,39),'CHEST  >  RAISE  >  HOLD  >  RETURN',fill='#b7c8bf')
    d.line((35,787,505,787),fill='#728279',width=2)
    canvas.paste(out,(95,85),out)
    label='CHEST HOLD' if u<.1 else 'RAISED HOLD' if u>.99 else 'TRANSITION - ROUGH'
    d.text((24,806),label+' | CUTOUT STUDY / NOT FINAL',fill='#d7d1bf')
    frames.append(canvas);poses.append(out)
OUT=ROOT/'previews';OUT.mkdir(exist_ok=True)
frames[0].save(OUT/'Niamh_cross_raise_preview_v1.gif',save_all=True,append_images=frames[1:],duration=50,loop=0,optimize=False)
poses[0].save(OUT/'Niamh_cross_chest_v1.png');poses[45].save(OUT/'Niamh_cross_raised_v1.png')
strip=Image.new('RGB',(540*3,840))
for j,k in enumerate([0,30,45]):strip.paste(frames[k],(j*540,0))
strip.save(OUT/'Niamh_cross_raise_contact_v1.png')
(ROOT/'preview_spec.json').write_text(json.dumps({'fps':FPS,'duration':4.5,'status':'rough pose and timing preview','sources':['user chest PSD _m','raise r01 U1 lower supporting arm','raise r01 U2 upper arm','existing game cross v2'],'limitations':['pose switch at middle of lift is visible','grip and shoulder seams require further painting','not production animation or Unity input']},indent=2),encoding='utf-8')
print(OUT/'Niamh_cross_raise_preview_v1.gif')
