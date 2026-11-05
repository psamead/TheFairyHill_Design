# 第一章 v3 修正（2026-11-01，Batch A / B 试玩后）

> 前提：`CH1_UNITY_REVISION_v3.md`。冲突时以本文件为准。保留用户手调值（妮芙胶囊、高石墙、草捆）。

## Batch A 修正

### A1. 栅门右柱放到妮芙前面

**问题**：v3 把整个门放在妮芙后面（Order -5），妮芙站在右柱位置时盖住了石柱，看不出前后关系。

**改法**：只把**右边那根石柱**提到妮芙前面，左柱和门板仍在后面。

| 层 | Sprite | Sorting Order | 说明 |
|---|---|---|---|
| 后层 `Gate_Back` | 关门 `S1_prop_gate.png` / 开门 `S1_prop_gate_open.png`，按 E 切换（规则同 v3） | -5（妮芙后面） | 左柱、门板、右柱都在这张里 |
| 前层 `Gate_PostR_Front` | 新图 `S1_prop_gate_postR_front.png`（414×240，只有右柱，其余全透明） | **5**（妮芙前面） | 固定显示，不随开关门变化 |

- 新图在 `TechArtAsset/Scenes/S1_Village/props/`，画布与关门 / 开门图完全相同，放在同一位置（图片左边 x 24.0，宽 4.14u，同一个父物体下），右柱正好盖在后层的右柱上。
- 右柱范围约 x 27.17–28.14；左柱约 x 24.00–24.98，留在妮芙后面。
- 隐形墙、互动范围、开关规则不变。不要再用 v2 的 `post_L / boards / post_R` 拆分图。

**验收**：妮芙站在右柱位置时被右柱挡住一部分；站在左柱位置时她在左柱前面；开门后门洞里没有木条残留。

## Batch B 修正

### B1. 荆棘墙红光变成一大片灰白、模糊的“拉伸”纹理

**现象**：荆棘墙整面被一层灰白、糊糊的漩涡状纹理盖住，看不到墙本身，也没有红色。

**原因（不是素材问题）**：灰白纹理就是 `F_prop_thornwall_v3_glow.png` 这张遮罩本身（它是白色、故意做软的光斑）。它应该被染成暗红、半透明地叠在墙上，现在却以白色、几乎满强度叠加：
- 红光挂在 **SpriteRenderer** 上，材质用的是 URP `Particles/Unlit`（Additive）。代码通过 `SpriteRenderer.color` 给它染红 `#B0202A` 并做呼吸 Alpha。
- 但这个粒子 Shader 不读 SpriteRenderer 的颜色（Unity 6 的 Sprite 颜色走 Sprite 专用通道，粒子 Shader 不认），材质 `_BaseColor` 又是纯白 (1,1,1,1)。结果颜色和 Alpha 全部丢失 → 白色遮罩满强度 Additive 叠在暗色墙上 → 一片灰白，呼吸和闪烁也看不出来。
- 墙图 `F_prop_thornwall_v3.png` 本身是清晰的（1079×900，Unity 里未压缩、100 PPU，与相机 1u≈100px 一比一），不用换。

**改法**（`ThornWall.cs` + `Chapter1SceneBuilder.GetThornGlowMaterial`）：
- 颜色和 Alpha 改为写材质的 `_BaseColor`，不再写 `SpriteRenderer.color`。用 `MaterialPropertyBlock`（或运行时材质实例）设置 `_BaseColor = (176/255, 32/255, 42/255, alpha)`。
- `SetGlow(alpha)` 与 IronPulse 熄灭（0.3 s）都改用这个方式；Point Light 的强度规则不变。
- Builder 里把共享材质的 `_BaseColor` 默认设为 `#B0202A`、Alpha 0.5，这样编辑器里不运行也能看到正确的暗红。
- `glow.color` 保持白色，避免以后 Shader 换回 Sprite 系列时颜色被乘两次。

**验收**：墙本身的枝条清晰可见；枝条缝隙里透出暗红光，0.35–0.7 缓慢呼吸，偶尔快闪；没有任何灰白色。按 Q 后红光 0.3 s 内熄灭。

### B2. 森林暗场照明（Deepnest 风格，2026-11-04 改版）

