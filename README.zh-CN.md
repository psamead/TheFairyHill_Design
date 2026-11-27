# 妖精丘陵 The Fairy Hills · 设计仓库

**2026-11-28 · 第一章试玩与小挎包**　[人读图解](TechnicalArt/妖精丘陵_第一章试玩与小挎包图解_2026-11-28.docx) · [工作站实机回报](ForDesignScreenShot/2026-11-28_for-chapter1-playtest/Chapter1_Playtest_2026-11-28_Unity_Review.md) · [下一批 Unity 执行单](CommandForAgentToInitialRun/2026-11-28_Niamh_Jump_Arm_Unity.md)。入口淡变、四页字幕和村庄音乐已在 Editor 复测。跳跃手型、同款细金框和小挎包待工作站回报。

**2026-11-26 · 第一章试玩修订**　[给制作人员的图解与经验](TechnicalArt/第一章序章转场与十字架首次破障_试玩修订_2026-11-26.docx) · [Unity 执行单](CommandForAgentToInitialRun/2026-11-26_Prologue_and_Thorn_Wall_Unity.md) · [背包设计接续](INVENTORY_SYSTEM_DESIGN.md)。


2026-11-24 · [五镜故事画与选定配乐 v9](TechnicalArt/OPENING_FIVE_SCENES_2026-11-24.md) · [人读复盘](TechnicalArt/开场五镜制作复盘与Unity交接_v9.docx) · [Unity 执行任务](CommandForAgentToInitialRun/2026-11-24_Opening_Story_B_Unity_Review.md)。


**2026-11-18 当前试装：** 开场铺满与叠加字幕、按键下划线和红墙前B直接举高已放实际工程，离线C#检查通过；实机待验。任务从共享 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md` 读取，无需复制到对方工程。详见 `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`。

[English](README.md) | **简体中文**

以爱尔兰神话为背景的 2D 手绘横版冒险 Demo 的**设计与美术文档**：故事、玩法方案、美术规格、Unity 交接记录、已完成的美术 / 音频资产。
原作者：**YiChun Jiang**；由 Psamead 维护。
Unity 工程在另一个仓库：<https://github.com/psamead/TheFairyHill2D>

> 本仓库**只读**：由 Psamead 维护和推送。拉取后请不要直接修改；有意见请告诉 Psamead / YiChun。

## 获取与更新

```bash
# 建议克隆到 Unity 工程旁边（同级文件夹）
git clone https://github.com/psamead/TheFairyHill_Design.git
# 以后更新
git pull
```

## Unity 素材交接（优先走共享网络）

