"""Archive owner downloads, record the 2026-11-14 decision, stage a reversible Unity trial.

Run from any directory with the bundled Python runtime. No image pixels are edited.
Network copy and Codex dispatch are separate steps; this script never claims execution.
"""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
MJ = ROOT / 'MJ_ref/Slideshow/Opening_v1'
ART = ROOT / 'TechArtAsset/Storyboards/Opening_v1/placeholder'
DROP = ROOT / 'TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder'
for p in (MJ, ART, DROP / 'Art', DROP / 'Docs'):
    p.mkdir(parents=True, exist_ok=True)

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

downloads = [
 ('psamead_A_gentle_hand-painted_story_illustration_for_The_Fairy__95a12e36-46aa-43e9-9d41-5c5ea9888e99.png', 'OP01_MJ_r04_U4_candidate_v1.png', [1456,816]),
 ('psamead_A_gentle_hand-painted_story_illustration_for_The_Fairy__36b2593f-0c39-4b78-aff4-db5cc7017613.png', 'OP01_MJ_r04_U4_upscale_candidate_v1.png', [2912,1632]),
]
records = []
for original, new, size in downloads:
    source, target = ROOT/'MJ_ref'/original, MJ/new
    if source.exists():
        if target.exists():
            raise FileExistsError(target)
        source.rename(target)
    if not target.exists():
        raise FileNotFoundError(target)
    records.append(dict(original_download_name=original, file=target.relative_to(ROOT).as_posix(), dimensions=size, sha256=sha(target), provenance='Owner downloaded from Discord; composition matches r04 U4. Original filename UUID is not asserted to be the parent generation job ID.'))
source = MJ/'OP01_MJ_r04_U4_upscale_candidate_v1.png'
asset = ART/'OP01_friends_dusk_placeholder_v1.png'
shutil.copy2(source, asset)
shutil.copy2(asset, DROP/'Art'/asset.name)

manifest_path = MJ/'generation_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
manifest['status'] = 'OP01_upscale_authorized_as_Unity_placeholder_2026-11-14'
manifest['final_art_status'] = 'not_approved_placeholder_only'
manifest['owner_downloads_2026_11_14'] = records
manifest['placeholder'] = {'file':asset.relative_to(ROOT).as_posix(), 'source':source.relative_to(ROOT).as_posix(), 'sha256':sha(asset), 'pixel_processing':'none; lossless file copy; retain native aspect 2912:1632', 'approval':'Owner explicitly authorized temporary Unity trial, not final character art approval', 'known_issues':['Characters too chibi and outer contours too strong', 'Niamh eyes green rather than reference grey', 'Costume and relic continuity require final-art review'], 'OP02_OP03':'No dedicated final images. Reuse OP01 temporarily with separate text beats; never claim three completed illustrations.'}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

