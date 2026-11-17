"""Publish the task through the existing shared-file handoff, never claim a process started."""
from pathlib import Path
import hashlib,json,shutil,datetime

ROOT=Path(__file__).resolve().parents[1]
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
DROP=ROOT/'TechnicalArt/unity_drop/2026-11-18_Opening_Immersive_Cross_Raise'
REF=UNITY/'Docs/References/Opening_Immersive_Cross_Raise_2026-11-18'
TASK='2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md'
REF.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((DROP/'implementation_manifest.json').read_text(encoding='utf-8'))
for item in manifest['applied_files']:
    assert sha(UNITY/item['path'])==item['sha256'],item['path']
for rel,digest in manifest['protected_sha256'].items():
    assert sha(UNITY/rel)==digest,rel
for source in [DROP/'implementation_manifest.json',DROP/'compile/final_validation.json',DROP/'compile/final.log']:
    target=REF/('offline_csharp_check.txt' if source.suffix=='.log' else source.name)
    shutil.copy2(source,target)
    assert sha(source)==sha(target)

note='''## 2026-11-18 当前任务 开场界面和举高十字架

设计端已将本轮代码与举高姿势复制进实际工程，离线 C# 类型检查通过，尚未在 Editor 导入/Play Mode 验证。负责人已授权网络电脑 Codex 继续检查。任务单唯一入口留在共享设计仓库 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`，直接从共享目录读取，不复制任务单进Unity工程。沿现有代码做实机检查与最小修复；不要重跑11月14日旧任务或重建关卡。素材/代码散列见 `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/implementation_manifest.json`。

这轮包括守灯人式铺满故事画与叠加字幕、按键字母下划线、Q 对受控红墙时直接举高十字架并恢复。采用 B，无胸前中间停留；保留原墙体效果，不新增大光束。完成后写 `Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md` 和同目录 `Unity_Trial/result.json`。用户要求做完后设计端汇总文档再 git push；网络端本地提交自己的任务文件，暂不 push。保护原场景/字体/AGENTS 修改。文件交接已完成不等于 Codex 已启动。
'''
context=UNITY/'Docs/AI/UnityProjectContext.md'
current=context.read_text(encoding='utf-8-sig')
heading=note.splitlines()[0]
if heading in current:
    assert '任务单唯一入口留在共享设计仓库' in current.split(heading,1)[1],'Review the older handoff note manually before migration'
else:
    context.write_text(current.rstrip()+'\n\n'+note,encoding='utf-8')
# Remove only the unnecessary copies created by this task, after exact content checks.
for name in [TASK,'SEND_TO_UNITY_CODEX.txt']:
    copied=REF/name
    original=(ROOT/'CommandForAgentToInitialRun'/name) if name==TASK else DROP/name
    if copied.exists():
        legacy='请读取本工程 Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md，继续已放入实际工程的开场界面、按键下划线和最终红障碍举高十字架改动。按任务在真实 Editor 编译、Play Mode 检查并修复，保存截图和 Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md；保留已有用户修改，不重建场景、不跑自动测试、不建副本工程。本地提交仅包含任务文件，暂不 push，完成后设计端汇总文档再 push。'
        assert sha(copied)==sha(original) or (name=='SEND_TO_UNITY_CODEX.txt' and copied.read_text(encoding='utf-8').strip()==legacy),str(copied)
        copied.unlink()
pending=REF/'UNITY_AGENT_PENDING_NOTE.md'
if pending.exists():
    assert pending.read_text(encoding='utf-8').startswith(heading),str(pending)
    pending.unlink()
status={
 'date':'2026-11-18','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'handoff_method':'read the single task in the shared design CommandForAgentToInitialRun directory; no Unity task copy',
 'task':str(Path('CommandForAgentToInitialRun')/TASK),
 'unity_task_copy':False,
 'files_transferred_and_sha256_verified':True,
 'source_implementation_applied':True,'offline_csharp_typecheck':'passed',
 'agent_process_started':False,'editor_import_verified':False,'playmode_verified':False,
 'attempts':[
  {'method':'Codex list_threads/list_projects','result':'only local host and projects available'},
  {'method':'existing SSH BatchMode access','result':'haoxi-rtx port 22 timed out'},
  {'method':'existing WinRM access','result':'authentication transport/TrustedHosts configuration rejected; configuration unchanged'}],
 'expected_feedback':'Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md',
 'owner_acceptance':'pending'
}
for p in [DROP/'dispatch_status.json',REF/'dispatch_status.json']:
    p.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Shared task entry and implementation evidence verified. No task copy in Unity; no remote process started.')
