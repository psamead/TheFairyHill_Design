# 11 月 25 日开场试玩反馈

[Unity 工作站原始回报](<//haoxi-rtx/C/Users/Administrator/Documents/UnityProject/TheFairyHill2D/Docs/Opening_Story_B_Unity_Review.md>)记录了 11 月 24 日真实 Editor 的两轮自然播放。首镜至章节卡分别为 30.600 和 30.602 秒，章节卡停留约 2 秒，接入村庄。五段文字在两种分辨率均无溢出。键盘路线使用 Unity 输入事件。报告记录了播放头和混音数据。

| 文件 | 来源与观察 |
|---|---|
| [01 设置卡](01_Settings_owner_markup.png) | 共享反馈原图 1.PNG，返回按钮在标题之上 |
| [02 无相机](02_Handoff_no_camera.png) | 共享反馈原图 2.PNG，Game View 显示 No cameras rendering |
| [03 村庄](03_Village_handoff.png) | 共享反馈原图 3.png，显示切场后的村庄 |
| [04 村庄首屏](04_BG01_owner_markup.png) | 共享反馈原图 4.PNG，红框指向右上山坡 |
| [05 五页排版预览](05_BG01_OP01_layout_study.jpg) | 根据运行图和本轮文字框位置静态排字 |
| [06 BG01](06_BG01_720p_before.png)、[07 BG02](07_BG02_720p_before.png)、[08 OP01](08_OP01_720p_before.png)、[09 第一章](09_Chapter_I_720p_before.png) | 修改前 Unity Game View，1280×720，原生像素 |
| [10 字色取样](10_Caption_color_owner_reference.png) | 共享反馈原图 5.png，色板 `#EFE3C2` |

本轮设计端已把修改写入真实 checkout。首镜字幕以三行放进右上红框位置，第三镜移到右下草地，五页统一为暖米色 `#EFE3C2`。设置卡在编辑模式默认隐藏，运行时由 Settings 打开。黑场保留开场相机直到 Core 接手，首帧与 v9 按同一音频时钟起拍。妮芙无自定义物理材质时采用零摩擦零弹力材质，作为贴墙卡住的修正，待实际石墙路线复测。原回报观测 v9 在进入章节卡时落后约 0.7–0.8 秒，持续偏移的来源尚需本轮 Editor 复核。五页 B 原文、30.6 秒设计时点、占位章卡继续使用。复测看[单一任务单](../../CommandForAgentToInitialRun/2026-11-25_Opening_Story_B_Fixes_Unity_Check.md)。
