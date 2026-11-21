# MJ_ref 图片资产清单（ASSETS）

## 2026-11-22 OP03 去挂件候选归档

[U4 放大原图及参考](Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/README.md) 已归档。原图 2912 × 1632，保留为去挂件后的设计候选。原下载名和 SHA-256 见 [生成清单](Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/generation_record.json)。人读附录 B 与 Prompt 第 7 章补页见 [OP03 候选与提示词](../TechnicalArt/OP03_REFERENCE_ARCHIVE_2026-11-22.docx)。

## 2026-11-20 OP02 三轮放大图归档

[r01 U2、r02 U4、r03 U4](Slideshow/Opening_v1/OP02_listening_2026-11-20/README.md) 均已按原下载像素归档，2912 × 1632。对应原名与 SHA-256 见 [生成清单](Slideshow/Opening_v1/OP02_listening_2026-11-20/generation_record.json)。人读补页见 [OP02 三轮选图](../TechnicalArt/OP02_REFERENCE_ARCHIVE_2026-11-20.docx)。


## 2026-11-20 BG01 第二轮放大原图

[BG01_MJ_r02_U4_upscale_candidate_v1.png](Slideshow/Opening_v1/Background_Proposal_2026-11-19/BG01_MJ_r02_U4_upscale_candidate_v1.png) 与 [BG01_MJ_r02_U1_upscale_candidate_v1.png](Slideshow/Opening_v1/Background_Proposal_2026-11-19/BG01_MJ_r02_U1_upscale_candidate_v1.png) 已归档。均为 2912 × 1632，保留原下载像素与元数据。对应原名和 SHA-256 见 [生成清单](Slideshow/Opening_v1/generation_manifest.json)。人读附录与 Prompt 参考索引补页已同步到 [开场选图文档](../TechnicalArt/BG01_BG02_2026-11-19.docx)。


## 2026-11-20 妮芙五张参考图归档

三张 OP01 单人试验图统一位于 [单人制作试验目录](Slideshow/Opening_v1/OP01_separate_characters_2026-11-19/README.md)，两张左右侧视图位于 [Turnaround_v3](Characters/Niamh/Turnaround_v3/README.md)。原路径、当前路径、尺寸及 SHA-256 见 [五图清单](Characters/Niamh/archive_manifest_2026-11-20.json)。人读资产附录及 Prompt 集参考索引补页为 [妮芙参考图归档](../TechnicalArt/NIAMH_REFERENCE_ARCHIVE_2026-11-20.docx)。


## 2026-11-19 BG02 丘陵传说

新归档 r01 U4、r03 U4、r06 U2、r06 U4 四张 PNG 原图。逐图链接、设计用途和状态见[BG02 下载原图表](Slideshow/Opening_v1/Background_Proposal_2026-11-19/BG02_r01_r02_record.md)，原下载名与 SHA-256 见[生成清单](Slideshow/Opening_v1/generation_manifest.json)。[选图补页](../TechnicalArt/BG01_BG02_2026-11-19.docx) 收录图像、用途与提示词入口。


> 用途：给 Codex 等 Agent 读取，并用于追踪美术资产的版本。和 Word 版「附录 B / Prompt 集第 7 章」使用同一份数据。
> 位置：`ShareWorkFolder/MJ_ref/`。最后更新：2026-11-22（OP03 去挂件候选归档）。

## 约定

- 文件命名：`对象_REF.png` 表示用作 Midjourney 参考的裁切图，`对象_v2.png` 表示生成结果，后缀 `_vN` 表示版本。新版本不覆盖旧版本。
- 状态取值：存档、参考、当前定稿参考、定稿候选、已被 vN 取代。
- 每次新增或替换图片，请同步更新本表和下方的「变更记录」。

## 总表