write('TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md', '''
# 开场故事画与章节过渡知识库

更新：2026-11-14。项目：The Fairy Hills。对象：负责人、学生、美术、制作与排版人员及任意后续 Agent。
用途：独立于聊天保留来源、审美判断、失败经验和 Unity 接手依据。当前任务是占位试装；正式美术和用户游戏内验收未完成。

## 先看当前决定

负责人选择 r04 U4 的双人黄昏草坡图放大，批准临时用于开场与第一章封面。背景色彩、草地和人物神态较接近；人物仍偏 Q、外轮廓过强、妮芙眼睛偏绿。批准占位不等于角色或画风定稿，不回写角色 v3 基准。

- 来源、原下载名、尺寸与 SHA-256：`MJ_ref/Slideshow/Opening_v1/generation_manifest.json`。
- MJ 原始单图：`MJ_ref/Slideshow/Opening_v1/OP01_MJ_r04_U4_candidate_v1.png`，1456×816。
- MJ 放大原图：同目录 `OP01_MJ_r04_U4_upscale_candidate_v1.png`，2912×1632。
- 游戏占位副本：`TechArtAsset/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png`。像素未改动，文件散列与放大原图一致。
- OP02/OP03 无专门成片。本轮用同一张 OP01 做三个独立字幕节拍，仅供流程和阅读节奏试玩。后续只换数据中的图片即可。

## 风格的判断顺序

人物以 `MJ_ref/NIAMH_REF_v3.png`、`OISIN_REF_v3.png` 及各自朝右侧面定稿为身份与手绘处理基准；环境以 `S1_VILLAGE_KEY_03_pan_empty.png` 和村庄实机为准。`MENU_BG_16x9.png` 可辅助判断环境色块与线条，不能把夜间菜单配色强加给黄昏开场。

原角色本身有适度大头，负责人反对的是新图进一步夸张、深色轮廓像贴纸、笔触过硬。不要把“降低 Q 感”直接翻译成写实长身人物。妮芙金发灰眼绿披风，奥伊芯红发琥珀眼、花冠红披肩；衣装与饰物分属各自角色。开场妮芙没有十字架：此前已交给奥伊芯，后来在森林捡回。未在图中清楚画出圣物不等于改变设定。

## 本轮实测经验与适用边界

### 参考图上传与聊天上下文

现象：网页参考图上传卡住；负责人改用 Discord 上传后成功生成。仅在提示词写“参照角色图”或“右下参考”，并不证明图已作为本任务输入。聊天中存在附件也不等于后续任务自动引用了附件。做法：核对实际请求中的图像引用和用途，保存完整提示词、实际参数和截图；不知道的字段写待核实。此处记录的是本轮现象，不推定服务端故障原因。

### 比例描述引起漂移

现象：强调更小头眼、更长四肢的一组结果变成另一种绘画风格，角色五官、比例和衣装偏远。可能与文字重心、缺少有效角色参考及模型解释有关，根因未隔离。做法：避免将人物比例和笔触一起大改；每批只检验一个目标。背景满意不能代替角色一致性验收。

### Vary (Subtle) 未编辑提示词

现象：负责人两次点击后直接生成，没有出现可编辑提示词窗口；新图继续保留偏 Q 和较重的外轮廓。事实：建议追加的细棕线文字没有在这两次操作中确认提交。不要把这些结果记成“已测试新提示词”或继续保证点该按钮一定弹框。是否存在额外模式设置及当前版本支持情况尚未核查；若以后再试，先验证编辑入口，再花生成额度。

### 两个人物区域重绘

现象：把两人都完整选中并替换提示词后，生成了偏写实的背影，角色身份和朝向漂移。遮罩允许重建选区，文字“保留原姿势”没有提供可靠的身份约束。此结果不采用。完整 prompt 与遮罩/结果截图见 `MJ_ref/Slideshow/Opening_v1/evidence/`。

### 单个人物区域重绘

现象：只选中完整妮芙，输入角色与柔和线条描述，四个结果均把妮芙替换成背景或花。原因未隔离，不能断言模型为何忽略人物。实证结论：此轮整人物遮罩没有保住角色，不能当作稳定的线条修正方法。停止同一操作的无目标重试，保留最接近候选先验证游戏流程。以后若修图，另存源文件、对照图、遮罩和可回退版本；Photoshop 局部处理尚未执行，不得写为已修好。

## Unity 占位制作与借鉴守灯人

复用方法：数据保存每页图片、字幕、时长、推拉范围；双 RawImage 过渡；输入锁；跳页/跳过；结束时只加载一次下一场。参考 `TheLanternKeeper2D` 的 StoryboardData/StoryboardPlayer 和设计经验，不复制其美术或剧情。

需检查的既有教训：推镜每页独立归一，跳页时无突然反向跳动；检查真实 `Time.timeScale=1`，不照搬其项目数值；字幕不能遮脸和越出屏幕，字幕与按钮分别留位；完成后退出 Play Mode，只留 MainMenu，避免堆叠场景。上述是守灯人已遇问题的迁移检查项，不代表妖精丘陵已经出现或已修复。

本轮流程：MainMenu Play → OP01/02/03 三个占位字幕节拍 → CHAPTER I / THE THRESHOLD（工作标题）→ 原有村庄出生点。第二、三节拍复用 OP01，故事由英文字幕说明，不能冒称画面已经表现了召唤和追赶。正式 OP02/OP03 的分镜仍看 `TechnicalArt/SLIDESHOW_OPENING_v1.md`。

只做第一章开头。普通村庄→森林换场不显示新章节。S2–S4、第二章、想象之眼主线及新 Niamh 动作是后续制作，Demo 第一、二章范围不缩减。

## 状态与资料索引

人读当前版：`TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`。v1 制作单保留为生图前历史快照。
Unity 执行任务：`CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`。
本地续接：`STORYBOARD_RESUME.md`。素材包：`TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder/`。
Unity 反馈约定：`Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md`；没有此反馈或实际场景证据时，不能把素材复制说成已接入/已运行。
''')

