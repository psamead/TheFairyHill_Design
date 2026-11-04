# HANDOFF — 《妖精丘陵 The Fairy Hills》

> 交接对象：后续负责游戏开发 / 程序架构的 Agent（如 Codex）。
> 交接时间：2026-10-11（v1.3：已加入 Demo 实施说明、美术方向、市场定位与前期方案 v2）。2026-10-13 v1.4：同步手绘高清规格、守门贵族改称 Ogma（见 `DESIGN_CHANGES.md`）。阶段：**概念设计完成 v1.1，概念图生成进行中，尚未开始任何代码。**
> 原作者：YiChun Jiang。本文件是摘要；**以 Word 文档为准**（见 §1）。

---

## 1. 必读文件（ShareWorkFolder）

文件夹结构：
- 根目录：给 Agent 读的 md 文件（本文件、STORY_BIBLE、DEMO_IMPLEMENTATION_PLAN、ART_DIRECTION、AGENT_PROCESS_GUIDELINES）
- `StoryDesign/`：给人看的 Word / Excel 文档
- `MJ_ref/`：参考图与生成图（清单见 ASSETS.md）
- `diagrams/`：故事图表
- `deprecated/`：旧版本，不要再引用

文件名中的 `_m`、`_v2`、`_故事v2` 是版本标记，新版本另存新文件，不覆盖旧文件。


| 文件 | 内容 | 何时读 |
|---|---|---|
| `StoryDesign/妖精丘陵_概念设计说明_m_故事v2.2更新.docx` | 世界观、规则、章节、角色、能力系统、道具、场景、美术规格、待确认问题、概念图进展 | **开发前必读** |
| `StoryDesign/妖精丘陵_Midjourney_Prompt集_m_故事v2.2.docx` | 所有概念图 prompt + 实测修订 | 需要补美术参考时 |
| `STORY_BIBLE.md` + `diagrams/STORY_*.png` | **故事 v2 设定**：欧甘契约法典、两条暗线、时间线、结局；含 4 张关系与流程图 | 写剧情、对话、关卡前必读 |
| `DEMO_IMPLEMENTATION_PLAN.md` | **Demo 范围（第一、二章）、MoSCoW 清单、系统规格、资产清单、里程碑、交付清单** | **开发前必读；按此执行和打勾** |
| `ART_DIRECTION.md` | 关键场景 K1–K4、英文标题（排字 + Retexture）、字体系统（含授权）、菜单动图、短片分镜 | 做 UI / 标题 / 菜单 / 宣传时 |
| `StoryDesign/妖精丘陵_市场定位玩家画像与可行性_v2.docx`、`StoryDesign/妖精丘陵_前期方案_平台类型内容策略_v2.docx` | v1（结合前作 2DBattleCarArea 编写）的改写版：短周期垂直切片定位、验证对象、平台、内容划分、后续开发路线 | 了解项目定位 |
| `AGENT_PROCESS_GUIDELINES.md` | 之前 Agent 的工作过程与准则 | 了解协作约定 |
| `MJ_ref/ASSETS.md` | 图片资产清单：每张图的来源、版本、状态，以及变更记录 | **使用或新增图片前必读**，新增图片时同步更新 |
| `MJ_ref/*.png` | 角色 / 道具 / 场景参考图。各文件用途见 Prompt 集 6.6 | 美术资产制作参考。两名主角的当前定稿是 `NIAMH_REF_v2.png` 和 `OISIN_REF_v2.png` |
| `../`（Animation_yichun 根目录）`YiCun_Development.xlsx`、`YiCun_Animate_Prologue.docx`、`L1`–`L6/`、`HW_Doc/` | 用户其他课程 / 开发资料，**之前的 Agent 未读取**，接手时请先查看 | 开始开发前 |

读取 docx：`pandoc -t markdown 文件.docx`。

**协作约定：**
- 不要覆盖用户编辑过的文件。用户改过的版本以 `_m` 后缀标记，新产出另起文件名。
- 原作者的设定要保留。任何改动都标注「改进 / 建议」，待确认的问题请交给用户决定。