| 文件 | 类别 | 对象 | 版本 | 来源 | 生成 / 裁切方式 | 用途 | 状态 |
|---|---|---|---|---|---|---|---|
| Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/OP03_MJ_r02_region03_U4_upscale_candidate_v1.png | 故事画 | OP03 两人跑向树林 | v1 | r02 U2 经三次局部修改 | 去挂件 U4 放大下载原图 | 衣装与构图修订底图 | 候选 |
| Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/references/OP03_r02_v3_side_reference.png | 角色参考 | 双人朝右侧面 | r02 | 两张 v3 侧视图 | 妮芙左、奥伊芯右并排 | 追溯本轮双人参考 | 历史 |
| Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/references/OP03_v3_side_reference_front_ornament_v2.png | 角色参考 | 双人朝右侧面 | v2 | 11 月 19 日修订妮芙侧视与奥伊芯 v3 | 以修订妮芙图替换左半 | 核对绿色前襟与金纹 | 当前参考 |
| ../TechArtAsset/Characters/Niamh/Cross_Actions/current/Niamh_cross_chest_local_v1.png | 动作静帧 | 妮芙胸前局部使用 | v1 | 用户胸前修订 PSD | 图层命名分组，右侧补透明画布至350×699，像素验证通过 | 关卡小怪、小障碍、小剧情；同名PSD为当前入口 | 当前静帧 |
| ../TechArtAsset/Characters/Niamh/Cross_Actions/current/Niamh_cross_raised_story_v1.png | 动作静帧 | 妮芙举起剧情释放 | v1 | 用户第二稿PSD | 图层命名分组，右裁全透明区至350×699，像素验证通过 | 剧情大光线、大型障碍湮灭的姿势；尚无光束特效 | 当前静帧 |
| ../TechArtAsset/Characters/Niamh/Cross_Actions/archive/psd_trials/Niamh_chest_hold_organized_v1.png | 动作静帧 | 妮芙胸前捧十字架 | v1 | 用户 `clean_wip_v1_m.psd` | 完整人物参考剪贴，用户手绘袖口及裁切游戏十字架；Agent 仅整理图层并导出 | 历史胸前命名稿；已由 Cross_Actions/current 中两动作取代 | 参考 |
| Characters/Niamh/Interaction_Study_2026-11-17/Niamh_raise_hands_MJ_r01_U1_raw_v1.png | 动作参考 | 妮芙举手，朝左 | v1 | 负责人下载的 MJ 保留轮 r01 U1 | 原图重命名归档，内容未修改 | 与 U2 组合双臂的参考 | 参考 |
| Characters/Niamh/Interaction_Study_2026-11-17/Niamh_raise_hands_MJ_r01_U2_raw_v1.png | 动作参考 | 妮芙举手，朝左 | v1 | 负责人下载的 MJ 保留轮 r01 U2 | 原图重命名归档，内容未修改 | 与 U1 组合双臂的参考 | 参考 |
| Characters/Niamh/Interaction_Study_2026-11-17/Niamh_raise_hands_MJ_r02_U4_raw_v1.png | 动作参考 | 妮芙举手握拳，朝左 | v1 | 负责人下载的 MJ 角度补跑轮 r02 U4 | 原图重命名归档，内容未修改 | 举手备用参考，十字架留到 PS 合成 | 参考 |
| Characters/Niamh/Interaction_Study_2026-11-17/Niamh_chest_hands_MJ_U1_raw_v1.png | 动作参考 | 妮芙胸前手势，朝右 | v1 | 负责人从 Discord 下载的 MJ U1 | 原图重命名归档，内容未修改 | 胸前手形与弯臂参考，握柄待检查 | 参考 |
| Characters/Niamh/Interaction_Study_2026-11-17/Niamh_chest_hands_MJ_U4_raw_v1.png | 动作参考 | 妮芙抬手，朝左 | v1 | 负责人从 Discord 下载的 MJ U4 | 原图重命名归档，内容未修改 | 抬起手的握拳参考，另一手垂下 | 参考 |
| ORIGINAL_SHEET.png | 原设计 | 总图 | v0 | 原作者 | 原作者提供的设计总图（对话中上传） | 全部设计的出发点 | 存档 |
| NIAMH_REF.png | 角色 | 妮芙 | v0 | 原设计总图裁切 | 裁左上主视图，白底方形，放大到 1024 | C01 首轮 Character Reference | 已被 v2 取代 |
| OISIN_REF.png | 角色 | 奥伊芯 | v0 | 原设计总图裁切 | 裁左下主视图，白底方形，1024 | C05 首轮 Character Reference（--cw 40） | 已被 v2 取代 |
| CROSS_REF.png | 道具 | 铁十字架 | v0 | 原设计总图裁切 | 裁道具图，去掉文字说明 | P01 Image Prompt | 参考 |
| LANDSCAPE_REF.png | 场景 | S1 风景 | v0 | 原设计总图裁切 | 原尺寸裁切，长边 1024 | S01 Image Prompt（--iw 0.5） | 参考 |
| SKETCH_1.png | 场景 | S2 古墓入口草图 | v0 | 原作者手绘 | 裁切，长边 1024 | S02 Image Prompt（--iw 0.5–0.8） | 参考 |
| SKETCH_2.png | 场景 | S4 藤蔓门厅草图 | v0 | 原作者手绘 | 裁切，长边 1024 | S04 Image Prompt | 参考 |
| SKETCH_3.png | 场景 | S3 古墓石廊草图 | v0 | 原作者手绘 | 裁切，长边 1024 | S03 Image Prompt | 参考 |
| Niamh_v2.png | 角色 | 妮芙 | v2 | Midjourney 生成 | C01（Niji 6, ar 3:2, cw 40, s 150, CR = NIAMH_REF）→ 编辑器 E01 重画头饰 | C01 结果（正 / 背） | 已被 v3 取代 |
| NIAMH_REF_v2.png | 角色 | 妮芙 | v2 | Niamh_v2 裁切 | 裁正面，方形 1024 | C01-R / C02 / C03 / C04 Character Reference（--cw 70–100） | 已被 v3 取代 |
| Niamh_v3.png | 角色 | 妮芙 | v3 | Niamh_v2 + PS 修改 | PS：十字架改暗铁色 + 手绘红绿缠线流苏；HEART_BUCKLE_REF 切左半贴腰带；手绘红绿手绳；靴子取 MJ 编辑结果（niji 6, Editor 涂 4 只靴子，prompt: forest green leather lace-up ankle boots…）→ Upscale (S) → 蒙版合成。源文件 Niamh_v3_wip.psd | 正 / 背标准立绘 | 当前定稿 |
| NIAMH_REF_v3.png | 角色 | 妮芙 | v3 | Niamh_v3 裁切 | 裁正面，补背景成方形，1024 | 3/4 侧面等后续生成的 Character Reference（--cw 70–100） | 当前定稿参考 |
| Niamh_v3_turnaround.png | 角色 | 妮芙四视图 | v3 | MJ Editor 扩画布 + PS | NIAMH_REF_v3 上传 MJ Editor，2:1 扩画布生成侧面+背面（niji 6）；PS：正面图的手移植到侧面、侧面眼睛调灰、侧面水平翻转得到朝右版本、清理挎包碎片。顺序：正面 / 侧面朝右（不带挎包）/ 侧面朝左 / 背面。源文件 Niamh_v3_turnaround.psd | 骨骼拆件与动画的标准参考（以朝右侧面为准） | 当前定稿 |
| NIAMH_REF_BOOTS.png | 角色 | 妮芙（靴子来源） | v3 | Midjourney 编辑 + Upscale (S) | 见 Niamh_v3 | 仅作靴子合成来源（十字架仍为旧绿色，勿直接使用） | 存档 |
| CIRCLET_REF.png | 饰物 | 妮芙家传银冠 | v2 | Niamh_v2 裁切 | 头饰特写，放大（原区域约 180 px） | P05 Image Prompt | 参考（清晰度有限） |
| CROSS_v2.png | 饰物 | 胸前十字架 | v2 | Niamh_v2 裁切 | 特写，放大（原区域约 80 px） | 造型参考 | 颜色错误（应为暗铁色） |
| Oisin_v2.png | 角色 | 奥伊芯 | v2 | Midjourney 生成 | C05-R（Niji 6, ar 16:9, cw 40, s 150, --no green cape, blonde hair, CR = OISIN_REF）→ Vary (Subtle) | C05 结果（3/4 正 / 正 / 背） | 已被 v3 取代 |
| OISIN_REF_v2.png | 角色 | 奥伊芯 | v2 | Oisin_v2 裁切 | 裁中间正面（带心形扣），方形 1024 | C06 及后续 Character Reference（--cw 70–100） | 已被 v3 取代 |
| OISIN_BACK_v2.png | 角色 | 奥伊芯背面 | v2 | Oisin_v2 裁切 | 裁背面，方形 1024 | 背面参考 | 参考 |
| Oisin_v3.png | 角色 | 奥伊芯三视图 | v3 | Oisin_v2 + PS（源 Oisin_v3_wip.psd） | 去掉铁钉 / 铁钥匙；大灰心换成右半心扣（妮芙半心扣翻转）；加红绿手绳 | 正面 / 3/4 / 背面定稿 | 当前定稿 |
| OISIN_REF_v3.png | 角色 | 奥伊芯正面 | v3 | Oisin_v3 裁切 | 正面方图 | 后续 MJ 参考（Style reference） | 当前定稿参考 |
| OISIN_SIDE_v3_raw.png | 角色 | 奥伊芯侧面原图 | v3 | MJ Create（niji 6，sref = OISIN_REF_v3，strict side profile 文字 prompt）→ Upscale (S) | 未修改的 MJ 原图 | 存档 | 存档 |
| Oisin_Side_v3_wip.png | 角色 | 奥伊芯朝右侧面 | v3 | OISIN_SIDE_v3_raw + PS（源 Oisin_Side_v3_wip.psd） | 眼睛琥珀色、头发偏红、白雏菊、裙摆米灰、去草、三叶草胸针、半心扣、手绳 | 拆件基准 | 当前定稿 |
| Oisin_v3_turnaround.png | 角色 | 奥伊芯四视图 | v3 | PS 拼合（源 Oisin_v3_turnaround.psd） | 顺序：正面 / 3/4 / 朝右侧面 / 背面；已知差异：侧面披肩画成长围巾，比正面短披肩长 | 骨骼拆件与动画参考（以朝右侧面为准） | 当前定稿 |
| HEART_BUCKLE_REF.png | 饰物 | 心形扣 | v2 | Oisin_v2 裁切 | 腰间特写，放大 | P04 Image Prompt；两人半心扣的基准 | 参考 |
| SunsetWorldEntrance.png | 主视觉 | 黄昏古墓入口（菜单 / 海报底图） | v2 | Midjourney 生成 | K2-v2（V7→编辑 --v 8.2, ar 16:9, s 250, 无参考图）选 1 号 → Upscale (S) → 编辑器 Smart Select 门洞 → Erase selection → 重画 Ogma 假身剪影（半透明青色） | 开始菜单背景 + 海报底图 | 定稿；右下角有 MJ 签名需遮盖 |
| MENU_BG_16x9.png | 主视觉 | 开始菜单背景 | v2 | SunsetWorldEntrance 裁切 | 居中裁 16:9，缩放 1920×1080 | Unity 标题菜单背景（门洞加欧甘字粒子 / 雾 / 剪影呼吸光） | 可用 |
| MENU_LAYOUT_GUIDE.png | 版式 | 菜单布局标注 | v2 | MENU_BG_16x9 标注 | 黄=标题，蓝=菜单按钮，青=门洞特效，红=签名遮盖 | UI 布局参考 | 参考 |
| POSTER_BG_2x3.png | 主视觉 | 海报底图 | v2 | SunsetWorldEntrance 裁切 | 裁 2:3（x 1050 起，避开签名），1200×1800 | 海报底图；标题天空偏窄，建议编辑器 2:3 向上扩图 | 临时 |
| POSTER_LAYOUT_GUIDE.png | 版式 | 海报布局标注 | v2 | POSTER_BG_2x3 标注 | 黄=标题，蓝=两主角背影合成，青=门洞字符 | 海报合成参考 | 参考 |
| NOBLE_DARK_REF.png | 角色 | 男妖精贵族（成熟黑暗版） | v0-作者新稿 | 原作者新稿裁切（角色（妖精贵族，路上小妖，铁制十字架）.jpg） | 从原图裁切，原尺寸 | 普卡假扮的 Ogma；需改 Q 版绘本风 | 参考（v2.2） |
| LANTERN_SPIRIT_REF.png | 角色 | 兜帽提灯小妖 | v0-作者新稿 | 原作者新稿裁切（同上） | 从原图裁切，原尺寸 | 路上小妖：黄眼=未被控制，红眼/裂纹变体=被普卡控制 | 参考（v2.2） |
| RELIC_CROSS_REF.png | 道具 | 铁十字圣物（原版造型） | v0-作者新稿 | 原作者新稿裁切（同上） | 从原图裁切，原尺寸 | 神族圣物原版；妮芙家传十字在此基础上加装饰 | 参考（v2.2） |
| ANCIENT_MEDIATOR_REF.png | 角色 | 金发少女（成熟版妮芙稿） | v0-作者新稿 | 原作者新稿裁切（角色（妮芙(Niamh)，奥伊芯（Ossian），女妖 （Bean Sídhe））.jpg） | 从原图裁切，原尺寸 | 千年前第一代媒介（回忆 / 序章） | 参考（v2.2） |
| ANCIENT_FRIEND_REF.png | 角色 | 红发少女（成熟版奥伊芯稿） | v0-作者新稿 | 原作者新稿裁切（同上） | 从原图裁切，原尺寸 | 千年前媒介的朋友（回忆 / 序章） | 参考（v2.2） |
| BANSHEE_REF.png | 角色 | 女妖 Bean Sídhe | v0-作者新稿 | 原作者新稿裁切（同上） | 从原图裁切，原尺寸 | 女妖；需降低头身比 | 参考（v2.2） |
| FOREST_A_REF.png | 场景 | 森林小径 A | v0-作者新稿 | 原作者新稿裁切（场景第一部分.jpg） | 从原图裁切，原尺寸 | 第一章 村庄→古墓之间的森林，奔跑教学 | 参考（v2.2） |
| FOREST_B_REF.png | 场景 | 森林小径 B（地面缺口） | v0-作者新稿 | 原作者新稿裁切（场景第一部分.jpg） | 从原图裁切，原尺寸 | 跳跃教学 | 参考（v2.2） |
| VILLAGE_FIELD_REF.png | 场景 | 绿色田野与小屋 | v0-作者新稿 | 原作者新稿裁切（场景第一部分.jpg） | 从原图裁切，原尺寸 | S1 村庄远景 | 参考（v2.2） |
| WOOD_WALL_REF.png | 场景 | 木墙、火把与刻痕符号 | v0-作者新稿 | 原作者新稿裁切（场景第一部分.jpg） | 从原图裁切，原尺寸 | 媒介小屋内部（回忆）或改石墙作 S3 欧甘字谜墙 | 参考（v2.2） |

