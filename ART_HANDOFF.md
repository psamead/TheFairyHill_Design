<!-- 美术交接文件：给新对话（美术宣传 + 技术美术）、Codex 和日后追踪用。2026-10-12 由故事框架对话拆出。 -->

# ART_HANDOFF：《The Fairy Hills》美术宣传 + 技术美术交接

## 0. 怎么用这份文件

- 这是**美术对话项**的起点。故事框架对话项已完成，故事与玩法以 `STORY_BIBLE.md`（v2.2）和 `handoff.md` 为准；美术工作以本文件为准。
- 新对话开始时先读：本文件 → `STORY_BIBLE.md` → `MJ_ref/ASSETS.md` → `AGENT_PROCESS_GUIDELINES.md`（第 5 章的 Midjourney 实操经验）。做场景前再读 `TechnicalArt/SCENE_SCALE_SPEC.md`（比例与跳跃尺度）和 `TechnicalArt/CH1_SCENE_PLAN.md`（第一章场景计划）。把场景放进 Unity 时读 `TechnicalArt/CH1_UNITY_HANDOFF.md`，再读 `TechnicalArt/CH1_UNITY_REVISION_v2.md`（试玩后的 7 条修改）；做新场景前先读经验库 `TechnicalArt/LESSONS_SCENE_PIPELINE.md`；给另一台电脑上 Codex 的任务指令在 `CommandForAgentToInitialRun/`。
- **设定可以改，但要走流程**：故事设定仍会影响美术，美术中也可能发现需要修改设定。任何修改先登记到根目录 `DESIGN_CHANGES.md`。只改美术细节的可以直接改并登记；涉及故事含义的只登记为「提议」，等用户确认后再改 `STORY_BIBLE.md`。需要查原因时回到故事框架对话项的记录。
- 每完成一项，在第 6 节的待办前把 ☐ 改为 ☑，并在第 9 节「变更记录」写一行。
- **同步给人读的 Word 文档**（用户 2026-10-26 要求）：改动 md 时，也同步到对应 Word——概念设计说明（`StoryDesign/妖精丘陵_概念设计说明_m_故事v2.2更新.docx`）、Demo 实施说明（由 `DEMO_IMPLEMENTATION_PLAN.md` 用 pandoc 重新生成）、`TechnicalArt/` 的技术美术方案与美术方向。改前先把旧版复制进 `deprecated/`（重名加 `_m` / `_m2`…）。Word 自动修改脚本在 `TechnicalArt/tools/`（PowerShell + Word COM）。

## 1. 项目速览

- 游戏：《The Fairy Hills》（中文工作名《妖精丘陵》），2D 横版叙事解谜，爱尔兰神话题材。原作者：YiChun Jiang；协作：Psamead。
- 引擎 Unity（URP 2D）；平台 PC + Web（WebGL，itch.io）。
- 游戏内文字、标题、菜单**只用英文**；爱尔兰语只作设定背景，只引用核实过的真实地名（Cnoc na Sí、Brú na Bóinne）。
- 策略：短周期「垂直切片」Demo（第一、二章，S1–S4），对标实际独立游戏，保留继续开发的可能。范围以 `DEMO_IMPLEMENTATION_PLAN.md` 的 MoSCoW 为准。

## 2. 关键决定（2026-10-12）

| 项目 | 决定 |
|---|---|
| 画面风格 | **手绘高清 2D + 骨骼动画**（呈现方式参照《空洞骑士》，配色与笔触保持绘本水彩风）。**取代此前的像素方案**：480×270、Pixel Perfect Camera、Tilemap、32×48 px 精灵、像素字体全部作废 |
| 背景 | Midjourney 概念图 → 拆 5 层（天空 / 远景 / 中景 / 可行走层 / 前景）→ 补画 → 统一 LUT 调色 → 直接作为游戏资产 |
| 角色 | 定稿立绘（3/4 侧面朝右）→ 拆件 PSB → Unity PSD Importer + 2D Animation 绑骨骼 → 做动作。不做逐帧 |
| 规格 | 参考分辨率 1920×1080（Web 默认 1280×720）；PPU 100；妮芙屏幕高约 200–220 px，部件按 2 倍绘制 |
| 平台顺序 | **先完成 PC 版，Web 版之后再考虑**。制作阶段不为 Web 压缩资产，但保留高质量源文件并按场景分开存放；Web 版的体积预算（≤ 50 MB、Addressables 分包、图集 ≤ 2048²）到时再处理 |
| 字体 | 标题 Uncial Antiqua；菜单标题 Fondamento；菜单与对话 Alegreya；过场字幕 IM Fell English（2026-10-13 确认，像素字体作废） |
| 文件分工 | 宣传美术（海报、菜单主视觉、标题字、短片）和技术美术（游戏内资产与管线）分开管理，见第 3 节 |
| 森林照明（2026-11-04 定） | 《空洞骑士》Deepnest 式暗场：环境光冷蓝 `#6878A0` 0.28；天空 / 远林 Unlit 压成暗蓝（`#38445C` / `#262F42`）；前景纯黑剪影（`#08090E`）；妮芙身上**暖光**点光 `#FFE2B8`、半径 5.5u，是画面最亮处；辅助灯只留三叶草光点、十字架金光、荆棘墙红光、出口冷紫光。定稿参考图 `TechnicalArt/mock/FOREST_LIGHTING_TARGET_warm.jpg`；以后的暗场关卡（S2 以后）沿用这套思路 |

完整规格见 Word：`TechnicalArt/妖精丘陵_技术美术方案_手绘高清与骨骼动画.docx`。

## 3. 文件夹约定

