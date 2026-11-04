# 妖精丘陵 · 第一章场景制作计划 v1（S1 / 森林小径 / S2 / S3 + S4 规划，2026-10-26）

> 先读：`TechnicalArt/SCENE_SCALE_SPEC.md`（比例与跳跃尺度）。流程依据：技术美术方案第 3 章「背景制作流程」与 `ART_HANDOFF.md` §5.1（原作者 L7/66 稿只作参考、按需简化）。
> 每个场景都有：灰盒布局图 `<Scene>_graybox_v1.png` + 布局数据 `<Scene>_layout_v1.json`（单位 u，给 Unity / Codex 搭灰盒用），都在 `TechArtAsset/Scenes/<Scene>/`。
> 布局总表与生成脚本：`TechnicalArt/tools/ch1_layout_v1.json`、`make_graybox.py`、`validate_layout.py`（检查缺口、台阶、净空是否符合尺度规则；v1 已全部通过）。

## 0. 总览

| 场景 | 文件夹 | 长度 | 主色 | 玩法节拍 | 参考 |
|---|---|---|---|---|---|
| S1 黄昏村庄 | `S1_Village` | 38.4u（3840 px，2 屏） | 琥珀金 / 草绿 | 走、第一次跳（1.2u 墙）、借干草捆上 1.8u 墙、推开栅门、收光点 | S01（村庄布局、远丘古墓）、VILLAGE_FIELD_REF |
| 森林小径 | `S1b_ForestPath` | 57.6u（5760 px，3 屏） | 苔绿 / 暮金 → 渐暗 | 跑；走跳小沟 1.4u；跑跳大沟 2.6u；荆棘丛下捡回铁十字；第一次用冷光驱散受控荆棘 | FOREST_A（奔跑）、FOREST_B（地面缺口） |
| S2 古墓入口 | `S2_TombEntrance` | 28.8u（2880 px，1.5 屏） | 暮紫 / 灰白 | 上坡；蹲看奥伊芯的脚印；查看三螺旋石；进入青光门洞 | S02（三曲枝刻石、门洞构图）、SunsetWorldEntrance |
| S3 古墓石廊 | `S3_TombCorridor` | 48u（4800 px，2.5 屏） | 土褐 / 青绿妖火 | 入口关闭；拾发卡 → 十字架首次发光；涂鸦记忆；冷光显形 3 块浮石过深坑；收 4 块石牌；拼字开门 | S03（青绿妖火火把、两个小女孩涂鸦） |
| S4 藤蔓门厅（规划） | `S4_VineHall` | 21.6u（单屏 + 少量平移，镜头锁定） | 深青 / 古铜金 | 走到台前触发对话；名字交易；门开 → 结尾卡 | S04（石门 + 兜帽人的站位） |

Demo 节奏：S1 + 森林约 2–3 分钟，S2 约 2 分钟，S3 约 5–7 分钟，S4 约 3–4 分钟，与 `DEMO_IMPLEMENTATION_PLAN.md` §3 一致。

## 1. 五层拆层与出图宽度

视差系数 p = 该层相对可行走层的移动比例（1.0 与角色同速）。Unity 视差脚本：`layer.x = startX + camera.deltaX × (1 − p)`。
每层最小宽度 = 1920 + (场景长 − 1920) × p（单位 px）。**实际出图再加 5% 余量**。高度：S1 / 森林 / S2 / S4 为 1200 px（上下留余量），S3 为 1280 px（坑里镜头会下移）。

| 场景 | L0 天空 p0.05 | L1 远景 p0.2 | L2 中景 p0.5 | L3 可行走层 p1.0 | L4 前景 p1.3 |
|---|---|---|---|---|---|
| S1 | 2016 | 2304 | 2880 | 3840 | 4416 |
| 森林 | 2112 | 2688 | 3840 | 5760 | 6912 |
| S2 | 1968 | 2112 | 2400 | 2880 | 3168 |
| S3 | 2064 | 2496 | 3360 | 4800 | 5664 |
| S4 | 1932 | 1968 | 2040 | 2160 | 2232 |

超过 2048 px 宽的层，导出时按 ≤ 2048 px 分段切图（`<Scene>_L3_Walk_01.png`、`_02` …），源文件保留整张 PSD。

## 2. 制作步骤（每个场景相同）

