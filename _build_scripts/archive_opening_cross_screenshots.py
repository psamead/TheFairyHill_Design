"""Archive unmodified Unity captures using the existing design screenshot rules."""
from pathlib import Path
import hashlib,json,shutil,struct,subprocess

ROOT=Path(__file__).resolve().parents[1]
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
SOURCE_REL=Path('Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/Unity_Trial')
SOURCE=UNITY/SOURCE_REL
DEST=ROOT/'ForDesignScreenShot/2026-11-18_for-opening-cross-raise'
DEST.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
order=[f'opening_{page}_{size}.png' for page in range(4) for size in [1920,1280]]+[
 'hud_underlines.png','hud_cross_acquired.png','hud_missing_cross.png','hud_no_target.png',
 'cross_raise_right.png','cross_raise_left.png','cross_restore_right.png','cross_restore_left.png',
 'cross_dissolving.png','cross_raise_wall.png','cross_restore.png','skip_chapter.png']
assert set(order)=={p.name for p in SOURCE.iterdir() if p.suffix.lower()=='.png'},'Review new source captures before changing the archive order'
files=[]
def copy_checked(source,target,kind):
    digest=sha(source)
    if target.exists():assert sha(target)==digest,f'Preserve modified destination: {target}'
    else:shutil.copy2(source,target)
    assert sha(source)==sha(target)==digest
    entry={'kind':kind,'source_project':'TheFairyHill2D','source':source.relative_to(UNITY).as_posix(),
      'destination':target.relative_to(ROOT).as_posix(),'sha256':digest,'bytes':target.stat().st_size,'source_bytes_preserved':True}
    if kind=='native_game_view_capture':
        header=target.read_bytes()[:24]
        assert header[:8]==b'\x89PNG\r\n\x1a\n'
        entry['width'],entry['height']=struct.unpack('>II',header[16:24])
    files.append(entry)

for i,name in enumerate(order,1):copy_checked(SOURCE/name,DEST/f'{i:02d}_{name}','native_game_view_capture')
copy_checked(UNITY/'Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md',DEST/'Opening_Immersive_Cross_Raise_Unity_Handoff.md','original_unity_feedback_report')
copy_checked(SOURCE/'result.json',DEST/'result.json','original_validation_result')
result=json.loads((DEST/'result.json').read_text(encoding='utf-8-sig'))
head=subprocess.check_output(['git','-C',str(UNITY),'rev-parse','HEAD']).decode().strip()
manifest={'task_date':'2026-11-18','archived_date':'2026-11-19','timezone':'Asia/Shanghai',
 'source_project_head_at_copy':head,'source_root_example':str(UNITY),'source_paths_are_relative_to_unity_root':True,
 'screenshot_count':len(order),'rule':'ForDesignScreenShot/YYYY-MM-DD_for-<round>/NN_original-name.png',
 'method':'copies only; no crops, resizing, annotations or source moves',
 'runtime_evidence':'tool-driven actual Unity Editor Play Mode; not a physical-input full-route playtest',
 'owner_acceptance':result['owner_acceptance'],'raw_console_and_driver':'remain in the source Unity_Trial directory',
 'files':files}
(DEST/'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'destination':str(DEST),'screenshots':len(order),'total_files_verified':len(files),'total_bytes':sum(f['bytes'] for f in files),'all_source_hashes_match':True},ensure_ascii=False))
