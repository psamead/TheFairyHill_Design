# 开始菜单 → Unity 场景搭建交接（给 Claude / Codex）

> 2026-10-24。项目：《妖精丘陵 The Fairy Hills》，2D 手绘高清 + 骨骼动画，先做 PC 版。
> 先读：`ART_HANDOFF.md`（美术总览）、`handoff.md`（项目与 Demo 范围）。本文件只讲开始菜单。

## 1. 素材（都在 `ShareWorkFolder/` 下）

| 用途 | 文件 | 说明 |
|---|---|---|
| 菜单分层源文件 | `TechArtAsset/Menu/MENU_wip.psd` | 1920×1080，图层见第 2 节 |
| 选中图标 | `TechArtAsset/UI/ICON_triskele.png` | 金色三曲枝，128px 透明底 |
| 标题牌原图 | `MJ_ref/TileArtFont_wip.psd` | 两行石刻标题牌，透明底 |
| 字体 | `TechnicalArt/fonts/Fondamento-Regular.ttf`、`UncialAntiqua-Regular.ttf` | 按钮用 Fondamento；标题已是图片，不用字体 |

## 2. MENU_wip.psd 图层（从上到下）

- `Buttons`（组）：`btn_Start` / `btn_Continue` / `btn_Settings` / `btn_Quit`（文字层，Fondamento 50px，左对齐）、`sel_icon_triskele`
- `title_plaque`：标题牌图片
- `left_dark`：左侧纵向深蓝渐变，45% 不透明，已裁到画布
- `BG_clean_signature`：去掉 MJ 签名后的背景（用这一张）
- `BG`：原始背景（不用）

**按钮不要导出成图片**：在 Unity 里用 TextMeshPro 重建文字，位置照 PSD。PSD 里的样式就是视觉规范。

## 3. 视觉规范

| 状态 | 颜色 | 效果 |
|---|---|---|
| 普通 | 米白 `#EFE3C2` | 深色外发光（让字在背景上可读） |
| 选中 / 悬停 | 暖金 `#F2D28A` | 同色外发光；左侧显示三曲枝图标（约 40px，离文字留 6–10px） |
| 不可用（无存档时的 Continue） | 米白 50% 不透明 | 无发光 |

- 当前 Unity 实现：W/S 或 Up/Down 上下切换；鼠标悬停会切换选中项，鼠标左键触发悬停按钮功能（Start / Settings / Quit），右键和中键未接入；图标以固定偏移贴随焦点，无缓动、无旋转。
- 分辨率基准 1920×1080，Canvas Scaler = Scale With Screen Size，Match 0.5。

## 4. 建议的场景结构

```
Scene: MainMenu
├─ Main Camera（正交，含场景唯一 AudioListener）
├─ Background
│   ├─ BG（BG_clean_signature 导出的 Sprite）
│   └─ LeftDark（left_dark 导出的 Sprite，或用 UI Image + 渐变）
└─ Canvas（Screen Space - Overlay）
    ├─ TitlePlaque（Image）
    └─ MenuButtons（Vertical Layout Group，左对齐）
        ├─ Start / Continue / Settings / Quit（Button + TextMeshPro）
        └─ SelectionIcon（Image，跟随选中项）
```

- 按钮功能先做占位：Start → 加载第一个关卡场景（名字待定，先用 `Scene_Forest_01` 占位）；Continue → 无存档时禁用；Settings → 空面板；Quit → `Application.Quit()`。
- 字体：用 Fondamento 生成 TMP Font Asset（只需英文字符集）。

## 5. 暂时不做（后续技术美术任务）

- 背景拆 3 层视差（天空 / 古墓与山丘 / 前景草）——目前背景只有一整张，需先在 PS 拆层。
- 门洞特效：欧甘字粒子、雾、门内剪影明暗。
- 菜单背景音乐尚未制作或接入（设计待办见 `MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md`）；Unity 已加入一个短促选中提示音，更多音效后续再定。

## 6. 交付后请记录

完成或新增菜单事项后，在 `ART_HANDOFF.md` 第 6 节更新待办、第 9 节追加记录，并在 `MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md` 更新当前状态或追加设计待办。未做 Play Mode 验证的事项不要标为已验证。
