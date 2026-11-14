# 妮芙动作声音 v1 试听稿

**日期**：2026-11-14
**状态**：Python 生成并检查文件格式；尚未由项目负责人试听确认，尚未复制或接入 Unity。此处的 `.ogg` 是试装候选，`.wav` 是可编辑母带。

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

先由项目负责人在村庄和森林 BGM 下听，并决定需要保留、修订或替换的声音。确认后只复制需要的 OGG 文件到 Unity 工程的 `Assets/_Project/Audio/SFX/Niamh_Motion_v1/`，通过双方可访问的共享网络传输。设计仓库保留 WAV 母带、脚本和试听盘。Unity 端记录复制清单、声音触发时机、实测画面及仍需确认项。木材音色保留给未来木箱，当前两处可玩场景没有已查到的木箱。

整体设计与接入注意事项见 `TechnicalArt/CHAPTER_TRANSITIONS_AND_SURFACE_AUDIO_v1.md`（路径相对于设计仓库根目录）。