1. **定构图**：把灰盒图（`<Scene>_graybox_v1.png`）当草图；在 PS 里新建全长画布（如 S1 3840×1200），按灰盒位置放好 `Niamh_side_static_v3.png`（高 210 px）。
2. **出关键帧**：Midjourney 用第 3 节的 prompt 出 16:9 关键帧（每场景 1–2 张），挑最接近灰盒节拍的一张；不满意的局部用 MJ 编辑器 Erase + 短 prompt 重画（一次改一处，见 ART_HANDOFF §7；不需要上传图片，所以不受上传故障影响）。
3. **拉长到全长**：MJ 编辑器的图片上传目前长期失败（技术美术方案「工具与流程调整」），所以扩图用 Photoshop 内容识别 / 生成式填充，或 Google Nano Banana 向右扩，直到可行走层宽度够用。MJ 里出的关键帧若能直接 Pan 也可以用。
4. **拆五层**：按 L0–L4 抠出；被遮住的地方用「空背景重画」补齐：擦掉上一层的物件后，用 PS 生成式填充或 Nano Banana 配合第 3 节每层的短 prompt 补出空的天空 / 远景 / 中景。
5. **对齐灰盒**：可行走层（L3）的地面线、平台、缺口必须与灰盒数字一致（1u = 100 px）；用 PS 参考线标出 y=0 地面线（画布底边上方 270 px + 余量）。
6. **统一调色**：五层合并后对整图做一张 LUT（`<Scene>_LUT.png`），保证不同 MJ 图拼在一起没有色差。
7. **可读性自查**：对照 `SCENE_SCALE_SPEC.md` 第 5 节的 6 条；必要时用 Design 插件的 design-critique 再查一遍主次与明暗层次。
8. **导出**：`<Scene>_L0_Sky.png … <Scene>_L4_Fore.png`（透明 PNG）+ 源文件 `<Scene>_wip.psd`，放 `TechArtAsset/Scenes/<Scene>/`；在 `MJ_ref/ASSETS.md` 登记用到的 MJ 图。

## 3. 各场景说明与 prompt

通用风格句（所有场景都加，保持和两位主角 v3、开始菜单一致）：

```
hand-painted storybook illustration, soft watercolor and gouache texture, gentle loose linework, simple readable shapes, low detail density, clear side-view 2D game background, flat horizontal ground line, no characters, no text --ar 16:9 --no people, text, letters, watermark, signature
```

不在 prompt 中写具体游戏、作品或艺术家名称；版本以 MJ 设置为准（场景用 V7 / 8.x）。

### 3.1 S1 黄昏村庄（`S1_Village`）

- **节拍**（灰盒编号）：①起点在妮芙家门口 → 第一次跳过 1.2u 干石墙（x≈10）→ 踩 0.9u 干草捆上 1.8u 石墙（x≈16–18）→ ②伸手推开木栅门（x≈24.5）→ ③走向出口进入森林。光点沿跳跃弧线排列，引导玩家第一次起跳。
- **借用 S01**：村庄的布局（村舍在左、田野向右展开）和远丘上的古墓剪影（伏笔）。**简化**：村舍只保留 1–2 栋，屋顶和墙面去掉碎纹理；远丘古墓只画轮廓和门洞一点青光。
- **层**：L0 黄昏渐变天空 + 云；L1 远丘与古墓剪影（x≈26–38 进入画面）；L2 村舍、山楂树、篱笆；L3 草地小路、干石墙、干草捆、栅门；L4 近处长草与野花（暗剪影，只在画面下角）。
- **关键帧 prompt**：`a quiet Irish village at golden dusk, a small whitewashed stone cottage with a thatched roof on the left, a dirt path running to the right across green fields, low dry stone walls, a hawthorn tree, distant rolling hills with a small ancient stone mound on the far hill, amber and grass-green palette, warm low sunlight,` + 通用风格句
- **补层 prompt**（擦掉上一层后用于生成式填充）：L1 `empty rolling green hills at dusk, soft haze`；L0 `clear amber dusk sky with soft clouds`；L2 `empty field behind the path, soft grass`。

### 3.2 森林小径（`S1b_ForestPath`）

> **照明定稿（2026-11-04）**：Deepnest 式暗场，妮芙身上暖光照亮周围约 5u，远景暗蓝、前景黑剪影。参考图 `TechnicalArt/mock/FOREST_LIGHTING_TARGET_warm.jpg`，参数见 `CH1_UNITY_REVISION_v3_fix.md` B2。

