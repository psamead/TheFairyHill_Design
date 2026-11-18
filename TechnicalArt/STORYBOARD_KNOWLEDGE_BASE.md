# 开场故事画与章节过渡知识库

**2026-11-19 Unity反馈经验：** Unity报告和20张原生截图的设计端入口为 `ForDesignScreenShot/2026-11-18_for-opening-cross-raise/README.md`。本轮证据是Unity Editor工具驱动与Input System模拟输入：可证明指定状态与保护逻辑被触发，不能替代真实键鼠、完整人工路线、声音、性能或负责人主观验收。报告中移动/跳跃恢复速度与保存日志不一致，引用数值前应复测。亮天空上的Next/Skip对比偏弱暂列待审观察，不自动改稿。日期/轮次目录、编号原图、源名映射与SHA256能让后续设计核图而不破坏Unity源证据；排版QA和美术候选仍放各自目录。详见 `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`。

**2026-11-18 休息期间推送授权（历史快照）：** 负责人明确可以传大文件，源码、美术、PSD及保留GIF发展记录随后完成推送。此处记录的是任务执行前的当时状态；后续Unity回报见本文件顶部2026-11-19经验条目。

**2026-11-18 开场界面、按键下划线与举高动作试装（派发时记录）：** 已参考双方新导入Claude记录和守灯人实际界面，给现有开场加入保持比例的铺满故事画、柔和底部字幕区与轻量导航；按键字母／名称加下划线。终段受控红墙Q事件采用B直接举高，使用用户原画与新花纹，原墙体消解结束恢复v8。代码和资源已放实际工程，离线C#类型检查通过；“Editor导入、Play Mode和用户画面认可仍待验证”是当时的派发状态，Unity运行反馈见本文顶部2026-11-19记录。没有新增大光束或胸前普通战斗功能。

