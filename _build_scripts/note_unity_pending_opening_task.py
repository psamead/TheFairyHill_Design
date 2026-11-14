"""Append a dated entry point to remote agent docs, preserving previous text."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
note='''## 2026-11-14 晚间：当前已授权的待执行任务

负责人已批准 OP01 放大候选图作为占位，要求接入菜单 Play 后的故事引入与第一章封面，在实际工程运行并回报。任务与素材已通过共享网络预置；读取并执行 `Docs/References/Opening_Chapter1_Placeholder_v1/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`，先核对 transfer_manifest.json。之前批准的动作音任务按该任务单分批核对/执行。

此条是待办入口：设计端只有共享复制通道，未启动远程 Agent，未验证接入、编译或 Play Mode。dispatch_status.json 记录了传输与连接事实，不把复制当执行。完成后写 `Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md`，声音另写 `Docs/Niamh_Surface_Audio_Unity_Handoff.md`，用户下次新对话将先读反馈再继续 Niamh 推门与举十字架动作。

旧接手快照中“妮芙只有静态 Sprite”的状态已被 `Docs/Niamh_Motion_v8_Unity_Handoff.md` 取代；基础 v8 动作已经试玩。保持已有分层角色、输入/碰撞与手调场景/字体。本轮设计端仅追加了 AGENTS.md 和 AI context 的这条待办入口，未改 Unity 代码/场景；将这两处本轮文档改动与原有 AI context 内容区分后再决定提交归属。
'''
for rel in ['AGENTS.md','Docs/AI/UnityProjectContext.md']:
    p=UNITY/rel
    text=p.read_text(encoding='utf-8-sig')
    if note.strip() not in text:
        p.write_text(text.rstrip()+'\n\n'+note,encoding='utf-8')
(ROOT/'TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder/Docs/UNITY_AGENT_PENDING_NOTE.md').write_text(note,encoding='utf-8')
print('Remote AGENTS.md and UnityProjectContext.md: pending task note appended; no process started.')