- **节拍**：0–26u 跑步段，缓坡和树根（FOREST_A）；①x≈30 走跳小沟 1.4u；之后 10u 平地助跑；x≈42 跑跳大沟 2.6u（FOREST_B 的地面缺口）；②x≈49 荆棘丛下捡到家传铁十字（挂绳断了）；紧接着 x≈52 一堵受控荆棘墙挡路 → 第一次用冷光，荆棘冒黑烟退开（玩家第一次看到「被控制的东西怕铁」）；③出口去 S2。
- **借用 FOREST_A / B**：A 的树干列和光斑节奏；B 的地面裂口和倒木。**简化**：树干分 2 个深度即可，不画满屏枝叶；裂口边缘画清楚（这是可行走层最重要的信息）。
- **层**：L0 树冠缝隙里的暮金天空；L1 远林剪影，向右逐渐变暗变紫（过渡到 S2）；L2 树干、倒木；L3 林间土路、树根、两条沟（沟底可见、不致死）、荆棘丛与荆棘墙（荆棘墙单独一层，做退散动画）；L4 近处蕨类和枝条剪影。
- **关键帧 prompt**：`a gentle Irish woodland path at late dusk, tall slender tree trunks with soft golden light between them, mossy roots on a dirt path, a narrow earth ravine crossing the path, ferns, the forest growing darker and more violet toward the right, moss green and dusky gold palette,` + 通用风格句
- **荆棘（单独出）**：`a tangle of dark thorny brambles with a faint red glow in the cracks, isolated on plain background` — 抠出后在 Unity 里做受控（红光裂纹）与退散两种状态。

### 3.3 S2 古墓入口（`S2_TombEntrance`）

- **节拍**：0–6u 平地 → 6–12u 上坡（升 1.5u）；①坡上蹲看奥伊芯的小脚印（x≈8.5）；②查看三螺旋刻石（x≈13.6–16.6，可跳过）；③白石英外墙中央的门洞（x≈24，1.6×3.4u）发青光，走进去切到 S3。
- **借用 S02**：三曲枝刻石放在门前、门洞居中的构图。**简化**：外墙只用大块白石英 + 灰石，螺旋纹只刻在一块刻石上（这是视觉焦点）；门洞内只有青光和一点雾，不画内部。
- **层**：L0 暮紫天空 + 第一颗星；L1 远丘；L2 古墓白石英外墙与草顶（墙上没有可踩的地方）；L3 山坡、刻石、门槛；L4 近处长草剪影。门洞青光用 Unity 2D Light 做，不画死在图上。
- **关键帧 prompt**：`a Neolithic passage tomb on a grassy hill at violet dusk, a curved facade of white quartz stones and grey granite, a low dark doorway in the center glowing faint blue-green, one large kerb stone carved with a triple spiral lying in front of the entrance, a grassy slope rising from the left, violet and pale grey palette,` + 通用风格句
- **补层 prompt**：L1 `empty grassy hills under a violet dusk sky`；L2（擦掉刻石后）`plain grassy slope in front of a white quartz wall`。

### 3.4 S3 古墓石廊（`S3_TombCorridor`）

- **节拍**：①进门后入口石块落下（回头受惊）；②x≈6 拾到奥伊芯的发卡 → 记忆 + 家传十字第一次发光；③x≈12 墙上两个小女孩的涂鸦（记忆碎片）；1.8u 壁龛台上第 1 块石牌；④x≈20.6 面对 9.4u 深坑举起十字架 → 3 块幻象浮石显形（高 0.6 / 1.2 / 0.6u，间距 1.4–1.5u），第 2 块石牌在中间浮石上方；掉下去后从坑底跳回左侧坑沿（高 2.0u，正好一次满跳；**不扣存在值**，2026-10-27 定）；x≈36 地上第 3 块石牌；2.0u 高台上第 4 块；⑤x≈45 欧甘字门，放入 4 块石牌拼字开门。
- **借用 S03**：青绿妖火火把（挂墙 2.4–2.8u 高，每 7–10u 一支）；墙上两个小女孩的涂鸦。**简化**：墙砖只在可行走层附近画清楚，往上逐渐融进暗部；火把是主光源，画面其他地方保持暗。
- **层**：L0 最深处的暗部 + 青绿雾（几乎纯色）；L1 远处墓道拱形剪影；L2 巨石墙面、涂鸦（涂鸦单独一层，记忆触发时发光）、火把支架；L3 石板地面、壁龛台、高台、坑沿、字门；浮石单独成组（显形 Shader）；L4 近处垂下的石块与树根剪影。火焰与光用粒子 + 2D Light。
- **关键帧 prompt**：`inside an ancient stone passage tomb, a long horizontal corridor of huge rough stone blocks, teal-green magical flames burning in iron torch holders on the walls, a dark pit in the stone floor, a simple childlike chalk drawing of two little girls holding hands on one wall, earthy brown and teal palette, deep shadows, warm-cool contrast,` + 通用风格句
- **字门与石牌**：欧甘字母 MJ 画不对，门和石牌只画空白刻槽；字母用 Unity 贴图叠上（ART_HANDOFF §4）。

