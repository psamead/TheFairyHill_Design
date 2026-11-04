# 妖精丘陵 · 音频制作流程（v1，2026-10-26）

> 原游戏计划没有音频部分，本文件补上。适用于 Claude / Codex / 人工。
> 第一首成品：开始菜单 BGM `TechArtAsset/Audio/MENU_BGM_v1_loop.ogg`。

## 1. 音乐风格基调

- 爱尔兰民间传说 + 妖精丘陵：安静的好奇、温暖、带一点忧伤；不恐怖、不史诗。
- 乐器：凯尔特竖琴（琶音）、低音哨笛 / 锡哨（旋律）、弦乐铺底、很淡的无词合唱、偶尔的风铃闪光；鼓尽量少。
- 调式优先 D 多利亚（Dorian）；菜单 / 探索约 60–80 BPM。
- 只做器乐，不要带歌词的人声。

## 2. 生成（Google Lyria 3 Pro）

工具：Google AI Studio 或 Gemini（Lyria 3 Pro，单首最长约 3 分钟）。同一提示词多生成 3–4 次，挑一首；挑选标准是**连续听三遍不烦**。

**提示词模板**（英文；替换【】里的内容）：

```
Instrumental background music for 【场景用途，如 the main menu / a forest level】 of a 2D hand-drawn fantasy game set in rural Ireland. The scene: 【画面描述】.

Mood: 【情绪】. Not scary, not epic.

Instruments: solo Celtic harp playing a simple, slow arpeggiated pattern; a soft low whistle carrying a short, singable melody; warm sustained string pad underneath; very faint wordless airy choir in the background; occasional distant chime shimmer. No drums or only a very soft frame drum heartbeat. No vocals with lyrics.

Musical details: around 【BPM】 BPM, D Dorian mode, calm and steady, no big build-up or climax, no sudden changes. Designed as a seamless loop for a game: no intro and no fade-out, it should start and end on the same chord with the same texture.

Length: about 90 seconds.
```

开始菜单用的实际提示词：场景 = dusk turning to night, a Neolithic stone passage-tomb on a grassy fairy hill, a faint blue-green light glowing from its doorway, two young girls standing at the threshold of the fairy world；情绪 = quiet wonder and gentle mystery, a little melancholy but warm and hopeful, like an old folk tale about friendship；70 BPM。

下载原曲，命名后放 `MJ_ref/`（例：`Threshold_of_the_Stone.mp3`）。原曲不改。

## 3. 处理成无缝循环

AI 生成的曲子即使提示词要求循环，通常仍有前奏、渐强和结尾淡出，不能直接循环。

用 `TechnicalArt/tools/make_loop.py`（需要 Python + numpy + ffmpeg）：

```
python make_loop.py MJ_ref/Threshold_of_the_Stone.mp3 TechArtAsset/Audio/MENU_BGM_v1_loop
```

原理：
1. 比较整首曲子每一小段的和声（12 音级）和音量，在前段找起点、后段找终点，挑最相似的一对。
2. 截出起点到终点之间的部分。
3. 结尾最后 3 秒做等功率交叉淡入：尾部淡出，同时叠上起点之前 3 秒的音频淡入；这样循环末尾自然接回开头。
4. 输出 `.wav`（母带）和 `.ogg`（给 Unity）。

自动找的点不满意时，可手动指定：`--start 11.7 --end 78.95`。

**验收**：把循环版的「结尾 8 秒 + 开头 8 秒」接起来连放两次，听不出接缝即通过。

## 4. 已完成

| 文件 | 来源 | 循环段 | 长度 | 状态 |
|---|---|---|---|---|
| `TechArtAsset/Audio/S1_VILLAGE_BGM_v1_loop.ogg` / `.wav` | `MJ_ref/Village_Dusk.mp3`（91 秒） | 21.65 → 72.20 秒 | 50.55 秒 | 2026-11-01 完成 |
| `TechArtAsset/Audio/S1b_FOREST_BGM_v1_loop.ogg` / `.wav` | `MJ_ref/Forest_Path.mp3`（121 秒） | 29.80 → 88.00 秒 | 58.20 秒 | 2026-11-01 完成 |
| `TechArtAsset/Audio/MENU_BGM_v1_loop.ogg` / `.wav` | `MJ_ref/Threshold_of_the_Stone.mp3`（88 秒） | 11.7 → 78.95 秒，3 秒交叉淡入 | 67.25 秒 | 用户已确认，待接入 Unity |

