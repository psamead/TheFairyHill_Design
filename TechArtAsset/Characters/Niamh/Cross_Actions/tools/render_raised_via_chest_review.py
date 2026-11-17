"""Use the owner's chest drawing for both previously distorted intermediate poses."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'previews/raised_via_chest_v2';QA=OUT/'_qa'
QA.mkdir(parents=True,exist_ok=True)
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
preserved={str(p.relative_to(ROOT)):digest(p) for d in ['hold_loops_v1','idle_to_actions_v1','chest_review_v2'] for p in (ROOT/'previews'/d).glob('*.gif')}
def nodes(ls):
 for l in ls:
  yield l
  yield from nodes(l.get('children',[]))
def render(src,steps,name):
 args=[CLI,'run',str(src)]
 for c,p in steps:args+=['--cmd',c,'--params',json.dumps(p)]
 path=QA/(name+'.png');args+=['--out',str(path)]
 subprocess.run(args,capture_output=True,text=True,check=True)
 im=Image.open(path).convert('RGBA');assert im.size==(350,699);return im
chestpsd=ROOT/'current/Niamh_cross_chest_local_v1.psd'
raisedpsd=ROOT/'current/Niamh_cross_raised_story_v1.psd'
info=json.loads(subprocess.run([CLI,'info',str(chestpsd),'--compact'],capture_output=True,text=True,check=True).stdout)
group=next(l['id'] for l in nodes(info['layers']) if l['name']=='01_CHEST_LOCAL_current')
idle=render(chestpsd,[('layer.setProps',{'layer':group,'visible':False})],'idle_base')
idle.alpha_composite(Image.open(ROOT.parent/'Motion_v8/parts/arm.png').convert('RGBA'))
chest=render(chestpsd,[],'chest_user_pose');raised=render(raisedpsd,[],'raised_user_pose')
for im in [chest,raised]:assert ImageChops.difference(im.crop((0,540,350,699)),idle.crop((0,540,350,699))).getbbox() is None
def frame(art,label):
 im=Image.new('RGB',(500,820),'#263141');d=ImageDraw.Draw(im)
 d.text((24,17),'NIAMH | 02 IDLE > CHEST > RAISED',fill='#f1e6ca')
 d.text((24,39),'USER KEY POSES | CHEST DRAWING AS INTERMEDIATE',fill='#acbeb2')
 d.line((30,769,470,769),fill='#829184');im.paste(art,(75,70),art)
 d.text((24,790),label+' | KEY-POSE PREVIEW / NO VFX',fill='#c7d0c4');return im
sequence=[(idle,'IDLE',650),(chest,'CHEST HOLD',850),(raised,'RAISED HOLD',1600),(chest,'CHEST HOLD',650),(idle,'IDLE',750)]
frames=[frame(a,n) for a,n,t in sequence]
sample=Image.new('RGB',(500*3,820))
for i,f in enumerate(frames[:3]):sample.paste(f,(500*i,0))
palette=sample.quantize(colors=256,method=Image.Quantize.MEDIANCUT)
encoded=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
output=OUT/'Niamh_idle_chest_raised_keyposes_v2.gif'
encoded[0].save(output,save_all=True,append_images=encoded[1:],duration=[t for a,n,t in sequence],loop=0,optimize=False,disposal=1)
sample.save(QA/'idle_chest_raised_contact.png')
with Image.open(output) as check:
 total=0
 for i in range(check.n_frames):check.seek(i);total+=check.info['duration']
 assert total==4500
for rel,sha in preserved.items():assert digest(ROOT/rel)==sha,'previous GIF modified'
data={'date':'2026-11-18','status':'user key-pose timing preview, awaiting review','action':'cross_raised_story','sequence':[{'pose':n,'duration_ms':t} for a,n,t in sequence],'duration_ms':4500,'middle_pose':'the exact current user-painted chest hold, replacing the two distorted intermediate poses','between_pose_interpolation':False,'source_psds':{str(p.relative_to(ROOT)):digest(p) for p in [chestpsd,raisedpsd]},'feet_fixed':True,'old_gif_hashes_verified_unchanged':preserved,'limitations':['direct key-pose changes; no smooth in-between limb animation','no beam or VFX','no Unity integration or runtime validation']}
(OUT/'preview_spec.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(output)