### 3.5 S4 藤蔓门厅（规划，本次不出图）

- **布局**：单屏（21.6u），进入后镜头锁定。左侧入口；x≈12.4 起 0.5u 的缓坡台；假 Ogma 站在台上 x≈15.8，背后是 6u 高的藤蔓石门；走到 x≈11.5 触发对话。交易结束后石门打开，接结尾卡。
- **借用 S04**：石门居中偏右、兜帽人物站在门前台上的站位。**简化**：藤蔓只沿门框和墙缝生长，不铺满；古铜金光只从门缝漏出，作为画面唯一的暖色焦点。
- **注意**：假 Ogma 的脸被光晕遮住（Unity 里用发光 Sprite 叠在脸上），背景不要在他头部位置放亮色，否则抢光晕。
- **待定**：交易对话期间的镜头推近（可用 Cinemachine 缩放到约 0.8 倍）；第三选项（反制符文，Could）需要字门同款的刻槽 UI。

## 4. 本次未决

1. ~~出图方式~~ **已定（2026-10-27）：先用 Midjourney 试出图**（用户手动出图，用第 3 节的 prompt；MJ 编辑器的图片上传是否已修复尚不清楚，用户会再试；修好了就用 MJ 编辑器扩图与补层，否则仍用 PS 生成式填充 / Nano Banana）。建议从森林小径或 S1 开始，每场景先出 2–4 张关键帧挑一张。
2. ~~S3 掉坑的代价~~ **已定（2026-10-27）：只跳回左侧坑沿，不扣存在值**（Demo 存在值系统简化）。

## 5. 进度：S1（2026-10-27）

