# 第一章 Unity 场景修改 v2（2026-10-30，用户试玩后提出的 7 条）

> 给人看，也给 Codex 照做。前提文档：`CH1_UNITY_HANDOFF.md`（v1 搭建说明）、`CH1_UNITY_PROGRESS.md`（Codex 的 v1 交付记录）。
> 本文件只写**改什么、为什么、用哪些新素材**。新素材都已放在共享文件夹，路径见每条。素材已全部到位（2026-10-30）。

## 总表

| # | 场景 | 问题 | 改法 | 素材 |
|---|---|---|---|---|
| 1 | S1 | 栅门是一整张图，妮芙站到门前时前后关系不对；碰撞贴着图片外框 | 拆成三块：左石柱 + 门板在妮芙**后面**，右石柱在妮芙**前面**；碰撞改为门位置一道高隐形墙，推开后关闭 | 已备 |
| 2 | 全部 | 设置面板、按键提示、互动提示直接压在画面上，看不清 | 统一加凯尔特结纹边框（9-slice，边上 Tiled） | 已备 |
| 3 | 森林 | 铁十字太小看不见；荆棘丛、荆棘墙不够夸张；黑烟粒子显示桃红色 | 物件夸张放大；铁十字平时只闪星星，走近才显现；粒子补材质 | 已备（荆棘墙边缘待 Nano Banana 修，先用 v2） |
| 4 | 森林 | 前景 L4 太突出，视差下晕 | 半透明 0.55，视差 1.3 → 1.15 | 无需新图 |
| 5 | S1 | 前景 L4 上沿碎草紧贴不动的路面，视差下晕 | 去掉上沿碎草，换 `S1_Village_L4_Fore_v2.png` | 已备 |
| 6 | 森林 | 背景树根（0.4）和路面（1.0）交界处一拉一停，晕 | 路面上沿加一条与路面同速的草土边，压住树根底部 | 已备 |
| 7 | 架构 | 妮芙、相机、HUD 每个场景各一份 | 常驻场景 + 关卡场景 Additive 加载（见第 7 节） | — |

## 1. S1 栅门拆三块

素材：`TechArtAsset/Scenes/S1_Village/props/S1_prop_gate_post_L.png`（112×240）、`S1_prop_gate_boards.png`（288×240）、`S1_prop_gate_post_R.png`（98×240）。由原 `S1_prop_gate.png`（482×240）按列切开，相邻块有 8 px 重叠。

| 块 | 世界 x（左边，u） | Sorting Order | 说明 |
|---|---|---|---|
| post_L | 24.00 | -5（妮芙后面） | 静态 |
| boards | 25.04 | -5（妮芙后面） | 打开时直接隐藏，离开范围后重新显示 |
| post_R | 27.84 | 15（妮芙前面） | 妮芙走过门时被右柱遮住一部分，形成「穿过门框」的感觉 |

碰撞：删掉贴图片外框的 BoxCollider2D。在门板中线（x ≈ 26.5）放一道 **宽 0.3u、高 8u** 的隐形墙（底在 y = 0），玩家跳不过去。

开关规则（2026-10-30 用户定）：
- 妮芙在门左侧 1u 内按 E → 门**打开**：门板 SpriteRenderer 直接隐藏（不做动画），隐形墙关闭。
- 门附近放一个范围 Trigger（门两侧各约 2u，覆盖整个门洞）。妮芙**离开这个范围**后，门**自动关闭**：门板重新显示，隐形墙重新打开。
- 门是可以反复开关的，状态不存进 GameState（不是一次性的剧情开关）。
- 关门时如果妮芙还站在门洞里（理论上不会，因为范围比门洞大），等她离开再关。

## 2. UI 边框（素材已到位，2026-10-30）

素材（`TechArtAsset/UI/Frame/`，Nano Banana 2.1 生成）：
- `UI_frame_celtic.png`（932×932，**透明底**，只有金色凯尔特结纹）——主用。由 `UI_frame_celtic_white.png`（白底原图）抠出。
- `UI_frame_celtic_stone.png`（带深蓝石底的版本）——需要实心底的面板可直接用。

