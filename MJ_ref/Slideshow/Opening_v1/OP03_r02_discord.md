# OP03 r02 · 2026-11-22 四宫格已回传

**当前衣装参照见本文末尾的「妮芙金色前襟纹样更正」。** 本轮提交稿使用的旧双人拼图留作记录。

负责人看过 r01 后指出两个人都不像原设。r02 用 v3 右侧视图直接约束人物，保留两人向右、奥伊芯在前的追赶关系。沿用 Niji 6、16:9 和 OP01 风格参考。r01 的第 4 格只作人工对照跑姿。

- `V3_PAIR_URL` 用 `OP03_r02_v3_side_reference.png` 的 Discord 图片链接。拼图左侧为[妮芙 v3 朝右侧面](../../Characters/Niamh/Turnaround_v3/Niamh_v3_turnaround_facing_right.png)，右侧为[奥伊芯 v3 朝右侧面](../../Oisin_Side_v3_wip.png)。用 `--cref` 和 `--cw 100` 一并参考脸、头发和衣装。奥伊芯侧面稿的披肩偏长，以[正面 v3](../../OISIN_REF_v3.png)核对短披肩。
- `OP01_URL` 用 [OP01 无界面原图](OP01_MJ_r04_U4_upscale_candidate_v1.png) 的 Discord 图片链接，填入 `--sref`。

```text
Two distinct girls in full-body right-facing profile sprint across a meadow at dusk. On the right, Oisin leads toward the trees. Oisin has a short curly copper-red bob, amber eyes, a full crown of red roses and white daisies, a short rose-red embroidered shawl over a cream bell-sleeved dress, and brown lace-up boots. Oisin carries a small iron cross tucked under her red shawl. On the left, Niamh runs after Oisin, with long golden-blonde hair flowing behind her, grey eyes, a silver leaf circlet, a forest-green hooded cape over a cream dress with pale green embroidery, and forest-green boots. A clear gap separates their running silhouettes. Warm village windows behind them on the far left, a cool blue-green tree line ahead on the right. Hand-painted golden dusk, tapered strokes in olive grass, soft distant hills. A quiet strip of grass across the bottom fifth. --cref https://cdn.discordapp.com/attachments/1556337295244926996/1573737234639880292/wAAAABJRU5ErkJggg.png?ex=6b031883&is=6b01c703&hm=f2730f74638c154a785478120ec4ddd8e7a7ccc1abce226257bd36f04f2101f5 --cw 100 --sref https://cdn.discordapp.com/attachments/1556337295244926996/1573733359220424814/fwE2vOMJ2NF3QAAAABJRU5ErkJggg.png?ex=6b0314e7&is=6b01c367&hm=71b832bf71e07d8f8ff13fa6979562692aab777931e40d3a9ce042bb2b72af3f --sw 100 --niji 6 --ar 16:9 --s 100 --no lettering subtitles interface borders watermark
```

四宫格先核对能否同时认出两张脸。妮芙看长金发、灰眼、银叶额饰和绿斗篷，奥伊芯看短红卷发、琥珀眼、玫瑰雏菊花冠和红披肩。随后核对两人都向右跑、奥伊芯在前，十字架若露出应只在奥伊芯身上。

双人参考图 SHA-256 为 `D3014EBCCBB61E592EAF084868AF7C843F3B8544E61963C5CFD3FBDE1959CD8D`。妮芙侧视源图为 `F1E7024D8D836609041D59D970B6DDD73842AA677DEC3F548B44B012637F9568`，奥伊芯侧视源图为 `BBACDC80D46D7B8F96F86720ED75B7681F95A2D011CD8F1D3789E138F37D9DCD`。上方命令已填入负责人提供的双人参考链接及首轮 OP01 链接。两个 Discord 附件尚未从本端验证。提交词及参数以 Discord 实际任务为准。

## 2026-11-22 四宫格初评

四格均为妮芙在左后、奥伊芯在右前，且绿斗篷与红披肩归位。画面仍有脸型、发型和饰物的偏差。妮芙在四格都穿棕靴，人物足部贴近画面下沿。截图未显示完整提交词、任务 ID 或模型参数，尚无放大原图。

| 格子 | 取舍 |
| --- | --- |
| 1 左上 | 奥伊芯的红卷发和花冠有辨识度。妮芙的兜帽遮住发顶和银叶额饰，两人步态偏走。 |
| 2 右上 | 本轮优先保留作构图与奥伊芯造型参考。奥伊芯的红发、红披肩和红玫瑰白雏菊花冠最接近，后脚抬起。两人距离清楚，左后有房屋、右前有树影。妮芙仍盖着兜帽，胸前有十字状饰物，身体直立，读起来像快走。 |
| 3 左下 | 妮芙露出发顶，斗篷和挎包可见。她戴花冠，奥伊芯的花冠缺少明显的红玫瑰。两人都像并序向右步行。 |
| 4 右下 | 妮芙胸前有明显十字架，奥伊芯的花冠变成叶枝。两人直立迈步。 |

本轮没有同时通过角色相似度和追赶动作的成图候选。r01 第 4 格继续作为双人跑姿参考，r02 第 2 格保留人物间距、村屋和树影的布局。后续对照原设逐人修正，重点为妮芙的露发轮廓、银叶额饰、绿靴和跑姿，以及十字架归属。