- 关键帧：`MJ_ref/S1_VILLAGE_KEY_03_pan.png`（4160×1152，MJ V8.1 Raw + 菜单背景作风格参考 `--sw 40`，编辑器 2:1 → 65:18 一次向右扩图；备选 `_pan_b`）。MJ 编辑器扩图可用（不需要上传）。
- **比例决定**：原尺度使用（不放大）。路面在原图 y≈1000，底部补 118 px 深草，使脚底距画底 270 px；整幅构图正好放进镜头。村舍在田野后方，作为中景（L2），不在可行走层；妮芙起点改为「村舍前的田间小路」。放大 1.5 倍的方案试过，天空和村舍顶会被镜头裁掉，放弃。
- **自动粗拆五层（WIP）**：`TechArtAsset/Scenes/S1_Village/_work/S1_Village_L0_Sky_wip.png … L4_Fore_wip.png`，脚本 `TechnicalArt/tools/split_s1_layers.py`；视差预览 `_preview_parallax_v2.jpg / .gif`（`preview_parallax.py`）。
- **待 PS 修**：① 远景层村舍背后的补画现在是模糊色块（视差时会露出），用生成式填充补出山坡与树丛；② 天空与山、田野与树线交界有零星黑点；③ 灰盒里的干石墙 1.2u、干草捆、1.8u 石墙、木栅门需要单独画成可行走层物件（原图的石墙在中景，不能踩）；④ 远丘只保留中间那座古墓（另两座在镜头外，裁掉即可）。
- 2026-10-27 修正：① 妮芙侧面图重抠（v1 把与底色相近的手臂、小腿、耳后皮肤抠掉了；现在只把与画布边缘连通的底色当背景），旧版在 `deprecated/Niamh_side_static_v3.png`，比例图与灰盒图已重新生成；② 田野顶边的黑块：中景从树线下的墨线以下开始，远景被遮住的部分改铺田野中位色；③ 前景层右端不够宽，改为水平镜像接上。最新预览 `_preview_parallax_v3.jpg / .gif`。
- 2026-10-27 远景补画完成：在 MJ 编辑器里把关键帧的村舍、树、石墙和左上小尖顶擦掉重画，得到 `MJ_ref/S1_VILLAGE_KEY_03_pan_empty.png`；脚本只取擦除区域（羽化 25 px）替换进远景 / 天空层，村舍背后现在是真正画出的山坡与树丛，不再是模糊色块。远丘只剩中间一座古墓。最新预览 `_preview_parallax_v4.mp4`（以 MP4 为准，GIF 只有 256 色会闪烁变色）。
- MJ 编辑器偶尔提交失败（提示 fail to upload），重新提交一次即可。
- S1 剩余：单独画可行走物件（干石墙 1.2u、干草捆、1.8u 石墙、木栅门）；正式导出前把各层按 ≤2048 px 切段。
- 2026-10-27 v5：修两处拉伸模糊：① 石墙下方的田野改由中景层完整覆盖（之前留空，露出远景的拉伸色）；② 可行走层不再向下拉伸，前景草空隙里露出的是原图的草。预览 `_preview_parallax_v5.mp4`。
- 2026-10-27 v6：树线下方那条模糊横带来自远景层「铺中位色」的补法；改为远景层树线以下直接用原图田野，中景与远景之间露出的窄缝就是真实纹理。预览 `_preview_parallax_v6.mp4`。经验：**补被遮挡区域时优先用真实画面（原图或 MJ 擦除重画），不要用拉伸或平均色**，视差一动就会露出来。
- 2026-10-28 v7：天空层残留了第二条山脊线（按颜色分天空时，山顶受光的部分被当成天空，和远景错开就出现两条线）。改为逐列从上往下找山体色定出山脊，山脊上方 8 px 以下全归远景，天空层在山脊以下整块重补。预览 `_preview_parallax_v7.mp4`。
- 2026-10-28 v8：天空里漂着的小黑点 / 短线（原画山肩上的虚线落在山脊判定线以上，被留在天空层，和山体错开）一并从天空层擦掉重补；天空层上半部已无暗点。预览 `_preview_parallax_v8.mp4`。
- 2026-10-28 v9：开场左上角的大缺口——最左边的山坡是低饱和的灰绿色，山脊判定没认出来，整块被分进天空层，和远景错开后露出空白竖条。山体色加入低饱和的冷色，左上角现在整块属于远景。预览 `_preview_parallax_v9.mp4`。
- **2026-10-29 S1 背景五层 v9 通过（用户确认）**。现行文件：`_work/S1_Village_L0_Sky_wip.png … L4_Fore_wip.png` + `_preview_parallax_v9.mp4`；旧预览移到 `deprecated/S1_Village_work_old/`。S1 剩余：可行走物件（干石墙 1.2u、干草捆、1.8u 石墙、木栅门）与正式导出切段。
- 2026-10-29 可行走物件：MJ 出图 `MJ_ref/S1_PROP_WALL_LOW_01.png`、`S1_PROP_HAY_01.png`（备选 `_b`、`_c`）、`S1_PROP_GATE_01.png`；高石墙 MJ 只出得来石柱，改为**低石墙同一张图放大**。抠图脚本 `TechnicalArt/tools/cut_props.py`，摆放脚本 `place_s1_props.py`。成品在 `TechArtAsset/Scenes/S1_Village/props/`：`S1_prop_wall_low.png`（1.2u，宽 2.8u）、`S1_prop_hay.png`（0.9u，宽 1.7u）、`S1_prop_wall_tall.png`（1.8u，宽 4.2u）、`S1_prop_gate.png`（2.4u）。布局更新为 `S1_Village_layout_v2.json`（地面拉平，物件宽度按实际图片；草捆紧贴高墙左侧）。预览 `_work/_preview_parallax_v10_props.mp4`。
- **2026-10-29 S1 完成 v1（用户确认 `_preview_parallax_v11_props.mp4`）**：栅门下方空隙的米色残留已去除（cut_props v3）。下一步：森林小径。

## 6. 进度：森林小径（2026-10-29）

