# Niamh 直接使用 _m 图层的动作预览 v4

日期：2026-11-14。状态：离线动作草稿，未用户确认、未接入 Unity。

用户明确要求使用 `../Motion_v1/Niamh_puppet_trial_v1_m.psd` 的部件。`Niamh_user_revision_source.psd` 是本轮保存快照，327×699 像素。

v2/v3 的导出脚本读取了 `_m`，但随后又对身体层应用了早期米白色平涂补丁，覆盖用户已经修好的裙子，在手臂摆开时显出不自然的浅色块。这是导出过程引入的问题，不能归因于用户补画或显示缓存。

本版删除该补丁，直接导出 `_m` 的 `head`、`hair_back`、`body`、`arm`、`leg`、`boot`，不再对其重切、补画、填色或自动清理。源文件保持原样。预览为比较运动而继续派生远侧腿、计算变换；没有修改原始部件像素。

`tools/export_user_parts.jsx` 在临时副本中切换图层可见性并导出 PNG；完整 `reference_original` 不参与动作。`tools/render_preview.py` 生成四格、4 秒、20 fps 的 `previews/Niamh_motion_v4.gif`。动作时序沿用 v3。

后续应从这一版或更新的用户 `_m` 修订继续，不再使用 v2/v3 的身体平涂导出逻辑。此版本仍有整体裙摆/披风、简化肢体和未验证 Unity 等限制。