## 变更记录

- 2026-11-22：将 OP03 去挂件 U4 放大原图移入镜头专用目录，校验原图散列一致。归档双人参考、三次局部选区与回传四宫格，更新人读补页和知识库。

- 2026-11-17 前襟花纹：将用户第二动作新增金色花纹同步胸前PSD/PNG、当前Motion_v8身体和静态备用图；保持尺寸、原点与alpha，用户原PSD保留。Unity对应两张PNG已复制且meta不变；导入与运行画面未验证。补片与版本记录见 `TechArtAsset/Characters/Niamh/Motion_v8/appearance_front_ornament_v1/`。

- 2026-11-17 晚：用户完成第二动作，确认只需胸前局部使用、举起剧情释放两动作。当前PSD/PNG统一命名迁入 `Cross_Actions/current/`，源稿、旧PSD和旧GIF分类归档，路径映射与SHA256见 `Cross_Actions/file_manifest.json`。画布统一350×699，人物像素保持；人读使用说明新增双动作规则文档。

- 2026-11-17：登记用户胸前衔接与道具修订的整理版静帧 `Niamh_chest_hold_organized_v1.png`；原 `_m` 保留，整理前后像素一致。旧 `Cross_Raise_Preview_v1` GIF 未采用此次最新道具修订，仅作粗测试。

