"""Type-check existing/staged gameplay sources against this Unity project's assemblies.
Does not open an Editor, run tests or write into the Unity-generated build folders.
"""
from pathlib import Path
import xml.etree.ElementTree as ET
import subprocess,json
ROOT=Path(__file__).resolve().parent.parent
TASK=ROOT/'TechnicalArt/unity_drop/2026-11-18_Opening_Immersive_Cross_Raise'
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
CSC=Path(r'C:\Program Files\dotnet\sdk\5.0.409\Roslyn\bincore\csc.dll')
OUTPUT=TASK/'compile';OUTPUT.mkdir(exist_ok=True)
tree=ET.parse(UNITY/'TheFairyHills.Gameplay.csproj')
refs=[]
for hint in tree.findall('.//HintPath'):
 p=hint.text
 if p.startswith('C:'):p=r'\\haoxi-rtx\C'+p[2:]
 else:p=str(UNITY/p)
 if Path(p).is_file():refs.append(p)
sources=list((UNITY/'Assets/_Project/Scripts/Gameplay').rglob('*.cs'))
reports=[]
for mode in ['baseline','staged']:
 actual=[]
 for src in sources:
  stage=TASK/'code'/src.name
  backup=TASK/'baseline'/src.name
  if mode=='baseline' and stage.exists() and not backup.exists():continue
  actual.append((backup if backup.exists() else src) if mode=='baseline' else (stage if stage.exists() else src))
 if mode=='staged':
  known={p.name for p in sources}
  actual.extend(p for p in (TASK/'code').glob('*.cs') if p.name not in known)
 rsp=OUTPUT/(mode+'.rsp')
 lines=['/nologo','/target:library','/langversion:9.0','/nostdlib+','/warn:4','/out:"'+str(OUTPUT/(mode+'.dll'))+'"']
 lines+=['/r:"'+r+'"' for r in refs]
 lines+=['"'+str(s)+'"' for s in actual]
 rsp.write_text('\n'.join(lines),encoding='utf-8')
 result=subprocess.run(['dotnet',str(CSC),'@'+str(rsp)],capture_output=True,text=True)
 (OUTPUT/(mode+'.log')).write_text(result.stdout+result.stderr,encoding='utf-8')
 report={'mode':mode,'source_files':len(actual),'references':len(refs),'exit_code':result.returncode,'method':'Roslyn C#9 type-check against actual Unity assemblies; not an Editor compile or Play Mode test'}
 reports.append(report);print(json.dumps(report));print(result.stdout[:10000]);print(result.stderr[:1000])
(OUTPUT/'validation.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
if any(r['exit_code']!=0 for r in reports):raise SystemExit(1)