---

## 1.3b 美术工作已拆到独立对话

设定修改流程与历史见根目录 **`DESIGN_CHANGES.md`**（两个对话项共用）。

美术宣传与技术美术的全部待办、规格和文件位置见根目录 **`ART_HANDOFF.md`**；给人看的 Word 在 `TechnicalArt/`，做好的游戏资产放 `TechArtAsset/`。本文件只保留故事与玩法。

## 1.4 故事 v2.2（重要，2026-10-12 更新）

故事大背景已改写，**与旧设定冲突时以 `STORY_BIBLE.md` 为准**。要点：
- 千年前，守门贵族 **Ogma** 与人类第一代媒介以交换名字的方式签订《欧甘契约法典》（The Ogham Compact），把两界分隔，所以「名字」有约束力。Ogma 签约后在回去见女王的路上被**普卡之首**（真正的大 Boss）诱杀，普卡从此假扮他。女王因此不知道契约的细节。
- 欧甘文字是人类的创造，通过契约交给了神族。契约有效时，妖精过不来，人也看不见文字。契约在千年间慢慢失效，近年文字散落两界：孩子们先看见文字，继而看见文字所定义的妖精。**游戏里的欧甘石牌就是散落的契约文字。**
- 妮芙是媒介后人，是「锁」；奥伊芯是「钥匙」：Ogma 死后，他所持的钥匙一半化为符文，千年后选中了她。荆棘女王想把钥匙留在里世界，她**不是**最终 Boss；第四章与她有一场 Boss 战：妮芙使用铁的方式是 Ogma 当年亲传给媒介的，女王熟悉这套手法，由此认出 Ogma 已死、身边的贵族是假的，战斗停止。
- **铁十字（v2.2）**：神族圣物，原用于对抗弗魔族，只有高阶者能用。女王赐给 Ogma（信任），Ogma 签约时连同用法交给第一代媒介（信任传递 + 保险）；Ogma 因此回程时无物克制弗魔之力而被普卡所杀。普卡和接受他力量的妖怪**惧怕**铁十字；未被控制的妖精**不怕**，只敬畏，见人类持圣物便放弃命令、让路离开。妮芙的十字是家传，被代代装饰过；她把它交给奥伊芯保管，奥伊芯被召唤途中被树枝刮落在森林，妮芙追来捡回，外观不同于原版（`MJ_ref/RELIC_CROSS_REF.png`）。第四章女王既认出 Ogma 的手法，也感应到自己赐出的圣物。
- 真结局是「重订契约」：文字回归法典，两人回家。看不见不代表失去能力；若将来又有人看见文字，就说明契约又出了问题。
- Demo（第一、二章）只埋伏笔，台词见 `DEMO_IMPLEMENTATION_PLAN.md` §3。图表在 `diagrams/`。注意：「Aos Sí」是妖精族群的统称，不是守门贵族的名字。

## 1.5 本项目范围（重要）

项目对标社会上实际的独立游戏，但当前开发周期短，所以采用「短而有效果」的策略：**本阶段只实现 Demo（垂直切片）**，即第一章 S1–S3 加上第二章 S4 的名字交易，最后接结尾卡，时长约 15–20 分钟。下文 §3–§5 是完整设计，实现时以 `DEMO_IMPLEMENTATION_PLAN.md` 的 Must / Should 为准。标为 Won't 的内容（第三至五章、女妖、Boss、战斗、存档等）**本阶段不要实现，但架构上要预留扩展接口**：数据驱动、章节可追加、NarrativeFlags 可序列化。项目以后要能继续开发下去，后续路线见实施说明第 11 节。

