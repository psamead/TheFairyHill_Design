"""Render two current user poses as separate gentle hold loops, not attack clips."""
from pathlib import Path
from math import sin,cos,pi
import subprocess,json,hashlib
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'previews/hold_loops_v1'
OUT.mkdir(parents=True,exist_ok=True)
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
FPS=20
N=60

def profile(y):
    if y>=540:return 0.
    if y<=310:return 1.
    t=(540-y)/230
    return t*t*(3-2*t)

def breathe(art,phase,kind):
    # A smooth inverse mesh keeps adjacent artwork continuous and boots fixed.
    # At phase zero the original artwork is shown without any deformation.
    breath=1.4*sin(phase)
    sway=(.9 if kind=='chest_local' else 1.2)*sin(phase)
    lift=(.35 if kind=='chest_local' else .7)*sin(phase)
    xs=[0,100,190,250,300,350]
    ys=[0,100,195,260,335,420,480,540,600,699]
    def src(x,y):
        f=profile(y)
        hand=max(0.,min(1.,(x-215)/100))*max(0.,min(1.,(335-y)/110))
        return (x-sway*f,y-breath*f-lift*hand)
    mesh=[]
    for ya,yb in zip(ys,ys[1:]):
        for xa,xb in zip(xs,xs[1:]):
            quad=sum((src(x,y) for x,y in [(xa,ya),(xa,yb),(xb,yb),(xb,ya)]),())
            mesh.append(((xa,ya,xb,yb),quad))
    # Pad before warping so the head edge touching y=0 cannot be clipped.
    padded=Image.new('RGBA',(370,719));padded.alpha_composite(art,(10,10))
    padded_mesh=[]
    for rect,quad in mesh:
        r=(rect[0]+10,rect[1]+10,rect[2]+10,rect[3]+10)
        q=tuple(v+10 for v in quad)
        padded_mesh.append((r,q))
    # The source canvas has an opaque edge at x=0/y=0. Output extends 3px
    # beyond those boundaries to retain its animated edge in the preview.
    # Using one full-domain mesh includes that padded border too.
    xs=[-3,0,100,190,250,300,350,353]
    ys=[-3,0,100,195,260,335,420,480,540,600,699,702]
    padded_mesh=[]
    for ya,yb in zip(ys,ys[1:]):
        for xa,xb in zip(xs,xs[1:]):
            quad=sum((src(x,y) for x,y in [(xa,ya),(xa,yb),(xb,yb),(xb,ya)]),())
            padded_mesh.append(((xa+10,ya+10,xb+10,yb+10),tuple(v+10 for v in quad)))
    return padded.transform(padded.size,Image.Transform.MESH,padded_mesh,Image.Resampling.BICUBIC)

records=[]
for kind,label in [('chest_local','01  LOCAL / CHEST HOLD'),('raised_story','02  STORY / RAISED HOLD')]:
    psd=ROOT/'current'/f'Niamh_cross_{kind}_v1.psd'
    png=OUT/f'_source_{kind}.png'
    subprocess.run([CLI,'convert',str(psd),str(png)],capture_output=True,text=True,check=True)
    art=Image.open(png).convert('RGBA');assert art.size==(350,699)
    frames=[]
    for i in range(N):
        phase=2*pi*i/N
        char=breathe(art,phase,kind)
        frame=Image.new('RGB',(480,810),'#263141');draw=ImageDraw.Draw(frame)
        draw.text((24,18),'NIAMH | '+label,fill='#f2e7cd')
        draw.text((24,40),'CURRENT ART + SHARED FRONT ORNAMENT',fill='#aebfb4')
        draw.line((35,758,445,758),fill='#829184')
        frame.paste(char,(55,49),char)
        draw.text((24,781),'GENTLE HOLD LOOP | OFFLINE PREVIEW',fill='#c4d0c5')
        frames.append(frame)
    # One palette for the whole clip avoids frame-to-frame color flicker.
    samples=Image.new('RGB',(480*6,810))
    for j in range(6):samples.paste(frames[j*10],(480*j,0))
    pal=samples.quantize(colors=256,method=Image.Quantize.MEDIANCUT)
    indexed=[f.quantize(palette=pal,dither=Image.Dither.NONE) for f in frames]
    out=OUT/f'Niamh_cross_{kind}_hold_v1.gif'
    indexed[0].save(out,save_all=True,append_images=indexed[1:],duration=50,loop=0,disposal=1,optimize=False)
    frames[0].save(OUT/f'Niamh_cross_{kind}_hold_v1.png')
    with Image.open(out) as test:
        duration=0
        for j in range(test.n_frames):test.seek(j);duration+=test.info.get('duration',0)
        assert duration==3000 and test.size==(480,810)
        count=test.n_frames
    records.append({'pose':kind,'source':str(psd.relative_to(ROOT)),'source_sha256':hashlib.sha256(psd.read_bytes()).hexdigest(),'gif':out.name,'encoded_frames':count,'duration_ms':duration})
    print(out)

(OUT/'preview_spec.json').write_text(json.dumps({'date':'2026-11-18','source_canvas':[350,699],'display_canvas':[480,810],'source_fps':20,'duration_seconds':3,'status':'separate pose-hold loops only','motion':'smooth continuous breathing and small hold sway; boots fixed','limitations':['no idle-to-pose or return transition','no attack or hit timing','no beam VFX','no Unity integration or Play Mode validation'],'clips':records},ensure_ascii=False,indent=2),encoding='utf-8')
