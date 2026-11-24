# BG02 Discord 远景试修

## 2026-11-24 手调静帧通过与上边缘修补
负责人确认 v3_m 的手调画面。[分层修补稿 v4](BG02_U4_PhotoCraft_foreshadow_v4.psd)新增独立像素层，取紧邻上边缘的八行天空镜像补齐顶部 8 px。[2912 × 1632 无人物 PNG](BG02_U4_PhotoCraft_foreshadow_v4.png) 已与源稿合成像素比对，差异仅限顶部 8 行。


**当前接续稿：** [伏笔版 v3_m](BG02_U4_PhotoCraft_foreshadow_v3_m.psd)。保留负责人在 Photoshop 手调后的分层画面与蒙版。

1. 上传 [01 BG02 r06 U2 原图](01_BG02_r06_U2_base.png)，用于保留中央丘体、前景草地与构图。
2. 上传 [02 OP01 远树](02_OP01_distant_trees.png)，参考低反差的单色树影与沿坡暖色短笔。
3. 上传 [03 OP01 天空和山坡](03_OP01_sky_and_slopes.png)，参考暖杏色天空、灰蓝远山与低反差平涂。
4. 从 Discord 图片逐张复制链接。在 `/imagine` 的 prompt 栏粘贴[试修提示词](BG02_discord_edit_prompt.txt)，将三个链接按顺序填入 `--edit` 后，去掉占位符及方括号。

[负责人红圈标注](BG02_owner_markup.png)供人核对修图范围，上传时从无标注的 01 开始。首轮重点看远山地平线能否只靠相邻色块交代、天空和屋外远坡的黄绿色是否退下、远树是否仍读作远景。中央圆丘位置、轮廓、体量及光面和暗面关系依 r06 U2。最近处草的剪影可保留。提交后补记实际参数、任务链接和四格评语。

[Midjourney Discord Edit 模型说明](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)

## 第一轮回图与第二轮范围

[负责人退回的 Discord 四格](BG02_MJ_r01_owner_grid.png)。四张都改变了坡线和层次，远山变成长而平直的斜带，前景整体压灰，主丘受光面与暗面的分界变弱。调出杏色与灰蓝的同时出现整画重绘。截图无法确认实际提交的完整词和任务 ID。本轮四张均退回。

[第二轮单图校色提示词](BG02_discord_edit_r02.txt)仅用 r06 U2 原图作为 Edit 输入。保留现有云块与远山起伏，只改天空、远坡颜色和远处的黑色地平线。本轮先不补远树。背景过关后再决定树影的数量与位置。

**第二轮最新范围**见[负责人地平线红圈](BG02_owner_r02_horizon_markup.png)。只修主丘背后狭长的远处地平线，用相邻色块接掉黑边，保留山线轻微右升。天空只减绿并保留原云。请用[更新后的 Discord 提示词](BG02_discord_edit_r02_horizon_only.txt)，以无标注 r06 U2 为唯一输入。当前待提交。

## 选定第二轮 U4

[负责人圈注的第二轮四格](BG02_MJ_r02_U4_owner_markup.png)。采用右下 U4 为局部试修底图。红框只覆盖主丘背后的远坡和低空交界，右边沿已有远山线微微抬升。这里参照 OP01 的低反差灰蓝、灰褐及浅杏色过渡，降低绿感。保留红框上方的天与云、主丘前侧、近草和现有构图。

[第三轮 Discord 提示词](BG02_discord_edit_r03_U4_transition.txt)的第一个链接必须是本轮选中的干净 U4 单图。后两个链接分别指向 `02_OP01_distant_trees.png` 和 `03_OP01_sky_and_slopes.png`，只取色块过渡。圈注截图供核对范围。第三轮待提交。

**第三轮最新操作**以 [U4 Discord 单图截图](BG02_MJ_r02_U4_single_discord.png)为依据。截图可见 Vary (Region)；实际局部提交仍待验证。优先沿红圈内两道深色地平线做窄选区，上下各带一点相邻色块，避开主丘金顶与前景草梗。红圈内去掉全部黑色描线，即使很细也用相邻色块交界接过去。低空灰杏与远坡灰蓝、灰褐维持低反差，适度减绿。若 Remix 可编辑，使用[局部提示词](BG02_discord_r03_U4_vary_region.txt)。前一版整图试修词存作备选。

**U4 单图已归档** [第二轮 U4 原件](BG02_MJ_r02_U4_selected.png) · 1456 × 816 · SHA-256 `b4ce7d97b91611edfff5bd7fda06ad25cba2d992c7da61b55c6bd43f4129fae8`。用户提供的 Discord 文件名含图像标识 `88b6b72f-2832-4dfe-ac9a-c8fe1e6a6b9c`，父任务仍待核。整图备用提示词已填入 U4 与两张参考链接，第三轮待提交。

