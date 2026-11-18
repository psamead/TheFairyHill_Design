# 开场界面 按键下划线与举高十字架 实机截图

任务及截图日期：2026-11-18。归档日期：2026-11-19。用于负责人和后续 Agent 设计核对，沿用本目录上级 README 的按轮次归档及 01、02… 编号规则。

20张图片均为网络电脑实际Unity Game view截图，按原文件字节复制，仅在文件名前增加顺序号。没有裁切、缩放、加圈或替换原图。Unity源截图保留原位；原名、尺寸、来源路径及SHA256见 [source_manifest.json](source_manifest.json)。

## 从这里看

| 内容 | 截图 |
| --- | --- |
| 开场与右上Next／Skip | [01 原生1920×1080](01_opening_0_1920.png)、[02 原生1280×720](02_opening_0_1280.png) |
| 第二、三段字幕及章节卡 | 03—08；同一节拍先1920，后1280 |
| 按键下划线 | [09 操作栏与E／Q消息](09_hud_underlines.png) |
| 拾取与条件提示 | 10—12；正常拾取、未获得十字架、没有受控目标 |
| B直接举高 左右朝向 | [13 朝右](13_cross_raise_right.png)、[14 朝左](14_cross_raise_left.png) |
| 红墙消解后的姿势恢复 | [15 朝右恢复](15_cross_restore_right.png)、[16 朝左恢复](16_cross_restore_left.png) |
| 同轮其他阶段记录 | 17—20；墙体消解、早期举高／恢复截图、Skip后的章节卡。优先用13—16核对最终左右朝向。 |

## 反馈与验收边界

保留源反馈副本：[Unity Handoff](Opening_Immersive_Cross_Raise_Unity_Handoff.md) 和 [result.json](result.json)。原报告中的 `Docs/...` 路径相对于Unity工程根目录；原始Console、运行日志和检查脚本仍在该工程对应的 `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/Unity_Trial/`。

- 源报告记录Editor编译通过、工具驱动Play Mode检查，以及下划线UI重建与朝向两个问题的修复。保存的最终Console采样为0 Error、1 Warning。
- 这是工具调用和Input System模拟输入的检查，森林段使用临时运行时定位；不能据此称为负责人亲手完整跑通关卡。用户视觉、声音、动作手感及性能仍待验收。
- 2026-11-19设计端看图观察：右上Next／Skip在明亮天空上对比偏弱，尚未据此修改。开场仍是占位图，不代表人物画风定稿。
- 报告称恢复后的移动／跳跃速度为 `(3.2,11.4)`，随附保存日志该项却是 `(0,0)`；本次归档保留原报告，不能把这个数字当作已独立核实的结论，留待复核。

本次仅归档与索引，不修改Unity代码或场景，不补跑测试，不代替用户验收，也不改变源报告的提交／推送状态。
