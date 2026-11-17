from pathlib import Path
import subprocess,json,math
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
SHARE=ROOT.parents[5]
CLI=r'C:\photocraft-0.5.0\photocraft-cli.exe'
SRC=SHARE/'TechArtAsset/Characters/Niamh/Cross_Actions/sources/user/Niamh_cross_chest_transition_user_source_2026-11-17.psd'
REF=SHARE/'MJ_ref/Characters/Niamh/Interaction_Study_2026-11-17'
def run(src,steps,out):
    args=[CLI,'run',str(src)]
    for c,p in steps:args+=['--cmd',c,'--params',json.dumps(p)]
    args+=['--out',str(out)]
    r=subprocess.run(args,capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stdout+r.stderr)
def export_visible(ids,name):
    steps=[('layer.setProps',{'layer':i,'visible':i in ids}) for i in range(2,14)]
    run(SRC,steps,ROOT/'parts'/name)
export_visible([3,4,5,6,8],'body.png')
export_visible([11,12],'chest_arms.png')
u2=[[600,900],[572,894],[511,876],[485,850],[459,804],[442,760],[431,707],[428,653],[437,583],[443,526],[448,470],[446,427],[431,407],[406,395],[374,390],[351,391],[332,405],[309,422],[298,445],[301,471],[309,492],[311,560],[315,650],[320,730],[324,800],[328,876],[334,924],[350,970],[370,991],[380,1020],[363,1057],[372,1100],[396,1145],[425,1170],[465,1187],[501,1208],[544,1209],[579,1198],[604,1180],[610,1000]]
u1=[[275,801],[300,791],[329,802],[350,825],[373,861],[407,887],[445,909],[499,925],[544,950],[579,987],[602,1041],[610,1100],[612,1210],[585,1190],[550,1190],[513,1198],[476,1190],[440,1173],[405,1137],[370,1090],[337,1041],[319,1002],[311,969],[285,951],[259,929],[250,902],[252,863],[260,828]]
for key,poly in [('U1',u1),('U2',u2)]:
    source=REF/f'Niamh_raise_hands_MJ_r01_{key}_raw_v1.png'
    steps=[('select.lasso',{'points':poly,'feather':1}),('layer.layerMask.revealSelection',{}),('select.deselect',{})]
    run(source,steps,ROOT/'parts'/f'raise_{key}_cut.png')
cross=SHARE/'TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_cross_v2.png'
run(cross,[('edit.transform',{'matrix':[.342,-.940,.940,.342,-10,120]})],ROOT/'parts/cross_vertical.png')
print(ROOT)
