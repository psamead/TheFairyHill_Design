# 第一章 S1 + 森林小径 → Unity 可玩场景交接（给 Claude / Codex，也作课堂演示）

> 2026-10-29。项目：《妖精丘陵 The Fairy Hills》，2D 手绘高清横版，先做 PC 版，Unity + URP 2D。
> 先读：`ART_HANDOFF.md`（美术总览）、`handoff.md`（项目与 Demo 范围）、`TechnicalArt/SCENE_SCALE_SPEC.md`（比例与跳跃）、`TechnicalArt/CH1_SCENE_PLAN.md` §5–6（这两个场景的制作经过）。
> 已有：`MainMenu` 场景（见 `MENU_UNITY_HANDOFF.md` / `MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md`），沿用同一个 Unity 工程与 `Assets/_Project/` 结构。
> 环境规则（共享文件夹映射为 `Z:`、只复制不改动共享文件夹里的素材、不覆盖他人修改）同 `MENU_UNITY_HANDOFF.md` §0。
> **2026-10-30 更新**：试玩后的修改与常驻场景架构见 `CH1_UNITY_REVISION_v2.md`，与本文件冲突时以它为准。
> 目标：**S1 黄昏村庄 → 森林小径** 两个场景能从菜单 Start 进入、走完、切到下一个场景；妮芙先用静态侧面图，骨骼动画以后替换。

## 1. 单位与相机（全章统一）

| 项目 | 值 |
|---|---|
| Pixels Per Unit | **100**（所有背景、物件、角色） |
| 参考分辨率 | 1920×1080；正交相机 Size **5.4**（高 10.8u） |
| 地面 | 世界 y = 0。角色站地面时，脚在屏幕底边上方 2.7u（相机中心 y = 2.7） |
| 妮芙 | 静态图 `TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png`（325×698），导入后 Scale 设为 0.30 → 约 2.1u 高；Pivot：底部中心。碰撞体胶囊 Size 0.23×2.08u，Offset (0.08, 1.04)；该值对应当前 Core_Persistent 实际场景。 |
| 手感参数（起始值） | 走 3.2 u/s，跑 5.6 u/s，最高跳 2.4u（上升 0.40s → 重力 30，起跳速度 12），下落重力 ×1.5，松键截断跳跃（轻点约 0.9u），土狼时间 0.10s，跳跃缓冲 0.12s。详见 `SCENE_SCALE_SPEC.md` §2 |
| 相机 | Cinemachine 跟随妮芙，只水平跟随（y 固定 2.7），左右边界 = 场景长度 |

## 2. 背景层与视差

所有层图片的 **地面线都在图片底边上方 270 px**。导入时 Sprite Mode = Single，Pivot = Custom **(0, 270 / 图片高度)**，即左下偏上；物体放在世界 (0, 0)，地面线自然落在 y = 0。Max Size 设 8192（最宽 7258 px），压缩先用 High Quality。

视差：`layer.x = cameraLeftEdge × (1 − p)`（p = 1 跟相机同速，即固定在世界里；p < 1 移得慢）。前景 p = 1.3 移得比镜头快。

### 2.1 S1 黄昏村庄（长 38.4u；文件夹 `TechArtAsset/Scenes/S1_Village/`）

| 层 | 文件 | 尺寸 | p | Sorting Order |
|---|---|---|---|---|
| L0 天空 | `_work/S1_Village_L0_Sky_wip.png` | 2117×1270 | 0.05 | -50 |
| L1 远景 | `_work/S1_Village_L1_Far_wip.png` | 2420×1270 | 0.2 | -40 |
| L2 中景（村舍、石墙带） | `_work/S1_Village_L2_Mid_wip.png` | 3025×1270 | 0.5 | -30 |
| L3 可行走层（小路） | `_work/S1_Village_L3_Walk_wip.png` | 4033×1270 | 1.0 | -10 |
| 物件 | `props/S1_prop_wall_low.png` 等，位置见 `S1_Village_layout_v2.json` | — | 1.0 | 0 |
| 妮芙 | — | — | — | 10 |
| L4 前景草 | `_work/S1_Village_L4_Fore_wip.png` | 4160×1270 | 1.3 | 20 |

物件（布局 `S1_Village_layout_v2.json` 的 `blocks`，单位 u，x 为左边，底边在 y = 0）：低石墙 x 9.5 宽 2.79 高 1.2；方草捆 x 15.0 宽 1.72 高 0.9；高石墙 x 16.8 宽 4.19 高 1.8（草捆紧贴其左侧，先跳草捆再上墙）；木栅门 x 24.0 高 2.4（伸手推开，互动点在 `interact`）。物件 Pivot = 底部左。碰撞：低石墙、草捆用 BoxCollider2D（顶面可站立）；高石墙当前由用户在 Unity 中手动微调为 BoxCollider2D Offset (2.0378294, 0.9)、Size (3.1901226, 1.8)，对象位置 (16.8, 0, 0)，顶面 y=1.8。该设置已保存于 Ch1_S1_Village.unity；Chapter1SceneBuilder 仍会按完整物件宽度生成碰撞体，重建场景会覆盖此手动值，详见 CH1_UNITY_PROGRESS.md。栅门用 Trigger。

