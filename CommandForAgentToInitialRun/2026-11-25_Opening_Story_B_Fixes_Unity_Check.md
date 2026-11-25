# Unity 工作站任务 · 复验开场 B 的试玩修订

2026-11-25。11 月 24 日的 B 已在真实 Editor 播放通过。设计端已在真实工程临时修改下表所列文件。由此单接续，从 MainMenu 正常 Play 复验现有改动，并在工程内回报。先看本地 Git 状态及手调修改。

| 检查项 | 已改内容和通过条件 |
|---|---|
| 首屏与第三页文字 | `Assets/_Project/Data/Storyboards/Opening_Chapter1.asset`。BG01 的框约为画面 x=63.5%–86%、y=27%–40%（从顶部量），采用三行：`At dusk in a little Irish village,` / `the elders told stories` / `of the hills.`OP01 约 (67%, 84%)，放到右下深色草地，避开妮芙和两人的手脸。1920×1080 与 1280×720 确认全部字行都在框内，五页文字统一使用 `#EFE3C2`，带暗底影；在 BG02、OP02 和 OP03 的淡天空上复核可读性，按正常阅读速度复核 BG01 与 BG02 的 4.6 秒。记录哪一页确实来不及读完。 |
| 设置卡 | `Assets/Scenes/MainMenu.unity` 和 `Assets/Editor/MainMenu/MainMenuSceneBuilder.cs`。Scene View 默认隐藏 SettingsPanel；Play Mode 点击 Settings 展开，从上到下为 SETTINGS、说明、Back。检查点击 Back 后回到正常菜单和焦点。沿用当前边框和占位文案。 |
| 音画同步 | `Assets/_Project/Scripts/Gameplay/OpeningSequencePlayer.cs`。v9 OGG 与首张图共享 DSP 起点，从首图实际可见时起算，四次交叠始于 4.6、9.2、14.8、21.4 秒，各 0.4 秒，30.6 秒进章卡。实测约 5、15、25、30 秒的画面钟与音频播放头差值，对照上轮两次约 0.7–0.8 秒落后。另用正常手感试听末尾和快速输入后的音乐衔接。 |
| 章卡进入村庄 | 同一 Player 改为等待 Core 接手前继续渲染黑场。自然播放和 Esc → Enter 两条路线都看章卡、黑场、村庄交接，黑场期间逐帧确认有活动显示相机，检查 Console 是否还出现无相机或 AudioListener 警告。确认村庄只进入一次且可移动。 |
| 妮芙碰撞 | `Assets/_Project/Scripts/Gameplay/PlayerController2D.cs` 为未配置物理材质的角色提供零摩擦、零弹力接触。到截图中的第一段矮石墙，从左右两侧贴墙跳、按方向键滑落、反向脱离；再过草垛与相邻石墙，确认没有悬空卡住，墙仍能挡人。若仍卡住，记录墙名、角色坐标、输入和接触法线，再调整具体碰撞体。 |

Chapter I 占位卡仍为 2 秒，正式章封面和第一节试玩封面等待后续设计。五段 B 旁白及 v9 音频文件为本轮基线。对照[反馈图与修订前证据](../ForDesignScreenShot/2026-11-25_for-opening-story-b-review/README.md)。

请把实测数据、使用的输入方式、听到的变化、Console 与任何最小修正写到 Unity 工程 `Docs/Opening_Story_B_Fixes_Unity_Check.md`。实机截图或短录屏放 `Docs/References/Opening_Story_B_Fixes/`。标明实测和待负责人确认的部分。
