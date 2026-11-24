# Unity 执行任务 · 五镜开场与 v9 配乐

**2026-11-24 · 当前交接**　[旁白 B 与原稿依据](../TechnicalArt/OPENING_STORY_B_2026-11-24.md) · [Unity 工作站任务](2026-11-24_Opening_Story_B_Unity_Review.md)。本地完成设计样片；真实工程已接入 A，B 待对端应用和回报。

2026-11-24。负责人选定 v9 配乐，并授权将该版五镜开场接入 TheFairyHill2D。先读本工程 AGENTS.md、设计端 TechnicalArt/UNITY_AGENT_RULES.md 和[素材与 SHA-256 清单](../TechnicalArt/unity_drop/2026-11-24_Opening_Five_Scenes_v9/manifest.json)。六件运行素材已复制到真实工程，执行前核对。按[有声参考](../MJ_ref/Slideshow/Opening_v1/Opening_five_scene_music_preview_v9.mp4)对齐；MP4 用于比较，游戏内由 Sprite、字幕和一条 OGG 驱动。

参考工程 TheLanternKeeper2D 的 SB_Prologue.asset 按页配置文字框、换行、颜色和对齐。试玩版 A 的位置从画面左上角量起，依次为 (56%,60%)、(10%,12%)、(10%,77%)、(53%,15%)、(19%,12%)。以左对齐的二至三行讲完该页的小事件，浅天空上用深墨字，草地上用浅字和柔和暗衬；每页分别检查人物、山包和屋顶。版式待负责人试玩反馈。旧有声片保留单行历史字幕。[试排 A 有声样片](../MJ_ref/Slideshow/Opening_v1/Opening_five_scene_story_layout_A_v9.mp4)为新版文字和位置的设计参考。

| 镜头 | 自开场起算的入画秒数 | 英文字幕 |
|---|---:|---|
| BG01 | 0.0 | Dusk settled over the village.<br>The hills still held the light. |
| BG02 | 4.6 | People said another world lay<br>just beneath those hills. |
| OP01 | 9.2 | Niamh and Oisín knew these slopes by heart.<br>There was always time for one more game. |
| OP02 | 14.8 | Oisín stopped. Something was calling<br>from the hill. Niamh listened,<br>but heard only the wind. |
| OP03 | 21.4 | Oisín ran towards the trees.<br>Niamh called after her. When her friend<br>kept running, Niamh followed. |

1. 现有入口是 MainMenu → Opening_Chapter1 → Chapter I / THE THRESHOLD → Ch1_S1_Village。五镜总长 30.6 秒，四次交叠各 0.4 秒，分别从 4.6、9.2、14.8、21.4 秒开始，末镜保持到 30.6 秒。章节卡另计，沿用现有图、标题和停留时间。现有 Player 在过渡后重置 PageElapsed，须按真实时间轴处理，避免每镜重复累加淡入时间。
2. 查看 Opening_Chapter1.asset、OpeningSequencePlayer、OpeningSequenceData、OpeningChapter1Builder 与实际场景序列化引用。正确导入五张 Sprite、维护现有 Builder 的重建结果；保留场景与字体的手工调整。显示五张独立画和逐页英文字幕，Oisín 重音完整。移除右上角可见 Next / Skip，保留 Space / Enter 推进及 Esc 跳过、章节卡及村庄交接。
3. BGM_Opening_Five_Scenes_v9.ogg 按一次播放。自然播放时音乐连续，23 秒之后可听见上扬后下行的长笛和低弦，末尾 2.8 秒已有淡出。防止菜单音乐叠播、换页重启、双重淡出或章节卡提前截断。手动提前推进时把音乐平滑带到相应剧情位置；跳过或离开时平滑退音，检查连续按键只触发一次交接。
4. 在真实工程从正常菜单 Play 一遍完整开场；另查手动推进、快速连续输入、Esc 去章节卡与重新进入。1920×1080、1280×720 检查页序、字幕和人物边缘，确认 UI、音量、章节卡和 S1；核对 Console。按项目规则保留既有修改，按任务范围处理素材导入、数据、播放逻辑和 Builder。若环境不具备实机操作，先交付可落地的修改，写清实际验证范围。
5. 回报到 Unity 工程 Docs/Opening_Five_Scenes_v9_Unity_Handoff.md。证据放 Docs/References/Opening_Five_Scenes_v9/Unity_Trial/；注明 Editor 版本、分辨率、实际输入方式、从首镜至章节卡的时长、声音与切场结果。设计端将实机证据回收至 ForDesignScreenShot/ 对应日期目录。负责人最终体验验收单列。
