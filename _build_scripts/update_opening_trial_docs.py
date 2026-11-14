"""Update entry points and archive screenshot evidence; preserve older design snapshots."""
from pathlib import Path
import json
import shutil
ROOT=Path(__file__).resolve().parents[1]
def append(rel,text):
    p=ROOT/rel
    old=p.read_text(encoding='utf-8-sig')
    if text.strip() not in old:
        p.write_text(old.rstrip()+'\n\n'+text.strip()+'\n',encoding='utf-8')
def replace(rel,old,new):
    p=ROOT/rel
    t=p.read_text(encoding='utf-8-sig')
    if old not in t:
        if new in t: return
        raise ValueError((rel,old[:60]))
    p.write_text(t.replace(old,new),encoding='utf-8')

latest='''**2026-11-14 晚间占位交接**：负责人已将 r04 U4 放大图批准用于 Unity 开场与第一章封面占位。新图已按规则命名并保留下载名/散列，正式角色画风未通过。当前人读版为 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`；知识库 `TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md`；下次新对话先读 `STORYBOARD_RESUME.md`。任务与素材包见 `CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`，传输/派发事实见对应 unity_drop 的 `dispatch_status.json`。未收到 Unity 反馈前不称已接入/已运行。'''
for rel in ['ART_HANDOFF.md','handoff.md','TechnicalArt/CH1_UNITY_PROGRESS.md','TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md']:
    append(rel,latest)

p=ROOT/'README.zh-CN.md'
t=p.read_text(encoding='utf-8')
start=t.index('**2026-11-14 最新进度**')
end=t.index('\n\n',start)
t=t[:start]+latest+t[end:]
t=t.replace('Python 音效试听稿在 `TechArtAsset/Audio/SFX/Niamh_Motion_v1/`；尚未人工听感确认或接入 Unity。','Python 音效试听稿在 `TechArtAsset/Audio/SFX/Niamh_Motion_v1/`；负责人已单独试听并批准游戏内试装，23 条 OGG 已网络预置；Unity 接入和游戏内听感尚待反馈。')
p.write_text(t,encoding='utf-8')
replace('README.md', '**2026-11-14 update:** The owner approved the 23 Niamh movement sounds for an in-game trial. They were copied to the Unity project over the shared network and hash-checked; integration is pending. Use [the Unity audio task](CommandForAgentToInitialRun/2026-11-14_Niamh_Surface_Audio_Unity_Trial.md). For the opening slideshow, [four OP01 candidate grids and feedback](MJ_ref/Slideshow/Opening_v1/README.md) are available alongside the [three-shot brief](TechnicalArt/SLIDESHOW_OPENING_v1.md). No image is final or integrated; the Word guide is a pre-generation snapshot.', '**2026-11-14 evening update:** The owner approved the OP01 r04 U4 upscale for a temporary opening sequence and Chapter I cover. Character art remains provisional. Use [the new Unity task](CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md), [knowledge base](TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md), and [next-chat entry point](STORYBOARD_RESUME.md). The readable current Word is `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`; v1 is historical. Assets are staged over the network; read the drop package dispatch status before claiming execution. The previously approved 23 movement sounds are also staged, with in-game integration awaiting feedback.')

