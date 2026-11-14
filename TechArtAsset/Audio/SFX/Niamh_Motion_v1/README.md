# 妮芙动作声音 v1 试听稿

**日期**：2026-11-14
**状态**：负责人单独试听后反馈“没有太大问题”，已批准放入游戏试装。23 条独立 OGG 已于 2026-11-14 经共享网络复制到 Unity 并核对 SHA-256；接入与游戏内混音尚待 Unity 端执行。`.wav` 是保留在设计端的母带。

## 先听

`Niamh_Motion_v1_listening_reel.wav` 是 14.60 秒的试听盘，顺序：土地 3 步 → 草地 3 步 → 木材 3 步 → 石头 3 步 → 干草 3 步 → 起跳 2 次 → 轻落地 2 次 → 重落地 2 次 → 擦草 2 次。各组间稍有停顿；它不用于 Unity 单次事件。

如果觉得不同材质难辨、脚步偏“电子噪声”、重落地过重或草声太尖，先修改脚本参数，重出新版本并保留本版。不要直接把这批声音当定稿。

## 文件

- `SFX_Niamh_Step_{dirt,grass,wood,stone,hay}_{01,02,03}_v1`：五种材质各三个脚步，共 15 条。
- `SFX_Niamh_Jump_{01,02}_v1`：起跳 2 条。
- `SFX_Niamh_Land_{light,heavy}_{01,02}_v1`：轻/重落地，共 4 条。
- `SFX_Niamh_HayBrush_{01,02}_v1`：草垛边缘摩擦，共 2 条。
- 所有单条均有 `.wav` / `.ogg` 两版，44.1 kHz 单声道；试听盘也有两版。脚本总共输出 24 个 WAV 和 24 个 OGG。

## 重生成

从设计仓库根目录运行，Python 需有 NumPy，系统需有 ffmpeg：

```text
python TechnicalArt/tools/make_niamh_motion_sfx_v1.py
```

脚本固定随机种子，输出同版可复现。生成算法为多频带噪声冲击、颗粒/草叶摩擦和少量衰减共鸣；所有样本峰值约 -8.5 dBFS，不作游戏内音量结论。

## 交给 Unity 的条件

负责人已批准游戏内试装，现进入在村庄与森林 BGM 下判断混音的阶段。23 条 OGG 已通过共享网络复制到 Unity `Assets/_Project/Audio/SFX/Niamh_Motion_v1/`。任务单见 `CommandForAgentToInitialRun/2026-11-14_Niamh_Surface_Audio_Unity_Trial.md`；Unity 内同件和复制清单在 `Docs/References/Niamh_Surface_Audio_v1/`。设计仓库保留 WAV 母带、脚本和试听盘。木材音色留给未来木箱；当前通用 Jump/Land 可轻叠地面 Step 表达材质，尚无每种地面独立制作的 Jump/Land 音频。正式游戏内听感待负责人试玩。

整体设计与接入注意事项见 `TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md`（路径相对于设计仓库根目录）。
