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