平台：**PC（Windows）+ Web（WebGL，发布到 itch.io）**——**先完成 PC 版，Web 版之后再做**，同一工程双导出；Web 版要注意包体，以及浏览器要求点击后才能播放音频。引擎：**Unity**，使用 URP 2D、2D Animation + PSD Importer（骨骼动画）、Cinemachine、TextMeshPro；参考分辨率 1920×1080（Web 默认 1280×720），PPU 100（v1.4 更新：原 Pixel Perfect Camera 480×270 与 Tilemap 方案已作废，规格见 `ART_HANDOFF.md`）。可参考前作 2DBattleCarArea 的 2D 代码。

语言与字体：游戏内**只用英文**，包括标题、菜单、对话和 UI。文本集中放在数据表里，以后可以加中文。字体都来自 Google Fonts，授权为 SIL OFL：
- 标题：Uncial Antiqua
- 菜单标题：Fondamento（2026-10-13 确认，替换像素字体 Jacquard 24）
- 菜单与对话：Alegreya（2026-10-13 确认，替换 Pixelify Sans）
- 过场字幕：IM Fell English

详见 `ART_DIRECTION.md` §3。**标题只用英文 The Fairy Hills**：先用 Uncial Antiqua 排字，再用 Midjourney Retexture 艺术化（prompt 见 Prompt 集 KT-R）。爱尔兰语和中文都不出现在标题与游戏画面中；爱尔兰语地名（如 Cnoc na Sí）只作为设定背景写在文档里。

