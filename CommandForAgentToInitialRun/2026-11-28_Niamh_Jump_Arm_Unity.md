# 妮芙跳跃手型、金色结纹框与小挎包圣物页

2026-11-28。上一轮菜单、字幕、村庄音乐的工作站回报已收到，见 Unity 工程 Docs/Chapter1_Playtest_2026-11-28_Unity_Review.md。本文件是本轮三项修改的唯一执行入口，已放入共享队列，待 Haoxi-RTX 工作站实施与实机验证。先读工程 AGENTS.md 并检查现有修改。

## 1. 跳跃手型：拇指在前

以[负责人逐笔标注的手型](../ForDesignScreenShot/2026-11-28_for-jump-arm/02_thumb_forward_markup.png)为准。妮芙朝右、前臂斜向右下时，短拇指位于手的前侧（画面右上侧），其余四指顺势向右下收拢。向左时随人物朝向镜像。[手部放大试排](../TechnicalArt/Niamh_jump_thumb_forward_review.png)用相同肩角比较原手与腕部局部翻转后的轮廓。右栏供确认方向，腕部接缝和肤色明暗须在最终手绘部件上修顺。[村庄截图](../ForDesignScreenShot/2026-11-28_for-jump-arm/01_village_player_feedback.png)用于定位角色。

修订范围为跳跃时的手型。采用现有 v8 跳跃肩部、前臂与腿部动作，撤销上一稿将 JumpUp、Apex、Fall 三段肩摆角度整体取反的试装建议。以用户已编辑的 arm 部件为源，另存同画布、同肩枢轴的跳跃手型，局部处理手腕与手掌，保留袖口与前臂。Unity 在相应跳跃姿势使用此部件，回到地面时恢复原动作部件。检查肩袖连接、腕口两边的轮廓、光影一致性与拇指在游戏尺寸下的辨识度。

在村庄录一段向左和向右的完整跳跃，至少一次跳过矮墙；以同一位置、同一缩放留上升、最高点、下落、落地前后对照。检查走跑及举十字架动作衔接。实机回报写到 Docs/Niamh_Jump_Arm_Unity_Review.md，截图和录屏放 Docs/References/Niamh_Jump_Arm/。负责人按录屏确认方向。

## 2. 同款金色凯尔特结纹框调细

负责人要求所有同款框一起调细，范围见[两张原图](../ForDesignScreenShot/2026-11-28_for-celtic-frame/README.md)。保持框的外轮廓、内容区尺寸与原有金色结纹造型，缩细四边、缩小四角花结。小挎包按下节接入，首次打开即显示断绳十字架。

Unity 先核对 Assets/_Project/Art/UI/Frame/UI_frame_celtic.png 的实际引用，以及运行时代码或重建工具创建的同款 Image。目前可定位 MainMenu 的 SettingsCard/Celtic Frame。其原图九宫格边界为 210，采用 Tiled，pixelsPerUnitMultiplier 为 3.5。建议先调到约 5.6（边饰宽度约为原来的 63%），把同一视觉比例落实到实际场景及 MainMenuSceneBuilder，并逐一检查其余命中的同款框。与小挎包的比例一致即可，各界面用自己的尺寸。复查小尺寸花结连续、四边无断口，按钮仍可点；在 1280×720、1920×1080 各截一张 Settings，列出检查到的其他使用位置，随本轮动作任务一起回报。

## 3. 小挎包圣物页接入

以[最终试排截图](../TechnicalArt/Satchel_v1/relics_unlocked.png)和[三张标注](../ForDesignScreenShot/2026-11-28_for-satchel-unlock/README.md)定位。深绿内衬只铺到 HUD 金框内沿，包沿与图文分隔处均去掉虚线。圣物格上下各两处、左右各一处接缝以实心金圆收口。