- 2026-11-17（举手补充）：归档举手 r01 U1、U2 和角度补跑 r02 U4 三张原图，同目录现共五张 MJ 动作参考；移动前后 SHA256 一致，原下载名见 `source_manifest.json`。负责人明确 U1、U2 手臂可组合，U4 留备用，十字架在 Photoshop 合成，本轮不再继续追求 MJ 完整持物图。

- 2026-11-17：将负责人下载的两张妮芙 MJ 单人物原图重命名为 `Niamh_chest_hands_MJ_U1_raw_v1.png`、`Niamh_chest_hands_MJ_U4_raw_v1.png`，移至 `Characters/Niamh/Interaction_Study_2026-11-17/`；原文件名与 SHA256 见目录内 `source_manifest.json`。负责人认可圈出的手形可参考，未确认为完整双手持十字架成品。

| 日期 | 变更 |
|---|---|
| 2026-10-11 | v0：从原设计总图裁出 NIAMH_REF、OISIN_REF、CROSS_REF、LANDSCAPE_REF、SKETCH_1/2/3 |
| 2026-10-11 | v2：妮芙 C01 生成并经编辑器修改得到 Niamh_v2；裁出 NIAMH_REF_v2、CIRCLET_REF、CROSS_v2 |
| 2026-10-11 | v2：奥伊芯 C05-R 生成并经 Vary (Subtle) 得到 Oisin_v2；裁出 OISIN_REF_v2、OISIN_BACK_v2、HEART_BUCKLE_REF |
| 2026-10-11 | 加入 ORIGINAL_SHEET.png（原作者设计总图存档） |
- 2026-10-12：新增 SunsetWorldEntrance（故事 v2 菜单 / 海报底图，门洞剪影 = 冒充 Ogma 的普卡假身）及 16:9 菜单裁切、2:3 海报裁切、两张布局标注图。
- 2026-10-12：新增原作者新稿 10 张裁切（NOBLE_DARK / LANTERN_SPIRIT / RELIC_CROSS / ANCIENT_MEDIATOR / ANCIENT_FRIEND / BANSHEE / FOREST_A / FOREST_B / VILLAGE_FIELD / WOOD_WALL），配合故事 v2.2。
- 2026-10-16：妮芙 v3：在 PS 中修改十字架（暗铁 + 红绿缠线流苏）、加左半心扣、红绿手绳，靴子换为 MJ 编辑生成的绿色绑带中筒靴，得到 Niamh_v3（PSD 保留图层）；裁出 NIAMH_REF_v3。Niamh_v2 / NIAMH_REF_v2 标为已被 v3 取代。修改过程中的 _wip 临时文件已移入 deprecated/。
- 2026-10-17：妮芙四视图 Niamh_v3_turnaround（正 / 右侧 / 左侧 / 背），朝右侧面作为拆件基准；Niamh_v3_turnaround_wip 移入 deprecated/。
- 2026-10-18：奥伊芯 v3 定稿（去铁钉、右半心扣、手绳）；MJ 生成朝右侧面并 PS 调色，拼成四视图 Oisin_v3_turnaround；v2 标为已被取代。
- 2026-10-18：宣传美术（不在 MJ_ref，记录备查）：`TechArtAsset/Poster/POSTER_v1.png`（源 POSTER_wip.psd）、`TechArtAsset/Poster/TITLE_PLAQUE_nb.png`（Nano Banana 两行石刻标题牌）；`MJ_ref/TileArtFont_wip.psd` = 两行石刻标题牌（透明底，748×1424），已用于开始菜单；单行横版（H 已改大写）为 Nano Banana 输出，备用。
- 2026-10-23：开始菜单静态稿 v1 定稿：`TechArtAsset/Menu/MENU_wip.psd`（背景 = MENU_BG_16x9 去签名）；UI 图标 `TechArtAsset/UI/ICON_triskele.png`。
- 2026-10-26：新增 `MJ_ref/AUTHOR_L7_66/`：原作者新稿 14 张副本（S01–S10 场景、普卡、荆棘女王、K03、十字架），**只作参考**，用途见 ART_HANDOFF §5.1。
- 2026-10-26：（不在 MJ_ref，记录备查）由 `Niamh_v3_turnaround.png` 朝右侧面抠出 `TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png`（透明底，325×698）；比例参照图 `TechArtAsset/Scenes/_Scale/SCALE_REF_Ch1_v1.png`；第一章灰盒图 `TechArtAsset/Scenes/<Scene>/<Scene>_graybox_v1.png`（非美术成品，供构图与灰盒用）。
- 2026-10-29：森林小径关键帧 `FOREST_KEY_01.png`（备选 `_b`）、扩图 `FOREST_KEY_01_pan.png`、远景试作 `FOREST_FAR_01.png`（未采用）；物件 `FOREST_PROP_BRAMBLE_01.png`（备选 `_b`）、`FOREST_PROP_THORNWALL_01.png`；S1 物件 `S1_PROP_WALL_LOW_01.png`、`S1_PROP_HAY_01.png`（备选 `_b`、`_c`）、`S1_PROP_GATE_01.png`。铁十字游戏道具取自 `AUTHOR_L7_66/CROSS_AUTHOR_REF.png`。
- 2026-10-30：（不在 MJ_ref）新素材：`TechArtAsset/FX/FX_sparkle_star.png`、`FX_soft_dot.png`（脚本生成）；栅门三块、森林物件 v2、S1 前景 v2、森林草土边（均由已有图生成）。待 Nano Banana：UI 边框、荆棘墙边缘。
- 2026-10-30：`UI_frame_celtic_stone.png`（Nano Banana 2.1，带石底的凯尔特边框，留作参考；游戏用副本在 `TechArtAsset/UI/Frame/`，另有白底版与透明版）。

