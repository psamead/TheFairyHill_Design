# Niamh 下落姿势预览 v7

日期：2026-11-14。状态：离线动作草稿，未接入 Unity。

依据用户标注 `references/user_falling_pose.png`，在最高点之后平滑过渡到低头、手向后、双腿向前的姿势；接近地面时手脚逐渐回收，头保持向下的趋势，并衔接 v5 的轻微落地下沉及复位。上升阶段沿用 v6 的抬头、手向前、腿向后动作。

素材直接复用用户 `_m` 的部件；没有重新拆件或修改源图。远侧腿仍是近侧素材的派生版本。下落时减小靴子的反向转动，避免抵消腿向前摆动。

`previews/Niamh_motion_v7.gif` 是四格动作预览，`previews/falling_pose_check.png` 展示最高点、下落过渡、落地和恢复的关键帧。`tools/render_preview.py` 与 `motion_preview_spec.json` 保存时序和参数。

画面是离线预览，实际控制器、动作切换、场景比例和 Play Mode 尚未验证。