预览：`S1_Village/_work/_preview_parallax_v9.mp4`（背景）、`_preview_parallax_v11_props.mp4`（含物件，用户确认的版本）。

### 2.2 森林小径（长 57.6u；文件夹 `TechArtAsset/Scenes/S1b_ForestPath/`）

| 层 | 文件 | 尺寸 | p | Sorting Order |
|---|---|---|---|---|
| L0 天空 | `_work/S1b_ForestPath_L0_Sky_wip.png` | — | 0.05 | -50 |
| L1 背景（路面以上整张森林） | `_work/S1b_ForestPath_L1_Far_wip.png` | 3629×1335 | **0.4** | -40 |
| L2 中景 | `_work/S1b_ForestPath_L2_Mid_wip.png` | — | 0.5 | -30（目前是空图层，可不导入） |
| L3 可行走层（含两条地沟） | `_work/S1b_ForestPath_L3_Walk_ditch_v2.png` | 6049×1335 | 1.0 | -10 |
| 物件 | `props/F_prop_bramble.png`、`F_prop_cross.png`、`F_prop_thornwall.png` | — | 1.0 | 0 / 1 |
| 妮芙 | — | — | — | 10 |
| L4 前景 | `_work/S1b_ForestPath_L4_Fore_wip.png` | 7258×1335 | 1.3 | 20 |

注意：森林的前排粗树干**没有**拆成中景（拆开后背后会露出空洞），整张森林作为一个背景层，p = 0.4。

地面与物件（`S1b_ForestPath_layout_v2.json`）：
- 地面分三段：0–30u、31.4–42u、44.6–57.6u。两个缺口就是地沟：**小沟 x 30–31.4（1.4u，走着跳得过）**、**大沟 x 42–44.6（2.6u，需要跑跳，前面有 10u 平地助跑）**。沟底按灰盒在 y = −1.6 / −1.8，沟底两侧做台阶或斜坡让玩家能爬回来；**掉沟不扣存在值**（只是绕回去）。地沟画面是 AI 局部重画的 V 形土坑，视觉比灰盒浅，以碰撞数据为准。
- 荆棘丛 x 48.4，宽 2.24 高 1.0：**纯装饰，不挡路**。
- 铁十字 x ≈ 50.5（露在荆棘丛右下）：拾取物，Trigger；拾取时妮芙播放「蹲下拾取」（暂用静态图）。拾取后显示「铁十字（断绳）」，加入背包。
- 受控荆棘墙 x 52.2，宽 2.2 高 3.0：**实心挡路**，跳不过去（比最高跳 2.4u 高）。拾到铁十字后按键释放 IronPulse，荆棘墙播放退散（先做淡出 + 黑烟占位）后碰撞关闭。
- 出口 x 57.0 → 切到 S2（S2 未做时先回菜单或显示「待续」）。

预览：`S1b_ForestPath/_work/_preview_parallax_v8_ditch.mp4`。

## 3. 课堂演示建议的搭建顺序

1. 新建场景 `Ch1_S1_Village`、`Ch1_S1b_ForestPath`；相机、Cinemachine、地面 y = 0 的灰盒碰撞（按 layout JSON，可写一个 Editor 脚本直接读 JSON 生成 BoxCollider2D）。
2. 放妮芙静态图 + PlayerController（手感参数按第 1 节），先在灰盒里调到「跳得过 1.2u 墙、跳不过 3u 墙、跑跳刚好过 2.6u 沟」。
3. 导入五层背景 + ParallaxLayer 脚本（一个 float p）；对照预览 MP4 检查。
4. 放物件与互动点（栅门推开、铁十字拾取、荆棘墙驱散）；三叶草光点按 layout 的 `lights`。
5. SceneLoader：菜单 Start → S1 → 森林 → （S2 / 回菜单）。
6. 可选：URP 2D Light 给铁十字一点冷光；后处理轻度 Bloom、暗角；森林越往右越暗可再加一层全屏渐变。

## 4. 暂时不做

- 妮芙骨骼动画（动作清单见 `NIAMH_ANIM_LIST_DEMO.md`，场景跑通后再拆件）。
- 荆棘墙红光裂缝的发光材质、IronPulse 冷光环正式特效（先用占位）。
- 层图片按 ≤2048 px 切段、Web 版压缩（PC 版先跑起来）。
- S2–S4 场景美术（S2 下一步出图）。

## 5. 交付后请记录

把实际用到的工程路径、脚本名、调过的手感数值、遇到的问题写回 `TechnicalArt/MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md`（或新建 `CH1_UNITY_PROGRESS.md`），并在 `ART_HANDOFF.md` §9 记一行。
