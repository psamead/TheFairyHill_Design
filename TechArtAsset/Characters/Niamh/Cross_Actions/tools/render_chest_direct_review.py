"""Fallback requested by the owner: idle cuts directly to the drawn chest hold."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import subprocess,json,hashlib,shutil

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'previews/chest_review_v2';OUT.mkdir(parents=True,exist_ok=True)
QA=OUT/'_qa';QA.mkdir(exist_ok=True)
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
SOURCE=ROOT/'current/Niamh_cross_chest_local_v1.psd'
def walk(layers):
 for l in layers:
  yield l
  yield from walk(l.get('children',[]))
meta=json.loads(subprocess.run([CLI,'info',str(SOURCE),'--compact'],capture_output=True,text=True,check=True).stdout)
group=next(l['id'] for l in walk(meta['layers']) if l['name']=='01_CHEST_LOCAL_current')
def render(steps,name):
 args=[CLI,'run',str(SOURCE)]
 for c,p in steps:args+=['--cmd',c,'--params',json.dumps(p)]
 path=QA/name;args+=['--out',str(path)]
 subprocess.run(args,capture_output=True,text=True,check=True)
 return Image.open(path).convert('RGBA')
chest=render([],'chest.png')
idle=render([('layer.setProps',{'layer':group,'visible':False})],'idle_base.png')
idle.alpha_composite(Image.open(ROOT.parent/'Motion_v8/parts/arm.png').convert('RGBA'))
assert ImageChops.difference(idle.crop((0,540,350,699)),chest.crop((0,540,350,699))).getbbox() is None
def canvas(char,label):
 im=Image.new('RGB',(500,820),'#263141');d=ImageDraw.Draw(im)
 d.text((24,17),'NIAMH | 01 IDLE > CHEST | DIRECT SWITCH',fill='#f1e6ca')
 d.text((24,39),'USER DRAWN POSES | NO IN-BETWEEN DISTORTION',fill='#acbeb2')
 d.line((30,769,470,769),fill='#829184');im.paste(char,(75,70),char)
 d.text((24,790),label+' | OFFLINE / NO VFX',fill='#c7d0c4');return im
frames=[canvas(idle,'IDLE'),canvas(chest,'TWO-HAND CHEST HOLD'),canvas(idle,'IDLE')]
sample=Image.new('RGB',(1500,820))
for j,f in enumerate(frames):sample.paste(f,(500*j,0))
palette=sample.quantize(colors=256,method=Image.Quantize.MEDIANCUT)
indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
output=OUT/'Niamh_idle_to_chest_direct_v2.gif'
indexed[0].save(output,save_all=True,append_images=indexed[1:],duration=[650,1700,650],loop=0,optimize=False,disposal=1)
with Image.open(output) as im:
 total=0
 for j in range(im.n_frames):im.seek(j);total+=im.info['duration']
 assert total==3000
sample.save(QA/'direct_switch_contact.png')
old=ROOT/'previews/idle_to_actions_v1/Niamh_idle_to_chest_local_v1.gif'
shutil.copy2(old,OUT/'Niamh_idle_to_chest_transition_trial_v1.gif')
assert hashlib.sha256(old.read_bytes()).digest()==hashlib.sha256((OUT/'Niamh_idle_to_chest_transition_trial_v1.gif').read_bytes()).digest()
data={'date':'2026-11-18','action':'cross_chest_local','review_scope':'first action only; high raise work deferred','direct_gif':output.name,'duration_ms':3000,'sequence':[{'pose':'idle','ms':650},{'pose':'exact user chest hold','ms':1700},{'pose':'idle','ms':650}],'interpolation':False,'source_psd_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'transition_trial':'Niamh_idle_to_chest_transition_trial_v1.gif','transition_trial_visual_review':'sleeve distortion and unnatural arm connection; retained only for comparison, not a final action','previous_hold_loops':'preserved unchanged','raised_action_next_direction':'idle to chest hold as intermediate, then raised; pending first-action review','vfx':False,'unity_changed':False}
(OUT/'preview_spec.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(output)
