# Unity 工作站任务 · 五镜开场旁白 B、v9 配乐与试玩回报

2026-11-24 · 设计端已发布，待 Unity 工作站执行。工作目录为真实的 `TheFairyHill2D`。本文件是本轮唯一执行入口，从下面的“接入”做到“回报”即可。上一轮已接入五张独立画、旁白 A、v9 OGG 和翻页逻辑，通过了离线编译；本轮把旁白改为 B，在 Editor 里验证完整开场。

## 接入五页旁白

1. 按工程 `AGENTS.md` 的工作规则查看当前场景、未提交修改和既有手调。在 `Assets/_Project/Data/Storyboards/Opening_Chapter1.asset` 中按镜头 ID 核对五张图，按下表设置英文。表格中每个分行对应一个真实换行符。保留每页已有的 Fondamento 字体、文字框位置和深浅字色；已符合 B 的页面直接进入核验。
2. 核对开场使用 `Assets/_Project/Audio/Music/BGM_Opening_Five_Scenes_v9.ogg`，一次连续播放。自然播放全长 30.6 秒，后四页在表列时点开始叠化，各 0.4 秒。现有的素材引用和手调构图继续使用。
3. 在 Editor 确认场景读取了上述数据，进入菜单可以播放。若发现引用缺失，可用[六件运行素材清单](../TechnicalArt/unity_drop/2026-11-24_Opening_Five_Scenes_v9/manifest.json)核对路径和文件散列；该历史清单中的字幕属于 A。B 版完整文案如下。

| 镜头 | 入画时点 | 游戏内英文与换行 |
|---|---:|---|
| BG01 · 村庄黄昏 | 0.0 秒 | At dusk in a little Irish village,<br>the elders told stories of the hills. |
| BG02 · 丘陵传说 | 4.6 秒 | A thin veil hid the Fair Folk.<br>“Never take their food,” the elders warned. |
| OP01 · 好友玩耍 | 9.2 秒 | Niamh and Oisín had played here<br>for as long as either could remember. |
| OP02 · 奥伊芯听见低语 | 14.8 秒 | That evening, Oisín stopped.<br>A whisper rose from the old mound.<br>Only she could hear it. |
| OP03 · 妮芙追向树林 | 21.4 秒 | Oisín ran towards the trees.<br>“Wait for me!” Niamh called,<br>and raced after her. |

## 从主菜单试玩

| 路线 | 操作与通过条件 |
|---|---|
| 自然播放 | 从 `MainMenu → Play` 开始，不操作直至村庄。核对五图、五段文字及四次叠化；菜单曲平滑退出，v9 连续播放。听 9–11 秒好友玩耍时乐句是否连贯、约 15 秒召唤是否自然进入，以及 23 秒后长笛从高处落向低弦、末尾 2.8 秒是否完整淡出。记录从首镜到章节卡的实际时间。 |
| 手动与重入 | 另从菜单开始，分别用 Space、Enter 翻页，试听音乐是否平滑接至对应乐句；快速连按，确认只交接一次。用 Esc 跳至章节卡，再进入村庄。重新进入开场时应从第一镜和音乐开头播放。右上角沿用无翻页按钮的版式。 |
| 两种画幅 | 在 1920×1080 和 1280×720 分别查看五页。确认弯引号与 Oisín 的重音显示完整，文字读得完，第三页两人的脸与手、第四页的视线、第五页的跑动剪影均可辨认。记下需要负责人试玩后调整的页号。 |
| 封面与关卡 | 本轮预期为第五页 → 现有 `CHAPTER I / THE THRESHOLD` 占位卡（2 秒）→ `Ch1_S1_Village`，确认村庄交还操作。后续规划为第一章大封面 → 第一节试玩封面 → 村庄；两张正式封面留待下一轮设计。 |

## 回报给设计端

在 Unity 工程写入 `Docs/Opening_Story_B_Unity_Review.md`。写明修改文件、Editor 版本、实测路线与输入方式、两种分辨率的逐页结果、实测时长、声音和章节交接结果、Console 新增错误或警告。截图或短录屏放 `Docs/References/Opening_Story_B/`，在报告里链接对应证据。若某项无法实测，写明该项与原因。设计端据此回收证据；文字和版式由负责人试玩后确定。

对照资料：[B 版 30.6 秒有声样片](../MJ_ref/Slideshow/Opening_v1/Opening_five_scene_story_B_v9.mp4) · [逐行数据](../TechnicalArt/unity_drop/2026-11-24_Opening_Five_Scenes_v9/story_B.json) · [中英文与故事依据](../TechnicalArt/OPENING_STORY_B_2026-11-24.md)。