write('CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md', '''
# 2026-11-14 开场故事引入与第一章封面占位试装

项目/读者：The Fairy Hills；Unity Codex/制作人员、负责人、学生与后续 Agent。
状态：用户已授权执行；素材与任务包由设计端预先复制。实际启动、接入、编译、Play Mode 与用户验收须写回反馈，不能由本任务单推定。
目标：从菜单 Play 体验故事引入、第一章封面，再在现有村庄控制妮芙；用户下次在新对话查看截图与反馈。
依据：设计 `STORY_BIBLE.md` §8.7–8.9、`DEMO_IMPLEMENTATION_PLAN.md`、`TechnicalArt/SLIDESHOW_OPENING_v1.md`、`CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md`、`STORYBOARD_KNOWLEDGE_BASE.md` 和用户本轮批准占位试装。

## 0. 开始与保护现场

先读工程 AGENTS.md、Docs/AI/UnityProjectContext.md、Docs/Niamh_Motion_v8_Unity_Handoff.md、设计 TechnicalArt/UNITY_AGENT_RULES.md。重新核对 git status 和实际编辑器，旧 context 中“只有静态角色”已被 v8 记录取代。2026-11-14 检查 HEAD 为 3d1b9e6；村庄和两份 TMP 字体有已有改动；音效与 AI docs 有预置未跟踪文件。不要 git reset、全量 add、强推、重建 Village/Forest/Core 或提交他人修改。有可归属的本任务修改才做检查点；否则记录起始 HEAD。

本轮不恢复自动化测试或临时工程。应在实际工程编译和观察 Play Mode（用户已要求跑出效果），结果需证据。遇到场景人工未保存改动先保护，不覆盖。

## 1. 输入已预放，不从 GitHub 取素材

- `Assets/_Project/Art/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png`，2912×1632；保持原像素和宽高比。
- `Docs/References/Opening_Chapter1_Placeholder_v1/opening_sequence_v1.json`：独立图片/字幕/时长数据和已知占位限制。
- 同目录 `transfer_manifest.json`：来源和 SHA-256；先校验再用，已有相同文件不重复复制。
- 设计源在共享网络 `Animation_yichun/ShareWorkFolder/`；当前包中有规格与知识库快照。缺料报精确相对路径、用途与目标路径，通过共享网络补齐；不改写共享原图。

这张画仅获准占位：人物仍偏 Q、轮廓过重、妮芙眼睛偏绿。OP02/03 尚无专门图片，三节拍暂复用同图，由字幕讲故事。不将任何一张标为最终美术或改写角色设定。

## 2. 最小可回退实现

1. 检查现有 MainMenu Start 回调和 ChapterSceneLoader；接入一个可配置 opening sequence。优先沿用已有加载结构、字体与 UI。参考守灯人 Assets/_Project/Scripts/Storyboard/StoryboardData.cs 与 StoryboardPlayer.cs 的数据、淡入和输入流程；适配本工程 Core 加法加载，不直接复制项目依赖或美术。
2. 菜单 Play → 3 个故事节拍 → 第一章封面 → 原村庄出生点。图片用独立配置，便于换正式画。可为序列建独立场景或可卸载 UI，实际方案由现有架构决定，文档写清。单独从 Village/Forest 调试不强制播序章。
3. 三页初值 6、7、6 秒，淡入/交叉淡入约 0.4 秒，轻推近最多 2%；若轻推引起跳页突跳，先关闭推镜保证稳定。每页计时重置，自动/手动换页走同一路径。不能靠调高全局 timeScale 加速；检查为 1。
4. 第一章封面默认沿用该占位图并在 UI 中压暗，叠 `CHAPTER I` 与 `THE THRESHOLD`（可替换工作标题，源于现有设计草稿，非新剧情定案）；约 2 秒，可前进。标题不烘焙进图。放在序章结束和村庄之前，本轮不做第二章封面或新 S2–S4。
5. 图片 Fit/保持比例；16:9 下不拉伸、不裁掉脸和脚。字幕用独立 TMP，在 1920×1080 与 1280×720 检查；必要时给底部独立字幕栏预留位置，避免遮住人物。优先项目已有 OFL 字体并核对英文和 Oisín 的重音。Skip 位于独立安全区，与字幕不重叠。暂不新增配音和未制作的低语。
6. 提供可见 `Next` / `Skip` 按钮及项目支持的键盘输入：Space/Enter 前进、Esc 跳过。末页前进或整段跳过都经过第一章封面并进入相同村庄初始状态；封面可前进。不让同一次按键穿透触发角色跳跃/互动。覆盖双击、连续按键，保证加载完成仅调用一次。
7. 叙事与封面时锁定游戏输入/隐藏玩法 HUD，不让玩家漂移、相机先跑或漏出错误光照。完成、跳过及返回路径释放输入和遮罩；保持 Core、单个 AudioListener、Niamh v8、背包/圣物已有状态结构。新游戏/返回菜单/再次 Play 都应按既有新游戏语义播放一遍，不新增永久存档跳过规则。
8. 音乐沿用当前可用素材做淡出/淡入，具体复用写入反馈。画面加载时不重复播放多个 BGM。

## 3. 同批已授权的声音任务

23 条动作音已在工程中预置，用户已批准试装。先查 `Docs/References/Niamh_Surface_Audio_v1/2026-11-14_Niamh_Surface_Audio_Unity_Trial.md` 是否完成；若尚未完成，在故事序列批次检查点之后按原任务接入并反馈，分别提交。避免把已存在的文件误称为声音已生效。不为木材声音新造木箱。

## 4. 运行与交付

- 在实际工程编译；从 MainMenu 完整播放、手动换页、各页 Skip、封面前进、返回菜单后再次 Play；检查村庄可走跑跳、进森林、v8 未回退、无叠加场景/遮罩/输入锁残留。按当前流程核对音效试玩，尚缺验证明示。
- 截图：三节拍各一张含字幕、封面、进入村庄后的画面；1920×1080，另留一张 1280×720 的字幕/Skip 画面。放在 `Docs/References/Opening_Chapter1_Placeholder_v1/Unity_Trial/`。Recorder 已可用则录正常和跳过各一段短视频；不可用就给截图和观察记录，不安装新包拖延。
- 写 `Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md`：实现路径、配置、采用字体/音乐、实际验证、截图/视频、已知占位问题、回退办法、未验证项、下一步；更新 Docs/CH1_UNITY_PROGRESS.md 与旧 AI context 中被本轮取代的状态，保留日期。
- 如声音执行，单独写 `Docs/Niamh_Surface_Audio_Unity_Handoff.md`，供设计端下次读取。
- 仅提交任务拥有的代码、配置、图片、必要 .meta 与证据/文档；检查 scene/font diff 的归属。按用户此前授权 git push Unity 当前分支，报告提交与推送状态；不推他人改动、不强推。失败写原始原因。
- 退出 Play Mode，卸载临时加载场景，最终只打开 MainMenu，保持方便用户下一次试玩。

## 可直接发送给 Unity Codex

请读取并执行 `Docs/References/Opening_Chapter1_Placeholder_v1/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`。用户已批准用预置 OP01 放大图作为占位，加入菜单 Play 后的故事引入与第一章封面，跑实际工程并留下截图/反馈，按任务处理之前已批准的动作音试装，然后仅提交和推送自己文件。素材和清单已通过共享网络放进工程，设计源只读。下次设计新对话会先读你写的 Handoff，再继续 Niamh 推门与举十字架动作。
''')