| 位置 | 放什么 | 读者 |
|---|---|---|
| 根目录 `*.md` | 给 Agent / Codex 读的说明（本文件、handoff、STORY_BIBLE、ART_DIRECTION、DEMO_IMPLEMENTATION_PLAN、AGENT_PROCESS_GUIDELINES） | Agent |
| `StoryDesign/` | 故事、设计、市场等给人看的 Word / Excel | 人 |
| `TechnicalArt/` | 美术相关给人看的文档：技术美术方案、宣传美术方向（《美术方向：关键场景 · 标题 · 字体》）、《标题字体与引擎决定》表 | 人 |
| `TechArtAsset/` | **做好的**游戏资产（分层背景、角色 PSB 与图集、特效、UI、菜单） | 人 + Unity |
| `MJ_ref/` | 参考图、Midjourney 生成图、裁切图、`ASSETS.md` 总表 | 人 + Agent |
| `diagrams/` | 故事图表 | 人 + Agent |
| `deprecated/` | 旧版本（用户手动移入） | — |

规则：新版本另存新文件名，不覆盖用户编辑过的文件；写入前比对设备上文件的修改时间。`TechArtAsset/` 子目录与命名：

```text
TechArtAsset/Scenes/<Scene>/<Scene>_L0_Sky.png … _L4_Fore.png, <Scene>_LUT.png
TechArtAsset/Characters/<Char>/<Char>_rig.psb, <Char>_parts.png
TechArtAsset/FX/   TechArtAsset/UI/   TechArtAsset/Menu/
```

## 4. 与美术有关的故事约束（v2.2 摘要）

- **妮芙 Niamh**（玩家，「锁」，媒介后人）：金色长发、家传旧银冠（一颗绿石，冠圈刻欧甘字母）、森林绿短披风带兜帽、奶白裙、绿色绑带中筒靴（v3 定稿，2026-10-16）、小挎包、左半心扣、红绿友谊手绳。主色：奶白 + 森林绿 + 金。
- **奥伊芯 Oisín**（「钥匙」）：短卷红发、玫瑰花冠、奶白钟袖裙、玫瑰红披肩、右半心扣、红绿手绳。主色玫瑰红。**不要**再画「腰间铁钉」（已删除的旧细节）；现有 `Oisin_v2.png` 先不改，下次生成时替换。
- **铁十字**：神族圣物（女王→Ogma→第一代媒介→妮芙家族→妮芙交给奥伊芯保管）。原版造型 = `RELIC_CROSS_REF.png`；妮芙的版本是被代代装饰过的：**暗铁色**铁芯 + 三叶草圆章 + 红绿缠绳与流苏（奥伊芯编的）。第一章挂绳被普卡控制的荆棘扯断，结局两人重新系好 → 需要「断绳 / 新系」两种状态。
- **妖精的两种反应**：被普卡控制（`Corrupted`）= 红眼 / 裂纹，见铁畏惧、冒黑烟退散；未被控制（`Loyal`）= 黄眼，见圣物低头让路。
- **假 Ogma**（普卡假扮的守门贵族）：脸被光晕遮住，看不清；可用 `NOBLE_DARK_REF.png` 改成 Q 版绘本风。
- 三叶草 = 人间与家的象征（和欧甘字母、妖精无关）；四叶草 = 隐藏收集物。
- 欧甘字母：MJ 画不出正确字母，一律在 Unity 里用贴图 / 粒子做。

## 5. 现有资产状态（详见 `MJ_ref/ASSETS.md`）

| 资产 | 状态 | 下一步 |
|---|---|---|
| `Niamh_v3.png` / `NIAMH_REF_v3.png`（PSD：`Niamh_v3_wip.psd`） | **正面 / 背面定稿**（2026-10-16） | 已改：暗铁十字架 + 红绿缠线流苏、左半心扣、红绿手绳、绿色绑带中筒靴。四视图 `Niamh_v3_turnaround.png`（2026-10-17）已完成，朝右侧面为拆件基准；拆件清单见 `TechnicalArt/NIAMH_RIG_PARTS.md` |
| `Oisin_v3.png` / `Oisin_Side_v3_wip.png` / `Oisin_v3_turnaround.png`（PSD 同名） | **四视图定稿**（2026-10-18） | 已改：去铁钉 / 铁钥匙、右半心扣、红绿手绳；朝右侧面为拆件基准。已知差异：侧面披肩为长围巾式，比正面长，拆件时按侧面做 |
| `SunsetWorldEntrance.png` | 定稿（宣传 + 菜单） | — |
| `MENU_BG_16x9.png` + `MENU_LAYOUT_GUIDE.png` | 可用；已放入 `TechArtAsset/Menu/`（MJ_ref 留副本） | 拆 3 层；右下角 MJ 签名需遮盖或补画 |
| `POSTER_BG_2x3.png` + `POSTER_LAYOUT_GUIDE.png` | 临时 | 编辑器 2:3 向上扩天空，再合成两人背影 + 标题 |
| 原作者新稿 10 张（NOBLE_DARK / LANTERN_SPIRIT / RELIC_CROSS / ANCIENT_MEDIATOR / ANCIENT_FRIEND / BANSHEE / FOREST_A / FOREST_B / VILLAGE_FIELD / WOOD_WALL） | 参考 | 用途见 `STORY_BIBLE.md` §8.10；角色稿需改 Q 版绘本风 |
| 原始设计稿（ORIGINAL_SHEET、SKETCH_1–3、LANDSCAPE_REF 等） | 参考 | — |
| **第一章场景：S1 黄昏村庄**（`TechArtAsset/Scenes/S1_Village/`） | **背景五层 + 可行走物件 v1 通过**（2026-10-29） | 放进 Unity（`CH1_UNITY_HANDOFF.md`） |
| **第一章场景：森林小径**（`TechArtAsset/Scenes/S1b_ForestPath/`） | **背景 + 地沟 + 荆棘丛 / 铁十字 / 荆棘墙 v1 通过**（2026-10-29） | 放进 Unity；荆棘墙红光与驱散特效在 Unity 做 |
| S2–S4 场景 | 只有灰盒与计划（`CH1_SCENE_PLAN.md`） | 下一步：S2 出图 |