## 2026-11-19 BG01 黄昏村庄

本次归档两张负责人下载的 MJ 原图（2912 × 1632）。[U4](Slideshow/Opening_v1/Background_Proposal_2026-11-19/BG01_MJ_r01_U4_upscale_candidate_v1.png) 建议用于衔接下一镜，[U3](Slideshow/Opening_v1/Background_Proposal_2026-11-19/BG01_MJ_r01_U3_upscale_candidate_v1.png) 为备选。原名、编号与 SHA-256 见 [生成清单](Slideshow/Opening_v1/generation_manifest.json)。人读版附录 B 和 Prompt 集第 7 章补页见 [BG01 候选与 BG02 提示词索引](../TechnicalArt/BG01_BG02_2026-11-19.docx)。

## 2026-11-14 开场故事画占位补充

| 文件（MJ_ref 相对路径） | 用途与状态 |
| --- | --- |
| `Slideshow/Opening_v1/OP01_MJ_r04_U4_candidate_v1.png` | 原 r04 U4 单图，1456×816；候选存档 |
| `Slideshow/Opening_v1/OP01_MJ_r04_U4_upscale_candidate_v1.png` | 用户放大下载，2912×1632；批准 Unity 占位，正式画风未通过 |
| `Slideshow/Opening_v1/evidence/` | 后续提示词、遮罩和失败结果截图；仅过程证据 |

原下载名与散列见同目录 generation_manifest.json。游戏使用像素不变的副本 `TechArtAsset/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png`。人物偏 Q、轮廓较重、妮芙眼色需校正；OP02/OP03 无专门图片。

变更：2026-11-14 晚间重命名并归档两个用户下载文件，建立占位授权与生成失败记录。Word 当前资产补充、Prompt 与经验索引收在 `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx` 第 2、3、5 页，作为旧概念说明附录 B 与 Prompt 集第 7 章的本轮补充；旧文档保留原件。
