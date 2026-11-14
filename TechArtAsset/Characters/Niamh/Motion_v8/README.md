# Niamh 下落摆幅调整预览 v8

日期：2026-11-14。状态：离线预览，未在 Unity 中验证。

按照用户 `references/user_fall_swing.png` 的标注，加强下落约 1.05 秒处手臂向后、双腿向前的摆幅。下落动作在 0.80–1.25 秒平滑展开和收回，约 1.025 秒达到最大，接近落地时回到站姿。头部下看与轻微落地沿用 v7。

部件来自用户 `_m` 文件的 v7 导出，不重新切割或补画。远侧腿仍由近侧部件派生。动画参数和完整计算保存在 `tools/render_preview.py` 与 `motion_preview_spec.json`。

`previews/Niamh_motion_v8.gif` 是四格同步预览；`previews/fall_comparison.png` 包含 v7 标注时刻与 v8 的下落关键帧对照。真实场景、动作切换及 Play Mode 尚未验证。