### 5.1 原作者新稿 L7/66（2026-10-26，**只作参考，不直接用**）

副本在 `MJ_ref/AUTHOR_L7_66/`（原图在 `L7/66/`，不动）。用户决定：
- **画面风格仍以我们现有的为准**（两位女主 v3、菜单、海报）。原稿单张都很精细，但放在一起会互相争抢、没有主次和前后层次，不适合直接当游戏画面。
- **游戏体量不变**，仍按 Demo 计划（第一章 S1–S3 + 第二章 S4）。
- 这批图证明相关内容已经考虑过；做到对应场景 / 角色时，**按需**取其中能用的构图、道具、造型，简化后改成我们的风格（降低细节密度、拉开前后景明暗），不是全部重做。

| 副本文件 | 对应 | 可借用的地方 | 何时用 |
|---|---|---|---|
| `S01_VILLAGE_REF.png` | S1 黄昏村庄 | 村庄布局、远处山丘古墓 | Demo |
| `S02_TOMB_ENTRANCE_REF.png` | S2 古墓入口 | 三曲枝刻石、门洞构图 | Demo |
| `S03_TOMB_CORRIDOR_REF.png` | S3 古墓石廊 | 青绿妖火火把；墙上两个小女孩涂鸦（记忆碎片） | Demo |
| `S04_VINE_HALL_REF.png` | S4 藤蔓门厅 | 石门 + 兜帽假 Ogma 的站位 | Demo |
| `S05_STONE_CIRCLE_REF.png` / `S05_STONE_CIRCLE_OTHERWORLD_REF.png` | S5 巨石阵（表 / 里世界） | 两种色调对照 | 第三章（Demo 后） |
| `S06_WITHERED_FOREST_REF.png` | S6 枯萎森林 | 石子箭头 + 圆圈的足迹标记 | 第三章 |
| `S09_THORN_QUEEN_COURT_REF.png` | S9 荆棘女王之庭 | 奥伊芯在女王怀中沉睡的构图 | 第四章 |
| `S10_HOMECOMING_DAWN_REF.png` | S10 归途·黎明 | 两人牵手跑出古墓 | 第五章 / 宣传图 |
| `PUCA_REF_1.png` / `PUCA_FORMS_REF.png` | 普卡 | 黑羽毛团 + 金眼；兔 / 山羊 / 马 / 乌鸦变身与切换过程 | 第三章；第二章结尾卡的金色眼睛可先借用 |
| `THORN_QUEEN_REF.png` | 荆棘女王 | 三视图、荆棘冠、配色 | 第四章 |
| `K03_KEYART_REF.png` | 宣传图构图 | 多角色主视觉排布（女妖未改） | 横版主视觉 K1W |
| `CROSS_AUTHOR_REF.png` | 妮芙家传十字 | 三叶草圆章、红绿缠绳的细节 | 十字架道具 / 图标时参考；不替换 v3 立绘 |

## 6. 待办

### 6.1 共用（先做）
- ☑ 妮芙标准立绘定稿：正面 / 背面 v3（2026-10-16）+ 四视图（2026-10-17）
- ☑ 奥伊芯 v3 四视图定稿（2026-10-18）

### 6.2 宣传美术（文档：`ART_DIRECTION.md` / `TechnicalArt/` 中的《美术方向：关键场景 · 标题 · 字体》）
- ☑ 标题字：石刻标题牌，Nano Banana 生成（MJ 做不出），两行版用于海报；两行透明底版存于 `MJ_ref/TileArtFont_wip.psd`，已用于开始菜单；单行横版（H 已改大写）备用。Uncial Antiqua 字体文件在 `TechnicalArt/fonts/`
- ☑ 海报 v1（2026-10-18）：`TechArtAsset/Poster/POSTER_v1.png`（源 POSTER_wip.psd）。PS 内容识别向上扩天空；合成两人背影 + 冷蓝 / 暖金光；标题为 Nano Banana 生成的石刻标题牌（三曲枝螺旋 + 结绳纹，Uncial 字体）
- ☐ 横版主视觉 K1W（itch.io 封面 / 视频首帧）
- ☐ 宣传短片 30–60 秒（分镜见 ART_DIRECTION 第 6 章）
- ☑ 开始菜单静态稿 v1（2026-10-23）：`TechArtAsset/Menu/MENU_wip.psd`。BG 去 MJ 签名（BG_clean_signature 层）、左侧压暗（left_dark：用户改为整列纵向渐变，已裁到画布 1920×1080）、左上两行石刻标题牌、Buttons 组：Start / Continue / Settings / Quit（Fondamento 50px，左对齐，整组由用户右移、在标题牌下方居中偏左；Start = 选中态金色 + 发光，其余米白 + 暗描边光）；选中图标 `TechArtAsset/UI/ICON_triskele.png`（金色三曲枝，128px 透明底）
- ☐ 菜单动图录屏（等技术美术的菜单分层与特效完成）