Unity 设置：
- Texture Type = Sprite (2D and UI)，Mesh Type = Full Rect。
- Sprite Editor 里四条边线（Border）都设 **210 px**：四角的结纹完整落在角里，不会被拉伸。边带约 56 px 厚。
- UI Image 的 Image Type 用 **Tiled**（不要用 Sliced）：边上是辫状结纹，Sliced 会把它拉长变形，Tiled 是重复排列。Fill Center 关掉（透明版中间本来就空）。
- 原图很大，用 Image 的 **Pixels Per Unit Multiplier ≈ 3–4**，让屏幕上的角饰约 50–70 px。
- 金边框后面另放一张半透明深色底（黑或深蓝灰，透明度 60–70%），文字才看得清；或直接用石底版。

**按键提示条（关卡左上角）的具体做法**（2026-10-30 用户定）：
- 三层叠放：最底一层是**半透明黑色方块**（UI Image，纯黑，Alpha 0.6 左右），比文字区域四周各大约 12–16 px；中间是金色边框 `UI_frame_celtic.png`（Tiled，Multiplier 调大，让细长条上的角饰小一些）；最上面是文字。
- 黑块的作用是把文字和亮色的天空、山坡隔开。没有黑块时，米白文字和金框都会和黄昏背景混在一起。
- 文字用米白 `#EFE3C2`，按键名（A / D、Shift、Space、E、Q）可以用暖金 `#F2D28A` 突出。
- 互动提示「Press E to …」和 Settings 弹窗用同一套三层做法。

用于：菜单 Settings 弹窗、关卡左上角按键提示（细长条，Multiplier 可调大让角饰更小）、互动提示「Press E to …」、以后的对话框和背包（`INVENTORY_SYSTEM_DESIGN.md`）。字色沿用菜单规范：米白 `#EFE3C2`，强调暖金 `#F2D28A`（`MENU_UNITY_HANDOFF.md` §3）。

## 3. 森林物件夸张放大 + 铁十字揭示

新素材（`TechArtAsset/Scenes/S1b_ForestPath/props/`），布局 `S1b_ForestPath_layout_v3.json`：

| 物件 | 文件 | 尺寸 | 位置（u） | 碰撞 |
|---|---|---|---|---|
| 荆棘丛 | `F_prop_bramble_v2.png` | 448×200（4.48×2.0u） | x 47.0 | 无，纯装饰 |
| 铁十字 | `F_prop_cross_v2.png` | 144×120（约 1.2u） | 中心 x 50.58，贴地 | Trigger 拾取 |
| 受控荆棘墙 | `F_prop_thornwall_v2.png` | 719×600（7.19×6.0u，两侧是散开的枝条） | 图片 x 50.8 | 只在中间实心部分 x 52.2–56.6（4.4u）放碰撞，IronPulse 后关闭；布局里用 `collider_x` / `collider_w` 指定 |
| 出口 | — | — | x 57.2 | Trigger |

铁十字揭示（制造悬念、引导玩家）：
- 平时十字架**不可见**（alpha 0），原位置循环播放闪光星星粒子：贴图 `TechArtAsset/FX/FX_sparkle_star.png`，每秒 2–3 颗，随机出现在十字架周围 0.6u 内，0.6 s 内由小变大再淡出，颜色暖白偏金。
- 妮芙走到 **2.5u 以内**时，十字架在 0.4 s 内淡入，星星减少；离开后不再隐藏（已被发现）。
- 拾取后十字架和星星都消失，背包记 `hasIronCross`。

黑烟粒子桃红色：原因是粒子没有材质（或用了内置管线材质）。新建材质 `M_FX_SoftParticle`：Shader 用 URP 的 `Universal Render Pipeline/Particles/Unlit`，Surface = Transparent，Blending = Alpha，贴图 `TechArtAsset/FX/FX_soft_dot.png`；黑烟颜色设深紫黑、透明度 0.6。星星粒子用同一 Shader，Blending = Additive，贴图 `FX_sparkle_star.png`。

荆棘墙两侧原本是直的截口，已用 Nano Banana 2.1 修成自然散开的枝条（输入 / 输出在 `TechArtAsset/_aistudio_in/`），抠图后覆盖了 `F_prop_thornwall_v2.png`；直边旧版在 `deprecated/S1b_ForestPath_props_old/`。图片变宽后，出口（x 57.2）落在荆棘墙图片范围内，驱散后才露出来，正好。

## 4. 森林前景 L4

不换图。Sprite Renderer Color 的 Alpha = **0.55**；ParallaxLayer Factor 1.3 → **1.15**。如果还晕，再降到 1.1，或 Alpha 到 0.45。

