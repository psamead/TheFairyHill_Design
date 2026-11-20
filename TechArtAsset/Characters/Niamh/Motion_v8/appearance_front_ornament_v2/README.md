# 妮芙静态侧身图前襟遮挡修正

2026-11-19，负责人指出金色前襟纹样盖在垂下的手上。v1静态PSD只有原人物整图与顶层前襟补丁，缺少位于花纹上方的手臂遮挡。

使用PhotoCraft在v1源PSD上新增原Motion_v8手臂层，置于花纹上方，蒙版仅保留原花纹补丁区域。保留原人物层与花纹智能对象，修订源为 static_front_ornament_source_v2.psd。后续导出静态侧身图使用此源。

PNG为 Niamh_side_static_v3_ornament_fix_v2.png，已同步本地角色目录的 Niamh_side_static_v3.png（相对于本目录为 ../../Niamh_side_static_v3.png）。修前入口PNG另存 static_before_v2.png。当前尺寸327×699。

validation.json记录可见改动628像素，范围x253–275、y372–431，原补丁区域之外可见像素一致，alpha逐字节一致。PhotoCraft重新导出会更改完全透明像素下的RGB，未将文件字节一致视为验收条件。散列见file_hashes.json。已查看修后PNG，手遮住前襟纹样，负责人审看待确认。

本次修正静态参考的局部遮挡。Motion_v8身体部件与独立手臂在动画中分别叠放，后续如反馈游戏动作遮挡问题，按该画面的实际层序另查。Unity本轮未修改。

反馈原截图位于 ForDesignScreenShot/2026-11-19_for-niamh-ornament-occlusion/。v1历史源和用户原稿保留。