### 6.3 技术美术（文档：`TechnicalArt/妖精丘陵_技术美术方案_手绘高清与骨骼动画.docx`）
- ☐ 妮芙拆件 PSB → Unity 绑骨骼 → 待机 / 走 / 跑 / 跳试做，评估每个角色工时（场景完成后再做；动作以 `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md` 为准，目前是草案：10 个片段，删去攀爬、推石）
- ☐ 菜单背景拆 3 层 + 门洞特效（欧甘字粒子、雾、剪影明暗）
- ☑ **第一章角色比例与跳跃尺度 v1**（2026-10-26）：`TechnicalArt/SCENE_SCALE_SPEC.md` + 参照图 `TechArtAsset/Scenes/_Scale/SCALE_REF_Ch1_v1.png`；妮芙侧面静态图 `TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png`（骨骼动画做好前用于场景合成与灰盒）
- ☑ **第一章灰盒布局 v1 + 场景制作计划**（2026-10-26）：`TechnicalArt/CH1_SCENE_PLAN.md`；每个场景 `TechArtAsset/Scenes/<Scene>/<Scene>_graybox_v1.png` + `_layout_v1.json`（S1_Village / S1b_ForestPath / S2_TombEntrance / S3_TombCorridor / S4_VineHall）；脚本 `TechnicalArt/tools/ch1_layout_v1.json`、`make_graybox.py`、`validate_layout.py`、`make_scale_ref.py`
- ☑ **S1 黄昏村庄背景五层 v9 通过**（2026-10-29）：`TechArtAsset/Scenes/S1_Village/_work/`，脚本 `TechnicalArt/tools/split_s1_layers.py`、`preview_parallax.py`；☑ S1 可行走物件 v1（2026-10-29，`S1_Village/props/`，布局 v2）
- ☑ **森林小径 v1**（2026-10-29）：背景 v6（路面以上整张原图作背景层，不拆前排树干）+ 地沟（Nano Banana 局部重画，`_ditch_fix/`）+ 荆棘丛、铁十字（取自原作者新稿 CROSS_AUTHOR_REF）、荆棘墙；布局 `S1b_ForestPath_layout_v2.json`
- ☑ **S1 + 森林小径放进 Unity 做成可玩场景 v1（课堂演示用，2026-10-29）**：`TechnicalArt/CH1_UNITY_PROGRESS.md` 记录场景、脚本、数值、Play Mode 验收与待办；交接仍以 `TechnicalArt/CH1_UNITY_HANDOFF.md` 为准。
- ☐ **Unity 修改 v2**（2026-10-30 用户试玩后 7 条：栅门拆三块、UI 边框、森林物件夸张放大 + 铁十字揭示、粒子材质、两处前景眩晕、森林草土边、常驻场景架构；另需把用户手动调的高石墙碰撞写进数据）：`TechnicalArt/CH1_UNITY_REVISION_v2.md`，Codex 指令 `CommandForAgentToInitialRun/2026-10-30_Ch1_Revision_v2.md`
- ☐ **待 AI 出图（Nano Banana 2.1）**：~~UI 凯尔特结纹边框~~ 已完成（`TechArtAsset/UI/Frame/UI_frame_celtic.png` 透明版 + `_stone` 石底版）；~~荆棘墙两侧不规则枝条边~~ 已完成
- ☐ S2 古墓入口、S3 古墓石廊（欧甘字谜墙）：出图与拆层（按 CH1_SCENE_PLAN §2–3；**2026-10-27 定：先用 Midjourney 试出图**）；S4 藤蔓门厅已有规划（§3.5），出图在 S1–S3 之后
- ☐ 提灯小妖 Loyal / Corrupted 两套配色；假 Ogma Q 版化
- ☐ 特效：IronPulse 冷光环、Corrupted 退散、Loyal 让路、幻象平台显形、存在值褪色
- ☐ UI：对话框（手绘凯尔特结纹 9-slice）、按钮、图标
- ☐ **背包界面（2026-10-26 新增）**：布挎包底图、分页标签 ×4、物品格三态、详情框、名字布签两态；物品图标（铁十字断绳 / 系好、石牌、发卡、涂鸦碎片、三叶草光点、四叶草）与 HUD 共用。清单见 `INVENTORY_SYSTEM_DESIGN.md` §6
- ☑ 菜单 / 对话字体确认为 Fondamento / Alegreya，已更新 `TechnicalArt/妖精丘陵_标题字体与引擎决定.xlsx`
- ☑ Unity MainMenu 场景与交互 v1（2026-10-24；Play Mode 视觉 / 音频终验待做）：场景、TMP、W/S 与方向键导航、鼠标悬停、静态选中图标、选中提示音及唯一 AudioListener 已接入；进度见 TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md。
- ☑ 开始菜单背景音乐：已将 `TechArtAsset/Audio/MENU_BGM_v1_loop.ogg` 复制到 Unity `Assets/_Project/Audio/Music/`；Streaming / Vorbis，Preload Audio Data 关闭。独立 2D AudioSource：Loop、Play On Awake 开启，音量 0.6；hover chime 仍为 0.35。素材为已确认的无缝循环，不加交叉淡入脚本。用户已在 Play Mode 确认音乐正常播放，且不影响 hover chime。

### 6.4 故事侧仍需补、但影响美术的
- ☐ Demo 对白脚本（第一、二章，英文）
- ☐ 欧甘字谜单词表（决定 S3 / S4 要画哪些石牌）

## 7. Midjourney 经验（摘自 AGENT_PROCESS_GUIDELINES §5）

- 角色：Niji 6 + Character Reference（`--cw` 先低 30–50 让改动生效，定稿后 70–100）；场景 / 道具：V7 或 8.x。设置里的版本会覆盖 prompt 里的 `--v`，先确认。
- 想摆脱原设计配色：Style reference 留空，用 `--no` 排除。
- 局部重画：**只点要改的那一块**（Smart Select 单击，不要拖）→ Erase selection → 短 prompt → Submit edit；一次改一处；保持原图比例。Firefox 上 Erase 笔刷光标可能不显示，可换 Chrome 或用 Smart Select。
- 提交后等出现进度再离开或刷新，否则可能丢失。
- 抽象小道具（铁钉等）容易画错，要么写得很具体，要么只写在设定里。
- 用户上传的图超过约 2 MB 时远程读取容易失败，请用户直接把图拖进对话。
- 不在 prompt 中写具体游戏、作品或艺术家名称。

## 8. 文档构建（给 Agent）

- Word 文档由 Node `docx` 脚本生成，内容模块：`doc_ta.js`（技术美术方案）、`doc_art.js`（宣传美术方向）、`story.js`（故事第 8 章）、`assets.js`（资产表，同时生成 `ASSETS.md`）。脚本打包在根目录 `_build_scripts.zip`；新对话的工作环境里没有这些文件，需要时解压使用（`node build_ta.js <输出目录>`）。
- 每份 Word 交付前转 PDF 逐页检查。