任务单唯一入口为共享设计目录 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`，对方直接读取，无需复制任务单到Unity工程。网络端回报保存在Unity `Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md`；设计端归档见 `ForDesignScreenShot/2026-11-18_for-opening-cross-raise/`。人读版 `TechnicalArt/妖精丘陵_开场界面与举高动作试装_2026-11-18.docx`，完整状态/经验 `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`。初始待运行状态由2026-11-19实测记录替代；尚待负责人审看的项目继续标注待确认。

更新：2026-11-16。项目：The Fairy Hills。对象：负责人、学生、美术、制作与排版人员及任意后续 Agent。
用途：独立于聊天保留来源、审美判断、失败经验和 Unity 接手依据。故事画占位试装与妮芙动作概念各有独立状态；逐项看下文，不能把一个项目的批准套用到另一项。

## 先看当前决定

**2026-11-18 已选定 B：** 第二种十字架动作采用 idle 直接举高，无胸前中间姿势。当前预览 `TechArtAsset/Characters/Niamh/Cross_Actions/previews/raised_fast_v3/Niamh_raised_fast_direct_v3.gif`，循环2秒（idle 300ms、举高1080ms、idle 620ms）。用户选择覆盖起手方式和预览节奏；不是技能冷却、光束时序或 Unity 运行验收。A、慢版、过渡试做和持势 GIF 全部保留作为发展记录。



**2026-11-17 衣装一致性更新：** 第二稿新增金色前襟花纹已同步到胸前动作、基础 `Motion_v8/parts/body.png` 与静态备用图；两动作画布仍350×699，基础角色仍327×699，alpha保持。新增可编辑修订源和备份见 `TechArtAsset/Characters/Niamh/Motion_v8/appearance_front_ornament_v1/`。Unity实际身体和静态备用PNG已网络复制，`.meta`不变；本次未连接Editor或验证Play Mode。当前源用户PSD不覆盖，重导出基础身体须使用新增修订源。



**2026-11-17 晚间最新决定：两个动作足够，不再制作第三个动作。** 第一个 `cross_chest_local`（胸前）用于关卡内小怪、小障碍和小剧情；第二个 `cross_raised_story`（举起）用于剧情触发的大光线、湮灭大型障碍等事件。当前文件统一放 `TechArtAsset/Characters/Niamh/Cross_Actions/current/`，使用语义名 PSD/PNG；画布均为 350×699，保留左上原点与人物像素。用户原稿、旧试验和旧粗 GIF 已分类，路径变更及像素校验见该目录 `file_manifest.json`。

Agent 使用原则见 `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md`，人读说明见 `TechnicalArt/妮芙十字架双动作使用规则与制作交接_v1.docx`，机器规则见 `TechArtAsset/Characters/Niamh/Cross_Actions/action_usage_rules.json`。两张用户绘画已准备和整理；连续动画、大光线特效及 Unity 接入尚未完成。该使用原则不自动扩大当前 Demo 的战斗系统范围。以下较早的“等待第二姿势 / 制作高举或第三姿势 / 当前仅胸前”记录只作历史，不再是任务要求。



**妮芙动作独立状态更新（2026-11-17）：** 用户已从完整人物参考剪贴胸前动作，手绘袖口过渡，并在最新 `_m` 调整和裁切现有游戏十字架。图层整理入口为 `TechArtAsset/Characters/Niamh/Cross_Actions/archive/psd_trials/Niamh_chest_hold_organized_v1.psd`；文件状态见该目录 `README.md`，方法集中于 `TechnicalArt/LESSONS_CHARACTER_ANIMATION.md` 最新工作流。较早的举十字 GIF 仅是面前高度粗测试，未采用最新道具修订，不能当成完成动画。此轮整理后停下，下一姿势由用户制作。以下故事画占位决定保持独立。

负责人选择 r04 U4 的双人黄昏草坡图放大，批准临时用于开场与第一章封面。背景色彩、草地和人物神态较接近；人物仍偏 Q、外轮廓过强、妮芙眼睛偏绿。批准占位不等于角色或画风定稿，不回写角色 v3 基准。

- 来源、原下载名、尺寸与 SHA-256：`MJ_ref/Slideshow/Opening_v1/generation_manifest.json`。
- MJ 原始单图：`MJ_ref/Slideshow/Opening_v1/OP01_MJ_r04_U4_candidate_v1.png`，1456×816。
- MJ 放大原图：同目录 `OP01_MJ_r04_U4_upscale_candidate_v1.png`，2912×1632。
- 游戏占位副本：`TechArtAsset/Storyboards/Opening_v1/placeholder/OP01_friends_dusk_placeholder_v1.png`。像素未改动，文件散列与放大原图一致。
- OP02/OP03 无专门成片。本轮用同一张 OP01 做三个独立字幕节拍，仅供流程和阅读节奏试玩。后续只换数据中的图片即可。

## 风格的判断顺序

人物以 `MJ_ref/NIAMH_REF_v3.png`、`OISIN_REF_v3.png` 及各自朝右侧面定稿为身份与手绘处理基准；环境以 `S1_VILLAGE_KEY_03_pan_empty.png` 和村庄实机为准。`MENU_BG_16x9.png` 可辅助判断环境色块与线条，不能把夜间菜单配色强加给黄昏开场。

原角色本身有适度大头，负责人反对的是新图进一步夸张、深色轮廓像贴纸、笔触过硬。不要把“降低 Q 感”直接翻译成写实长身人物。妮芙金发灰眼绿披风，奥伊芯红发琥珀眼、花冠红披肩；衣装与饰物分属各自角色。开场妮芙没有十字架：此前已交给奥伊芯，后来在森林捡回。未在图中清楚画出圣物不等于改变设定。

## 本轮实测经验与适用边界

### 参考图上传与聊天上下文

现象：网页参考图上传卡住；负责人改用 Discord 上传后成功生成。仅在提示词写“参照角色图”或“右下参考”，并不证明图已作为本任务输入。聊天中存在附件也不等于后续任务自动引用了附件。做法：核对实际请求中的图像引用和用途，保存完整提示词、实际参数和截图；不知道的字段写待核实。此处记录的是本轮现象，不推定服务端故障原因。

### 比例描述引起漂移

现象：强调更小头眼、更长四肢的一组结果变成另一种绘画风格，角色五官、比例和衣装偏远。可能与文字重心、缺少有效角色参考及模型解释有关，根因未隔离。做法：避免将人物比例和笔触一起大改；每批只检验一个目标。背景满意不能代替角色一致性验收。

### Vary (Subtle) 未编辑提示词

现象：负责人两次点击后直接生成，没有出现可编辑提示词窗口；新图继续保留偏 Q 和较重的外轮廓。事实：建议追加的细棕线文字没有在这两次操作中确认提交。不要把这些结果记成“已测试新提示词”或继续保证点该按钮一定弹框。是否存在额外模式设置及当前版本支持情况尚未核查；若以后再试，先验证编辑入口，再花生成额度。

### 两个人物区域重绘

现象：把两人都完整选中并替换提示词后，生成了偏写实的背影，角色身份和朝向漂移。遮罩允许重建选区，文字“保留原姿势”没有提供可靠的身份约束。此结果不采用。完整 prompt 与遮罩/结果截图见 `MJ_ref/Slideshow/Opening_v1/evidence/`。

### 单个人物区域重绘

现象：只选中完整妮芙，输入角色与柔和线条描述，四个结果均把妮芙替换成背景或花。原因未隔离，不能断言模型为何忽略人物。实证结论：此轮整人物遮罩没有保住角色，不能当作稳定的线条修正方法。停止同一操作的无目标重试，保留最接近候选先验证游戏流程。以后若修图，另存源文件、对照图、遮罩和可回退版本；Photoshop 局部处理尚未执行，不得写为已修好。

## Unity 占位制作与借鉴守灯人

复用方法：数据保存每页图片、字幕、时长、推拉范围；双 RawImage 过渡；输入锁；跳页/跳过；结束时只加载一次下一场。参考 `TheLanternKeeper2D` 的 StoryboardData/StoryboardPlayer 和设计经验，不复制其美术或剧情。

需检查的既有教训：推镜每页独立归一，跳页时无突然反向跳动；检查真实 `Time.timeScale=1`，不照搬其项目数值；字幕不能遮脸和越出屏幕，字幕与按钮分别留位；完成后退出 Play Mode，只留 MainMenu，避免堆叠场景。上述是守灯人已遇问题的迁移检查项，不代表妖精丘陵已经出现或已修复。

本轮流程：MainMenu Play → OP01/02/03 三个占位字幕节拍 → CHAPTER I / THE THRESHOLD（工作标题）→ 原有村庄出生点。第二、三节拍复用 OP01，故事由英文字幕说明，不能冒称画面已经表现了召唤和追赶。正式 OP02/OP03 的分镜仍看 `TechnicalArt/SLIDESHOW_OPENING_v1.md`。

只做第一章开头。普通村庄→森林换场不显示新章节。S2–S4、第二章、想象之眼主线及新 Niamh 动作是后续制作，Demo 第一、二章范围不缩减。

## 状态与资料索引

人读资料的统一版式按 `TechnicalArt/人读Word文档统一版式规范.md`：以技术美术方案 3.1 场景清单为主要样本，标题统一编号，规格、步骤、状态与检查清单排成深绿表头、白/浅灰绿交替行的表格；长说明保留为段落。只换字体和标题颜色不能算套用完成。跨页重复表头、图片与图注同页，并使用 Word/LibreOffice 实际页面核对。此为 2026-11-16 负责人确认的现行及今后人读文档标准。

人读当前版：`TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`。v1 制作单保留为生图前历史快照。
Unity 执行任务：`CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md`。
本地续接：`STORYBOARD_RESUME.md`。素材包：`TechnicalArt/unity_drop/2026-11-14_Opening_Chapter1_Placeholder/`。
Unity 反馈约定：`Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md`；没有此反馈或实际场景证据时，不能把素材复制说成已接入/已运行。

## 妮芙双手捧十字架动作参考（2026-11-16）

同日后续反馈：负责人退回文档整理后生成的胸前/中段/高举候选，指出多手、多指、手臂连接错误及胸前衣装细节丢失。候选、对照板和隔离手臂图只保存为失败研究，禁止作成品输入。旧概念获认可的是风格与姿势方向；手部仍须检查。下一轮先修一张胸前静帧，保留原胸前系带/饰件、领口与披风开口，明确两条肩肘腕连接及恰好两只手，再推进后续姿势。文件和截图见研究目录 `README.md`。

负责人认可静态概念图 `TechArtAsset/Characters/Niamh/Interaction_Study_2026-11-16/Niamh_two_hands_pose_study_v1.png` 的姿势与游戏风格贴合度，可据此继续制作离线动作预览。现有游戏内妮芙侧面图是身份与画风基准；Unity 里的十字架资产是道具基准。Discord 的 Midjourney U2 只提供双臂弯曲和双手持物姿势；最终整合图由 Codex 内置 ImageGen 参考原角色、MJ 姿势图、原十字架资产生成。不能把工具称作 Google Imagen：本轮实际使用的是 Codex 内置 ImageGen，服务端具体模型版本未显示。

认可范围：静态图看起来能接近现有游戏角色，双手捧十字架这个姿势可继续。未认可/未验证：像素作为成品、拆件质量、遮挡和关节补画、连续动作、栅门动作、Unity 导入或 Play Mode。接下来先制作可分层姿势和离线 GIF，由负责人审看后再派新的 Unity 任务。细节与文件索引见 `TechnicalArt/妮芙双手捧十字架动作参考_2026-11-16.md`、`TechnicalArt/LESSONS_CHARACTER_ANIMATION.md` 的 Trial 2。