> 参考：《空洞骑士》深邃巢穴（Deepnest）——整体近乎全黑，远景只剩一点冷蓝的轮廓，前景是纯黑剪影，角色身上一圈柔光是画面里最亮的东西。
> 效果预览：`TechnicalArt/mock/forest_dark_x20.jpg`（上：现在；中：冷白光；下：**暖光，用户选定（2026-11-04）**）。脚本 `TechnicalArt/tools/mock_forest_dark.py`。预览图左侧的横条纹是预览脚本的问题，游戏里不会有。

**现状问题**：A1/B1 之后，有人在 Niamh 下面放了一盏 **Global Light**——全局光不管放在哪都照亮整个画面，所以森林变得和白天一样亮。删掉它。

**1. 全局光**
- 全局光只有一盏，在 `Core_Persistent` 根下（不在 Niamh 下面）。关卡场景里不放 Global Light。
- `LevelInfo` 加 `ambientColor`、`ambientIntensity`，切关时在淡入**之前**写入。
  - 村庄：白色 1.0（不变）。
  - 森林：冷蓝 `#6878A0`，强度 **0.28**（用户可在 LevelInfo 里调，0.2–0.35 之间试）。

**2. 各层的处理**

| 层 | 材质 | 颜色（SpriteRenderer.color 乘色） | 说明 |
|---|---|---|---|
| L0_Sky | `Sprite-Unlit-Default` | `#38445C` | 远景不受妮芙的灯影响，只剩暗蓝轮廓 |
| L1_Far | `Sprite-Unlit-Default` | `#262F42` | 同上，更暗 |
| L2_Undergrowth、L3_Walk、L3b_GrassEdge | `Sprite-Lit-Default` | 白 | 受环境光 + 妮芙的灯 |
| 物件（荆棘丛、荆棘墙、十字架）、妮芙 | `Sprite-Lit-Default` | 白 | 同上 |
| L4_Fore | `Sprite-Unlit-Default` | `#08090E` | 前景变成纯黑剪影 |

只在森林这样设；村庄各层保持原样。数值写进 `S1b_ForestPath_layout_v4.json` 的 `layers`（加 `unlit`、`tint` 字段），builder 读取。

**3. 妮芙随身光**（取代那盏放错的 Global Light）
- Niamh 子物体 `Niamh_Light`，URP 2D **Point Light**，位置 (0, 1.2)。
- 颜色**暖光 `#FFE2B8`**（用户 2026-11-04 选定，预览图下排），强度 **1.2**，Inner Radius 0.8u，Outer Radius **5.5u**，Falloff Intensity 0.7（边缘柔和地衰减到黑），不开阴影。
- 强度 ±4% 慢呼吸（约 3 s），不闪。
- `LevelInfo.playerLight`：森林开、村庄关；进关 1 s 淡入。

**4. 辅助灯**（只保留会“讲事情”的光，写进 layout，builder 生成）

| 名称 | 位置 | 颜色 | 强度 / 半径 | 规则 |
|---|---|---|---|---|
| 三叶草光点 ×9 | layout 已有的 `lights` 坐标 | 淡绿 `#BFE8B0` | 0.6 / 1.2u | 常亮，沿跳跃弧线指路；同时放一个小的 Additive 光点 Sprite（可先用 `FX_soft_dot`，0.25u） |
| 十字架金光 | 十字架中心 | `#F2D28A` | 0.8 / 1.8u | x > 44.6 后与星星一起亮起；拾起后 0.5 s 熄灭 |
| 荆棘墙红光 | 墙中心 | `#B0202A` | **1.2 × 呼吸 Alpha** / **7u** | 暗场里是画面主色；IronPulse 时 0.3 s 熄灭 |
| 出口光 | (59, 1.5) | 冷紫 `#8A7BD0` | 0.7 / 4u | 墙消失后 1 s 内淡入 |

不再加暮光补光（与暗场冲突）。

**验收**
- 森林第一帧不黑也不亮成白天：远景只看得见暗蓝轮廓，前景是黑剪影，妮芙周围约 5u 被柔光照亮，是画面里最亮的地方。
- 走动时光跟着她；离开她的光，地面和树几乎看不清，但能看出路面的边。
- 光点沿两条沟的跳跃弧线发光；跳过大沟后十字架有金光；靠近荆棘墙时红光把周围照红。
- 墙消失后出口亮冷紫光。回到村庄亮度正常、妮芙身上无光。

### B3. 荆棘墙烟雾不显示，Console 报错 739 条

**现象**：按 Q 后看不到烟雾；Console 不停报 `Particle Velocity curves must all be in the same mode`。

