# 第一章负责人试玩修订

2026-11-28。设计端按负责人反馈逐条登记。本文件是本轮 Unity 工作站接手和回报的唯一入口。第 1–3 项已收到工作站实机回报（[实机回报归档](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/Chapter1_Playtest_2026-11-28_Unity_Review.md)），待负责人确认画面和听感。有后续意见时接续到本文件。

## 1. 主菜单进入序章时淡变

负责人从 Start Menu 点 Start，观察到直接跳到序章第一张村庄图。入口希望接成后面进入第一章时的淡变。见[试玩截图 01](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/01_start_menu_to_prologue.png)，原文件名为 1.PNG，静帧用来定位落点。

工作站先读 Unity 工程 AGENTS.md 和 Docs/Prologue_and_Thorn_Wall_Unity_Review.md。现有 MainMenuController.EnterNewGame() 淡出菜单音乐后载入 ch1_S0_prologue，OpeningSequencePlayer 在 v9 开始播放时把黑幕直接清零。以之后章卡进入村庄的黑幕过渡为参照，实现完整画面淡出和淡入。

1. 点 Start 后，使菜单背景、标题与按钮一起平顺淡到黑。菜单音乐沿既有逻辑淡出。加载期间保持全屏黑幕，等首图和界面就绪再揭开。
2. 从黑幕平顺淡入序章首图 BG01。字幕和右下角按键提示随首图显现。优先沿用现有第一章淡变曲线和约 1 秒的淡入作为试装基准。保持现有 v9 渐入与故事时间轴，实机确认首句字幕仍有足够可读时间。
3. 切换中防止重复点 Start、长按确认或输入穿透。淡入结束并松键后，正常接受翻页和 Esc。若实际进入现有备用关卡路径，也须释放遮罩和输入占用。

从 MainMenu 用鼠标和键盘分别启动。用连贯有声录屏保留菜单、渐黑、BG01 渐显和首次正常翻页。在 1280×720 与 1920×1080 检查无闪白、露出中间帧或直接跳画面。确认从第五页经过章节封面到村庄仍正常。工作站在 Docs/Chapter1_Playtest_2026-11-28_Unity_Review.md 记录实际时长、复测结果及未验证项，证据放 Docs/References/Chapter1_Playtest_2026-11-28/。

## 2. 按红框调整序章四处字幕

把「At dusk in a little / Irish village, the elders / told stories of the hills.」三行整体下移，落进[试玩截图 02 的红框](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/02_bg01_caption_red_box.png)。红框上边在当前第三行附近，作为新文字块的上沿参考。沿用当前左对齐、字号 33.8、英文原文和手动三行换行。右下角按键提示仍用自己的位置。

在 Opening_Chapter1.asset 中，BG01 只需调整纵向锚点。现有 Y 为 0.440 / 0.586，以两端同时减约 0.12 作为试排起点（0.320 / 0.466，Unity 自底向上），以真实字形落入红框为准。用 1280×720 与 1920×1080 的 Game View 截图确认三行完整、左边齐，和新入口淡入一起复验。回报记录最终锚点及两种分辨率截图。

另外三页各按自己的红框定位。以下偏移是从标注图估算的试排起点，以 Game View 的实际文字块为准。偏移用画面宽高的比例表示。

| 页 | 目标位置 | 试排偏移 |
|---|---|---|
| [OP01 两人在草坡上](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/03_op01_caption_red_box.png) | 右下草坡的红框，拉开与右下角按键提示的距离 | 左移约 1.5%，上移约 2.8% |
| [OP02 奥伊芯听见低语](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/04_op02_caption_red_box.png) | 画面右侧山坡的红框，从红框左沿略留空开始排 | 左移约 3.8%，上移约 3.8% |
| [OP03 两人往树林跑](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/05_op03_caption_red_box.png) | 右侧树林前的红框，三行左缘对齐，末行靠近田地上缘 | 左移约 4.5%，轻微下移约 0.5% |

三页先保留各自现有字号、文案和换行。红框用于定位，若手绘框的宽度与原行长有出入，先将首行和左缘放到标注区域，确认各行完整且易读。两种分辨率各留 BG01、OP01、OP02 和 OP03 截图，记录最终锚点。右下角按键提示与故事字幕保持可辨间距。

## 3. 村庄开场音乐播出后突然变小

负责人试玩反馈是进入第一章村庄后，声音已经开始播放，随后突然变小。上一版听感正常，本版出现回归。目标是村庄音乐平顺起声，达到原有的正常音量后保持稳定。见[试玩截图 06](../ForDesignScreenShot/2026-11-28_for-chapter1-playtest/06_village_audio_handoff.png)，截图用于定位场景，听感以录音或实机为准。

现工作站文件中，Ch1_S1_Village 的 Level Music 勾选了 Play On Awake，音量为 0.5。OpeningSequencePlayer.Complete() 在村庄载入、交接 AudioListener 并等待初始化后，才把该音源置为 0 并随画面淡入，最后恢复音量。这两处顺序可能造成先听到正常音量，再被拉低。Chapter1SceneBuilder 创建音源时则把 playOnAwake 写为 false。先结合当前未提交场景差异和运行时音量、播放状态及监听器交接的时间线复现，核对是否确是这一次归零。

确认由同一条流程启动和淡入村庄音乐，首次可听前就准备好音量，避免先以目标音量播放再被归零。沿用村庄现有曲目和正常目标音量，保留 v9 尾声和章卡到村庄的画面淡变。同步场景和重建入口。检查直接打开村庄、序章走完、Esc 跳过和森林返回村庄时的播放入口，确保都能起声且不会重复启动或持续过轻。

有声录屏从章卡消失前开始，录到村庄可操作后至少 10 秒。同设备、同监听和主音量，对比本版复现与修订后的听感。记录音乐第一次可听、任何突然变化、达到目标音量与控制恢复的时刻。附到本任务第 1 项指定的回报和证据目录。