读工程 AGENTS.md，检查 git 状态、活动场景和输入绑定，保留手调场景、字幕、材质与音量。设计依据为 [背包原稿](../INVENTORY_SYSTEM_DESIGN.md)、[Demo 清单](../DEMO_IMPLEMENTATION_PLAN.md) 和 [故事原案](../STORY_BIBLE.md)。[交互试排](../TechnicalArt/Satchel_v1/index.html) 从第一章第二段森林、尚未拾取十字架开始。页面下方的中文控件仅供演示，森林与村庄底图仅示意场景。Unity 叠在当前游戏画面上。四页均属 Demo Must，本单只开放 Relics，后三个标签作静态预留；不接入配装、修绳、战斗或新存档系统。

### 3.1 画面与素材

以原型的相对比例试装。暗化当前场景，居中打开棕色布挎包。深绿内衬收在内容区 HUD 金框内沿，包沿和图文之间均去掉虚线，以留白分隔图文；页眉、横向布签、左侧结纹圣物袋、右侧详情、底部暂停与关闭提示。保持 1280×720 和 1920×1080 的画面安全边距。布纹为试排材质，工作站可用面板和九宫格复现。标题用工程内 Fondamento SDF，正文沿用可读的现有菜单正文字体，检查弯引号字形。仅圣物布签有三曲枝与金色下划线。首次可操作的圣物页直接选中已拾取的十字架。

| 元素 | 英文显示 |
|---|---|
| 标题与标签 | Niamh’s Satchel · Relics / Ogham Stones / Memories / Niamh |
| 首次拾取教学 | Iron Cross found. Press F to open your satchel. |
| 持有 | Iron Cross · Broken cord |
| 圣物描述 | I left it with her. The cord has snapped, but the iron is whole. |
| 状态与操作 | Game paused · Close · F / Esc　Close；探索中的入口提示可用 F　Satchel。按键名加下划线。 |

- 图标采用 [IronCross_BrokenCord.png](../TechArtAsset/UI/Satchel/IronCross_BrokenCord.png)，128×128 RGBA。与作者 MJ_ref/AUTHOR_L7_66/CROSS_AUTHOR_REF.png 对形，取自 TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_cross_src.png，挂环上保留两段不等长的绳头。森林里继续使用已导入的 F_prop_cross_v2.png。导入一份 UI Sprite，保持长宽比；HUD 若需同一图，引用同一资产。
- 2026-11-28 细框试排沿用金色原图，按 210 px 九宫格切片，边饰占格子各向尺寸的 14%，约为初稿的 62%。在圣物格上下边的两个拼接点和左右边中点，共放六个金色实心小圆；整块圣物与详情共用 HUD/UI_frame_thin.png 的 24 px 九宫格细框。原型直接引用 TechArtAsset/UI/ICON_triskele.png 和 Frame/UI_frame_celtic.png。Unity 内先复用 Assets/_Project/Art/UI/MainMenu/ICON_triskele.png、Frame/UI_frame_celtic.png（相对 Art/UI）与 HUD/UI_panel_dark.png。已核对的石框、白框和森林地面图均保留原用途。制作期间不覆盖原图。
- 破障后仍显示 Broken cord。重新系绳属于故事结局，两位女孩一起完成；此轮无修复按钮。冷却如有运行时数据，应与 HUD 共读；本轮试排没有设定秒数或新能力。

### 3.2 拾取、暂停和输入锁