**原因**：`CreateSmoke` 里 Velocity over Lifetime 只给 **y** 设了随机范围（Two Constants），x、z 还是默认的单个常数——Unity 要求 x / y / z 三条曲线模式一致，否则每帧报错，烟雾不正常模拟。余烬子发射器同样的问题。贴图本身是对的（`M_FX_SoftParticle` 已指向 `FX_soft_dot.png`）。

**改法**（`Chapter1SceneBuilder.CreateSmoke`）：
- 烟雾：`velocity.x = new MinMaxCurve(0f, 0f)`、`velocity.z = new MinMaxCurve(0f, 0f)`（与 y 一样是 Two Constants），`velocity.space = Local`。
- 余烬：同样把 x、z 设成 `MinMaxCurve(0f, 0f)`。
- 暗场里深紫黑烟看不见：烟雾颜色改为暗紫灰 `#3B2D4D`（Alpha 220 → 透明），余烬改亮红 `#E0303A`。烟雾材质是 Unlit，不受光照影响，所以在黑底上能看清。

**验收**：Console 里没有 Particle 报错；按 Q 后红光熄灭，接着整面墙冒出往上翻腾的紫灰烟雾和红色余烬，墙在 0.6 s 内淡出。

## 第三轮修正 C（2026-11-05，B2/B3 试玩后）

B2 暗场、B3 报错已生效。用户试玩后的 5 条：

### C1. 栅门石柱看起来悬空 → 柱脚加碎石堆
- 新图（`TechArtAsset/Scenes/S1_Village/props/`，脚本 `TechnicalArt/tools/make_gate_rubble.py`，从矮石墙底部取石块做成小土堆）：
  - `S1_prop_gate_rubble_L.png`（150×46）：左柱脚下，底边中心 x **24.49**、y **-0.12**，Order **-4**（妮芙后面，和左柱一起）。
  - `S1_prop_gate_rubble_R.png`（160×50）：右柱脚下，底边中心 x **27.65**、y **-0.15**，Order **6**（妮芙前面，盖在右柱前层上）。
- 碎石比地面线略低，盖住柱脚与路面的接缝，前面的右柱看起来“踩在地上、离镜头更近”。预览 `TechnicalArt/mock/_gate_rubble_chk.jpg`。
- 写进村庄布局 JSON 的 gate 块（`rubble` 字段），builder 生成；与开关门无关，始终显示。

### C2. 三叶草光点：运行时只要光，不要看得见的“灯”
- 去掉光点上的白色小圆点 Sprite（`FX_soft_dot` 0.25u），只保留 Point Light 2D 的淡绿光晕。
- 注：Scene 视图里的白色灯泡是 Unity 的 Gizmo 图标，游戏画面里不会出现；Game 视图的 Gizmos 按钮关掉即可。

### C3. 铁十字星星：更大、更夸张，原地呼吸 + 间歇旋转
- **主星**（十字架中心）：**1.6u**（原 0.8u 的 2 倍）。
  - 呼吸：缩放 0.85–1.15、Alpha 0.6–1.0，周期约 1.2 s，原地一闪一闪（不再快速开关）。
  - 间歇旋转：每 2.5–4 s 一次，0.4 s 内转 360°，同时放大到 1.4 倍再回落（“叮”一下）。
  - 背后加一层光晕：`FX_soft_dot`，2.5u，暖金 `#F2D28A`，Alpha 0.35，随呼吸一起明暗。
- **散星**：**0.8–1.4u**，在十字架周围 1.5u 内随机位置**原地**出现：长大 → 呼吸 1–2 次 → 淡出，每颗约 1.2 s；同时存在 3–5 颗；约 1/3 的散星出现时带一次慢旋转（0.8 s 转 180°）。
- 颜色暖白偏金，Additive（颜色写 `_BaseColor`，见 B1）。触发规则不变（x > 44.6 后出现，拾起后消失）。

### C4. 荆棘丛移到妮芙后面
- 荆棘丛 Order 由 12 改为 **-3**（妮芙后面），十字架 **-4**（仍在荆棘丛后面，透过枝条露出）。妮芙走过时不再被挡住。更新 layout v4 的 `sorting_order`。