replace('TechnicalArt/SLIDESHOW_OPENING_v1.md','**当前状态**：负责人已通过 Discord 为 OP01 生成并下载四组候选，正在比较，尚无定稿、尚未接入 Unity。原图、分轮记录与负责人对第 4 轮左上和右下的评价见 `MJ_ref/Slideshow/Opening_v1/`。OP02、OP03 尚未生成。浏览器控制曾因连接和读取超时受阻，后续由负责人手动操作。','**当前状态（2026-11-14 晚间）**：r04 U4 单图及其 2912×1632 放大图已归档；负责人批准临时进入 Unity，正式画风未获批。OP02/OP03 尚无专门成片，试装时复用 OP01 配三节拍字幕。网络包与任务已准备；实际传输/派发看 unity_drop 的 dispatch_status.json，实际实现与试玩以 Unity Handoff 为准。后续整人物区域重绘导致风格漂移或人物消失，微变未出现提示词框，见 STORYBOARD_KNOWLEDGE_BASE.md。')
replace('TechnicalArt/SLIDESHOW_OPENING_v1.md','**人读版**：[开场故事画制作单](妖精丘陵_开场故事画制作单_v1.docx)，按一镜头一页排版，配现有角色与环境参考；所有参考均明确标为非成片。','**人读当前版**：[开场故事画与章节过渡交接 v2](妖精丘陵_开场故事画与章节过渡交接_v2.docx)。原 v1 制作单保留为生图前分镜快照；当前可执行规格看新任务单。')
append('TechnicalArt/SLIDESHOW_OPENING_v1.md','''## 本轮占位例外与后续正式制作

负责人现已授权用未经最终画风通过的 OP01 放大图先验证故事与第一章封面流程。图在 `TechArtAsset/Storyboards/Opening_v1/placeholder/`，保留 2912×1632 原像素，Unity 保持比例 Fit，不拉伸到 16:9。该例外不把候选升级成最终美术，不要求先生成另外两图才可试流程。三个字幕节拍临时共用一图，约 6/7/6 秒；封面约 2 秒，CHAPTER I / THE THRESHOLD 为可替换工作标题。

本文件中关于模型参数、先后顺序和多人物区域修订的内容是制作计划；实际执行后产生的失败优先按知识库处理，不再建议不验证就重画完整人物。正式 OP02/OP03 仍需按上面的分镜另做，正式交付规格仍保留；新占位文件不可当成三个镜头的定稿。''')
append('TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md',latest)
append('CommandForAgentToInitialRun/README.md','''## 2026-11-14 晚间新增可执行任务

- `2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`：负责人已授权 OP01 放大图占位，要求加开场故事引入、第一章封面并运行。图片/数据/任务包通过网络预放，实际状态看 unity_drop 的 dispatch_status.json 与 Unity Handoff。包含先核对已有动作音任务、未完成则分批执行的要求。
- `../STORYBOARD_RESUME.md` 是本地新对话续接说明，不是另一台机器的执行命令。

本索引较早的“MJ 未提交生成”描述已被晚间记录取代：已产生候选，已批准占位，正式 OP02/OP03 尚未制作。''')
replace('CommandForAgentToInitialRun/README.md','章节故事画在设计端推进，首批分镜见 `../TechnicalArt/SLIDESHOW_OPENING_v1.md`；MJ 操作受连接故障阻挡，当前没有提交生成。Demo 范围仍为第一、二章 S1–S4 与结尾卡，想象之眼为 Must。','章节故事画的首批分镜见 `../TechnicalArt/SLIDESHOW_OPENING_v1.md`；晚间已批准 OP01 候选放大图作为占位进入 Unity。Demo 范围仍为第一、二章 S1–S4 与结尾卡，想象之眼为 Must。')
replace('TechnicalArt/NIAMH_ANIM_LIST_DEMO.md','| 想象之眼 | 推迟到第三章 | Demo 里是 Could |','| 想象之眼 | 2026-11-14 已升为 Demo Must，S3 获得并在后续主线再次使用；反馈可先用现有姿态与视效 | 取代原“推迟第三章 / Could”的旧决定 |')
append('TechnicalArt/NIAMH_ANIM_LIST_DEMO.md','''## 下次动作制作顺序（2026-11-14 晚间接续）

先读 Unity 对本轮开场和声音任务的反馈，再基于用户 `_m` 修订与 Motion_v8 继续现有场景动作：栅门伸手/推门 → 举铁十字与森林红障碍湮灭配合。先审实际交互时机和手型/遮挡，离线 GIF 通过后另给 Unity 新任务。此处是制作计划，推门和举十字仍未制作，不重做已通过的基础走跑跳。''')
append('AGENT_PROCESS_GUIDELINES.md','''## 2026-11-14 晚间：故事画接手与实测补充

本地续接摘要放根目录 `STORYBOARD_RESUME.md`；远程可执行任务放 `CommandForAgentToInitialRun/`，两者用途分开。故事画的可迁移经验与失败边界集中在 `TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md`。用户已批准 OP01 候选图占位试装，必须保留 placeholder 身份、来源和未通过问题；复制到 Unity 不等于自动派发或实际运行。Vary(Subtle)没有出现编辑框时，不把建议追加的提示词记为已测试；完整人物遮罩重绘曾导致身份漂移与人物消失，不再当作可靠的线条修正步骤。''')