## 单图复核与下一次局部修改

负责人回传两张 Discord 单图截图，确认 r01 Image #4 为跑姿参考、r02 Image #2 为构图和奥伊芯造型参考。两张截图均显示 Vary (Region) 按钮。建议以 r02 Image #2 为底图，第一步单独修妮芙头部。r01 Image #4 的双人前倾、屈肘和后脚抬起用于后续跑姿比对。

在 Discord 开启 Remix Mode，打开 r02 Image #2 的 Vary (Region)。圈住左侧妮芙的侧脸、头顶和整个兜帽轮廓，选区略过原兜帽边缘以便补背景。将长发尾端、肩线和衣领下方留在选区外。用下列短提示词描述头部选区。

```text
Right-facing side profile of Niamh, a soft round face, a light grey eye, long golden-blonde hair with a side-swept fringe and a small silver leaf circlet across her exposed forehead. Hair uncovered, hood down behind the shoulders. Hand-painted warm dusk light.
```

回图先对照 v3 朝右侧面检查侧脸轮廓、灰眼、刘海与额饰。头部通过后，胸前十字饰物、绿靴和跑姿各自另处理。

### 妮芙头部局部修改回图

提交界面截图显示使用了上述英文和头部选区。回传四格均去掉兜帽，长发大体接上。左上和左下露出两只偏青的眼，脸偏向镜头。右上有棕发箍和发花。右下第 4 格的朝右侧脸最清楚，长发衔接自然，额饰仍被画成金色发辫。右下暂作下一次额饰修改的底图。

下一次只圈右下第 4 格从耳朵上方延伸到额头的辫带，沿辫带边缘带一点发色。眼、眉、耳与长发主体留在选区外。

```text
A thin silver metal circlet with small silver leaf ornaments, resting on smooth golden-blonde hair, seen from the right side. Fine silver highlights on the leaves.
```

### 妮芙额饰局部修改回图

提交界面截图显示选区覆盖原辫带，眉眼和耳朵留在外面。回图中四格侧脸均朝右。右上第 2 格的耳上到太阳穴一段出现独立叶片，色相偏橄榄绿与铜棕，靠额头处仍有金色辫痕。其余三格仍可读作发辫。保留右上作为局部修改候选。额饰后续按 v3 校成银灰并清理辫痕。

下一次局部修改可先处理关系到分镜的道具归属。在右上第 2 格圈住妮芙胸前的十字形吊坠和下方长挂件，选区边缘带少量相邻布纹。保持面部、斗篷外轮廓和前臂在选区外。

```text
Plain cream linen dress bodice with soft vertical folds and the edge of a forest-green cloak at the neckline, in warm dusk light.
```

上方为发现旧参考前准备的道具选区提示词。是否提交未核实。绿靴、姿态和字幕留白继续待修。

### 妮芙金色前襟纹样更正

负责人指出 r02 双人拼图里的妮芙侧面为旧版，手边绿色前襟缺少后补的金色花纹。以后以 [2026-11-19 修订侧身图](../../../TechArtAsset/Characters/Niamh/Motion_v8/appearance_front_ornament_v2/Niamh_side_static_v3_ornament_fix_v2.png) 为 OP03 前襟参照。金色纹样沿绿色前襟往下，垂手在纹样前方。按奔跑时的手臂位置重新判断遮挡。

新版双人参考文件为 `OP03_v3_side_reference_front_ornament_v2.png`，用修订后的妮芙侧身图替换左半，右半沿用同一张奥伊芯侧面。拼图 SHA-256 为 `4DA3968D2725BCDD8D5B0BD75B04F2A33823251BC9DD91CA140066DE8F911A46`。妮芙侧身源图 SHA-256 为 `64D3639F2552DD2C57051A6D23693F91D32E8C887CCD5AE5CC04E4F841DFEA53`。

去除胸前十字形吊坠和下方长挂件时，已正确的绿襟金纹留在选区外。若该段前襟花纹缺失，把缺纹的绿色布边一起圈进选区，按新版侧身图校对。提示词改用以下版本。

```text
Cream linen bodice with soft folds, beside a narrow forest-green cloak front panel embroidered with fine interlaced gold scrollwork. Warm dusk light.
```

### 妮芙胸前挂件移除回图

提交前将选区收回至胸前十字形吊坠和下方长挂件，保留手、裙面和裙边。提交界面最后显示的提示词如下。

```text
Cream linen bodice with soft folds, a clean forest-green cloak edge at the neckline, and warm dusk shading.
```

回图选右下第 4 格。十字和长挂件均已退去，领口只有小圆扣，米白布褶自然接到腰线。左上新增深色系带，右上新增叶状胸饰，左下仍有一条深色纵向线。第 4 格的无界面放大原图、参考图与五轮四宫格已归入 [OP03 归档](OP03_running_to_trees_2026-11-22/README.md)。

绿襟金纹后续按修订侧身图补绘。[负责人原纹样补片](../../../TechArtAsset/Characters/Niamh/Motion_v8/appearance_front_ornament_v1/front_ornament_patch_same_origin.png)可作金纹来源。补片只含一段新增花纹，绿襟的长度、布纹和手部遮挡以修订侧身和实际跑姿为准。