### C5. 荆棘墙湮灭：暗场里要看得见，加火光亮点和发光烟雾，夸张
按 Q 后顺序：红光 0.3 s 熄灭 →（同时开始）下列效果，持续约 2 s：
- **爆闪**：墙中心一盏 Point Light 2D，橙 `#FF6A2A`，半径 **10u**，强度 0.1 s 内升到 **3**，再 1.2 s 降到 0。把周围树、地面和妮芙一起照亮。
- **墙“烧亮”**：墙 Sprite 颜色 0.2 s 内变成亮橙白 `#FFB070`，然后在 0.6 s 内淡出（原来是直接淡出）。
- **火星**：Additive（`M_FX_EmberAdditive`），爆发 **150** 颗 + 1.5 s 内每秒 60 颗；大小 0.08–0.25u；颜色 `#FFE6A0` → `#FF5A1F` → 透明；向上 2–6 u/s（60° 锥形散开），Noise 1.0，寿命 0.8–1.8 s；开 Trails（Ratio 0.5、Lifetime 0.15）拉出火星尾巴。
- **发光烟雾**：在原来暗紫灰烟雾之上再加一层 Additive 烟：爆发 40 颗，大小 2–4u，颜色 `#FF7A3A`（Alpha 0.3）→ `#6A2A80`（Alpha 0.15）→ 透明，向上 1–2 u/s，Noise 0.8，寿命 1.5–2.5 s。原暗烟保留，做“暗底”。
- 所有特效 Sorting Order **25**（在前景 L4 之上），速度曲线三轴同模式（B3 规则）。
- 爆闪结束后，出口冷紫光照常 1 s 淡入。

**验收（C）**：右柱脚下有碎石、不再悬空；光点只看到淡绿光晕；十字架主星大而醒目、原地呼吸并时不时转一圈；荆棘丛在妮芙后面；按 Q 后画面被橙光照亮，墙先烧亮再消失，大量火星带尾巴往上飞，暖色发光烟翻腾，暗场里清楚可见。

## 第四轮修正 D（2026-11-05 下午，C 试玩后）

### D1. 右柱碎石要挡住妮芙的脚
- 左柱碎石保持在妮芙后面（用户确认 OK）。
- 右柱碎石 `S1_prop_gate_rubble_R`：放大到 **1.4 倍**（约 2.24×0.7u），底边中心移到 (27.55, **-0.35**)，Order 6 不变。这样碎石顶部高过路面约 0.35u，妮芙站到右柱位置时脚被碎石盖住，读起来右柱和碎石在她前面。

### D2. 森林背景里的绿色光斑 → 删掉三叶草光点灯
- 光斑来自 9 盏三叶草 Point Light 打在中景矮植被上，不是全局光的问题。森林的“暗”已经由全局光（冷蓝 0.28）做到，不需要靠点光。
- 删除 9 盏 Clover Point Light（layout `light_fx` 里的 clover 项一起删）。妮芙的暖光、十字架金光、荆棘墙红光、出口光保留。
- 以后真正做三叶草收集物时，光点改用 Additive 小 Sprite（自发光，不照亮环境），不用 Point Light。

### D3. 十字架和星星：放到荆棘丛前面，离红墙远一点
- 十字架中心 x 由 50.58 改为 **47.8**（仍在荆棘丛范围 45.6–52.3 内、离开红墙和红光），y 不变。走近显现半径 2.5u 不变。
- 十字架 Order **-2**（荆棘丛 -3 之前、妮芙 0 之后）；星星和光晕 Order **12**（在荆棘墙和红光之上，不被挡住）。十字架金光跟着移到新位置。
- 触发线 x 44.6 不变。

### D4. 荆棘墙的白边 → 换去白边的新图
- 白边是抠图残留：半透明边缘像素是浅灰（平均约 146），而墙本身很暗（约 36），暗场里就成了一圈白线。
- 新图 `TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_thornwall_v4.png`（同尺寸 1079×900，脚本 `TechnicalArt/tools/fix_thornwall_edge.py`）：边缘颜色改用内部颜色外扩填充，最外一圈染暗红，最淡的雾边去掉——看起来是红光透出的光边。对比图 `TechnicalArt/mock/_tw_edge_compare.jpg`（左旧右新）。
- 红光遮罩 `F_prop_thornwall_v3_glow.png` 不变（同画布）。layout 里 thornwall 的 `sprite` 改为 v4。

**验收（D）**：妮芙站在右柱处脚被碎石挡住；森林背景没有绿色光斑；十字架在荆棘丛前面、离红墙有一段距离，星星完整可见；荆棘墙边缘没有白线，只有暗红光边。

## E. 三叶草光点 ShamrockLight（2026-11-05 定，素材已备）

