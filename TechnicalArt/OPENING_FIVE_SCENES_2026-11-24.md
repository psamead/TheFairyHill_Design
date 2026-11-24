# 妖精丘陵五镜开场制作与接续

**2026-11-24 · 当前交接**　[旁白 B 与原稿依据](OPENING_STORY_B_2026-11-24.md) · [Unity 工作站任务](../CommandForAgentToInitialRun/2026-11-24_Opening_Story_B_Unity_Review.md)。本地完成设计样片；真实工程已接入 A，B 待对端应用和回报。

2026-11-24 · 五页故事、试排 A 与 v9 已接入真实工程。运行时与开场重建工具离线编译通过；目标 Editor 实播和负责人试玩待验。[Unity 实施回报](<//haoxi-rtx/C/Users/Administrator/Documents/UnityProject/TheFairyHill2D/Docs/Opening_Five_Scenes_v9_Unity_Handoff.md>)

2026-11-24。负责人选用 v9，授权把带这五镜的版本交给 Unity。审片依据为[30.6 秒有声预览](../MJ_ref/Slideshow/Opening_v1/Opening_five_scene_music_preview_v9.mp4)；[人读图解](开场五镜制作复盘与Unity交接_v9.docx)、[运行文件校验清单](unity_drop/2026-11-24_Opening_Five_Scenes_v9/manifest.json)、[执行单](../CommandForAgentToInitialRun/2026-11-24_Opening_Five_Scenes_v9_Unity.md)。以下时间均从自然播放第一帧起算。

本次游戏首轮试排参考《The Lantern Keeper》实际序章资产 SB_Prologue.asset 的逐页文字框与留白。[试排 A 有声样片](../MJ_ref/Slideshow/Opening_v1/Opening_five_scene_story_layout_A_v9.mp4)结合下表英文和已选配乐。上一版 MP4 供音画时点比较。版式待负责人试玩后调整。

| 起点 | 画面与导出文件 | 字幕 |
|---|---|---|
| 0.0 s | [BG01 黄昏村庄](../MJ_ref/Slideshow/Opening_v1/Opening_backgrounds_2026-11-24/BG01_MJ_r01_U4_village_edit_v1.png) | Dusk settled over the village.<br>The hills still held the light. |
| 4.6 s | [BG02 丘陵传说](../TechnicalArt/references/opening_review_2026-11-23/BG02_MJ_trial/BG02_U4_PhotoCraft_foreshadow_v4.png) | People said another world lay<br>just beneath those hills. |
| 9.2 s | [OP01 草地玩耍](../MJ_ref/Slideshow/Opening_v1/OP01_MJ_r04_U4_upscale_candidate_v1.png) | Niamh and Oisín knew these slopes by heart.<br>There was always time for one more game. |
| 14.8 s | [OP02 听见召唤](../MJ_ref/Slideshow/Opening_v1/OP02_listening_2026-11-20/OP02_Oisin_listening_composite_v1.png) | Oisín stopped. Something was calling<br>from the hill. Niamh listened,<br>but heard only the wind. |
| 21.4 s | [OP03 追向树林](../MJ_ref/Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/OP03_U1_duo_layout_v6.png) | Oisín ran towards the trees.<br>Niamh called after her. When her friend<br>kept running, Niamh followed. |

## 画面从故事关系入手

村庄是熟悉的家，田野的暖光和安静的云形确立日常。第二页以独立小丘和灰调伏笔交代传说，顶部手调露底仅修补八行，v4 分层修补稿的其余像素与 v3_m 相同。第三页的手势和视线相接，是后两页读懂友谊的依据。第四页先读奥伊芯的脸再顺目光入坡，只有一丝冷意。第五页冷色扩至天空、山与林，中央草地仍要衬出领跑与追赶。比较全尺寸笔线，再按游戏显示尺寸看轮廓、脚下落点和前后关系。

## 从失败回图到可用合成

首轮回图变成方形，后续显式写 `--ar 91:51`。用整幅文字要求“层次更丰富”时，生成结果把小山头和鞍部连成平行斜坡；下一轮固定山脊、分别调整山面明度。MJ 仍产生远山勾线。转用 ImageGen 时，底图承担形状，OP02 小样承担相邻平涂色块的笔触，之后 BG01 承担宽平云底与横向云尾。保留冷暮色，再沿屋顶、树冠和林缘将天空远山接回高清 U1。相关[源稿、分层和合成记录](../MJ_ref/Slideshow/Opening_v1/OP03_running_to_trees_2026-11-22/README.md)保存了各次分工。

双人生成出现衣装或花冠互换。单独选奥伊芯领跑与妮芙回喊的表演，再用 v4 的人物组套入新背景。角色大小、左右间距、远近和朝向以负责人手调为准，纹样按显示尺寸判断。v5 对比人物组边界，v6 只迭代云层。输出对照时分别看原图、分层、无人物背景及合成 PNG。

## 让镜头决定音乐修改的位置

参考《Lantern Keeper》的程序编排方式，第一版音色被听出电子感；第二版借用菜单录音又太像菜单。第三版为本片重写乐句，以真实竖琴、长笛及大提琴单音采样演奏。菜单原曲来自项目既有 Google Lyria 流程；v9 使用 VSCO 2 CE 实录采样，由[本片乐谱脚本](../TechArtAsset/Audio/Opening/_src/score_acoustic_opening_v9.py)重建。

v4 延长 11–15 秒与 20 秒后的乐句。v5 把召唤提前到 14.54 秒渐入，v6 又针对截图中的第 11 秒把两笛音交叠约 1.65 秒并压轻竖琴起音。v7 解决尾声骤停，v8 将追赶改为下行。v9 在下行中跃至高 E，再落向 F♯，大提琴托住低 E；末镜增加 3.2 秒，最后笛音约 3.4 秒，末 2.8 秒整体淡出。前四镜沿用原来的四个转场点。保留每版供按时间码比较。

## 文件与验收

[WAV 母带](../TechArtAsset/Audio/Opening/BGM_Opening_Five_Scenes_v9.wav)用于制作；[OGG](../TechArtAsset/Audio/Opening/BGM_Opening_Five_Scenes_v9.ogg)用于游戏；MP4 含画面和字幕，作为联调参照。PNG 为五张无字幕的最终合成静帧，过场字幕由 Unity 独立绘制。区分负责人对配乐的选用、运行文件的校验和游戏内实测。十一月十八日的实机记录只覆盖旧三页占位。

[Prompt 集第 7 章增补](../StoryDesign/妖精丘陵_Midjourney_Prompt集_m_故事v2.2_开场五镜增补.docx) · [概念设计附录 B 增补](../StoryDesign/妖精丘陵_概念设计说明_m_故事v2.2更新_开场五镜增补.docx)。两份保留原编辑版，在对应章节新增本轮索引。