## 第三轮两种提交的回图

- [整图 Edit 四格](BG02_MJ_r03_full_edit_discord.png)。截图可见按三图参考提交，参数为 V8.1、16:9、Raw、Edit，实际文字为较早的三图过渡提案。四格均明显改变红圈外的明暗和色彩，主丘暗面、近草一起变灰，远坡又出现拉长的暖色斜带。整图回图不建议采用。
- [Vary (Region) 四格](BG02_MJ_r03_vary_region_discord.png)。截图可见无描线局部提示词、V8.1、16:9 和 Variations (Region) 标识，选区截图、实际局部重绘模型和任务 ID 待核。主丘金顶、深绿暗坡和前景大体延续 U4。左上 U1 右坡仍有一段硬轮廓，左下 U3 把小树排到左侧地平线，右下 U4 的右侧树团偏黑。右上 U2 天空与右坡的交界较干净，最右端仍多出一簇深色树，右坡受光面也略亮。
- 建议先放大局部版右上 U2，核对红圈内的线条及绿感。若整体过渡合适，只需局部去掉最右树簇与残线。局部版尚未定稿、未接入五页 GIF 或 Unity。

## 两张 U4 的 PhotoCraft 合成

负责人选用两组各自右下 U4，覆盖上文建议比较局部版 U2 的意见。先以局部重绘 U4 为底，保留其主丘与近草。从整图 Edit U4 只取主丘后红框窄带所需的减绿过渡。按各自坡线对齐，通过蒙版控制接缝、去净远山黑线，另存分层稿与 PNG。两张原件到齐后执行。

## PhotoCraft 合成 v1

[分层 PSD](BG02_U4_PhotoCraft_composite_v1.psd) · [审片 PNG](BG02_U4_PhotoCraft_composite_v1.png)

- 底图是 [局部重绘 U4](../../../../MJ_ref/Slideshow/Opening_v1/Opening_backgrounds_2026-11-24/BG02_MJ_r03_U4_vary_region_v1.png)。远景配色取自 [整图 Edit U4](../../../../MJ_ref/Slideshow/Opening_v1/Opening_backgrounds_2026-11-24/BG02_MJ_r03_U4_full_edit_v1.png)。两张均为负责人下载的 2912 × 1632 PNG。两张原件已按轮次、选图和用途改名，见[下载名对照](../../../../MJ_ref/Slideshow/Opening_v1/Opening_backgrounds_2026-11-24/README.md)。
- 两张山脊高度不同。依底图重建一条从低空灰杏到远坡灰蓝的色块交界，使用整图 Edit 的取样色。局部过渡保留为可编辑蒙版层，遮挡按主丘和近草处理。已核对导出图在蒙版外与局部重绘 U4 逐像素一致。
- 底图 SHA-256 `97ed0a77ce7467270065fbe6d43e90a75dc2272a45fa381de7bc4f9eabe08641`。整图 Edit SHA-256 `1fe44b81c84232aa399fe30da0bd55a7e89a4b6e93cdc2f4c1d9944acbbd2220`。合成已出图，GIF 和 Unity 接入待审后处理。

## PhotoCraft 伏笔版 v2

[分层 PSD](BG02_U4_PhotoCraft_foreshadow_v2.psd) · [审片 PNG](BG02_U4_PhotoCraft_foreshadow_v2.png) · [负责人标注](BG02_foreshadow_owner_boundary.png)

负责人意图是先交代妖精丘陵作为故事起点。事件尚未发生，用丘陵及天空的低饱和灰调作视觉伏笔，坡脚前仍是暖色草地。PhotoCraft 在 v1 上新增灰调 U4 层，依据标注在坡脚对齐并收窄接缝。导出为 2912 × 1632，蒙版之外与 v1 像素一致。伏笔版待审。

## 2026-11-24 负责人手调稿

将负责人保存的 `BG02_U4_PhotoCraft_foreshadow_v2_m.psd` 顺延重命名为 [`BG02_U4_PhotoCraft_foreshadow_v3_m.psd`](BG02_U4_PhotoCraft_foreshadow_v3_m.psd)，保留 `_m` 标记。仅改文件名，PSD 的 SHA-256 保持一致（`e3fb87088b1fd66b720ff399a1ef010986b8b0dc78f861006bbf9767602bbc69`）。v2 的 PSD 和 PNG 仍可用于对照。