## 9. 变更记录

- 2026-10-30：用户手动微调并保存 Unity 场景 Ch1_S1_Village 中 StoneWall_Tall_1.8u 的 BoxCollider2D：Offset (2.0378294, 0.9)，Size (3.1901226, 1.8)，对象位置 (16.8, 0, 0)。碰撞体比 4.19u 图片窄，以贴合石墙外形；Chapter1SceneBuilder 仍按完整物件宽度生成，重建会覆盖此手动值。详见 TechnicalArt/CH1_UNITY_PROGRESS.md。

- 2026-10-29：S1 黄昏村庄与森林小径已在 Unity 做成可玩场景 v1。MainMenu → S1 → 森林 → MainMenu 路由、1.2u 墙、1.4u 走跳、2.6u 仅跑跳及 3u 荆棘墙 / IronPulse 均在 Play Mode 检查通过；实现与仍需设计/美术跟进项见 `TechnicalArt/CH1_UNITY_PROGRESS.md`。妮芙仍为静态图，IronPulse 为淡出 + 黑烟占位；Cinemachine 未安装，暂用固定 Y 的水平跟随脚本；S2–S4 未制作。

- 2026-10-12：从故事框架对话拆出美术工作；确定手绘高清 + 骨骼动画；新建 `TechnicalArt/` 技术美术方案 Word；像素相关规格在 handoff / Demo 计划 / 美术方向中标为作废。
- 2026-10-13：菜单 / 对话字体确认为 Fondamento / Alegreya；美术方向 Word 与字体决定表移入 `TechnicalArt/`；`MENU_BG_16x9.png` 放入 `TechArtAsset/Menu/`。
- 2026-10-16：妮芙 v3 正 / 背定稿（暗铁十字 + 红绿流苏、左半心扣、手绳、绿色绑带中筒靴）。
- 2026-10-17：妮芙四视图定稿；新建 `TechnicalArt/NIAMH_RIG_PARTS.md`（拆件 / 骨骼清单）。
- 2026-10-18：奥伊芯 v3 四视图定稿；海报 v1 完成（`TechArtAsset/Poster/POSTER_v1.png`）；石刻标题牌由 Nano Banana 生成（MJ 编辑器上传故障期间的替代方案）；Uncial Antiqua 字体放入 `TechnicalArt/fonts/` 并装到本机（PS 需重启才识别）。中间文件 `_preview_title*.jpg`、`POSTER_title_draft.png` 已移入 deprecated/。下一步：开始菜单。
- 2026-10-23：开始菜单静态稿 v1；Fondamento 字体放入 `TechnicalArt/fonts/` 并装到本机；新增 UI 图标 ICON_triskele。用户调整：按钮组右移、left_dark 改为纵向整列渐变并裁到画布；静态稿 v1 定稿。待进 Unity：背景拆 3 层视差 + 门洞特效。
- 2026-10-24：Unity MainMenu v1 已在本机项目 C:\Users\Administrator\Documents\UnityProject\TheFairyHill2D 搭建：W/S 与方向键导航、鼠标悬停选中、图标固定跟随且不旋转、短促合成 hover chime、Main Camera 唯一 AudioListener。Play Mode 视觉与音频终验尚未完成；菜单背景音乐未制作，待办与后续追加列表见 TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md。
- 2026-10-26：接入 MainMenu BGM `MENU_BGM_v1_loop.ogg`；Unity 导入设为 Streaming / Vorbis / preload off，独立 2D AudioSource 循环播放、Play On Awake、音量 0.6。Hover chime 维持 0.35。用户已在 Play Mode 确认音乐播放正常且不干扰 hover chime；最终视觉检查与 Player build 仍未确认。进度见 TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md。
- 2026-10-26：原作者新稿 L7/66（9 张场景 + 普卡 + 荆棘女王 + 十字架 + K03）复制到 `MJ_ref/AUTHOR_L7_66/`。决定：风格沿用现有，体量按 Demo 计划，新稿只作参考、按需简化借用（见 §5.1）。评估表 `TechnicalArt/L7_66_新原画评估.xlsx`。
- 2026-10-26：确认加入背包系统（妮芙的小挎包）；设计 `INVENTORY_SYSTEM_DESIGN.md`；UI 资产加入 §6 待办与 Demo 计划 §6.3。
- 2026-10-26：给人读的 Word 文档补齐近期改动：概念设计说明加 3.3 背包、6.4 音乐与音效、7.7 两位主角 v3 定稿（含四视图）；技术美术方案与美术方向各加「进度更新（2026-10-26）」一章；Demo 实施说明按 md 重新生成（含背包、菜单 BGM）。旧版均已备份到 deprecated/。
- 2026-10-26：**制作顺序调整（用户决定）**：先做第一章场景 S1–S3（及 S4 规划），用妮芙 v3 侧面静态图定角色比例与跳跃尺度；场景完成后再按实际需要的动作做妮芙拆件与骨骼动画，借此删减 Demo 不需要的动作。理由：先有可展示成果给原作者，且拆件需要反复试，需求明确后再做更省工。
- 2026-10-26：第一章场景前期：定角色比例与跳跃尺度（`SCENE_SCALE_SPEC.md`，妮芙 2.1u / 210 px，最高跳 2.4u，走跳 2.3u，跑跳 4.1u）；从四视图抠出妮芙朝右侧面静态图；五个场景的灰盒布局图与布局数据、制作计划（`CH1_SCENE_PLAN.md`：五层出图宽度、借用 L7/66 的取舍、prompt；因 MJ 上传故障，扩图与补层改用 PS 生成式填充 / Nano Banana）；妮芙 Demo 动作清单草案（`NIAMH_ANIM_LIST_DEMO.md`）。技术美术方案 Word 新增「进度更新（2026-10-26 下午）」一章，旧版备份为 deprecated/`妖精丘陵_技术美术方案_手绘高清与骨骼动画_m.docx`。未完成：场景出图（出图方式待用户确定）；S3 掉坑代价暂定存在值 −1，待确认。
- 2026-10-27：用户确定第一章场景**先用 Midjourney 试出图**（prompt 见 CH1_SCENE_PLAN §3）；S3 深坑说明改为「从坑底跳回左侧坑沿（2.0u）」，掉坑代价（存在值 −1）仍待定。
- 2026-10-27：S3 掉坑定为**只从坑底跳回、不扣存在值**（Demo 存在值系统简化）。MJ 编辑器图片上传是否修复未知，用户会再试：修好则扩图 / 补层回到 MJ 编辑器，否则继续用 PS 生成式填充 / Nano Banana。
- 2026-10-27：S1 关键帧定稿 `MJ_ref/S1_VILLAGE_KEY_03_pan.png`（MJ 编辑器扩图可用）；原尺度使用，村舍作中景；自动粗拆五层 + 视差预览在 `TechArtAsset/Scenes/S1_Village/_work/`，待 PS 修补（详见 CH1_SCENE_PLAN §5）。
- 2026-10-27：S1 远景用 MJ 编辑器擦除重画（`S1_VILLAGE_KEY_03_pan_empty.png`）补齐村舍背后；妮芙侧面图重抠（手臂 / 小腿皮肤不再被抠掉，旧版在 deprecated/）。S1 五层视差可用，剩可行走物件待画（CH1_SCENE_PLAN §5）。
- 2026-10-29：S1 背景五层视差 v9 用户确认通过（v1–v8 依次修了：比例、拉伸补色、树线墨线、山脊重影、天空墨点、左上灰绿山坡误判）；经验写入 CH1_SCENE_PLAN §5：被遮挡区域只用真实画面补（原图或 MJ 擦除重画）。
- 2026-10-29：S1 可行走物件完成 v1（低石墙 / 草捆 / 高石墙=低石墙放大 / 木栅门），布局 v2，预览 `_preview_parallax_v10_props.mp4`。
- 2026-10-29：S1 黄昏村庄 v1 完成（背景五层 + 可行走物件，用户确认 v11 预览）；开始森林小径。
- 2026-10-29：森林小径关键帧与扩图完成，自动拆五层 v2（`S1b_ForestPath/_work/_preview_parallax_v2.mp4`），待用户确认；地沟、荆棘物件待做。
- 2026-10-29：森林小径背景 v6 通过（路面以上整张原图作背景层，不拆前排树干）；开始做地沟与荆棘物件。
- 2026-10-29：森林物件 v1：荆棘丛、荆棘墙、铁十字（取自原作者新稿 CROSS_AUTHOR_REF）、两条地沟（脚本挖出，边缘待 PS 手修）；预览 `S1b_ForestPath/_work/_preview_parallax_v7_props.mp4`。
- 2026-10-29：森林地沟改用 Nano Banana 2.1 局部重画后贴回（`_ditch_fix/`，可行走层 `S1b_ForestPath_L3_Walk_ditch_v2.png`），预览 v8。
- 2026-10-29：第一章 S1 + 森林小径美术 v1 完成，准备进 Unity。新增 `TechnicalArt/CH1_UNITY_HANDOFF.md`（单位、相机、五层导入与视差、物件与碰撞、搭建顺序）与 Codex 指令 `CommandForAgentToInitialRun/2026-10-29_Ch1_S1_Forest_Scenes.md`；森林布局 v2。§0、§5、§6.3 已同步。技术美术方案 Word 新增「进度更新（2026-10-29 晚）」，旧版备份为 deprecated/`妖精丘陵_技术美术方案_手绘高清与骨骼动画_m2.docx`。
- 2026-10-30：用户试玩 Unity v1 后提出 7 条修改，写成 `TechnicalArt/CH1_UNITY_REVISION_v2.md` 与 Codex 指令 `CommandForAgentToInitialRun/2026-10-30_Ch1_Revision_v2.md`；新素材：栅门三块、S1 前景 v2（去碎草）、森林草土边、森林物件 v2（荆棘丛 2u / 荆棘墙 6u / 铁十字 1.2u）、`TechArtAsset/FX/` 星星与软圆点、森林布局 v3。新增经验库 `TechnicalArt/LESSONS_SCENE_PIPELINE.md`。
- 2026-10-30：UI 凯尔特结纹边框完成（Nano Banana 2.1，白底生成后抠透明），9-slice 边线 210 px，边上用 Tiled；用法见 `CH1_UNITY_REVISION_v2.md` §2。
- 2026-10-30：荆棘墙边缘用 Nano Banana 2.1 修成自然枝条（719×600），覆盖 `F_prop_thornwall_v2.png`；布局 v3 碰撞只取中间 4.4u。Unity 修改 v2 所需素材全部到位，可交 Codex。

