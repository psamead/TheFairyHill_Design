# Unity 工作站任务 · Story B 按原字号复测字幕位置

2026-11-26 接续：此轮原字号复测已完成。下一轮执行[序章与森林破障任务](./2026-11-26_Prologue_and_Thorn_Wall_Unity.md)。


2026-11-25。负责人要求保留红框调整前的实际字号，红框用于定位。设计端已将四页恢复到调整前的实机字号并放宽文字框。复测时可微移文字框或调整换行，字号以表为准。画面上的文字和阴影可略超出手绘框边，完整留在 Game View 内。

上轮为了装入红框曾把四页缩到 26.70–30.25。该轮的实测与截图保留作历史记录。[上轮红框实测](<//haoxi-rtx/C/Users/Administrator/Documents/UnityProject/TheFairyHill2D/Docs/Opening_Story_B_Caption_Red_Boxes_Unity_Check.md>)

## 工程当前设置

以下坐标为 RectTransform 归一化锚点，原点左下。字号按 1920×1080 参考画布，两个分辨率均用同一 TMP 值。四页固定字号。第三页 OP01 使用原来的位置和 36 号。沿用现有 Fondamento、#EFE3C2、阴影、五张图、v9 配乐与章卡。

| 镜头 | Anchor Min | Anchor Max | 字号 | 英文与换行 |
|---|---|---|---:|---|
| BG01 | 0.713, 0.440 | 0.942, 0.586 | 33.8 | At dusk in a little<br>Irish village, the elders<br>told stories of the hills. |
| BG02 | 0.132, 0.270 | 0.446, 0.373 | 36 | A thin veil hid the Fair Folk. “Never<br>take their food,” the elders warned. |
| OP02 | 0.703, 0.272 | 0.969, 0.421 | 36 | That evening, Oisín stopped.<br>A whisper rose from the old<br>mound. Only she could hear it. |
| OP03 | 0.742, 0.306 | 0.986, 0.455 | 36 | Oisín ran towards the trees.<br>“Wait for me!” Niamh<br>called, and raced after her. |

工程已更新 `Assets/_Project/Data/Storyboards/Opening_Chapter1.asset`、`Assets/_Project/Scripts/Gameplay/OpeningSequenceData.cs` 和 `OpeningSequencePlayer.cs`。资产校验 SHA-256 为 `636599698fcc636b39b394bcca2e98bfa5dfd82a4ffec9b5b2765a235489c272`。

## 试玩与回报

1. 从实际 MainMenu 点 Start，在 1920×1080 与 1280×720 逐页截图。确认 BG01 为 33.8，BG02、OP01、OP02、OP03 为 36。确认完整字幕可读、无溢出或额外折行、贴近红框且避开画面主体。按实际画面微调锚点或换行。记录实际字体大小与改动。
2. 写入 Unity 工程 `Docs/Opening_Story_B_Caption_Fixed_Size_Unity_Check.md`，新截图放 `Docs/References/Opening_Story_B_Caption_Fixed_Size/`。保留上轮红框缩字的报告与截图，记录本轮 Console 和未验证项。

[原始红框截图和原字号静态预览](../ForDesignScreenShot/2026-11-25_for-opening-caption-red-boxes/README.md)。