**2026-11-14 晚间占位交接**：负责人已将 r04 U4 放大图批准用于 Unity 开场与第一章封面占位。新图已按规则命名并保留下载名/散列，正式角色画风未通过。当前人读版为 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`；知识库 `TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md`；下次新对话先读 `STORYBOARD_RESUME.md`。任务与素材包见 `CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`，传输/派发事实见对应 unity_drop 的 `dispatch_status.json`。未收到 Unity 反馈前不称已接入/已运行。

设计仓库是源文件和已批准游戏素材的权威位置。Unity 制作端开始任务时，应先检查 Unity 工程中是否已预先放好本任务需要的文件；已放好的文件直接使用，不要为了拿素材再从 GitHub 下载。

如果缺少素材，Unity 制作端把**缺少的仓库相对路径、用途、目标 Unity 路径和所需格式**发给项目维护者。维护者将批准使用的文件放进本仓库 `TechnicalArt/unity_drop/<日期_任务名>/`，并通过双方可访问的共享网络文件夹通知 Unity 制作端。制作端从共享文件夹复制到 Unity 工程，确认文件名、尺寸和版本后继续；不要移动、删除或改写共享源文件。任务结束后保留交接记录，注明复制清单和源版本。

例如：`TechnicalArt/unity_drop/2026-11-14_Niamh_Motion_v8/`。若网络盘符或共享根目录不同，以本机可访问的共享文件夹为准；`Z:` 只是维护者环境的映射示例。不得把某一台电脑的主机名或绝对路径写成所有接手者都必须使用的路径。

GitHub 用于仓库版本同步、代码审阅和备份，不是 Unity 制作端索取大体积美术素材的默认传输渠道。若任务所需素材已随 Unity 仓库提交并在工程目录中，直接用工程内副本；只有共享网络不可用或需要追溯版本时，才由维护者明确安排其他传输方式。

## 查阅、接手与复用

这些资料供项目负责人、学生、制作与排版设计人员，以及现在和未来的 Agent 使用。查阅或排版时按需读取相关资料；继续开发时按以下步骤核对工程。

1. 克隆本仓库和 Unity 仓库，放在同一个上级文件夹里。
2. 在 Unity 仓库先读根目录 `AGENTS.md`，再按下面的清单让你的 Agent（Claude、Codex 等）读取与任务有关的资料。人和 Agent 应以同一份当前资料为依据。
3. 先在自己的 Unity 工程运行 `git status --short`，确认是否已有未提交的场景、素材或代码修改；查看 Build Settings 和实际文件，区分设计目标与已经做出的内容。
4. 想看某个问题是怎么一步步解决的：看 `CommandForAgentToInitialRun/`（当时交给 Codex 的任务单）和 `TechnicalArt/LESSONS_SCENE_PIPELINE.md`（实际踩过的坑）。旧任务单是过程记录，不能不核对现状就重新执行。

## 接手时怎样判断资料

- **设计目标**：故事以 `STORY_BIBLE.md` 为准；本阶段范围以 `DEMO_IMPLEMENTATION_PLAN.md` 为准；具体美术与资产规格看 `ART_HANDOFF.md`、`TechnicalArt/` 和 `MJ_ref/ASSETS.md`。
- **实际进度**：先看 Unity 工程的场景、脚本、Git 状态及有日期的 `Docs/` 记录，再读本仓库 `TechnicalArt/CH1_UNITY_PROGRESS.md`。文档中的“已接入”“已编译”“Play Mode 已验证”“用户已确认”是不同状态。
- **历史记录**：`handoff.md` 的早期阶段说明、各轮修正和 `CommandForAgentToInitialRun/` 有助于理解过程；遇到冲突时核对日期、是否被取代和当前工程，不把旧计划当成当前待办。
- **旧 Prompt**：`StoryDesign/` 的 Prompt 集记录当时的模型、参数与试验。使用前核对对应参考图、已选资产、模型版本与本轮目标；不能只复制旧 Prompt 就视为定稿要求。
- **自己的交付**：每次给人和 Agent 留下目标、输入文件、改动位置、实测结果、未验证项和下一步。Prompt 要保存模型版本、参考图、参数、原文、选图理由及产出路径。统一写法见 `AGENT_PROCESS_GUIDELINES.md` 的“接手材料写法”。

排版、摘编和再次利用时，保留可编辑源文件、导出成品与来源版本的对应关系，以及图注、字体和已知使用限制。另存整理后的成品，保留原件；具体写法见 `AGENT_PROCESS_GUIDELINES.md` §5.7。游戏按独立游戏 Demo 的定位制作，游戏内文字保持英文。

## Agent 先读（按顺序，按需）

1. `ART_HANDOFF.md` **§0（怎么用）和 §9（变更记录，最新的在最下面）** —— 现在做到哪了
2. `handoff.md` —— 项目速览、Demo 范围、代码约定
3. `DEMO_IMPLEMENTATION_PLAN.md` —— 场景、机制、实施清单
4. `STORY_BIBLE.md` —— 故事与设定；`INVENTORY_SYSTEM_DESIGN.md` —— 背包系统
5. `TechnicalArt/SCENE_SCALE_SPEC.md` —— 角色比例与跳跃尺度
6. `TechnicalArt/CH1_SCENE_PLAN.md` → `CH1_UNITY_HANDOFF.md` → `CH1_UNITY_REVISION_v2.md` / `v3.md` / **`v3_fix.md`** —— 第一章从设计到 Unity，按顺序
7. `TechnicalArt/LESSONS_SCENE_PIPELINE.md` —— 经验库
8. `TechnicalArt/UNITY_AGENT_RULES.md` —— Unity 端给 Agent 的规则
9. `DESIGN_CHANGES.md`、`AGENT_PROCESS_GUIDELINES.md` —— 设定怎么改、怎么记录

角色动画先看给人读的 `TechnicalArt/妮芙动作试做与Unity试玩记录_v8.docx`，再按需要读 `TechnicalArt/LESSONS_CHARACTER_ANIMATION.md`、`TechArtAsset/Characters/Niamh/Motion_v8/README.md` 与 `UNITY_TRIAL_README.md`。Niamh v8 已在 Unity 试玩；`CommandForAgentToInitialRun/2026-11-14_Niamh_Motion_v8_Unity_Trial.md` 是**已执行的历史任务单**，实际结果以 Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md` 为准。