- 2026-10-30：Unity 第一章 v2 实施已写入 `TechnicalArt/CH1_UNITY_PROGRESS.md`：新增 Core_Persistent 常驻场景架构；S1 / 森林场景结构与 MainMenu Start 路由更新；栅门拆层与可逆碰撞；UI 凯尔特框、森林揭示星光与粒子材质、L4 / L3b 视差调整；高石墙及草捆手动碰撞参数写入布局数据并由 builder 保留。Unity MCP 编译和场景结构检查通过；MCP Play Mode 的 `Time.time` 停在 0，未能确认完整的自动启动与交互验收。待在正常推进的 Play Mode 验收门、铁十字跨场景状态、荆棘墙与整体视差观感。后续美术：妮芙骨骼动画、IronPulse 最终光环 / 裂纹 VFX、背包 UI。
- 2026-10-30：Unity S1 草捆视觉对齐更新：`HayBale_0.9u/Visual` 子物件相对根节点左移 1.0u，根节点位置 `(15, 0, 0)` 与碰撞盒 Offset `(-0.15596342, 0.42)` / Size `(1.3790255, 0.84)` 保持不变。当前 Sprite 与 BoxCollider2D 世界包围盒中心分别为 `(14.86, 0.45)` 与 `(14.84, 0.42)`。本地布局数据和 Chapter1SceneBuilder 已记录该 sprite-only offset，后续重建会保留；未重建场景或运行时验证。

