from pathlib import Path
import subprocess,json,hashlib,shutil
from PIL import Image,ImageChops
SHARE=Path(__file__).resolve().parent.parent
OLD=SHARE/'TechArtAsset/Characters/Niamh/Interaction_Study_2026-11-16'
ROOT=OLD.parent/'Cross_Actions'
if (ROOT/'file_manifest.json').exists():
    raise SystemExit('Already organized. Read Cross_Actions/README.md; do not overwrite current user work by rerunning this migration.')
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
for d in ['current','sources/user','archive/psd_trials','evidence','tools']:(ROOT/d).mkdir(parents=True,exist_ok=True)
def run(src,steps,out):
    args=[CLI,'run',str(src)]
    for c,p in steps:args+=['--cmd',c,'--params',json.dumps(p)]
    args+=['--out',str(out)]
    r=subprocess.run(args,capture_output=True,text=True);r.check_returncode()
def convert(src,out):
    r=subprocess.run([CLI,'convert',str(src),str(out)],capture_output=True,text=True);r.check_returncode()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for kind,filename in [('chest_local','Niamh_chest_composite_clean_wip_v1_m.psd'),('raised_story','Niamh_chest_composite_clean_wip_v1_m2.psd')]:
    src=OLD/filename;out=ROOT/'current'/f'Niamh_cross_{kind}_v1.psd';steps=[]
    if kind=='raised_story':
        names={21:'cross_raised_user_cut',20:'raised_arm_costume_user_group',19:'cape_transition_user_paint',18:'front_costume_user_paint',17:'raised_arm_sleeve_user_cutout',16:'chest_transition_user_paint',15:'chest_cross_backup',14:'cross_smartobject_backup',13:'chest_sleeve_paint_backup',12:'chest_hands_backup',11:'reference_U1_raster',10:'reference_U1_smartobject',9:'hair_back',8:'original_arm_backup',7:'lower_front_costume_user_patch',6:'body_costume',5:'leg',4:'boot',3:'head',2:'original_character_reference'}
        groups=[('01_RAISED_STORY_current',[21,20,7]),('02_CHARACTER_base',[9,6,5,4,3]),('90_REFERENCES_BACKUPS_hidden',[15,14,13,12,11,10,8,2])]
    else:
        names={14:'cross_chest_user_cut',13:'cross_smartobject_backup',12:'sleeve_transition_user_paint',11:'chest_hands_sleeve_cutout',10:'reference_U1_raster',9:'reference_U1_smartobject',8:'hair_back',7:'original_arm_backup',6:'body_costume',5:'leg',4:'boot',3:'head',2:'original_character_reference'}
        groups=[('01_CHEST_LOCAL_current',[14,12,11]),('02_CHARACTER_base',[8,6,5,4,3]),('90_REFERENCES_BACKUPS_hidden',[13,10,9,7,2])]
    for i,n in names.items():steps.append(('layer.setProps',{'layer':i,'name':n}))
    for title,ids in groups:
        for j,i in enumerate(ids):steps.append(('layer.select',{'layer':i,'mode':'replace' if j==0 else 'add'}))
        steps.append(('layer.groupLayers',{'name':title}))
        if title.startswith('90'):steps.append(('layer.setProps',{'visible':False}))
    steps.append(('image.canvasSize',{'width':350,'height':699,'anchor':'topLeft','extensionColor':'transparent'}))
    run(src,steps,out)
    before=ROOT/'evidence'/f'{kind}_source_render.png';after=out.with_suffix('.png');convert(src,before);convert(out,after)
    a=Image.open(before).convert('RGBA');b=Image.open(after).convert('RGBA')
    expected=Image.new('RGBA',(350,699));expected.alpha_composite(a,(0,0))
    same=all(t==(0,0) for t in ImageChops.difference(expected,b).getextrema())
    if a.width>350:assert a.crop((350,0,a.width,a.height)).getchannel('A').getbbox() is None,'crop cuts visible art'
    assert same,'layer organization changes art'
    checks.append({'pose':kind,'source':filename,'source_sha256':sha(src),'source_canvas':list(a.size),'current_canvas':list(b.size),'source_alpha_bounds':a.getbbox(),'pixel_identical_after_canvas_adjustment':same,'current_psd':str(out.relative_to(SHARE))})
