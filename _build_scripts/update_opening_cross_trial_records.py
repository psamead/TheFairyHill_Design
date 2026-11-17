"""Synchronize current design records without rewriting historical snapshots."""
from pathlib import Path
import json,shutil
ROOT=Path(__file__).resolve().parents[1]
UNITY=Path(r'\\haoxi-rtx\C\Users\Administrator\Documents\UnityProject\TheFairyHill2D')
TITLE='2026-11-18 开场界面 按键下划线与举高动作试装'
NOTE='''**2026-11-18 开场界面、按键下划线与举高动作试装：** 已参考双方新导入Claude记录和守灯人实际界面，给现有开场加入保持比例的铺满故事画、柔和底部字幕区与轻量导航；按键字母／名称加下划线。终段受控红墙Q事件采用B直接举高，使用用户原画与新花纹，原墙体消解结束恢复v8。代码和资源已放实际工程，离线C#类型检查通过；Editor导入、Play Mode和用户画面认可仍待验证，没有新增大光束或胸前普通战斗功能。

任务单唯一入口为共享设计目录 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`，对方直接读取，无需复制任务单到Unity工程。当前远程Codex进程尚未启动；反馈以Unity `Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md` 为准。人读版 `TechnicalArt/妖精丘陵_开场界面与举高动作试装_2026-11-18.docx`，完整状态/经验 `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`。用户已授权当前项完成后整理文档并git push，尚未运行的项目继续明确标注待验。
'''
def prepend_after_heading(rel,note):
    p=ROOT/rel;text=p.read_text(encoding='utf-8-sig')
    if note.splitlines()[0] in text:return
    first,rest=text.split('\n',1)
    p.write_text(first+'\n\n'+note+'\n'+rest.lstrip('\n'),encoding='utf-8')
for rel in ['STORYBOARD_RESUME.md','ART_HANDOFF.md','TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md']:
    prepend_after_heading(rel,NOTE)
for rel in ['README.zh-CN.md','README.md']:
    short='**2026-11-18 当前试装：** '+('开场铺满与叠加字幕、按键下划线和红墙前B直接举高已放实际工程，离线C#检查通过；实机待验。任务从共享 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md` 读取，无需复制到对方工程。详见 `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`。' if rel.endswith('zh-CN.md') else 'Immersive story frames/captions, underlined key hints and the direct raised-cross red-wall presentation are in the actual Unity project; offline C# type-check passed, Editor/Play Mode pending. Read the task in shared `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`; do not copy the task into Unity. See `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`.')
    prepend_after_heading(rel,short+'\n')
prepend_after_heading('TechArtAsset/Characters/Niamh/Cross_Actions/README.md','''**2026-11-18 Unity当前试装：** 举高原画已接到原受控红墙Q事件，B直接举高，覆盖原1.9秒墙体反馈后恢复v8，无胸前中间停留；没有新增大光束。350像素新图沿用基础327像素角色的163.5px脚底原点。源码/资源已放实际工程，离线C#检查通过；Editor导入与Play Mode待验。任务单留共享设计目录 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`。下文更早的“未接入”是历史记录。\n''')
for rel in ['TechnicalArt/NIAMH_ANIM_LIST_DEMO.md','TechnicalArt/CH1_UNITY_PROGRESS.md','DESIGN_CHANGES.md']:
    p=ROOT/rel;text=p.read_text(encoding='utf-8-sig')
    if TITLE not in text:p.write_text(text.rstrip()+'\n\n## '+TITLE+'\n\n'+NOTE,encoding='utf-8')