## 5. S1 前景 L4

换成 `TechArtAsset/Scenes/S1_Village/_work/S1_Village_L4_Fore_v2.png`（尺寸、Pivot 与 v1 相同）：上沿的碎草已去掉，只保留成片的深色草。Factor 先保持 1.3，仍晕就降到 1.2。

## 6. 森林路面草土边

新层 `TechArtAsset/Scenes/S1b_ForestPath/_work/S1b_ForestPath_L3b_GrassEdge.png`（6049×1335，与可行走层同尺寸、同 Pivot `(0, 270/1335)`），Factor **1.0**，Sorting Order **-9**（可行走层 -10 之上、物件 0 之下）。内容：取原图路面上沿的草和土做成的一条起伏草边（约 0.9–1.2u 高），盖住背景层树根的底部；两条地沟处留空。原理：画面里多一条「与路面同速」的稳定带，树根往后退的动作被它挡住一部分，眼睛有了参照，就不晕了。

## 7. 架构：常驻场景 + 关卡场景

| 场景 | 内容 | 加载方式 |
|---|---|---|
| `MainMenu` | 菜单 UI、菜单音乐 | Single |
| `Core_Persistent`（新） | 妮芙（PlayerController）、Main Camera + 跟随 + **唯一的 AudioListener**、HUD / UI Canvas + EventSystem、`GameState`（单例：背包、存在值、剧情标记，可序列化）、`SceneLoader` | 从菜单 Start 时 Additive 加载一次，之后**不卸载**；不使用 DontDestroyOnLoad |
| `Ch1_S1_Village`、`Ch1_S1b_ForestPath`、以后的 S2… | 背景层、物件、碰撞、互动点、`SpawnPoint`、`LevelInfo`（场景长度 → 相机左右边界；场景名；下一关） | `SceneLoader` Additive 加载 / 卸载，切换时黑场淡入淡出 |

规则：
- 关卡场景里**不放**妮芙、相机、AudioListener、EventSystem。删掉 v1 里各场景自带的这些对象。
- 每个关卡至少一个 `SpawnPoint`（如 `Spawn_Start`、`Spawn_FromVillage`）。`ChapterSceneExit` 写明目标场景和目标出生点名。
- `ParallaxLayer`、`ChapterCameraFollow` 不在场景里拖引用，运行时找 `Camera.main` / `LevelInfo`。
- 跨场景的数据（拿到铁十字、栅门已开）只存在 `GameState`，关卡对象在 `Start` 时读它恢复状态。
- 在编辑器里单独打开关卡场景按 Play 时，`LevelBootstrap` 检测到没有 Core 就自动 Additive 加载 `Core_Persistent`，方便调试（课堂演示也方便）。

这样以后改妮芙（换骨骼动画、调手感、加能力），只改 Core 里一份。对应 `handoff.md` §8 的 `GameState`「唯一的跨场景单例」。

## 7b. 保留用户手动调过的碰撞（重要）

用户已在 `Ch1_S1_Village` 里手动收窄高石墙 `StoneWall_Tall_1.8u` 的 BoxCollider2D：Offset (2.0378294, 0.9)，Size (3.1901226, 1.8)，对象在 (16.8, 0, 0)（世界范围约 x 17.24–20.43）。`Chapter1SceneBuilder` 重建场景时会按图片宽度重新生成、覆盖这个值。**重建前先把它写进数据**：在布局 JSON 的这个 block 里加 `collider_offset` / `collider_size` 字段（或在 builder 里读覆盖表），以后所有手动调的碰撞都走这个机制。栅门的高隐形墙同理写进数据。

## 8. 验收

- S1：妮芙穿过栅门时，左柱在身后、右柱在身前；按 E 前跳不过门；按 E 后门板消失可通过；走远后门板重新出现、又挡住。
- 森林：远处看到星星、看不到十字架；走近 2.5u 内十字架出现；拾取后荆棘墙（6u 高）按 Q 驱散；黑烟不再是桃红色。
- 两个场景走一遍，前景和地面交界不再晃眼（主观，请用户确认）。
- 高石墙的碰撞仍是用户手动调过的窄版。
- 切场景后妮芙只有一个、相机只有一个、AudioListener 只有一个；拿到的铁十字在下一个场景仍然在。
