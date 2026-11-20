# OP01 单独人物生成与合成试验

**2026-11-20 存储归档。** r01 U4、r03 U1、r04 U4 的根目录重复副本经 SHA-256 核对后合并，当前文件统一位于本目录。左右侧视裁图位于 MJ_ref/Characters/Niamh/Turnaround_v3/。历史 review 中 renamed_download_file 保留当时路径，canonical_current_file 指向当前路径。完整清单见 [归档清单](../../../Characters/Niamh/archive_manifest_2026-11-20.json)。


2026-11-19 负责人确认以 OP01 黄昏双人草坡画作为游戏内故事插画的画风基准。此目录保留单人生成、PhotoCraft 分层合成和 ImageGen 描摹的制作方法与过程文件。现行参考与用法见 [故事画知识库](../../../../TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md#2026-11-19-故事画风格基准与制作方法)。

日期 2026-11-19。适用于《妖精丘陵》开场OP01，负责人在Discord提交，设计端归档与合成。当前为待提交方案。

## 本轮目标

2026-11-19 负责人提出用 Google AI Studio 的 Nano Banana 试双图编辑。第一轮 U4 用于姿势与构图，正面原设计用于校准衣装与画风。当日试验已完成并收到反馈，风格笔触未通过，进入可编辑合成。见 Niamh_NanoBanana_r01_prompt.txt 和 Niamh_NanoBanana_r01_request.json。

2026-11-19 r01回报：负责人圈选右下U4为较接近的保留候选，并确认已放大下载。已从 MJ_ref 核对并归档为 Niamh_OP01_MJ_r01_U4_upscale.png（1792×2688）。评审记录见 Niamh_MJ_r01_review_r02_plan.json。下一轮 Niamh_MJ_r02_ready_prompt.txt 仅增加发尾停在裙摆附近的约束，引用与参数沿用已发r01。十字架按开场剧情由奥伊芯保管，妮芙本轮不佩戴。

负责人提出单独生成更接近两张v3原设计的人物，再与背景合成。先检验妮芙一组的身份、轻棕细线和柔和色块，选中后再推进奥伊芯与双人合成。源OP01和所有人工原稿保留。

当前双人故事画里人物外线、头发高光和衣装明暗较强。新候选对照原v3检查，不以旧动作试稿作人物定稿。原设计也有大头比例，沿用参考比例，避免额外拉长四肢。独立生成仍须检查脸、衣装、朝向及双手。

## Discord实际输入

### 2026-11-19 turnaround补充

从原版 `MJ_ref/Niamh_v3_turnaround.png` 以原比例截出两张 350×728 米色底 PNG。第二身为 `MJ_ref/Characters/Niamh/Turnaround_v3/Niamh_v3_turnaround_facing_right.png`，第三身为 `MJ_ref/Characters/Niamh/Turnaround_v3/Niamh_v3_turnaround_facing_left.png`，保留了各自挎包的可见情况。两张供单独核对发长、披风和朝向。OP01 的妮芙站画面左侧朝右；第三轮衣装试验的身份与画风输入见 `Niamh_MJ_r03_costume_trial_prompt.txt`，均取自正面原设计。修过手与前襟遮挡的侧面参考另见下文。

同日负责人指出朝右静态参考的前襟花纹盖住手部，已用PhotoCraft修正并同步本地 TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png。可编辑源和修前备份见该角色 Motion_v8/appearance_front_ornament_v2/。若Discord曾上传旧侧面PNG，本轮使用修后文件重新上传取得链接。

负责人提供 Niamh_v3_turnaround.png 与 Oisin_v3_turnaround.png，两张作为现有多视角设计资料。妮芙的朝右单人侧面已有 TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png，可用作身份与朝向参考；NIAMH_REF_v3.png继续提供柔和笔触与色彩。新增Niamh_prompt_v2_turnaround_template.txt，仍输出一个三分之四朝右的完整人物，原模板保留。需核对生成是否被侧面参考拉成严格侧面。

奥伊芯turnaround中的侧面比左侧正面更鲜亮，花冠更繁密，衣摆图案与笔触亦有差异。本轮保留OISIN_REF_v3.png作为身份和画风主参考，侧面只用于人工校对结构。Oisin_Side_v3_wip.png已查看，为同类偏鲜亮侧面，文件状态仍按WIP记录。整张turnaround用于人工核对；若提交单人参考，优先单视图，减少多人物排版对结果的影响。此建议尚未生成验证。

上传 MJ_ref/NIAMH_REF_v3.png 与 MJ_ref/OISIN_REF_v3.png 的原始PNG。已在Discord上传且可确认对应原图的有效图片链接可复用。图在聊天历史里出现，不代表新imagine自动引用。

两份txt中 NIAMH_IMAGE_URL / OISIN_IMAGE_URL 必须换成对应图片真实链接，包含cref与sref两处。此处没有经核验的两个原图链接。每轮仅引用该人物自己的原图。cref约束身份，sref参考同张原图的笔触与色彩。此组合为本轮新试验，尚无结果。旧截图开头是另一张动作图的Image Prompt，末尾cref来自侧面角色动作研究，身份图内容仍需点开核对。本轮提交全新提示词。

参数采用截图及项目记录可识别的Niji 6和cw 100，s150沿用旧动作建议。2:3为本轮给完整人物、披风和手势留位的画幅建议。模型可用性以负责人Discord实际返回为准，实际值写入生成记录。此组不设旧动作图的iw2。

先生成妮芙。检查灰眼、发型、头饰、绿披风、原前襟、包与靴子，开场妮芙不佩戴十字架。原v3图中带有十字架，因此明确用no cross并检查结果。奥伊芯的圣物可在合成时用已有道具补到她身上，核对红绿挂绳和遮挡。

BG01/BG02环境图使用村庄环境图作为风格依据，须在各自请求内指定有效链接和用途。生成环境的指令应采用对应环境参数与引用。人物身份图用于独立人物轮。

## 合成顺序

1. 两个人物分别得到可用候选。妮芙朝右、奥伊芯朝左，目光与伸手高度在合成画布对齐；先保持双手各自独立，避免强行生成接触的手。
2. 准备OP01干净草坡背景。现有双人图的人物覆盖区域需要重建，仅把新人叠上去会留下旧人物。原无人物丘陵图可作为重建依据；实际选用哪个底图，随合成文件记录。
3. MJ白底图需抠图得到实际alpha，检查发丝和袖口边缘。白底成图不等于已有透明素材。
4. Photoshop另存分层PSD，分开保留背景、妮芙、奥伊芯、接地影与前景草。调整尺度、地面透视、同向黄昏光和色温。人物双脚完整且接地，面部避开下方字幕区。
5. 导出一张静态合成候选给负责人看。像素、姿势、角色身份与手部通过后，才继续其他人物镜头。

## 张数说明

五张为五幅最终故事插画。章节卡复用故事画背景并叠加独立文字，为第六个显示页面，无需另生第六张插画。五张结构仍属待确认提议。人物和背景分开制作会增加源素材数量，最终故事页数量按序列计算。

## 原图与记录

每轮保留完整实际prompt、实际模型参数、引用链接与本地文件对应、参考用途、job链接或ID、四格原图、放大原图、选中编号和理由。原始文件名和SHA256写入manifest。候选、合成图、负责人认可与Unity接入各自记状态。

截图由负责人在本聊天提供，原样归档到 evidence/，仅作操作与画面证据，不能作为干净生成输入。两份英文prompt保留为未提交草稿。

官方说明于2026-11-19核对
- https://docs.midjourney.com/hc/en-us/articles/33329788681101-Legacy-Features
- https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference
- https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts


第三轮四格已于2026-11-19收到，负责人评价「这次更接近点」。负责人已下载左上 U1。现统一在本目录以 Niamh_OP01_MJ_r03_U1_upscale.png 保存（1792×2688），用于衣装参考。见 Niamh_MJ_r03_review.json。

第四轮四格已收到。U1、U3、U4 有向右伸手的动作，脸和躯干仍整体偏正面。左下 U3 的单条绿底金纹前襟可作局部参考。朝右互动姿势继续参考第一轮 U4。见 Niamh_MJ_r04_review.json。

第四轮右下 U4 的原图已按规则重命名为 Niamh_OP01_MJ_r04_U4_upscale.png，并复制进本目录。原下载名、尺寸和 SHA-256 见 Niamh_MJ_r04_review.json。第五轮在第四轮原提示词前加第一轮 U4 的图片链接。已填写负责人提供的链接，见 Niamh_MJ_r05_pose_reference_prompt.txt。第五轮四格已收到，U2 接近轻微右转，仍以第一轮 U4 作朝右互动参考。评审见 Niamh_MJ_r05_review.json。

妮芙单人合成初稿为 Niamh_OP01_composite_v01.psd 与同名 PNG。原设计裙料、前襟和绿腰带分层，来源与检查结果见 Niamh_OP01_composite_v01_record.json。

负责人随后提出用 ImageGen 按原版画风描摹一次。合成稿提供姿势与构图，正面原设计提供身份与画风。本轮产出 Niamh_OP01_ImageGen_style_trace_v01.png 候选，完整提示词、输入与散列见 Niamh_OP01_ImageGen_style_trace_v01_record.json。