章节过渡与妮芙动作声音的**新提案**见给人读的 `TechnicalArt/妖精丘陵_章节过渡与妮芙动作声音设计_v1.docx`，给 Agent 的详细规格见 `TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md`。Python 音效试听稿在 `TechArtAsset/Audio/SFX/Niamh_Motion_v1/`；负责人已单独试听并批准游戏内试装，23 条 OGG 已网络预置；Unity 接入和游戏内听感尚待反馈。S2–S4 仍是灰盒，正式故事画面需与后续实机场景风格核对。

**Demo 核心体验（2026-11-14）**：范围仍按 `DEMO_IMPLEMENTATION_PLAN.md` 做第一、二章 S1–S4 与结尾卡。项目负责人明确「想象之眼」切换现实与幻象视野是必须展现的能力：获得后在主线上再次使用，并推动人物互动；它与铁十字架的瞬时脉冲分开。完整五章仍是正式游戏蓝图。

最近发生了什么：看 `ART_HANDOFF.md` §9、`TechnicalArt/CH1_UNITY_PROGRESS.md`，或 `git log`。

> 指令里的路径：`Z:` = 维护者电脑上的本仓库文件夹，`W:` = Unity 工程。换成你自己的本地路径即可；不要依赖维护者电脑的局域网名称或盘符。

## 文件夹

| 位置 | 内容 |
|---|---|
| 根目录 `*.md` | 给人和 Agent 读的说明与交接 |
| `StoryDesign/` | 故事、概念设计、Demo 方案、市场分析（Word） |
| `TechnicalArt/` | 技术美术与宣传美术文档（Markdown + Word）、字体、工具脚本（`tools/*.py`）、Unity 进度、效果预览 |
| `MJ_ref/` | 概念图、生成图、原作者原画（`AUTHOR_L7_66/`）、`ASSETS.md` 资产总表 |
| `TechArtAsset/` | 做好的游戏资产（PNG、OGG、布局 JSON） |
| `CommandForAgentToInitialRun/` | 交给 Codex 的分步指令（按日期） |
| `ForDesignScreenShot/` | 试玩截图，按修改轮次分文件夹（见其中 README） |
| `diagrams/` | 故事关系图、时间线等 |
| `_build_scripts/` | 生成 Word 文档的 Node 脚本 |
| `deprecated/` | 被取代的旧版本和过程图（保留视觉演变） |

## 版权

- 字体：SIL Open Font License。
- 音乐由 Google Lyria 生成；音效由代码合成（`TechnicalArt/tools/make_sfx.py`）。
- 其余设计文档与美术为本项目作品（YiChun Jiang 与协作者），仅供本课程 / 项目协作使用；未经许可请勿用于课程以外。


## 历史上下文与经验导入 — 2026-11-18

[Claude 上下文与可复用经验](CLAUDE_CONTEXT_2026-11-18.md) 保留历史设计理由，并指向 STORYBOARD_RESUME.md 的较新决定，不替代当前设计或验收规则。共享 Obsidian 知识库已新增独立 TheFairyHill2D 项目入口及对应参考笔记。


Midjourney 提示词、参考图和迭代方法见[项目经验指南](MIDJOURNEY_PROJECT_LESSONS.md)：保留实测结果与失败边界，新增模板明确标注为未测试。
