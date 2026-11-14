# Niamh 用户修订版动作预览 v2

> 已由 `../Motion_v4/` 取代。本版导出时额外加入的身体平涂会覆盖用户 `_m` 修补，造成浅色残块；后续使用用户 `_m` 原始部件及 v4 无补丁导出流程。

日期：2026-11-14。用途：沿用用户补画的图层，更新待机、走、跑、跳跃落地的离线 GIF。状态：动作草稿，未用户验收、未接入 Unity。

## 来源与保护

用户在 Photoshop 修改并保存了 `../Motion_v1/Niamh_puppet_trial_v1_m.psd`。本版以它为依据，不重新执行 v1 的多边形拆件脚本。

`Niamh_user_revision_source.psd` 是该文件的完整快照，保留图层、用户补画及可见性；原始画布现为 327×699 像素。`references/user_revision_2026-11-14.png` 是用户提供的 Photoshop 截图。

原始参考图层 `reference_original` 在用户源文件中可见。导出动画时必须将它隐藏，逐个导出命名部件，避免完整静态角色掩盖运动中的缺口。

## 本轮处理

- 在源文件的临时副本中单独导出 `head`、`hair_back`、`body`、`arm`、`leg`、`boot`。保留全画布坐标。
- `body` 层上仍有原手臂，运动时出现双重手臂。只在导出副本中以米白色平涂修补前臂区域，保留独立 `arm`。此修补是预览用近似，应继续根据实际画面细化裙子纹理。
- 保留 v1 的动作时序与枢轴，使用用户新部件复合；预览背景为中性绿色，不代表游戏灯光。

## 文件与复现

- `previews/Niamh_motion_v2.gif`：四格同步、4 秒循环、20 fps。
- `previews/parts_without_reference.png`：隐藏完整静态参考之后的部件合成。
- `parts/`：供预览读取的透明 PNG，包含上述 body 导出修补。
- `tools/export_user_parts.jsx`：在 Photoshop 临时副本中执行导出与修补，不保存修改到用户源文件。
- `tools/render_preview.py`：Pillow 13 离线预览脚本。
- `motion_preview_spec.json`：当前参数与限制。

本轮未制作新的 MJ 图。远侧腿仍来自近侧素材，裙摆和披风仍为整体，头发没有独立次级摆动，肘膝权重未细化。没有写入 Unity，也没有发出接入执行任务。