设计早已有（`DEMO_IMPLEMENTATION_PLAN.md` Must：三叶草光点收集，每 10 个回复 1 点存在值；`handoff.md` ShamrockLight），只是一直没有素材，之前用 Point Light 临时代替（D2 已删）。

**外观**：飘在空中的发光三叶草，作为跳跃引导。约 0.35u（128 px 图）。手绘墨线风格，参考十字架上的三叶草圆章（`MJ_ref/AUTHOR_L7_66/CROSS_AUTHOR_REF.png`）。

**出图（用户用 Nano Banana，参考图 = CROSS_AUTHOR_REF.png）**：
```
Using the shamrock emblem on this iron cross as the style reference, draw a single
three-leaf shamrock as a standalone game collectible icon. Three heart-shaped leaves,
short curved stem, fresh spring green with a soft pale-gold inner glow and thin dark
ink outlines, hand-painted storybook style matching the reference. Front view, centered,
filling about 70% of the frame, plain flat white background, no shadow, no text,
no frame, no other objects. Square 1:1.
```
MJ 备选：`a single glowing three-leaf shamrock, game collectible icon, heart-shaped leaves, spring green with pale gold glow, thin dark ink outline, hand-painted storybook illustration, centered, plain white background, no shadow --ar 1:1 --v 7` + `--sref` 用 CROSS_AUTHOR_REF。
出 2–4 张，挑一张放进 `MJ_ref/SHAMROCK_01.png`。Claude 负责抠图、缩到 128 px、做光晕图和收集特效。

**表现（Unity，下一轮指令）**：
- 位置：村庄与森林布局里已有的 `lights` 坐标（沿跳跃弧线）。
- 浮动：上下 ±0.08u、周期约 2 s，左右轻摆 ±8°；每颗相位随机。
- 发光：背后一张 Additive 柔光光晕（自发光，**不用 Point Light**，不照亮背景）；暗场里也清楚可见。
- 收集：妮芙碰到 → 0.25 s 飞向妮芙胸口并缩小消失 + 一圈小绿光粒子 + 计数 +1（`GameState`）。每 10 个存在值 +1 的逻辑等存在值系统做时接入。
- 音效：先不加（Batch C 音频时一起做）。

**素材（已备，2026-11-05）**：原图 `MJ_ref/SHAMROCK_01.png`（Nano Banana 2.1，参考 CROSS_AUTHOR_REF）。脚本 `TechnicalArt/tools/make_shamrock.py` 抠图、去白边：
- `TechArtAsset/FX/Shamrock/FX_shamrock_128.png`：游戏内用，显示 **0.35u**（Sprite，PPU 100，pivot 居中，缩放 0.35/1.28）。
- `FX_shamrock_256.png`：背包 / HUD 图标。
- `FX_shamrock_glow.png`（384×384）：Additive 光晕，显示约 **1.0u**，颜色写 `_BaseColor` `#CFF0A0`，Alpha 0.6–0.85 随浮动慢呼吸。
- 收集特效：沿用 `FX_soft_dot`（绿 `#BFE8B0`，Additive，爆发 12 颗、0.06–0.12u、向外 1–2 u/s、寿命 0.4 s）。
- 暗场预览 `TechnicalArt/mock/_shamrock_chk.jpg`。

## 第五轮修正 F（2026-11-05 傍晚，D + 三叶草 E 试玩后）

用户确认：三叶草引导很好；荆棘墙湮灭（爆闪、火星、发光烟）效果很好。

### F1. 荆棘墙“从边缘向中心灼烧”消失
- 新遮罩 `TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_thornwall_v4_burnmask.png`（灰度，与墙同画布 1079×900；0 = 外缘最先烧，1 = 中心最后烧；距离场 + 噪声，火线不规则）。脚本 `TechnicalArt/tools/make_thornwall_burnmask.py`，阶段预览 `TechnicalArt/mock/_thornwall_burn_stages.jpg`。
- 墙改用一个溶解材质（URP 2D Sprite，HLSL 或 Shader Graph）：参数 `_Burn`（0→1）。`mask < _Burn` 的像素丢弃；`_Burn ≤ mask < _Burn + 0.06` 是火线，颜色亮橙 `#FF9A3C`，自发光（不受暗场光照影响），火线内侧 0.03 再加一圈暗红焦黑 `#3A0E08`。
- 时间线（取代原来的“烧亮 0.2 s + 淡出 0.6 s”）：红光 0.3 s 熄灭 → 爆闪、火星、发光烟照旧开始 → `_Burn` 在 **1.6 s** 内 0 → 1（前快后慢，EaseOut）→ 碰撞关闭 → 出口光淡入。火星发射区域可以跟着火线收缩（可选）。