1. 从 MainMenu 正常开局并定位持久 Core。现有 IronCrossPickup 在显现结束后由触碰触发，经 PlayerController2D.CollectIronCross() 写入 GameState.HasIronCross。继续使用原入口、提示和拾取音；打开背包时读当前 GameState，不另存背包布尔值。已有物品时重入森林应隐藏拾取物且无重复音效。直接开关卡的 Editor 路径等 Core 就绪且已持有十字架才可开包，避免读取玩家临时 fallback 造成两套结果。
2. 使用工程 Input System，F 单次开关，Esc 仅在包已开时关闭。手柄 Select/View 留在同一动作绑定（有设备再报告验证）。在第一章第二段首次成功拾取、HasIronCross 从 false 变为 true 时显示英文教学一次，玩家主动按 F 开包。拾取前同时隐藏入口和教学；持有后仅在自由游戏中给入口提示，UI 内可点击 Close。开包同帧消费输入并冻结物理、位移、跳跃、交互、施放、拾取和游戏计时；UI 用独立于暂停的输入。关包恢复此前时间倍率、焦点及允许的控制，清空跳跃/交互缓冲与长按状态，关包键不穿透；多个暂停来源各自释放自己的占用。禁用/卸载 UI 或回菜单也应清理自己的占用。
3. CanOpenInventory 须同时满足 HasIronCross、处在可操作关卡和无剧情锁。开场故事、章封面、进出淡变、加载、脚本过场、交易、结尾卡及设计中后续 Boss / 逃脱均禁开；原剧情仍可接收其自己的翻页或跳过。主菜单、设置界面或其他高优先级弹窗持有焦点时，背包不能抢占。过场先于同帧开包按键；如果外部强制切场时包已开，先收包并将控制交给切场锁，避免露出一帧自由操作。
4. 首次破障从接受剧情触发的那一帧起持锁，涵盖举起、初闪、窄束、加强、实际命中后持续照射满 3 秒、障碍湮灭，直至通路开放且妮芙恢复控制。各段都拒绝背包、走跑跳、互动、重复 Q；锁定期的 F 不排队。复用上一任务实际演出结束信号，不能用背包另计 3 秒解锁。中断或重进时按实际进度恢复，禁止提前开通路、残锁或重复发放物品。
5. 跨场景读 Core 的 GameState；往返村庄与森林仍有同一件。回主菜单后新游戏按新会话初始化。若实际分支有 Continue / 旧档，先查版本和真实字段：已有持有标志按原值读，缺失时用可靠既有拾取进度迁移，否则默认未持有并确保可再拾取。仅有旧场景名或通关位置不能推定获得。旧档不原地改写；用副本验证。若无可读旧档或 Continue 为占位，报告适用边界，勿添加持久化系统。

### 3.3 实机验收与回报

| 路径 | 必须留下的观察 |
|---|---|
| 新开局 → 可操作村庄 → 森林 | 分别在序章、章卡和加载中尝试 F；在村庄及森林拾取前再按 F，背包保持关闭且 HUD 无背包提示。原有剧情导航仍正常。 |
| 显现 → 走近 → 开包 | 记录实际触发、物体消失、首次开包的图标和全部英文；关闭后立即能走。来回开关、长按、同时按 Q / E，检查无重复拾取、无跳跃或施放穿透。 |
| 暂停 → 恢复 | 比较开包前/停留数秒/关包后的角色位置、物理和相关计时；Esc 仅关包一次。测试切场或模态抢占时清理暂停。 |
| 森林 → 村庄 → 森林 → 新游戏 | 两次重开包仍显示 Broken cord，森林没有第二件；新会话可重新拾取。记录旧档实际可测条件与结果。 |
| 首次破障 | 连续录屏注明触发、命中、满 3 秒、开始湮灭、恢复控制五个时间点。在举起、细束、照射、消散各尝试开包及移动/重复施放；演出后松键重按可开包，仍为断绳，关闭能通过。 |
| 显示与稳定性 | 两种指定分辨率各留拾取前游戏画面、首次拾取教学和持有页，检查图标绳头、边缘、选中提示、长句和关闭按钮；记录设备、按键和 Console 新增问题。 |

工作站在工程 Docs/Niamh_Jump_Arm_Unity_Review.md 回报版本、实际改动、与上一任务的锁接口、逐项结果与未测项。证据放 Docs/References/Niamh_Jump_Arm/，附上述界面截图、拾取至往返的连续操作、首次破障锁定录屏及时间戳。工作站实测后交负责人试玩，本单不代替序章与荆棘墙的独立回报。

三项共用上述一份实机回报，分别列出实际改动、测试结果、证据链接和待负责人确认项。