# Reorder hidden group to the bottom after PSD reload has assigned fresh IDs.
for p in (ROOT/'current').glob('*.psd'):
    data=json.loads(subprocess.run([CLI,'info',str(p),'--compact'],capture_output=True,text=True,check=True).stdout)
    groups={l['name'][:2]:l['id'] for l in data['layers']}
    tmp=p.with_name('_reorder.psd')
    run(p,[('layer.moveTo',{'layer':groups['90'],'target':groups['02'],'position':'below'}),('layer.setExpanded',{'layer':groups['90'],'expanded':False}),('layer.setExpanded',{'layer':groups['02'],'expanded':False}),('layer.select',{'layer':groups['01']})],tmp)
    tmp.replace(p);convert(p,p.with_suffix('.png'))
    ref=next(c for c in checks if c['pose'] in p.stem);a=Image.open(ROOT/'evidence'/f"{ref['pose']}_source_render.png").convert('RGBA');b=Image.open(p.with_suffix('.png')).convert('RGBA');expected=Image.new('RGBA',b.size);expected.alpha_composite(a,(0,0));assert all(t==(0,0) for t in ImageChops.difference(expected,b).getextrema())
records=[]
def move(src,dst):
    src=src.resolve();dst=dst.resolve()
    assert src.is_relative_to(SHARE) and dst.is_relative_to(SHARE)
    assert not dst.exists(),str(dst)
    h=sha(src) if src.is_file() else None
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(src),str(dst))
    if h:assert sha(dst)==h
    records.append({'old':str(src.relative_to(SHARE)),'new':str(dst.relative_to(SHARE)),'sha256':h})
userfiles={'Niamh_chest_composite_clean_wip_v1_m.psd':'Niamh_cross_chest_local_user_source_2026-11-17.psd','Niamh_chest_composite_clean_wip_v1_m2.psd':'Niamh_cross_raised_story_user_source_2026-11-17.psd','Niamh_chest_composite_preparation_wip_m.psd':'Niamh_cross_chest_transition_user_source_2026-11-17.psd'}
for old,new in userfiles.items():move(OLD/old,ROOT/'sources/user'/new)
for p in list(OLD.iterdir()):
    if p.is_file() and (p.suffix.lower()=='.psd' or p.name.startswith(('Niamh_chest_composite_','Niamh_chest_hold_organized_'))):move(p,ROOT/'archive/psd_trials'/p.name)
preview=OLD.parent/'Cross_Raise_Preview_v1'
if preview.exists():move(preview,ROOT/'archive/Cross_Raise_Preview_v1')
(ROOT/'file_manifest.json').write_text(json.dumps({'date':'2026-11-17','canvas_origin':'top-left; no character scaling or translation','validation':checks,'relocations':records},ensure_ascii=False,indent=2),encoding='utf-8')
# Repair exact project-root path mentions in Agent/human Markdown and local build scripts.
mapping={r['old'].replace('\\','/'):r['new'].replace('\\','/') for r in records}
for p in SHARE.rglob('*'):
    if p.suffix.lower() not in ['.md','.py','.json','.ps1','.js'] or '.git' in p.parts or p.is_relative_to(ROOT):continue
    try:s=p.read_text(encoding='utf-8')
    except (UnicodeError,OSError):continue
    t=s
    for old,new in mapping.items():t=t.replace(old,new).replace(old.replace('/','\\'),new.replace('/','\\'))
    if t!=s:p.write_text(t,encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2));print('relocated',len(records))
