# Agent 任务单索引与写法

本目录保存《妖精丘陵》各轮交给 Codex 等 Agent 的任务单，供项目负责人、学生、制作与排版设计人员，以及任何后续 Agent 查阅、复用并追溯“当时要求什么、后来怎样改”。**按日期排列不等于仍待执行**：开始任何任务前，先读设计仓库 `README.zh-CN.md`、Unity 工程根目录 `AGENTS.md`、最新进度记录，并查看实际场景与 Git 状态。被后续修正替代的旧指令只作历史参考。

旧任务单中的 `Z:` 是设计仓库根目录，`W:` 是 Unity 工程根目录；换成自己电脑的路径。不要依赖维护者电脑的盘符或局域网名称。设计仓库对学生和协作者只读，源素材只复制到自己的 Unity 工程。

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

- `2026-11-14_Niamh_Motion_v8_Unity_Trial.md`：**已执行的历史任务单**。用户修订的 Niamh v8 已作为可回退分层角色接入 Unity，编译通过并在 Village / Forest 场景试玩，项目负责人反馈基本可用；实际结果见 Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md`。美术过程与经验见 `../TechArtAsset/Characters/Niamh/Motion_v8/UNITY_TRIAL_README.md` 和 `../TechnicalArt/LESSONS_CHARACTER_ANIMATION.md`。

下一轮章节过渡与动作声音目前是设计方案及未批准的试听稿，见 `../TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md`；尚未形成可执行的 Unity 任务单。Demo 范围仍为第一、二章 S1–S4 与结尾卡，想象之眼已提升为 Must；详见 `../DEMO_IMPLEMENTATION_PLAN.md`。