- 2026-11-01：Unity 第一章妮芙碰撞体更新：`Core_Persistent.unity` 的 Niamh 使用竖直 CapsuleCollider2D，Size `(0.23, 2.08)`、Offset `(0.08, 1.04)`、Is Trigger 关闭；根节点 `(3.5, 0, 0)`，Rigidbody2D 为 Dynamic、Gravity Scale 0。Chapter1SceneBuilder 已同步该值，重建 Core 时保留；没有重建场景或 Play Mode 验证。
- 2026-11-01：用户第二次试玩后提出 9 条 + 音频，写成 `TechnicalArt/CH1_UNITY_REVISION_v3.md` 与 Codex 指令 `CommandForAgentToInitialRun/2026-11-01_Ch1_Revision_v3.md`。已备：游戏内细框 `TechArtAsset/UI/HUD/UI_frame_thin.png` + `UI_panel_dark.png`；森林荆棘丛 3u（v3）、荆棘墙 9u（v3）+ 红光遮罩、草土边连续、前景 L4_Fore_v2 纵向渐变、布局 v4。**待用户出素材后再交 Codex**：栅门开门图（Nano Banana）、森林中速矮植被带（MJ）、两首 BGM（Lyria）、四个音效（见 `AUDIO_PIPELINE.md` §7）。Codex 已同步妮芙碰撞胶囊 (0.23, 2.08) / Offset (0.08, 1.04)。
- 2026-11-01：v3 素材全部到位：栅门开 / 关两张图（共用 Nano Banana 补全的石柱）、森林中速矮植被层（MJ）、两首 BGM 无缝循环（Lyria + make_loop.py）、四个程序合成音效（make_sfx.py，用户已试听）。可把 `CommandForAgentToInitialRun/2026-11-01_Ch1_Revision_v3.md` 交给 Codex。
- 2026-11-01：新增 `TechnicalArt/UNITY_AGENT_RULES.md`（Unity 环境规则 + 按任务类型决定是否写 PlayMode 自动化测试；开启 Run In Background 解决 Play Mode 不推进）。v3 Codex 指令已加上测试要求。
- 2026-11-01：v3 一次做完 10 条的尝试被用户回滚（Core 提示条未更新、村庄进不去森林）。改为分三批交给 Codex：`CommandForAgentToInitialRun/2026-11-01_Ch1_v3_BatchA_Village_UI.md`（Core 细框 + 栅门）→ `BatchB_Forest_Visuals` → `BatchC_Audio`；每批前先 git commit，不跑自动测试，用户逐批在 Play Mode 确认。原一次性指令移到 `deprecated/`。
- 2026-11-01: Batch A slimmed — art + `S1_Village_layout_v3.json` pre-made (copies in `TechnicalArt/unity_drop/v3_batchA/`) and placed into the Unity project by Claude after the share permission fix (see LESSONS). Old full Batch A → `deprecated/2026-11-01_Ch1_v3_BatchA_Village_UI_full.md`.
- 2026-11-01: Revision v3 Batch A (Village UI) implemented: two-state Village gate and thin/dark 9-slice HUD in Core; rebuilt and saved only Core_Persistent and Ch1_S1_Village. Niamh capsule retained. Forest/MainMenu/build settings unchanged; Village exit x=37.8 still targets Forest. Missing-script scan found zero in all four scenes. Unity Editor build succeeded; automated tests were not run per Batch A rule, so user Play Mode checks remain pending.
- 2026-11-01: Batch B slimmed — forest v4 art + layout placed in the Unity project by Claude (ground extended to x 60 to reach exit 59.5; grass edge as _v3). thornwall_v3.png upload failed, Codex copies it. Old → deprecated/2026-11-01_Ch1_v3_BatchB_Forest_Visuals_full.md.
- 2026-11-01: Revision v3 Batch B (Forest visuals) implemented: imported v4 layers/v3 props; rebuilt only the Forest scene with layout-driven parallax, star reveal, red wall glow/light, IronPulse smoke/fade, and the 60u exit. Unity editor compilation and scene structure checks succeeded; no automated tests were run. User Play Mode visual and interaction checks remain.
- 2026-11-01：用户 Play Mode 确认 Batch A 通过（细框提示、栅门开关、村庄→森林）。Batch B 已由 Codex 完成，待用户验收（视差、星星、荆棘前后、红光、Q→烟雾→墙消失→出口）。下一步 Batch C 音频。
- 2026-11-01：共享素材文件夹改名 `TechArtAsset/Backgrounds` → `TechArtAsset/Scenes`；文档与 `TechnicalArt/tools/*.py` 路径已同步（旧 Codex 指令保持原样作记录）。Unity 工程内 `Assets/_Project/Art/Backgrounds/` 不变。
- 2026-11-01：Claude 现在可直接把素材 / 布局 JSON 写进 Unity 工程（W: = `\\Haoxi-RTX\C`，共享权限给 Administrator 加了 Change）；只能放文件，不能在那边跑命令，git 提交与 C# 由 Codex 做。
- 2026-11-01：用户试玩 Batch A / B 后的修正写成 `TechnicalArt/CH1_UNITY_REVISION_v3_fix.md`。A1：只把栅门**右柱**提到妮芙前面（新图 `TechArtAsset/Scenes/S1_Village/props/S1_prop_gate_postR_front.png`，414×240，与关门图同画布），左柱和门板仍在后面。B1：荆棘墙红光显示成灰白糊状——是 Particles 材质不读 SpriteRenderer 颜色，改写材质 `_BaseColor`，素材不变。B2：森林照明方案（环境光压暗 + 妮芙随身暖光 + 暮光 / 三叶草光点 / 十字架 / 出口辅助灯），解决进森林黑屏。A1 + B1 已发 Codex：`CommandForAgentToInitialRun/2026-11-01_Ch1_v3_Fix_A1_B1.md`；B2 等 A1/B1 验收后再发；Batch C 音频暂缓。
- 2026-11-04：用户确认 A1（栅门右柱）、B1（荆棘墙红光）通过。新问题：烟雾不显示、Console 739 条 `Particle Velocity curves must all be in the same mode`（B3：速度曲线 x/z 模式不一致）；森林被一盏放在 Niamh 下的 Global Light 照成白天。B2 改版为《空洞骑士》Deepnest 式暗场：环境光冷蓝 0.28、远景 Unlit 压暗、前景纯黑剪影、妮芙暖光点光 `#FFE2B8` 5.5u（用户选暖光）、只留三叶草光点 / 十字架 / 红光 / 出口四类辅助灯。效果预览 `TechnicalArt/mock/forest_dark_x20.jpg`（脚本 `tools/mock_forest_dark.py`）。Codex 指令 `CommandForAgentToInitialRun/2026-11-04_Ch1_v3_Fix_B2_B3.md`。
- 2026-11-04：技术美术方案 Word 新增「进度更新（2026-11-04）：v3 试玩修正与森林暗场照明」（含照明定稿图），旧版备份为 deprecated/`妖精丘陵_技术美术方案_手绘高清与骨骼动画_m5.docx`。设计仓库准备公开到 GitHub：`psamead/TheFairyHill_Design`（与 Unity 仓库 `psamead/TheFairyHill2D` 配套）。
- 2026-11-05：B2 暗场与 B3 粒子报错已由 Codex 完成并生效。用户试玩后提出第三轮修正 C（写入 `CH1_UNITY_REVISION_v3_fix.md`）：C1 栅门柱脚碎石堆（新图 `S1_prop_gate_rubble_L/R.png`，脚本 `make_gate_rubble.py`）；C2 光点去掉可见圆点只留光；C3 星星放大、原地呼吸 + 间歇旋转；C4 荆棘丛移到妮芙后面；C5 荆棘墙湮灭加爆闪、烧亮、火星拖尾、发光烟雾。Codex 指令 `CommandForAgentToInitialRun/2026-11-05_Ch1_v3_Fix_C.md`。
- 2026-11-05 下午：第四轮修正 D：右柱碎石放大下移挡住妮芙脚；删除三叶草点光（背景光斑来源）；十字架移到 x 47.8、排在荆棘丛前面，星星在红墙之上；荆棘墙去白边新图 `F_prop_thornwall_v4.png`（`tools/fix_thornwall_edge.py`）。指令 `CommandForAgentToInitialRun/2026-11-05_Ch1_v3_Fix_D.md`。
- 2026-11-05：三叶草光点（ShamrockLight，Demo Must）开始做素材：用户用 Nano Banana 以 CROSS_AUTHOR_REF 的三叶草圆章为参考出图（prompt 见 `CH1_UNITY_REVISION_v3_fix.md` §E），Claude 抠图做光晕与收集特效，再交 Codex。之后用户转去做守灯人。
- 2026-11-05：三叶草光点素材完成：`TechArtAsset/FX/Shamrock/`（128 / 256 图标 + Additive 光晕），脚本 `tools/make_shamrock.py`。Codex 指令 `CommandForAgentToInitialRun/2026-11-05_Ch1_Shamrock_E.md`（排在 v3 fix D 之后）。
- 2026-11-05 傍晚：用户确认三叶草引导与荆棘墙湮灭效果。第五轮修正 F：墙从边缘向中心灼烧消失（溶解遮罩 `F_prop_thornwall_v4_burnmask.png`）；栅门音效 v3（按守灯人菜单音效的做法拆段：吱呀 ×3 变体 + 停住/扣上共用一段，`make_gate_sfx_v3.py`，待用户试听）并随音频批次 C 一起接入；十字架移到 x 46.8、星星 Order 30；主星 pivot 改中心，原地呼吸 + 同步 45° 转动 + 间歇闪光。指令 `CommandForAgentToInitialRun/2026-11-05_Ch1_v3_Fix_F.md`。
- 2026-11-05 傍晚：F 完成并由 Codex 推送 Unity 仓库。第六轮修正 G：烧蚀火线在湮灭前不显示（`_Burn` 从 -0.1 开始）；十字架光晕缩到 1.2u 贴住主星；十字架显现只看距离；audio listener 警告检查。指令 `CommandForAgentToInitialRun/2026-11-05_Ch1_v3_Fix_G.md`。
- 2026-11-05 晚：**第一章 v3 修正（A1–G）全部完成**，用户确认效果基本没问题，场景阶段告一段落。设计仓库 `psamead/TheFairyHill_Design`、Unity 仓库 `psamead/TheFairyHill2D` 均已推送。
  - 留到后面（未做）：转场过渡（淡入淡出 / 场景切换表现）；内容与任务提示、对话框；Batch C 之外的音效细化；三叶草“每 10 个 +1 存在值”（等存在值系统）。
  - **下一步：妮芙骨骼动画制作（开新对话）**。先读 `TechnicalArt/NIAMH_RIG_PARTS.md`（拆件 / 骨骼 / 枢轴）、`TechnicalArt/NIAMH_ANIM_LIST_DEMO.md`（Demo 需要的 10 个动作）、`TechnicalArt/SCENE_SCALE_SPEC.md`（2.1u、走跑跳数值）、`MJ_ref/Niamh_v3_turnaround.png` 与 `Niamh_v3_wip.psd`；Unity 里妮芙目前是静态图 `Niamh_side_static_v3.png`，碰撞胶囊 (0.23, 2.08) / (0.08, 1.04) 不变。
