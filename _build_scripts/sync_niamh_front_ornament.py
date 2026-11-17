from pathlib import Path
from PIL import Image,ImageChops
import subprocess,json,hashlib,shutil
SHARE=Path(__file__).resolve().parent.parent
NIAMH=SHARE/'TechArtAsset/Characters/Niamh'
CROSS=NIAMH/'Cross_Actions'
REV=NIAMH/'Motion_v8/appearance_front_ornament_v1'
BACK=CROSS/'archive/front_ornament_sync_2026-11-17'
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
if (REV/'sync_manifest.json').exists():raise SystemExit('Sync already prepared; inspect manifest before further edits.')
REV.mkdir(exist_ok=True);BACK.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def info(p):return json.loads(subprocess.run([CLI,'info',str(p),'--compact'],capture_output=True,text=True,check=True).stdout)
def walk(ls):
 for l in ls:
  yield l
  yield from walk(l.get('children',[]))
def run(src,steps,out):
 a=[CLI,'run',str(src)]
 for c,p in steps:a+=['--cmd',c,'--params',json.dumps(p)]
 a+=['--out',str(out)];r=subprocess.run(a,capture_output=True,text=True);r.check_returncode()
def convert(src,out):subprocess.run([CLI,'convert',str(src),str(out)],capture_output=True,text=True,check=True)
raised=CROSS/'current/Niamh_cross_raised_story_v1.psd'
patchid=next(l['id'] for l in walk(info(raised)['layers']) if l['name']=='lower_front_costume_user_patch')
patch=REV/'front_ornament_patch_same_origin.png'
run(raised,[('layer.showOnly',{'layer':patchid})],patch)
overlay=Image.open(patch).convert('RGBA');assert overlay.size==(350,699);assert overlay.getbbox()==(253,372,292,453)
records=[]
def validate(old,new):
 a=Image.open(old).convert('RGBA');b=Image.open(new).convert('RGBA');assert a.size==b.size
 expected=a.copy();expected.alpha_composite(overlay.crop((0,0,a.width,a.height)))
 # PNG loading may normalize RGB beneath alpha=0. Restore those invisible
 # bytes from the original so exported PNGs also preserve the source data.
 original_pixels=a.load();updated_pixels=b.load()
 for y in range(a.height):
  for x in range(a.width):
   if original_pixels[x,y][3]==0:updated_pixels[x,y]=original_pixels[x,y]
 b.save(new)
 assert all(z==(0,0) for z in ImageChops.difference(expected,b).getextrema()),'unexpected visible pixels changed'
 assert a.getchannel('A').tobytes()==b.getchannel('A').tobytes(),'silhouette changed'
 return ImageChops.difference(a,b).convert('RGB').getbbox()
# Chest action: add the shared garment patch above the body, below the arms.
chest=CROSS/'current/Niamh_cross_chest_local_v1.psd'
for p in [chest,chest.with_suffix('.png')]:
 if not (BACK/p.name).exists():shutil.copy2(p,BACK/p.name)
chest_source=BACK/chest.name
bodyid=next(l['id'] for l in walk(info(chest_source)['layers']) if l['name']=='body_costume')
tmp=REV/'chest_updated.psd'
run(chest_source,[('layer.select',{'layer':bodyid}),('file.placeEmbedded',{'path':str(patch.resolve()),'fit':False,'scale':100,'center':[175,349.5]}),('layer.setProps',{'name':'front_ornament_shared_from_raised_v1'})],tmp)
png=REV/'chest_updated.png';convert(tmp,png);changed=validate(BACK/chest.with_suffix('.png').name,png)
records.append({'target':str(chest.relative_to(SHARE)),'before_sha256':sha(chest_source),'changed_pixel_bounds':changed})
shutil.copy2(tmp,chest);shutil.copy2(png,chest.with_suffix('.png'));tmp.unlink();png.unlink()
# Preserve the current base-art filenames and canvas registration.
for source,stem in [(NIAMH/'Motion_v8/parts/body.png','body'),(NIAMH/'Niamh_side_static_v3.png','static')]:
 old=REV/(stem+'_before.png');shutil.copy2(source,old)
 psd=REV/(stem+'_front_ornament_source.psd')
 run(source,[('layer.setProps',{'name':stem+'_original_pixels'}),('file.placeEmbedded',{'path':str(patch.resolve()),'fit':False,'scale':100,'center':[175,349.5]}),('layer.setProps',{'name':'front_ornament_shared_from_raised_v1'})],psd)
 out=REV/(stem+'_updated.png');convert(psd,out);changed=validate(old,out)
 records.append({'target':str(source.relative_to(SHARE)),'before_sha256':sha(source),'changed_pixel_bounds':changed})
 shutil.copy2(out,source)
# Historical source PSD snapshots are kept; the new editable overlay sources are above.
manifest={'date':'2026-11-17','source_psd':str(raised.relative_to(SHARE)),'source_sha256':sha(raised),'patch_layer':'lower_front_costume_user_patch','patch_bounds':[253,372,292,453],'scope':'front garment ornament only','source_user_psds_modified':False,'silhouette_alpha_unchanged':True,'validation':'RGBA equals original plus same-origin patch; alpha byte-identical','local_updates':records,'unity_updates':[],'unity_playmode_verified':False}
(REV/'sync_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(records,ensure_ascii=False,indent=2))