## 5. 放进 Unity

- **只把 `.ogg` 复制进 Unity 项目**（建议 `Assets/_Project/Audio/Music/`）。`.wav` 是母带，留在共享文件夹，不进项目。
- 导入设置：Load Type = Streaming（音乐）；Compression = Vorbis；Preload Audio Data 关闭。
- AudioSource：Loop 勾选，Play On Awake 勾选，音量约 0.6；UI 提示音约 0.35，提示音要比音乐清楚。
- 文件已接好缝，不需要额外的交叉淡入淡出脚本；只用 AudioSource Loop 即可。

## 6. 待办

- [ ] 第一章森林探索、古墓内部、Boss（普卡之首）、结局：各一首，同一流程。
- [ ] 音效：菜单选中提示音（目前占位）、确认 / 返回、脚步、铁十字冷光、妖怪退散等。
- [ ] 可选：菜单「首次进入先播前奏再进循环」——从原曲剪 0–11.7 秒做 intro，Unity 里播完 intro 再切循环。

## 7. 第一章关卡音频（2026-11-01）

### 7.1 BGM（Lyria，流程同 §2–3）

S1 黄昏村庄：场景 = golden dusk in a quiet Irish village, a whitewashed thatched cottage, dry stone walls and wide open fields, a little girl setting out on a walk；情绪 = warm, gentle, curious and a little homesick, the calm before an adventure；**76 BPM**。原曲存 `MJ_ref/Village_Dusk.mp3` → 循环 `TechArtAsset/Audio/S1_VILLAGE_BGM_v1_loop`。

森林小径：场景 = a deep woodland path at late dusk, tall trees with golden light between them fading into violet haze, roots and ferns, something hidden watching from the thorns；情绪 = hushed wonder turning slowly uneasy, mysterious but still storybook, not horror；**66 BPM**；乐器在模板上改为 harp + low whistle + low cello drone + soft wind texture, very sparse。原曲存 `MJ_ref/Forest_Path.mp3` → `TechArtAsset/Audio/S1b_FOREST_BGM_v1_loop`。

### 7.2 音效

音效用 ElevenLabs Sound Effects、Gemini / AI Studio 里能出音频的模型，或免费音效库（Freesound，注意授权 CC0）。要求：单声道或立体声 .wav，44.1 kHz，前后不留长空白。生成后自己裁到合适长度，转 `.ogg` 放 `TechArtAsset/Audio/SFX/`。

| 文件 | 长度 | 提示词（英文） |
|---|---|---|
| `SFX_gate_open` | 约 1.2 s | old wooden farm gate creaking open on rusty iron hinges, short wooden knock at the end, outdoors, dry and clear |
| `SFX_gate_close` | 约 0.8 s | old wooden farm gate swinging shut against a stone post, soft wooden thud, short creak |
| `SFX_cross_pickup` | 约 1.5 s | a small iron cross picked up from the forest floor: soft rustle of leaves, a light metallic clink, then a gentle magical shimmer of bells rising, warm and hopeful |
| `SFX_thornwall_banish` | 约 2.5 s | dark magical thorny brambles dissolving: a low cold whoosh, crackling and snapping branches, a deep hiss of black smoke, a faint distorted whisper fading away, ending in quiet |

### 7.3 音效改为程序合成（2026-11-01，用户已试听可用）

ElevenLabs 的 Music 页面会把音效提示词当成整首歌（贵且不对）；最后改用 `TechnicalArt/tools/make_sfx.py` 用 numpy 合成四个音效（吱呀 = 黏滑调幅的谐波 + 带通噪声；木头敲击 = 衰减正弦；铃声 = D 大调上行琶音；湮灭 = 低通噪声呼啸 + 随机噼啪 + 高频嘶声 + 调幅低语，最后加简易混响）。输出 `TechArtAsset/Audio/SFX/*.wav` + `.ogg`，清单 `TechnicalArt/第一章音效_v1.xlsx`。好处：可以改参数重新生成，适合课堂讲解。

