"""Add faster timing comparisons without replacing any development-record GIF."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageChops
import subprocess,json,hashlib
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'previews/raised_fast_v3';QA=OUT/'_qa';QA.mkdir(parents=True,exist_ok=True)
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
preserved={str(p.relative_to(ROOT)):sha(p) for p in (ROOT/'previews').rglob('*.gif') if not p.is_relative_to(OUT)}
def walk(ls):
 for l in ls:
  yield l
  yield from walk(l.get('children',[]))
def render(src,steps,name):
 a=[CLI,'run',str(src)]
 for c,p in steps:a+=['--cmd',c,'--params',json.dumps(p)]
 path=QA/(name+'.png');a+=['--out',str(path)];subprocess.run(a,capture_output=True,text=True,check=True)
 im=Image.open(path).convert('RGBA');assert im.size==(350,699);return im
chestpsd=ROOT/'current/Niamh_cross_chest_local_v1.psd';raisedpsd=ROOT/'current/Niamh_cross_raised_story_v1.psd'
data=json.loads(subprocess.run([CLI,'info',str(chestpsd),'--compact'],capture_output=True,text=True,check=True).stdout)
g=next(l['id'] for l in walk(data['layers']) if l['name']=='01_CHEST_LOCAL_current')
idle=render(chestpsd,[('layer.setProps',{'layer':g,'visible':False})],'idle_base')
idle.alpha_composite(Image.open(ROOT.parent/'Motion_v8/parts/arm.png').convert('RGBA'))
chest=render(chestpsd,[],'chest');raised=render(raisedpsd,[],'raised')
for im in [chest,raised]:assert ImageChops.difference(im.crop((0,540,350,699)),idle.crop((0,540,350,699))).getbbox() is None
variants=[
 ('fast_via_chest','A  FAST / BRIEF CHEST',[(idle,'IDLE',300),(chest,'PASSING CHEST',80),(raised,'RAISED',1000),(chest,'RETURN',60),(idle,'IDLE',560)]),
 ('fast_direct','B  FAST / DIRECT RAISE',[(idle,'IDLE',300),(raised,'RAISED',1080),(idle,'IDLE',620)])
]
records=[]
for key,title,seq in variants:
 frames=[]
 for art,label,ms in seq:
  im=Image.new('RGB',(500,820),'#263141');d=ImageDraw.Draw(im)
  d.text((24,17),'NIAMH | 02 '+title,fill='#f1e6ca')
  d.text((24,39),'TIMING COMPARISON | USER KEY POSES',fill='#acbeb2')
  d.line((30,769,470,769),fill='#829184');im.paste(art,(75,70),art)
  d.text((24,790),label+' | 2 SEC LOOP / NO VFX',fill='#c7d0c4');frames.append(im)
 samples=Image.new('RGB',(500*len(frames),820))
 for j,f in enumerate(frames):samples.paste(f,(500*j,0))
 palette=samples.quantize(colors=256,method=Image.Quantize.MEDIANCUT)
 indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
 out=OUT/f'Niamh_raised_{key}_v3.gif'
 indexed[0].save(out,save_all=True,append_images=indexed[1:],duration=[ms for a,n,ms in seq],loop=0,optimize=False,disposal=1)
 with Image.open(out) as test:
  times=[]
  for j in range(test.n_frames):test.seek(j);times.append(test.info['duration'])
  assert sum(times)==2000 and times==[ms for a,n,ms in seq]
 records.append({'variant':key,'gif':out.name,'sequence':[{'pose':n,'duration_ms':ms} for a,n,ms in seq],'duration_ms':sum(times)})
 print(out)
for p,h in preserved.items():assert sha(ROOT/p)==h,'old GIF changed'
record={'date':'2026-11-18','status':'faster timing alternatives awaiting owner preference','previous_duration_ms':4500,'new_duration_ms':2000,'source_psds':{str(p.relative_to(ROOT)):sha(p) for p in [chestpsd,raisedpsd]},'clips':records,'all_prior_gifs_preserved':preserved,'interpolated_frames':False,'feet_fixed':True,'source_psds_changed':False,'vfx_or_unity_work':False}
(OUT/'preview_spec.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