sequence = {
 'schema_version':1, 'project':'The Fairy Hills', 'status':'authorized_placeholder_trial_not_final_art',
 'image':'Assets/_Project/Art/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png',
 'image_dimensions':[2912,1632], 'preserve_aspect':True, 'transition_seconds':0.4, 'maximum_zoom':1.02,
 'frames':[
  {'id':'OP01','duration_seconds':6,'caption':'At dusk, the hills were still a place to play.','art_status':'OP01 candidate approved for placeholder'},
  {'id':'OP02','duration_seconds':7,'caption':'Then Oisín heard something Niamh could not.','art_status':'reuses OP01; dedicated summons illustration not produced'},
  {'id':'OP03','duration_seconds':6,'caption':'Oisín ran towards the trees. Niamh followed.','art_status':'reuses OP01; dedicated pursuit illustration not produced'}],
 'chapter_card':{'number':'CHAPTER I','title':'THE THRESHOLD','title_status':'working title from design; configurable','duration_seconds':2,'background':'same placeholder image with runtime UI darkening'},
 'next_scene':'Ch1_S1_Village','standalone_level_debug_plays_opening':False,
 'controls':{'next':['Space','Enter','Next button'],'skip':['Escape','Skip button']},
 'acceptance_pending':['Unity import','Integration','Compilation','Play Mode','Owner review']}