### F2. 栅门音效
- 村庄开门 / 关门目前没有声音：音频批次（Batch C）还没交给 Codex，这次一起做。
- 用户觉得原来合成的开门声不对，并要求像守灯人菜单音效那样**拆段、由代码按事件播放**：门转动的吱呀一段，门停住 / 扣上一段（两者共用）。v3（脚本 `TechnicalArt/tools/make_gate_sfx_v3.py`，“黏滑摩擦脉冲 + 木头共振”合成）：
  - `TechArtAsset/Audio/SFX/SFX_Gate_Creak_01_v3.ogg` / `_02_v3` / `_03_v3`：合页吱呀三个变体（干声约 0.85 / 0.75 / 0.95 s，后面带约 0.5 s 混响尾）。每次随机取一个，不和上一次相同。
  - `SFX_Gate_Latch_v3.ogg`：门板撞停的木头闷响 + 门闩“咔”。开门转到头、关门扣上都用它。
- 播放规则：
  - **开门**（按 E）：播一个 Creak（pitch 1.0）→ 在 Creak 片段长度 − 0.5 s 时播 Latch（音量 0.6，表示门转到头停住）。
  - **关门**（离开范围）：播一个 Creak（pitch 0.9，略低、略慢）→ 同样时机播 Latch（音量 0.9，扣上更重）。
  - 门的图片切换时机不变；Creak 和 Latch 用同一个 AudioSource 的 PlayOneShot。音量总体 0.7。
- **快速来回开关门**（玩家在门前反复进出 / 连按 E）：
  - 无加载延迟：四个门音效导入设为 Load Type = **Decompress On Load**、Preload Audio Data 开；场景开始时就引用好，不在触发时 `Resources.Load`。
  - 两个 AudioSource：`creakSource` 用 `Play()`（可被打断），`latchSource` 用 `PlayOneShot`。
  - 新的开 / 关事件到来时：取消还没播出的 Latch（停掉计时协程），当前 Creak 在 0.05 s 内淡出并停止，再播新的 Creak。不会出现两段吱呀叠在一起。
  - 防抖：距离上一次开 / 关事件不足 0.15 s 的事件只切换门的状态与图片，不重播声音。
  - 已经播出的 Latch 不打断（很短，让它自然结束）。
- v1、v2 保留不删。用户不满意时可换成真实录音（freesound CC0），按同样文件名替换即可。

### F3. 十字架和星星：再远离红墙，排在所有东西前面
- 十字架中心 x 由 47.8 改为 **46.8**，y 不变（倒在荆棘丛左侧边缘，离红墙更远）。十字架金光跟着移。
- 星星（主星、散星、光晕）的 SpriteRenderer **和** ParticleSystemRenderer 的 Sorting Order 都设为 **30**（高于荆棘丛、荆棘墙、红光、前景 L4 的 20）。上一轮只改了一部分，仍被挡住。
- 主星位置 = 十字架中心上方 **0.8u**（现在落在地面以下）。

### F4. 主星：一颗大星星在原地呼吸、绕自己的中心转
- 原因：`FX_sparkle_star.png` 导入时 pivot 是 (0, 0)（左下角），所以旋转时整颗星绕角落甩出去。**改为 pivot (0.5, 0.5)**。
- 主星 1.6u，固定在原地不移动：
  - 呼吸：缩放 0.85 ↔ 1.15、Alpha 0.6 ↔ 1.0，周期 1.2 s。
  - 旋转与呼吸同步：每次“吸气”（变大）时绕自身中心顺时针转 **45°**（EaseInOut），“呼气”时停住——一下一下地转。
  - 间歇闪光：每 3 次呼吸一次，在最亮时放大到 1.5、光晕 Alpha 冲到 0.8，0.15 s 回落。
- 散星减少为同时 1–2 颗、0.5–0.8u，只在主星周围 1u 内原地闪一下，作为点缀。

**验收（F）**：按 Q 后墙从外缘向中心被一圈不规则的橙色火线吃掉；村庄开门 / 关门有声音（且用户认可）；十字架离红墙有明显距离，星星在所有东西前面完整可见；主星原地呼吸、绕自己中心一下一下地转，间歇闪亮。
