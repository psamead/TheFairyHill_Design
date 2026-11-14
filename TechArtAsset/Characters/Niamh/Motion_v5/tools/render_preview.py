"""Render Photoshop-cut puppet parts. Preview only; no Unity files are modified."""
from pathlib import Path
from math import sin, cos, pi, radians
import json
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT=Path(__file__).resolve().parent.parent
parts={n:Image.open(ROOT/'parts'/f'{n}.png').convert('RGBA') for n in ['head','hair_back','body','arm','leg','boot']}
W,H=parts["body"].size
FPS=20
def spin(p,a,c):
    return p.rotate(a,Image.Resampling.BICUBIC,center=c)
def shifted(p,x,y):
    out=Image.new('RGBA',(W,H));out.alpha_composite(p,(round(x),round(y)));return out
def rotate_point(x,y,a,c):
    a=radians(a);x-=c[0];y-=c[1]
    return (c[0]+x*cos(a)+y*sin(a),c[1]-x*sin(a)+y*cos(a))
def pose(kind,t):
    phase=2*pi*t/({'idle':2.,'walk':.8,'run':.5,'jump':2.}[kind])
    leg=0; knee=0; lean=0; arm=0; bob=0; head=0; rise=0;squash=1;land=0
    if kind=='idle':bob=2*sin(phase);head=.8*sin(phase);arm=1.2*sin(phase+.5)
    elif kind in ('walk','run'):
        isrun=kind=='run';leg=(34 if isrun else 21)*sin(phase)
        knee=(28 if isrun else 15)*max(0,-sin(phase));arm=-leg*.55
        bob=-abs(sin(phase))*(12 if isrun else 6);lean=-7 if isrun else -2
        head=1.5*sin(phase+.4)
    else:
        u=t%2
        if u<.2: squash=1-.02*sin(pi*u/.2)
        elif u<1.25:
            v=(u-.2)/1.05;rise=-160*sin(pi*v);leg=16*sin(pi*v);knee=20*sin(pi*v);arm=12*sin(pi*v);lean=-4*sin(pi*v)
        elif u<1.55: land=sin(pi*(u-1.25)/.30)**2
    out=Image.new('RGBA',(W,H))
    for far in (True,False):
        a=-leg if far else leg
        k=(max(0,leg)*.7 if far else knee)
        hip=(187,532);joint=(185,579)
        foot=spin(parts['boot'],-k,joint)
        limb=Image.alpha_composite(parts['leg'],foot)
        limb=spin(limb,a,hip)
        if far:
            rgb=ImageEnhance.Brightness(limb.convert('RGB')).enhance(.86);rgb.putalpha(limb.getchannel('A'));limb=rgb
        out.alpha_composite(shifted(limb,-9 if far else 4,0))
    # Whole dress/cape preserves the original painted silhouette.
    out.alpha_composite(shifted(parts['hair_back'],-land,3*land))
    out.alpha_composite(shifted(parts['body'],0,3*land))
    out.alpha_composite(shifted(spin(parts['arm'],arm,(219,323)),land,4*land))
    out.alpha_composite(shifted(spin(parts['head'],head,(180,214)),0,4*land))
    canvas=Image.new('RGBA',(520,900));out=out.resize((W,round(H*squash)),Image.Resampling.LANCZOS)
    canvas.alpha_composite(out,(75,round(150+bob+rise+698*(1-squash))))
    canvas=spin(canvas,lean,(263,680+rise))
    if kind in ('walk','run'):
        bounds=canvas.getbbox()
        corrected=Image.new('RGBA',canvas.size)
        corrected.alpha_composite(canvas,(0,848-bounds[3]))
        canvas=corrected
    return canvas

def frame(t):
    im=Image.new('RGB',(1120,490),'#e8e4db');d=ImageDraw.Draw(im)
    d.text((24,16),'NIAMH | Motion study v5 | User-revised artwork | NOT IN UNITY',fill='#37453c')
    for i,kind in enumerate(('idle','walk','run','jump')):
        x=i*280
        d.rectangle((x+8,49,x+272,470),fill='#a5b9a4')
        d.rectangle((x+8,397,x+272,470),fill='#54664b')
        d.line((x+8,397,x+272,397),fill='#344c39',width=2)
        d.ellipse((x+92,391,x+192,404),fill='#465b45')
        d.text((x+20,62),{'idle':'IDLE / breathing','walk':'WALK / 0.8 sec','run':'RUN / 0.5 sec','jump':'JUMP + LAND'}[kind],fill='#223b30')
        char=pose(kind,t).resize((182,315),Image.Resampling.LANCZOS)
        im.paste(char,(x+40,100),char)
    return im

if __name__=='__main__':
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as pool:
        frames=list(pool.map(frame,[i/FPS for i in range(FPS*4)]))
    out=ROOT/'previews';out.mkdir(exist_ok=True)
    frames[0].save(out/'Niamh_motion_v5_still.png')
    frames[0].save(out/'Niamh_motion_v5.gif',save_all=True,append_images=frames[1:],duration=50,loop=0,optimize=False)
    strip=Image.new('RGB',(1120,490*3))
    for row,idx in enumerate((4,12,20)):strip.paste(frames[idx],(0,490*row))
    strip.save(out/'Niamh_motion_v5_contact.png')
    data={'status':'motion study; not integrated or accepted','fps':FPS,'source_canvas':[W,H],'pivots':{'head':[180,214],'arm':[219,323],'hip':[187,532],'knee':[185,579]},'clips':{'idle':2,'walk':.8,'run':.5,'jump':2},'landing':{'start_seconds':1.25,'duration_seconds':.30,'body_and_hair_down_px':3,'head_and_arm_down_px':4,'hair_left_px':1,'arm_right_px':1,'foot_stays_fixed':True,'whole_body_landing_scale':1.0,'takeoff_min_scale':.98},'limitations':['single rigid dress/cape','far leg derived from near leg','uses user-edited layers; check moving-arm backdrop','no separate elbow or knee weighting','no Unity validation']}
    (ROOT/'motion_preview_spec.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(out/'Niamh_motion_v5.gif')
