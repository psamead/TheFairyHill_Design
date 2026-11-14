"""Copy approved files to the network Unity checkout; verify every copied byte.

This is a file transfer only. No task, Editor command or remote process is started.
"""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
DROP=ROOT/'TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder'
REF='Docs/References/Opening_Chapter1_Placeholder_v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
previous_manifest=DROP/'transfer_manifest.json'
previous_hashes={f['unity_target']:f['sha256'] for f in json.loads(previous_manifest.read_text(encoding='utf-8'))['files']} if previous_manifest.exists() else {}
sources=[
 ('TechArtAsset/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png','Assets/_Project/Art/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png'),
 ('TechArtAsset/Storyboards/Opening_v1/placeholder/opening_sequence_v1.json',REF+'/opening_sequence_v1.json'),
 ('CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md',REF+'/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md'),
 ('TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md',REF+'/STORYBOARD_KNOWLEDGE_BASE.md'),
 ('TechnicalArt/SLIDESHOW_OPENING_v1.md',REF+'/SLIDESHOW_OPENING_v1.md'),
 ('TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md',REF+'/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md'),
 ('TechnicalArt/UNITY_AGENT_RULES.md',REF+'/UNITY_AGENT_RULES.md'),
 ('TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx',REF+'/妖精丘陵_开场故事画与章节过渡交接_v2.docx'),
]
records=[]
for source,target in sources:
    local=ROOT/source
    if not local.exists():raise FileNotFoundError(local)
    staged=DROP/('Art' if target.startswith('Assets/') else 'Docs')/local.name
    staged.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(local,staged)
    remote=UNITY/target
    remote.parent.mkdir(parents=True,exist_ok=True)
    if remote.exists() and sha(remote)!=sha(local) and sha(remote)!=previous_hashes.get(target):
        raise FileExistsError(f'Different file already staged, inspect before overwrite: {remote}')
    shutil.copy2(local,remote)
    if sha(local)!=sha(remote):raise ValueError(f'Network hash mismatch: {remote}')
    records.append(dict(design_source=source,unity_target=target,sha256=sha(local),bytes=local.stat().st_size,verified=True))
manifest={'schema_version':1,'project':'The Fairy Hills','date':'2026-11-14','status':'copied_over_shared_network_sha256_verified_not_integrated','files':records,'do_not_use_github_for_art':True,'placeholder_not_final_art':True}
for target in [DROP/'transfer_manifest.json',UNITY/REF/'transfer_manifest.json']:
    target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
prompt='请读取并执行 Docs/References/Opening_Chapter1_Placeholder_v1/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md。用户已授权用预置 OP01 放大图占位接入开场故事引入和第一章封面，在实际 Unity 工程跑出效果，记录截图及 Handoff，核对并分批完成之前已批准的动作音试装，然后只提交和推送任务自己的文件。素材已从共享网络复制并核对散列，不从 GitHub 下载美术。保护现有场景和字体人工修改。下次设计新对话先读你的反馈，再继续 Niamh 推门和举十字架动作。'
for target in [DROP/'SEND_TO_UNITY_CODEX.txt',UNITY/REF/'SEND_TO_UNITY_CODEX.txt']:
    target.write_text(prompt+'\n',encoding='utf-8')
status={
 'project':'The Fairy Hills','recorded_date':'2026-11-14','transfer_status':'complete_sha256_verified','files_verified':len(records),
 'agent_dispatch_status':'not_started_no_remote_execution_channel',
 'remote_thread_available':False,
 'execution_attempts':[
 {'method':'Codex app list_threads','result':'Only local host threads returned; no target Unity workstation thread available'},
 {'method':'SSH BatchMode existing access','result':'haoxi-rtx port 22 connection timed out; no remote command executed'},
 {'method':'WinRM existing access','result':'Current authentication requires HTTPS or TrustedHosts configuration; command not executed; security configuration not changed'}],
 'manual_start':'On the Unity workstation, open TheFairyHill2D in its existing Codex chat and paste SEND_TO_UNITY_CODEX.txt.',
 'unity_task':REF+'/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md',
 'expected_feedback':'Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md',
 'integration':'pending','compilation':'not_run','play_mode':'not_run','owner_acceptance':'pending',
 'art_approval':'temporary_placeholder_only'
}
for target in [DROP/'dispatch_status.json',UNITY/REF/'dispatch_status.json']:
    target.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(DROP/'README.md').write_text('''# 开场和第一章封面占位交接包

2026-11-14。Art/ 是获准试装的图；Docs/ 是规格、序列、人读版与任务单快照。transfer_manifest.json 保存来源与 Unity 目标散列，逐文件复制后核对。dispatch_status.json 区分文件传输与远程执行；本轮只有共享复制通道，Agent 尚未启动。

在 Unity 电脑既有 Codex 对话中粘贴 SEND_TO_UNITY_CODEX.txt 即可开始；它执行的是本目录任务，不需要重新选图或获取确认。反馈位置由任务约定。本地设计续接入口在仓库根 STORYBOARD_RESUME.md。
''',encoding='utf-8')
print(json.dumps(status,ensure_ascii=False,indent=2))