write('TechArtAsset/Storyboards/Opening_v1/placeholder/opening_sequence_v1.json',json.dumps(sequence,ensure_ascii=False,indent=2))
write('TechArtAsset/Storyboards/Opening_v1/placeholder/README.md','''
# 开场占位资产 v1

2026-11-14 负责人批准临时放入 Unity。OP01 原图来自 MJ r04 U4 的用户放大下载，像素未修订。此目录始终为占位状态，不代表最终画风/人物获批。
图片 2912×1632，保持宽高比，游戏由 UI 放置英文字幕与章节标题；不用图像生成文字。人物过 Q、轮廓较重、妮芙灰眼未校正。OP02/OP03 暂时复用同一图，不宣称三张画已完成。
来源与散列见 `MJ_ref/Slideshow/Opening_v1/generation_manifest.json`；可配置序列见 `opening_sequence_v1.json`；执行与验收见本轮任务单。
''')
shutil.copy2(ART/'opening_sequence_v1.json', DROP/'Docs/opening_sequence_v1.json')
for rel in ['TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md', 'CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md', 'TechnicalArt/SLIDESHOW_OPENING_v1.md']:
    shutil.copy2(ROOT/rel, DROP/'Docs'/Path(rel).name)

write('STORYBOARD_RESUME.md','''
# 妖精丘陵：新对话接续入口

日期：2026-11-14；适用于负责人、学生、制作人员与任何后续 Agent。用户暂时转去推进《守灯人》，《妖精丘陵》继续遵守第一、二章 Demo 计划。本文件是本地设计续接说明，不是发给另一台电脑执行的命令。

## 下次从这里开始

1. 读本文件 → `TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md` → `ART_HANDOFF.md` 最新记录，先看可读版 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`。
2. 通过共享网络查 Unity `Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md` 和 `Docs/Niamh_Surface_Audio_Unity_Handoff.md`，以及实际工程 git status/HEAD；记录哪些反馈真实存在。文件尚无时先查本地派发记录，不假设任务已运行。
3. 看三节拍、第一章封面、字幕/Skip、小分辨率和进村庄截图，再核对试玩记录。反馈有缺陷先修；用户下次人工确认画面和听感。素材复制/提交不代表实际运行。
4. 续做 Niamh 动作：以用户修订 `_m` PSD 与 Motion_v8 六部件/Unity 已有七状态为基准；先为现有栅门做伸手/推门，再做举铁十字配合现有红荆棘墙湮灭。先看实际交互和手型/肩部遮挡，再做离线 GIF 审查；批准后另写新任务给 Unity，不重放 v8 历史指令。
5. 然后按 Demo 计划推进 S2–S4、想象之眼获得与现实/幻象切换，在后续主线上再次使用并推动人物互动。想象之眼已升为 Must；不要照旧表推迟到第三章。

## 交接到哪里

- 新任务：`CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`。
- 网络包：`TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder/`。
- Unity 预置图片：`Assets/_Project/Art/Storyboards/Opening_v1/placeholder/`；任务/数据/散列：`Docs/References/Opening_Chapter1_Placeholder_v1/`。
- 本地派发记录：`TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder/dispatch_status.json`。它记的是传输/派发事实，不把待运行写成已完成。

## 当前决定与保留问题

用户批准 r04 U4 放大图占位，正式人物仍需改善偏 Q、重轮廓和眼色。背景整体可用，暂不继续整人物区域重绘：两人重绘变成偏写实背影，单人重绘使妮芙消失。Vary(Subtle)两次未出现提示词框，建议追加的词没有被确认提交。这些是实测结果，根因未隔离。原图、失败提示词和截图已归档；不把占位图当角色定稿。

不因用户切换项目而扩大本轮任务到新场景或完整人物骨骼。现有 WIP 拆件 PSD/PNG 是用户现场，保持原件。设计仓库与 Unity 仓库分开提交；素材优先网络，不从 GitHub 默认下载。
''')

print(json.dumps({'renamed':records,'placeholder':str(asset),'drop':str(DROP)},ensure_ascii=False,indent=2))
