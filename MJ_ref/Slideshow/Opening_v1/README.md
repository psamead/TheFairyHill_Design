# 开场故事画 MJ 制作包

2026-11-14：**准备完成，未提交 MJ，尚无候选或定稿**。Chrome 已打开 Create；本轮浏览器扩展连接失败，窗口读取重试超时。恢复连接后从 OP01 开始，不需要重新申请制作授权。

- 人读版：`TechnicalArt/妖精丘陵_开场故事画制作单_v1.docx`（从仓库根目录打开）。
- 设计及接入说明：`TechnicalArt/SLIDESHOW_OPENING_v1.md`。
- 每张完整提示词：本目录 `OP01_prompt.txt`、`OP02_prompt.txt`、`OP03_prompt.txt`。
- 输入参考与 SHA-256：`generation_manifest.json`。`jobs` 为空表示没有生成任务，不能当作完成。

## 操作顺序

1. 在 Create 核对实际模型与参考附件位置。计划为 V8.2 Edit；若界面不同，记录实际方案再执行，不把旧 Niji 6 参数直接混入。
2. OP01 附妮芙、奥伊芯 v3 参考以及干净村庄背景；环境图同时按网页支持方式设置 Style Reference。角色立绘用于身份，村庄图用于环境和画风。
3. 只提交 OP01 一组，记录实际完整 prompt、设置、引用文件与 job URL/ID。检查角色身份、圣物归属、画风、画幅和字幕区，再决定所选候选。
4. OP02、OP03 延续同一候选的风格；如更换或添加参考，将实际引用记录到对应 job。不要上传带 HUD 的实机截图作为图像内容参考。
5. 候选保留 MJ 原始输出和编号，生成记录写入 manifest 的 `jobs`。通过后才将修订源文件及 1920×1080 PNG 交付到 `TechArtAsset/Storyboards/Opening_v1/`，然后通过共享网络复制到 Unity。

现有参考图不是故事画成品。妮芙立绘带十字架，但开场圣物已交给奥伊芯；所有镜头必须修正这一点。字幕和章节标题由 Unity 独立显示。