readme=ROOT/'MJ_ref/Slideshow/Opening_v1/README.md'
readme.write_text('''# 开场故事画 MJ 制作包

2026-11-14 晚间：负责人将原 r04 U4 单图放大并批准作为 Unity 占位。已归档单图 1456×816 与放大图 2912×1632，原下载名与 SHA-256 见 generation_manifest.json。人物仍偏 Q、轮廓过强，正式画风未通过；OP02/OP03 无专门成片。

- 当前人读版：仓库 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`。v1 是历史分镜快照。
- 当前知识库：`TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md`；本地新对话入口：`STORYBOARD_RESUME.md`。
- 游戏占位副本：`TechArtAsset/Storyboards/Opening_v1/placeholder/`，像素不变，三个字幕节拍共用一图。
- 首四轮原始 WebP 拼图保留；后续过程截图在 `evidence/`，截图不是 MJ 干净原始输出。
- 原分镜 OP01/02/03 prompt 保留为计划；OP01_r05_prompt_draft.txt 是历史草稿，缺少有效图像参考时不能假定“参照原图”文字能引用它。
- 原四轮评价：OP01_比较与反馈_2026-11-14.md；后续实测和占位决定看知识库。
- Unity 执行：`CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`。素材从共享网络复制，派发与运行须有独立证据。

后续如再出正式图，先确认实际模型、引用的角色/风格图与可编辑提示词入口，再小批试验。保存请求、参数、原始输出、选区和结果。不要把截图中 --v 8.2 当成所有历史轮次都经核实的版本；不确定的 job、种子和参数保留待核实。
''',encoding='utf-8')
append('MJ_ref/Slideshow/Opening_v1/OP01_比较与反馈_2026-11-14.md','''## 晚间结果与占位决定

后续纯文字调整一度偏离角色；Vary(Subtle)直接生成，未出现编辑提示词框；整两人重绘转为偏写实背影，只选妮芙的整人重绘则把人物替换成草花背景。上述结果未采用，不能继续称“新词已成功测试”。完整过程见 evidence/ 与知识库。

负责人放大并下载原 r04 U4，批准在 Unity 暂作开场与第一章封面占位。新文件 `OP01_MJ_r04_U4_candidate_v1.png` 和 `OP01_MJ_r04_U4_upscale_candidate_v1.png` 已记录原下载名、尺寸与 SHA-256。背景和人物气质较接近，但偏 Q、重轮廓、妮芙绿眼仍未通过。占位授权不等于正式美术验收；后续正式图另作。''')
append('MJ_ref/ASSETS.md','''## 2026-11-14 开场故事画占位补充

| 文件（MJ_ref 相对路径） | 用途与状态 |
| --- | --- |
| `Slideshow/Opening_v1/OP01_MJ_r04_U4_candidate_v1.png` | 原 r04 U4 单图，1456×816；候选存档 |
| `Slideshow/Opening_v1/OP01_MJ_r04_U4_upscale_candidate_v1.png` | 用户放大下载，2912×1632；批准 Unity 占位，正式画风未通过 |
| `Slideshow/Opening_v1/evidence/` | 后续提示词、遮罩和失败结果截图；仅过程证据 |

原下载名与散列见同目录 generation_manifest.json。游戏使用像素不变的副本 `TechArtAsset/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png`。人物偏 Q、轮廓较重、妮芙眼色需校正；OP02/OP03 无专门图片。

变更：2026-11-14 晚间重命名并归档两个用户下载文件，建立占位授权与生成失败记录。Word 当前资产补充、Prompt 与经验索引收在 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx` 第 2、3、5 页，作为旧概念说明附录 B 与 Prompt 集第 7 章的本轮补充；旧文档保留原件。
''')

evidence=ROOT/'MJ_ref/Slideshow/Opening_v1/evidence'
evidence.mkdir(exist_ok=True)
screens=[
 ('11f10d23-9e98-4156-827f-d7f0ba1be1ae','OP01_r05_style_drift_screenshot'),
 ('73de04dc-cd43-462c-a09f-e4d38384f550','OP01_subtle_heavy_contours_screenshot'),
 ('a5ac4b9f-a7af-4b36-ae3d-8df8e6dbd096','OP01_inpaint_both_mask_prompt_screenshot'),
 ('9e070d46-0ab7-4eda-b234-8af0bd49db1a','OP01_inpaint_both_failed_screenshot'),
 ('07711713-1531-43a1-9543-a22227197dc0','OP01_inpaint_niamh_mask_prompt_screenshot'),
 ('5bc88783-95cd-4a6c-9253-f5d9a33c2329','OP01_inpaint_niamh_disappeared_screenshot'),
 ('34475e79-7df7-4713-a37a-db19811c3baf','OP01_subtle_no_prompt_edit_screenshot')]
saved=[]
for uid,name in screens:
    source=Path('C:/Users/Administrator/AppData/Local/Temp')/('codex-clipboard-'+uid+'.png')
    dest=evidence/(name+'.png')
    if source.exists():
        shutil.copy2(source,dest)
        saved.append(dest.name)
(evidence/'README.md').write_text('''# 本轮操作证据

2026-11-14 用户提供的 Discord 截图副本。截图用于核对选区、输入的提示词和失败结果，不是可进游戏的 MJ 干净成片。图片中账户名、界面按钮和时间属于当时界面证据。公开分享和排版时只摘取与制作有关的画面，保留出处；原截图存档。

两个人物遮罩重绘变成偏写实背影；只选完整妮芙则人物消失；Vary(Subtle)未出现提示词编辑框。原因未隔离。知识库给出适用边界，不能由失败截图推导所有模型均如此。
''',encoding='utf-8')
(evidence/'OP01_inpaint_niamh_failed_prompt.txt').write_text('Niamh, a softly stylized young girl with long pale golden hair, grey eyes, a dark green embroidered cloak and a cream dress. Keep her existing pose, face and childlike proportions. Delicate thin warm brown outlines, soft painted colours and subtle texture, matching a gentle 2D game character illustration.\n',encoding='utf-8')
(evidence/'OP01_inpaint_both_failed_prompt.txt').write_text('Two young friends with gently stylized child proportions, slightly smaller heads and eyes, and naturally longer limbs. Niamh has long pale golden hair, soft grey eyes, a green embroidered cloak and a cream dress. Oisin has short auburn hair, amber eyes, a rose and daisy flower crown, a red patterned shawl and a cream dress.\n\nMatch the soft hand-painted finish of the character references: fine warm brown contours, delicate edges, softly blended colours and subtle fabric details. Preserve their gentle expressions, poses, clothing colours and the existing landscape.\n',encoding='utf-8')
print(json.dumps({'archived_screenshots':saved,'updated':'entry points, assets, knowledge base, animation priority'},ensure_ascii=False))