- 关键帧 `MJ_ref/FOREST_KEY_01.png`（备选 `_b`），MJ 编辑器一次扩到 127:36（4064×1152，约 3.5:1）→ `FOREST_KEY_01_pan.png`。编辑器里 `--sw` 会被忽略（风格来自原图）。
- 自动拆五层 `TechnicalArt/tools/split_forest_layers.py` → `TechArtAsset/Scenes/S1b_ForestPath/_work/S1b_ForestPath_L0…L4_wip.png`，预览 `_preview_parallax_v2.mp4`。原尺度，路面在原图 y≈1065；可行走层与前景不够宽处水平镜像拼接。中景 = 前排深色树干 + 灌木带；远景被挡处：粗树干用左侧等宽背景镜像复制，细缝按行插值（v1 的横向拉丝已去掉）。路面下方用灌木带翻转压暗补齐。越往右整体压暗、偏紫，过渡到 S2。
- 待做：两条地沟（1.4u、2.6u）、荆棘丛 + 铁十字、受控荆棘墙，作为可行走物件单独出图。
- 2026-10-29 v6：拆前排粗树干的方案行不通（树干背后的空洞太宽：镜像复制有重复树、编辑器擦除会补回粗树干、另出的远景图 `FOREST_FAR_01.png` 风格与色彩接不上）。改为**路面以上整张原图作为一个背景层（视差 0.4）**，可行走层 1.0、前景 1.3；中景层留空，之后放地沟、荆棘等物件。没有空洞可露，画面干净。预览 `_preview_parallax_v6.mp4`。经验：前景物体又大又密的关键帧，不要硬拆；视差主要靠「背景 / 路面 / 前景」三层差就够。
- **2026-10-29 森林小径背景 v6 通过（用户确认）**。下一步：地沟 ×2、荆棘丛（藏铁十字）、受控荆棘墙，单独出图做物件。
- 2026-10-29 森林物件 v1：荆棘丛 `MJ_ref/FOREST_PROP_BRAMBLE_01.png`（备选 `_b`）→ `S1b_ForestPath/props/F_prop_bramble.png`（1.0u，x≈48.4，下方暗洞放铁十字，十字架小道具未做）；荆棘墙 `FOREST_PROP_THORNWALL_01.png` 取中段竖向拉成 `F_prop_thornwall.png`（3.0u×2.2u，x=52.2，红光裂缝待加强）。地沟 MJ 出不准，改脚本 `make_forest_ditches.py` 在可行走层上挖（`S1b_ForestPath_L3_Walk_ditch_wip.png`）：目前读得出是深洞，但边缘方正像箱子，待用户决定 PS 手修或接受为占位。预览 `_preview_parallax_v7_props.mp4`。
- 2026-10-29 铁十字：用原作者新稿 `MJ_ref/AUTHOR_L7_66/CROSS_AUTHOR_REF.png`（暗铁 + 金边 + 红绿绳 + 三叶草，符合 v3 设定），抠出 `props/F_prop_cross_full.png`（背包 / 特写用大图，只留一小截断绳）与地面小图 `F_prop_cross.png`（侧倒，约 0.4u，露在荆棘丛右下）。荆棘丛底部残留的蓝灰影子已去掉。地沟边缘待用户在 PS 手修。
- 2026-10-29 地沟 v2：用 Google AI Studio 的 Nano Banana 2.1 在原图上局部重画两个坑（输入 / 输出在 `S1b_ForestPath/_ditch_fix/`，同一对话里先 A 后 B，画法一致），脚本 `paste_ditch_fix.py` 按 `_offsets.json` 贴回可行走层（只取路面上沿以下、沟两侧各 2u，羽化）→ `S1b_ForestPath_L3_Walk_ditch_v2.png`。预览 `_preview_parallax_v8_ditch.mp4`。经验：局部修图（保留周围不变）用 Nano Banana 比 MJ 准；MJ 适合出整张关键帧和独立物件。
- **2026-10-29 S1 + 森林小径美术 v1 完成**，交 Unity：`TechnicalArt/CH1_UNITY_HANDOFF.md`。下一个出图场景：S2 古墓入口。

## 7. 试玩后修改（2026-10-30）

见 `TechnicalArt/CH1_UNITY_REVISION_v2.md`。经验已整理进 `TechnicalArt/LESSONS_SCENE_PIPELINE.md` §3–4（视差眩晕、物件夸张、先暗示后揭示）。之后出 S2 时：背景层的地面部分尽量平淡，有细节的东西放在与路面同速的层；关键物件一开始就按夸张尺寸出图。