lessons={
 'TechnicalArt/LESSONS_CHARACTER_ANIMATION.md':'''### 2026-11-18 不同宽度动作图的原点与状态恢复

两张动作图为350×699，基础v8部件为327×699，左上人物像素原点相同。Unity新Sprite不能一律底部居中：用原角色的163.5px原点（新图归一化x=0.467142857），保持100PPU和原根缩放，才能避免切姿势时横移。举高时仅隐藏六部件，使用同材质/排序组的覆盖Sprite；结束恢复原可见状态，禁用时清理。不要改写原Animator曲线或用户PSD来迁就试装。当前是源码实现和离线类型检查结果，真实脚底、朝向及恢复仍待Play Mode。

用户选B只规定直接举高；GIF循环时序不决定玩法冷却。当前事件覆盖既有墙体1.9秒反馈，没有新增光束系统。共享任务单和实际运行反馈分别记录。''',
 'TechnicalArt/LESSONS_SCENE_PIPELINE.md':'''### 2026-11-18 故事画阅读与按键提示

对照守灯人实际StoryboardPlayer和截图，借鉴保持比例的铺满画面、字幕按画面留白放置、轻量导航及稳定切关保护。不要直接复制另一游戏夜间色调或扩大剧情范围。现有同图三字幕仍属占位，界面形式改变不代表画风通过。

用户要求按键字母下加线。现有开场静态TMP图集没有下划线字形，直接使用富文本u标签可能无有效显示；本轮以link标记按键并根据字形基线绘制UI线条，保留共享字体。需实机检查换行、动态提示、禁用再启用和小分辨率，不能仅凭C#通过声称可读性通过。

任务单唯一入口在共享设计目录CommandForAgentToInitialRun，由网络电脑Agent直接读取；无需另复制任务单进工程。共享文件可读、Agent启动、Editor编译、Play Mode、构建和用户认可必须区分。'''}
for rel,block in lessons.items():
    p=ROOT/rel;text=p.read_text(encoding='utf-8-sig')
    if block.splitlines()[0] not in text:p.write_text(text.rstrip()+'\n\n'+block+'\n',encoding='utf-8')
rules=ROOT/'TechArtAsset/Characters/Niamh/Cross_Actions/action_usage_rules.json'
data=json.loads(rules.read_text(encoding='utf-8'))
data['implementation_status']['unity_integration']='raised story pose wired to existing controlled-thorn-wall Q event; source and resource applied; Editor import and Play Mode pending'
data['runtime_trial_2026_11_18']={
 'action':'cross_raised_story','variant':'B direct raised; no chest intermediate',
 'trigger':'existing Q IronPulse on a nearby controlled ThornWall with the iron cross',
 'presentation_seconds':1.9,'timing_source':'existing wall glow 0.3s plus dissolve 1.6s; not GIF timing or a cooldown',
 'new_beam_vfx':False,'chest_combat_system_added':False,
 'sprite_resource':'Assets/_Project/Resources/Niamh/CrossRaisedStory.png',
 'ppu':100,'pivot_px':[163.5,0],
 'source_and_resource_applied':True,'offline_csharp_typecheck':'passed',
 'editor_import_verified':False,'playmode_verified':False,'owner_runtime_acceptance':'pending',
 'shared_task':'CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md',
 'task_copy_to_unity_required':False
}
rules.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
implementation='''# Opening interface and raised-cross source trial 2026-11-18

The design workstation applied seven Gameplay scripts and the user-drawn raised-cross Sprite to this actual project. Offline C#9 type-check against the project's 285 assembly references passed; this is not Editor import, Editor compilation or Play Mode acceptance. Existing four protected user-modified paths remain unchanged.

The opening now trials full-bleed cover art, in-picture soft-shaded captions, lighter Next/Skip and underlined keyboard hints. The existing story text, timing, chapter card, load mask and input-release protections remain. The existing controlled ThornWall Q event directly displays the raised pose for its original 0.3s glow + 1.6s dissolve, briefly holds horizontal/jump input, then restores v8. No chest intermediate or new beam system. The 350px sprite uses custom bottom pivot x=163.5px (0.467142857), 100 PPU.

Read the task directly in the shared design repository: `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`. The owner explicitly says no extra task copy in this Unity project. `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/` holds implementation hashes and later actual Editor evidence. No remote process was started by the shared-file handoff.

Expected actual-project feedback: `Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md` and the reference folder's `Unity_Trial/result.json`. Record Editor import/compile, actual callbacks versus hardware input, screenshots, recovery, missing checks and owner acceptance separately. Design documentation and approved push follow the task result. No automated suite or duplicate project.
'''
(UNITY/'Docs/Opening_Immersive_Cross_Raise_Implementation.md').write_text(implementation,encoding='utf-8')
for rel in ['Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md','Docs/Niamh_Motion_v8_Unity_Handoff.md']:
    p=UNITY/rel;text=p.read_text(encoding='utf-8-sig')
    addition='## 2026-11-18 Source trial pending actual Editor check\n\nNew interface/key underline and raised-cross presentation source was applied after the historical results above. See `Docs/Opening_Immersive_Cross_Raise_Implementation.md`; the shared design task is the sole execution instruction. Offline type-check passed; this dated update does not extend the old Play Mode evidence to the new changes.\n'
    if addition.splitlines()[0] not in text:p.write_text(text.rstrip()+'\n\n'+addition,encoding='utf-8')
print('Current design, human/agent links, rules and Unity source status synchronized.')
