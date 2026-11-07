# 妖精丘陵 The Fairy Hills · 设计仓库

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

## 学生怎么用

1. 克隆本仓库和 Unity 仓库，放在同一个上级文件夹里。
2. 让你的 Agent（Claude、Codex 等）先读下面的「Agent 先读」清单，再开始工作。
3. 想看某个问题是怎么一步步解决的：看 `CommandForAgentToInitialRun/`（每次交给 Codex 的指令）和 `TechnicalArt/LESSONS_SCENE_PIPELINE.md`（踩过的坑）。

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

最近发生了什么：看 `ART_HANDOFF.md` §9、`TechnicalArt/CH1_UNITY_PROGRESS.md`，或 `git log`。

> 指令里的路径：`Z:` = 维护者电脑上的本仓库文件夹，`W:` = Unity 工程。换成你自己的本地路径即可。

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