三叶草与四叶草：三叶草是人间与家的象征，和欧甘字母、达南神族无关。四叶草是 Could 级的隐藏收集物，拾得后一处幻象平台会显形。出处见 [A10](#a10)，说明见 `DEMO_IMPLEMENTATION_PLAN.md` §11。

### 1.6 原作者新稿（v2.2，`MJ_ref/`）
| 文件 | 用途 |
|---|---|
| `NOBLE_DARK_REF.png` | 普卡假扮的 Ogma（需改 Q 版绘本风） |
| `LANTERN_SPIRIT_REF.png` | 路上小妖：黄眼 = `Loyal`，红眼 / 裂纹变体 = `Corrupted` |
| `RELIC_CROSS_REF.png` | 铁十字圣物原版造型 |
| `ANCIENT_MEDIATOR_REF.png` / `ANCIENT_FRIEND_REF.png` | 千年前第一代媒介与她的朋友（回忆） |
| `BANSHEE_REF.png` | 女妖 |
| `FOREST_A_REF.png` / `FOREST_B_REF.png` | 第一章森林小径（奔跑 / 跳缺口教学） |
| `VILLAGE_FIELD_REF.png` | S1 村庄远景 |
| `WOOD_WALL_REF.png` | 媒介小屋（回忆）或 S3 欧甘字谜墙 |

## 2. 游戏一句话

2D 横版平台探险 + 轻解谜。小女孩**妮芙（Niamh）**没有魔法、不会战斗，为救误入妖精丘陵的挚友**奥伊芯（Oisín）**，在表世界 / 里世界之间穿梭，用「铁、回忆、孩子的视角、真名」破解妖精规则。

- **题材**：爱尔兰神话（[Sídhe / 达南神族 / Aos Sí](#a1)、[欧甘字母 Ogham](#a2)、[Bean Sídhe](#a4)、[Púca](#a5)）。主角名取自 [妮芙与奥伊芯的神话](#a3)。全部出处见 [§9 附录](#9-附录神话出处与参考链接)
- **参考**：《Celeste》的手感，《超级玛丽》的收集节奏
- **游戏内画面**：手绘高清 2D + 骨骼动画（2026-10-12 起取代像素风，见 `ART_HANDOFF.md`）；章节间穿插 2D / 3D 过场动画
- **主题**：救朋友的每一步都在付出代价

---

## 3. 核心系统（程序实现重点）

### 3.1 存在值 Existence（核心资源，HP 的替代）

- **归零**：被同化。坏结局 / 关卡失败。
- **减少**：普卡攻击、触碰妖精食物、处在女妖声波范围内、在交易中付出名字或记忆。
- **增加**：收集三叶草光点、使用「回忆」。
- **视觉**：数值越低，角色越褪色、边缘出现透明抖动（dithering）。UI 用三叶草心形表示。
- **交易会降低上限**：第二章交出名字时，存在值上限 -1。

### 3.2 四项能力

| ID（建议） | 能力 | 输入 | 效果 | 消耗 / 限制 | 解锁 |
|---|---|---|---|---|---|
| `IronPulse` | 圣物之铁（家传铁十字） | 按键 | 冷光环：`Corrupted` 妖怪畏惧受伤退散；`Loyal` 妖精行礼让路、放弃命令；荆棘退开；幻象平台显形 | 冷却时间 | 第一章森林小径捡回 |
| `Remember` | 回忆 | 站定长按 | 消耗「记忆碎片」回复存在值；第五章用于维持奥伊芯不消失 | 记忆碎片数 | 第一章 |
| `ImagineEye` | 想象之眼 | 切换开关 | 蓝色蜡笔滤镜，显示隐藏平台 / 线索并触发剧情 | 持续消耗存在值 | 第三章开头 |
| `TrueName` | 说出真名 | 对目标使用 | 定身 / 解除交易 / Boss 终结技 | 需已知该目标的真名 | 第二章（交出名字则封印到第四章） |

### 3.3 辅助系统

- **OghamStone（欧甘石牌）**：关键收集物，每块一个字母，用于拼字解谜：安抚符文（女妖）、反制符文（贵族交易）、Boss 真名。
  - 字母数量待定：全部 20 个，或精简到 8–10 个。
- **ShamrockLight（三叶草光点）**：普通收集物，代替金币，每收集 X 个回复存在值。
- **Trade（交易）**：普卡 / 贵族提出交易，弹出代价卡（名字 / 记忆 / 承诺）。玩家的选择会改变：
  - NPC 对妮芙的称呼
  - 存在值上限
  - 能力是否可用
- **Assimilation（奥伊芯同化度）**：剧情数值，玩家拖延或反复失败时上升，影响结局动画中奥伊芯的透明程度。
- **Inventory（背包 / 妮芙的小挎包，2026-10-26 新增）**：随时可打开查看铁十字、欧甘石牌、记忆碎片、名字与存在值上限；交易、过场、Boss 战、逃脱段时禁用。只查看与回忆，不做配装。设计见 `INVENTORY_SYSTEM_DESIGN.md`。
- **MemoryFragment（记忆碎片）**：奥伊芯沿路留下的足迹物（发卡、石头标记、墙上涂鸦），回忆能力的燃料。

### 3.4 妖精法则（关卡规则来源）

1. 不吃妖精食物（[A6](#a6)）：触碰会大幅扣存在值。
2. 不随便说出真名。
3. 铁能驱散妖精（[A6](#a6)）——v2.2：只对被普卡控制的妖怪有效，其余妖精只是敬畏让路。
4. 交易必须付出代价。
5. 原路返回：第五章必须按来时收集足迹的顺序返回。
6. 被款待的孩子会被同化（换生灵，[A6](#a6)）。

---

## 4. 章节 → 关卡 → 场景

| 章节 | 关卡要点 | 场景 ID | 对手 / 守护者 |
|---|---|---|---|
| 序 | 过场动画（泥金手抄本风格） | — | — |
| 1 朋友误入（教程） | 移动、跳跃、收集；获得第一块石牌；在森林捡回家传铁十字（妮芙交给奥伊芯保管，奥伊芯被召唤途中被树枝刮落） | S1 黄昏村庄 → 森林小径 → S2 古墓入口 → S3 古墓石廊 | 无 |
| 2 规则 | 名字交易：接受 / 拒绝；第三选项（反制符文）需足够石牌才出现 | S4 藤蔓门厅 | 守门贵族 Ogma（实为普卡之首假扮；v1.4 更新，原写 Aos Sí） |
| 3 穿行 | 追踪足迹；拼字解谜；普卡交易 | S5 巨石阵 / S6 枯萎森林 / S7 哀歌之谷 | 普卡群、女妖 Bean Sídhe |
| 4 真相 | 揭示真相；半心扣合一；Boss 战 | S8 地下神域 → S9 荆棘女王之庭 | 荆棘女王（Boss 战后停战）、假 Ogma 现出原形 |
| 5 回家 | 牵手逃脱，按原路返回 | S10 归途·黎明 | 普卡之首 / 弗魔族入侵 |

**结局：**（v2.2 起以 `STORY_BIBLE.md` §8.5 结局表为准）
- **真结局**：打败 Boss 并原路返回。
- **坏结局**：Boss 战中存在值归零，妮芙留在丘陵里，成为花冠上的一朵花。

**场景主色**（相邻场景刻意拉开反差）：

| 场景 | 主色 |
|---|---|
| S1 | 琥珀金 / 草绿 |
| S2 | 暮紫 / 灰白 |
| S3 | 土褐 / 青绿妖火 |
| S4 | 深青 / 古铜金 |
| S5 | 银灰 / 极光青 |
| S6 | 灰紫 / 骨白 |
| S7 | 月银 / 冰蓝 |
| S8 | 金 / 青绿 / 珍珠白（全作最亮） |
| S9 | 苍白 / 山楂红 / 暗金 |
| S10 | 玫瑰金 / 嫩绿 |

---

## 5. 角色与实体

| 实体 | 类型 | 行为要点 |
|---|---|---|
| Niamh 妮芙（[A3](#a3)） | 玩家 | 动画：待机、走、跑、跳（起跳 / 滞空 / 下落 / 落地）、攀爬、推石、举十字架、回忆、想象之眼、说真名、受击、褪色、牵手同行 |
| Oisín 奥伊芯 | NPC / 护送对象 | 同化三阶段外观；第五章牵手跟随 |
| 守门贵族 Ogma（[A12](#a12)，服饰 [A7](#a7)） | NPC | 第二章出现的是普卡之首假扮的 Ogma，脸被光晕遮住；只交易不战斗；身后的光迹记录玩家的交易选择。真 Ogma 只在回忆中出现（v1.4 更新，原写 Aos Sí） |
| Bean Sídhe 女妖（[A4](#a4)） | 区域守护者 | 不可击败；声波环会碎裂平台并暴露隐藏路径；用安抚符文通过 |
| Púca 普卡（[A5](#a5)） | 敌人 / 向导 / 谜题 | 可变形：兔、山羊、马、乌鸦。眼色表示态度：琥珀 = 中立，绿 = 友好，红 = 敌对。玩家身上有负面状态时会攻击 |
| Hawthorn Queen 荆棘女王（[A9](#a9)） | 妖精族群的统治者（**故事 v2：不是最终 Boss**） | 目标是两界互不侵犯；不知契约细节；想把奥伊芯留在里世界；真结局中代表妖精一方重新签约 |
| 普卡之首 Púca Chief（[A5](#a5)、[A11](#a11)） | **最终 Boss（故事 v2）** | 千年前诱杀守门贵族 Ogma 并假扮他；千年前投靠弗魔族；痛恨欧甘文字与契约；以名字交易夺走媒介的名字 |

---

## 6. 美术规格与资产状态

（v1.4 更新：像素规格作废，以 `ART_HANDOFF.md` 第 2 节为准）

- **角色**：手绘高清，Q 版约 2.5 头身；定稿立绘（3/4 侧面朝右）拆件为 PSB，Unity 2D Animation 绑骨骼，不做逐帧。妮芙屏幕高约 200–220 px，部件按 2 倍绘制。
- **场景**：Midjourney 概念图拆 5 层（天空 / 远景 / 中景 / 可行走层 / 前景）→ 补画 → 统一 LUT 调色，直接作为游戏资产；不使用 Tilemap。
- **想象之眼滤镜**：蓝色蜡笔手绘质感，参考 `MJ_ref/SKETCH_*.png`。

| 资产 | 状态 |
|---|---|
| 妮芙 | **v3 四视图定稿**（`Niamh_v3_turnaround.png`）；拆件清单 `TechnicalArt/NIAMH_RIG_PARTS.md` |
| 奥伊芯 | **v3 四视图定稿**（`Oisin_v3_turnaround.png`）；铁钉已删、右半心扣、手绳 |
| 饰物参考 | `CIRCLET_REF.png`（妮芙银冠）、`HEART_BUCKLE_REF.png`（心形扣，奥伊芯腰间；两人的「半心扣」以此为基准）、`CROSS_v2.png`（十字架造型，颜色待改为暗铁色） |
| 其他角色 / 道具 / 场景 | 只有 prompt，尚未生成 |
| 宣传 / UI | 海报 v1、石刻标题牌、开始菜单静态稿 v1 完成；Unity MainMenu v1 已搭建（见 `TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md`） |
| 关卡美术资产 | 第一章 S1 黄昏村庄、森林小径 v1 完成（分层背景 + 可行走物件，2026-10-29）；Unity 搭建见 `TechnicalArt/CH1_UNITY_HANDOFF.md`；S2–S4 只有灰盒，见 `ART_HANDOFF.md` |
| 音频 | 见下方 6.1 |

### 6.1 音频（2026-10-26 新增，原计划未列）

原游戏计划没有写音频。现定：
- **音乐**：用 Google Lyria 3 Pro（Google AI Studio / Gemini）生成器乐，再处理成无缝循环。制作方法、提示词模板、循环处理脚本见 `TechnicalArt/AUDIO_PIPELINE.md`。
- **已完成**：开始菜单 BGM `TechArtAsset/Audio/MENU_BGM_v1_loop.ogg`（67 秒无缝循环，用户已确认）。
- **音效**：菜单选中提示音目前是 Codex 合成的占位音；其余音效（脚步、铁十字冷光、妖怪退散等）未开始。
- **Demo 需要的音乐清单（建议）**：开始菜单（已完成）、第一章森林、古墓内部、Boss / 普卡之首、结局。每首按同一流程制作。
- **格式**：Unity 项目里只放 `.ogg`；`.wav` 是母带，留在共享文件夹备份。

---

## 7. 待原作者确认（开发前需定）

1. 金发 = 妮芙、红发 = 奥伊芯的对应是否正确？
2. 朋友的名字是否保留 Oisín（神话中为男性名），还是改为女性名（Aoife / Clíodhna）？（游戏内英文拼写）
3. 故事 v2 的四项待确认已全部确定，记录见 `STORY_BIBLE.md` 8.9。
4. 第二章交易是否采用简化版？
5. 欧甘字母用全部 20 个还是精简到 8–10 个？
6. 引擎已定为 Unity，平台为 PC + Web；画面为手绘高清 2D，参考分辨率 1920×1080（Web 默认 1280×720）。

---

## 8. 建议的下一步（游戏开发）

1. **先读资料**：阅读 §1 中尚未读过的 `YiCun_Development.xlsx`、`YiCun_Animate_Prologue.docx`、`L1`–`L6`。与用户确认 §7 的问题。
2. **搭垂直切片（第一章）**：平台移动手感（土狼时间、跳跃缓冲、可变跳跃高度）+ 收集物 + 存在值 + IronPulse，用灰盒关卡 S1–S3。
3. **系统化数据**：交易、法则、石牌、对话改为数据驱动（ScriptableObject / JSON），方便原作者调数值。
4. **建议的架构模块**：
   - `PlayerController`
   - `ExistenceSystem`
   - `AbilitySystem`（下含四项能力）
   - `TradeSystem`
   - `OghamPuzzle`
   - `GameState`（唯一的跨场景单例，挂 Inventory / NarrativeFlags / Existence，可序列化）——**2026-10-30 定：放在常驻场景 `Core_Persistent`，与妮芙、相机、HUD、SceneLoader 一起；关卡场景 Additive 加载，只放关卡内容。详见 `TechnicalArt/CH1_UNITY_REVISION_v2.md` §7**
   - `InventorySystem` + `InventoryUI`（数据与界面分开；见 `INVENTORY_SYSTEM_DESIGN.md`）
   - `NarrativeFlags`（章节、选择、同化度）
   - `SceneLoader` / `WorldLayer`（表世界 / 里世界）
   - `ImagineEyeOverlay`（后处理 + 隐藏层显隐）
5. 美术资产到位前，先用占位色块，配色按 §4 的场景主色。S1 与森林小径的美术已到位（2026-10-29），按 `TechnicalArt/CH1_UNITY_HANDOFF.md` 直接用正式图层；手感参数与关卡尺度按 `TechnicalArt/SCENE_SCALE_SPEC.md`；掉沟不扣存在值。

---

## 9. 附录：神话出处与参考链接

与 `StoryDesign/妖精丘陵_概念设计说明_m_故事v2.2更新.docx` 的「附录 A」内容一致。民俗类资料多为二手整理，写正式文案前请再核实。

<a id="a1"></a>
### A1 妖精丘陵 Sídhe / 贵族妖精 Aos Sí / 达南神族

**游戏中的用途**：整个「里世界」、妖精族群的统称（Aos Sí）、故事序中达南神族退居地下。

- [Aos Sí（维基百科，含达南神族退居丘陵）](https://en.wikipedia.org/wiki/Aos_S%C3%AD)

<a id="a2"></a>
### A2 欧甘字母 Ogham

**游戏中的用途**：欧甘石牌、拼字解谜（安抚符文 / 反制符文 / 真名）、银冠刻字。

- [Ogham（维基百科）](https://en.wikipedia.org/wiki/Ogham)
- [The Collector：爱尔兰「树木字母」](https://www.thecollector.com/ogham-script-early-medieval-alphabet/)
- [Let's Learn Irish：欧甘字母的用法](https://letslearnirish.com/articles/ogham)

<a id="a3"></a>
### A3 妮芙与奥伊芯 Niamh & Oisín（青春之国 Tír na nÓg）

**游戏中的用途**：主角与朋友的名字；游戏反转了神话——妮芙进入异界把奥伊芯带回家。

- [Niamh（维基百科）](https://en.wikipedia.org/wiki/Niamh_(mythology))
- [IrishCentral：青春之国的传说](https://www.irishcentral.com/roots/history/tir-na-nog-legend-eternal-youth)

<a id="a4"></a>
### A4 报丧女妖 Bean Sídhe（Banshee）

**游戏中的用途**：女妖守护者、哭声、银梳。

- [Let's Learn Irish：An Bhean Sí](https://letslearnirish.com/articles/banshee/)
- [Mary Jones 凯尔特百科：Bean Sídhe](https://maryjones.us/jce/beansidhe.html)

<a id="a5"></a>
### A5 普卡 Púca

**游戏中的用途**：会变形的小怪 / 向导 / 交易者。

- [Atlas Obscura：普卡](https://atlasobscura.com/articles/monster-mythology-puca)
- [Spooky Isles：会变形的普卡](https://spookyisles.com/puca-shape-shifter-ireland)

<a id="a6"></a>
### A6 铁驱妖精、妖精食物与换生灵

**游戏中的用途**：妖精法则 1/3/6、铁十字架、奥伊芯被「款待」与同化。v2.2 改编：本作中铁十字是神族圣物，只有被普卡控制的妖怪才怕铁；民间「妖精怕铁」被解释为人类只看到了这一部分（原创改编，无神话出处）。

- [南加州大学民俗档案：铁](https://folklore.usc.edu/tag/iron/)
- [Irish Mythology Stories：换生灵](https://irishmythologystories.substack.com/p/the-changeling-in-irish-mythology)
- [梅奥郡：妖精信仰](https://mayo-ireland.ie/en/about-mayo/arts-culture/superstitions-fairies/fairies.html)

<a id="a7"></a>
### A7 青铜时代黄金饰物（lunula / torc）

**游戏中的用途**：守门贵族的颈环与臂钏。

- [Gold lunula（维基百科）](https://en.wikipedia.org/wiki/Gold_lunula)
- [爱尔兰国家博物馆：Ór 黄金展](https://source.museum.ie/en-IE/Museums/Archaeology/Exhibitions/Or-Ireland-s-Gold)
- [Ask About Ireland：青铜时代艺术](https://askaboutireland.ie/learning-zone/secondary-students/art/art-in-ireland/irish-art-through-the-age/bronze-age)

<a id="a8"></a>
### A8 纽格莱奇 Newgrange 通道式古墓

**游戏中的用途**：古墓入口（S2）与石廊（S3）：白色石英外墙、三螺旋纹巨石。

- [Newgrange（维基百科）](https://en.wikipedia.org/wiki/Newgrange)
- [爱尔兰国家博物馆：Newgrange 冬至](https://museum.ie/en-IE/Collections-Research/Irish-Antiquities-Division-Collections/Irish-Antiquities-Articles/The-Winter-solstice-at-Newgrange)

<a id="a9"></a>
### A9 山楂树「妖精之树」

**游戏中的用途**：Boss「荆棘女王」与 S9 王座场景（建议新增）。

- [Latoon 妖精树（维基百科）](https://en.wikipedia.org/wiki/Latoon_fairy_bush)
- [科克大学：山楂树](https://www.ucc.ie/en/tree-explorers/trees/a-z/crataegusmonogyna/)
- [Brehon Academy：爱尔兰「布条树」](https://brehonacademy.org/beneath-the-rag-tree-how-the-irish-fairy-tree-invokes-superstition-reverance-and-healing-in-irish-folklore/)

<a id="a10"></a>
### A10 三叶草与四叶草（民间象征，非古代妖精神话）

**游戏中的用途**：三叶草定义为人间与家的象征（服饰、光点、心形扣）；四叶草为可选的隐藏收集物，民俗中能看穿妖精幻术。与欧甘字母、达南神族无关。

- [TIME：三叶草的历史](https://time.com/5550579/shamrock-history/)
- [Brehon Academy：三叶草的根源](https://brehonacademy.org/the-simple-shamrock-the-roots-of-irelands-cultural-emblem/)
- [耶鲁 HRAF：爱尔兰乡村的民俗与妖精](https://hraf.yale.edu/?p=11007)
- [Four-Leaf Clover in Faerie Folklore（个人博客，需再核实）](https://stephraemoran.substack.com/p/four-leaf-clover-uses-in-faerie-folklore)

<a id="a11"></a>
### A11 弗魔族 Fomóire

**游戏中的用途**：故事 v2：普卡之首千年前暗中投靠的势力，达南神族的古老宿敌；最坏结局中乘虚而入。

- [Fomorians（维基百科）](https://en.wikipedia.org/wiki/Fomorians)

<a id="a12"></a>
### A12 奥格玛 Ogma 与欧甘字母的起源

**游戏中的用途**：故事 v2.1：守门贵族名为 Ogma（已确定；Aos Sí 是族群统称）。神话中欧甘字母被归于达南神族的奥格玛；本作设定为人类发明、由 Ogma 带回族群。

- [Ogma（维基百科）](https://en.wikipedia.org/wiki/Ogma)
- [Ogham（维基百科）](https://en.wikipedia.org/wiki/Ogham)

<a id="a13"></a>
### A13 铁匠神哥布纽 Goibniu、达南神族四宝与第二次莫伊图拉之战

**游戏中的用途**：故事 v2.2 铁十字「神族之铁」的神话依据；四宝中并无铁十字，圣物为本作原创。与民俗的冲突对照见 `STORY_BIBLE.md` §8.2.2。

- [Goibniu（维基百科）](https://en.wikipedia.org/wiki/Goibniu)
- [Four Treasures of the Tuatha Dé Danann（维基百科）](https://en.wikipedia.org/wiki/Four_Treasures_of_the_Tuatha_D%C3%A9_Danann)
- [Cath Maige Tuired（维基百科）](https://en.wikipedia.org/wiki/Cath_Maige_Tuired)
