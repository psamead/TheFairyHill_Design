# Agent 任务单索引与写法

**2026-11-28 · 当前工作站任务**　[跳跃手型、同款细金框与小挎包圣物页](2026-11-28_Niamh_Jump_Arm_Unity.md)。三项共用一份执行单和一份实机回报，已供工作站取用。

**2026-11-28 · 负责人试玩修订**　[本轮 Unity 任务](2026-11-28_Chapter1_Playtest_Unity.md)。三项已收到工作站实机回报，待负责人确认。包括主菜单进入序章的画面淡变、四页字幕位置与村庄入场音量。

**2026-11-26 · 背包设计起点**　[背包规格](../INVENTORY_SYSTEM_DESIGN.md)记录首轮试排到拾取解锁的变化。实施见上方 11 月 28 日执行单。

**2026-11-26 · 已有工作站回报**　[第一章序章、封面过渡与森林首次破障](./2026-11-26_Prologue_and_Thorn_Wall_Unity.md)。[序章与荆棘墙实机回报](<//haoxi-rtx/C/Users/Administrator/Documents/UnityProject/TheFairyHill2D/Docs/Prologue_and_Thorn_Wall_Unity_Review.md>)。


**2026-11-26 · 原字号字幕复测已回报**　[原任务单](2026-11-25_Opening_Story_B_Caption_Red_Boxes_Unity_Check.md) · [实机结果与截图](../ForDesignScreenShot/2026-11-26_for-opening-caption-fixed-size/README.md)。

**2026-11-24 · 当前交接**　[旁白 B 与原稿依据](../TechnicalArt/OPENING_STORY_B_2026-11-24.md) · [Unity 工作站任务](2026-11-24_Opening_Story_B_Unity_Review.md)。本地完成设计样片；真实工程已接入 A，B 待对端应用和回报。

上一轮[五镜素材与旁白 A 接入单](2026-11-24_Opening_Five_Scenes_v9_Unity.md)保留作实施记录。本轮执行上方旁白 B 任务单。

本目录保存《妖精丘陵》各轮交给 Codex 等 Agent 的任务单，供项目负责人、学生、制作与排版设计人员，以及任何后续 Agent 查阅、复用并追溯“当时要求什么、后来怎样改”。**按日期排列不等于仍待执行**：开始任何任务前，先读设计仓库 `README.zh-CN.md`、Unity 工程根目录 `AGENTS.md`、最新进度记录，并查看实际场景与 Git 状态。被后续修正替代的旧指令只作历史参考。

旧任务单中的 `Z:` 是设计仓库根目录，`W:` 是 Unity 工程根目录；换成自己电脑的路径。不要依赖维护者电脑的盘符或局域网名称。设计仓库对学生和协作者只读，源素材只复制到自己的 Unity 工程。

**2026-11-18 负责人明确：** 发给另一台电脑 Agent 的任务文件留在本共享目录，由对方直接读取；无需再复制一份任务单到对方工程。素材和运行证据仍按对应交接规则放置。目录中存在任务文件不表示远程进程已启动。

## 一轮工作，一个执行入口

同一轮追加的要求直接合并到当前任务单正文，写明最终决定、执行顺序、实机验收和回报路径。发给工作站时只给该文件名；截图、设计说明和旧单作为参考链接。验收目标发生在下一轮（例如本轮序章完成后的背包制作）时，再独立开一份单。

交接消息只需给出当前任务单文件名。把聊天补充和上一轮尚需执行的事项合入同一文件，按顺序写全版本、最终文案或参数、操作、验收和回报位置。清楚标出已完成的基线、这次的改动及以后再设计的事项。链接用于取素材、核对来源和查看旧记录。发布前，用“只拿到这个文件，能否做到回报”核对一遍，并把索引与旧单指向现行入口。

## 新任务单模板

把下面字段写在新任务单的开头，再写具体步骤。中英文均可，文件路径和验收条件要明确。

```text
# YYYY-MM-DD 任务名称

项目 / 读者：The Fairy Hills；本轮执行人员或 Agent、项目负责人和后续查阅者
用途：开发 / 美术 / 资料整理 / 排版等；注明本轮用途
状态：拟执行 / 进行中 / 已接入 / 已在 Play Mode 验证 / 用户已确认
依据：设计文档及章节；当前 Unity 提交和 Git 状态；是否取代旧任务单
目标：本轮要达成的可观察结果
输入：设计仓库相对路径、文件版本、参考图或 Prompt 记录
改动范围：允许修改的文件、场景或排版输出；源文件与导出成品的位置
保护现场：已有人手调或未提交的值，以及重建场景前要同步的数据
步骤：按依赖顺序，尽量只做一小批相互关联的工作
验收：按任务选择编译 / 场景配置 / Play Mode / 人工画面或听感；资料与排版任务检查来源、版本、文字和图注，以及导出效果
交付：实际改动、证据位置、未验证项、下一步，写回哪些进度文档
```

Prompt 若用于本轮出图，也要保存模型与版本、完整原文、参数、参考图及用途、选图理由、输出路径；详细规范见 `../AGENT_PROCESS_GUIDELINES.md` §5.7。

## 任务单状态

- `2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`：**当前待实机检查**。开场铺满/叠加字幕、按键下划线和终段红墙Q直接举高已写入实际工程，离线C#类型检查通过。任务沿本目录与共享网络副本交接，并写入UnityProjectContext待办；负责人已发给网络电脑Codex执行，Editor/Play Mode结果待回报。反馈后设计端更新相关文档并按用户授权push。旧11月14日开场、音频与v8已有实现报告，不要原样重跑。

- `2026-11-14_Niamh_Motion_v8_Unity_Trial.md`：**已执行的历史任务单**。用户修订的 Niamh v8 已作为可回退分层角色接入 Unity，编译通过并在 Village / Forest 场景试玩，项目负责人反馈基本可用；实际结果见 Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md`。美术过程与经验见 `../TechArtAsset/Characters/Niamh/Motion_v8/UNITY_TRIAL_README.md` 和 `../TechnicalArt/LESSONS_CHARACTER_ANIMATION.md`。

- `2026-11-14_Niamh_Surface_Audio_Unity_Trial.md`：**可执行的新任务**。负责人已批准声音放入游戏试装；23 条 OGG 已通过共享网络预先复制到 Unity，SHA-256 核对一致。任务单也在 Unity `Docs/References/Niamh_Surface_Audio_v1/`，尚未确认 Unity Codex 已读取或开始执行；接入、编译和游戏内听感待记录。

章节故事画的首批分镜见 `../TechnicalArt/SLIDESHOW_OPENING_v1.md`；晚间已批准 OP01 候选放大图作为占位进入 Unity。Demo 范围仍为第一、二章 S1–S4 与结尾卡，想象之眼为 Must。

## 2026-11-14 晚间新增可执行任务

- `2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`：负责人已授权 OP01 放大图占位，要求加开场故事引入、第一章封面并运行。图片/数据/任务包通过网络预放，实际状态看 unity_drop 的 dispatch_status.json 与 Unity Handoff。包含先核对已有动作音任务、未完成则分批执行的要求。
- `../STORYBOARD_RESUME.md` 是本地新对话续接说明，不是另一台机器的执行命令。

本索引较早的“MJ 未提交生成”描述已被晚间记录取代：已产生候选，已批准占位，正式 OP02/OP03 尚未制作。
