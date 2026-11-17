# 历史举十字架粗预览归档

本目录早于用户第二稿，不是当前双动作动画。当前文件见 `../../README.md`。本次只归档，不重渲染。

# Niamh 举十字架预览 v1

**2026-11-17 后续状态：用户已在 `../Interaction_Study_2026-11-16/Niamh_chest_composite_clean_wip_v1_m.psd` 完成胸前十字架的手工调整与裁切。当前图层整理入口为同目录 `Niamh_chest_hold_organized_v1.psd`。本目录 GIF 早于这次修订，保留作粗测试记录，未重渲染；不是最新静帧的动画版。当前等负责人制作下一个姿势。**

2026-11-17。状态：粗略姿势与节奏测试，未验收，不作 Unity 输入。

预览：`previews/Niamh_cross_raise_preview_v1.gif`；关键姿势对照：`previews/Niamh_cross_raise_contact_v1.png`。20 fps，4.5 秒循环，胸前停留 → 抬至面前 → 停留 → 回落。本版未达到头顶高举。

起始人物与胸前双手采用用户保存的 `Interaction_Study_2026-11-16/Niamh_chest_composite_preparation_wip_m.psd`，保留 Layer 2 的用户袖口过渡。U1 提取下方支撑手臂，U2 提取上方举臂，水平翻转接回朝右人物；U4 备用，未使用。十字架采用现有 `TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_cross_v2.png`。

`tools/build_preview.py` 用 PhotoCraft CLI 读取 PSD、按图层导出并建立参考图选区蒙版；`tools/render_gif.py` 用 Pillow 排列剪贴部件与打包 GIF。原 `_m` PSD 未覆盖。

实测问题：抬起中段是关键姿势替换，存在明显跳变；肩部和袖口接缝未完成；高低两手与握柄的接触及遮挡仍需绘制；抠图浅色边缘仍在；未完成连续肘腕运动或头顶高举。本版仅用于判断方向与节奏。
