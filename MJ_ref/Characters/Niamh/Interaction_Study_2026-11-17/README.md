# 妮芙胸前与举手动作 MJ 原图参考

**2026-11-17 后续更新：** 原图归档后已开展剪贴合成；用户最新胸前袖口及道具修订保留在 `TechArtAsset/Characters/Niamh/Cross_Actions/sources/user/Niamh_cross_chest_local_user_source_2026-11-17.psd`，当前图层整理入口为同目录 `Niamh_chest_hold_organized_v1.psd`。较早粗 GIF 已制作，未采用最新道具修订且非正式动画。以下「下一 task」「尚未剪贴」为归档当时记录，当前状态统一读根目录 `STORYBOARD_RESUME.md`。原图用途和来源不变。

归档日期：2026-11-17。负责人在 Discord 生成并下载，明确指出 U1、U4 圈出的手形较合理，现按资产规则重命名、归档；图片内容未经修改。原下载文件名、SHA256 和对应选择见 `source_manifest.json`。

| 文件 | 来源与方向 | 用途与限制 |
| --- | --- | --- |
| `Niamh_chest_hands_MJ_U1_raw_v1.png` | 四格左上 U1，朝右 | 胸前手形、手腕和弯臂姿势参考；十字架未清晰生成，双手与握柄仍需检查。 |
| `Niamh_chest_hands_MJ_U4_raw_v1.png` | 四格右下 U4，朝左 | 抬起手的握拳轮廓参考；另一只手垂下，尚非双手捧持姿势。 |
| `Niamh_raise_hands_MJ_r01_U1_raw_v1.png` | 举手保留轮 r01 左上 U1，朝左 | 与同轮 U2 组合双臂的来源之一；另一手位于下巴附近。 |
| `Niamh_raise_hands_MJ_r01_U2_raw_v1.png` | 举手保留轮 r01 右上 U2，朝左 | 负责人圈选的抬臂轮廓，与 U1 组合使用。 |
| `Niamh_raise_hands_MJ_r02_U4_raw_v1.png` | 十字架角度补跑轮 r02 右下 U4，朝左 | 负责人要求保留的举手握拳参考；未生成可用十字架。 |

`r01`、`r02` 是本目录中保留的两轮举手候选编号，不是本聊天全部 MJ 作业的全局编号。五张都是负责人下载的完整人物原图，未裁切、未翻转或改色。

生成方案：胸前捧持图作 Image Prompt，原版 `TechArtAsset/Characters/Niamh/Niamh_side_static_v3.png` 作 Character Reference；本聊天提交给负责人的参数为 `--niji 6 --ar 1:2 --s 150 --cw 100`。不将提示词参数等同于已独立核验的后端运行日志。

## 负责人确认的制作方法与下一 task

2026-11-17：负责人明确，先生成完整人物，再从人物中取动作区域；不单独让 MJ 生成手。举手 r01 的 U1、U2 可以组合为双臂，r02 U4 也保留备用。十字架最终在 Photoshop 中使用现有游戏道具合成；MJ 没画出十字架不影响保留合理的手臂参考。本轮生图探索到此结束。

胸前轮沿用 `--niji 6 --ar 1:2 --s 150 --cw 100`；两轮保留的举手图发给负责人的提示词增加 `--iw 2`。r02 尝试竖直十字架、正面稍朝镜头转的三分之四角度，但没有得到有效道具角度结果，不将这一尝试视为角度已定稿。

下一 task：读取 `STORYBOARD_RESUME.md` 的最新记录，再以原侧面立绘、用户修订 PSD / Motion_v8 为基准，在 Photoshop 新版本文件中试做合成静帧。优先胸前捧持，再检查举手组合；只取需要的手臂、手形与袖口区域，保留原脸、头发、披风、领口、系带和饰件。朝左参考接回朝右角色时要核对左右手、光影、拇指方向和遮挡；不要将整个人物替换为 MJ 角色。游戏十字架来源为 Unity 工程 `Assets/_Project/Art/Backgrounds/S1b_ForestPath/props/F_prop_cross_v2.png`，需读取实际素材后再确定角度与握柄遮挡。

当前仅完成五张参考原图归档。尚未剪贴、未分层、未制作离线动画、未接入 Unity。负责人要求整理后切到下一 task，本 task 不继续执行 Photoshop 合成。
