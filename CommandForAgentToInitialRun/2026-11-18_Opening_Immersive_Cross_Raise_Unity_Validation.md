# 开场界面与举高十字架 实机检查

日期：2026-11-18。用户已授权网络电脑 Codex 执行本任务。设计端已直接修改实际 Unity 工程，本任务从现有修改继续检查与修复，不重复实施、不重建关卡。

## 目标与边界

1. 开场 slideshow 试用守灯人形式：故事画铺满屏幕、保持比例覆盖，字幕叠在画面下方的柔和渐暗区域；去掉原分页分隔线和页码。保持原三节拍、章节卡、Next/Skip、切关遮罩与输入释放保护。现有占位画身份不变。
2. 按键提示的按键字母或名称加下划线，覆盖开场 Space/Enter/Esc、HUD 移动键和交互 E/Q 等。只标记按键，不把普通英文单词加线。`KeyHintUnderlines` 根据 TMP 字形位置绘制 UI 线条，避免改写用户字体 atlas。
3. 最后受控红荆棘障碍：有铁十字架、在原 Q 作用范围内触发时，妮芙直接切到用户画的举高姿势，原墙体驱散结束后恢复 v8。采用 B，无胸前中间姿势。沿用原红光 0.3 秒与消解 1.6 秒；本轮没有新增大光束或第三个姿势，也不新增伤害、冷却或范围规则。短暂停止水平/跳跃输入覆盖既有墙体消解时长；物理与碰撞继续运行。重点检查这个暂定表现是否自然。

## 工程和已实施内容

- 本机工程：`C:\Users\Administrator\Documents\UnityProject\TheFairyHill2D`。
- 参考项目 TheLanternKeeper2D 只读，不改动、不扫描其 Library/Temp/Logs。
- 已读双方 2026-11-18 Claude 导入记录；可复用经验为人物身份保留、聚焦已有可玩路线、分开记录实现/编译/运行/用户认可。
- 本轮之前的花纹同步已单独 checkpoint：`3a38c22`。检查当前 HEAD 和工作区，不假设旧任务已完成本轮验收。
- 已改 `Assets/_Project/Scripts/Gameplay/` 下：`OpeningSequencePlayer.cs`、`OpeningSequenceData.cs`、`NiamhMotionV8Presentation.cs`、`PlayerController2D.cs`、`ThornWall.cs`、`ChapterHUD.cs`；新增 `KeyHintUnderlines.cs` 与 `.meta`。
- 新资源 `Assets/_Project/Resources/Niamh/CrossRaisedStory.png` 与 `.meta`。350×699，100 PPU，自定义 pivot 为 `(0.467142857,0)`，对应原327像素角色的 `(163.5,0)`，防止姿势切换脚底平移。来源为当前 `Niamh_cross_raised_story_v1.png`，SHA256 `f708046d9789ff53e2b1956d8153300bb09782458e502392ce414a6a2b5df86f`。
- `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/implementation_manifest.json` 记录目标文件及散列。
- 设计端使用实际 Unity DLL 的离线 Roslyn C#9 类型检查已通过，原有3项序列化字段警告不新增；这不等于 Editor 编译、资源导入或 Play Mode。

## 保护现场

先读本工程 AGENTS.md、`Docs/Opening_Chapter1_Placeholder_Unity_Handoff.md`、`Docs/Niamh_Motion_v8_Unity_Handoff.md` 和上述 manifest。

任务开始前已有的 `AGENTS.md`、`Assets/Scenes/Ch1_S1_Village.unity`、`Assets/TextMesh Pro/Resources/Fonts & Materials/LiberationSans SDF - Fallback.asset`、`Assets/_Project/Fonts/Fondamento SDF.asset` 是用户/既有修改，不能覆盖、回退或一并提交。manifest 的 protected_sha256 可核对。本轮代码与新资源是设计端刚放入的任务内容，不能当作无关修改丢弃。不要使用 git reset/clean 或重建菜单/Core/关卡。自动测试和副本工程仍暂停；在实际工程小批 Play Mode 检查。

## 实机检查与可修复范围

1. 连接真实 Editor，等待导入/编译，记录 Console 的新错误与原有信息。确认 Resources.Load 能得到 Sprite；脚底、大小、朝向、材质及排序符合原 v8。
2. 从正常菜单 Play 进入开场，1920×1080 和1280×720检查三段字幕、Next/Skip、按键下划线、柔和遮罩、画面人物不被不当裁切。保留章节卡和正常进入村庄；重复/快速推进、Skip、按住导航键都不能重复切关或把输入带入游戏。可分别记录实际键鼠和工具调用路径，不能混报。
3. HUD 的 A/D、方向键、Shift、Space、E、Q 下划线与提示框宽度正常；反复开关消息/交互后没有残留线、重影、额外点击拦截、普通词被误标或布局抖动。特别看动态添加组件后的首帧与禁用再启用。
4. 沿现有流程获得铁十字架，靠近最终受控红墙按 Q：直接举高、十字架握持与新花纹正确，无双重手臂；保持朝向；原墙消解与光效正常，结束恢复 idle/移动/跳跃。检查另一朝向、重复 Q、无十字架/无目标时提示、切场景或禁用后恢复。不要为验收在已保存关卡写入临时作弊状态。
5. 对本轮缺陷做最小修复，重编译并复查受影响路径；不要安装 Recorder/新包或增加无关功能。`storybookLayout` 默认 true，false 可回到原界面；如当前试版确实不可读，报告证据再调整字幕位置或字号。
6. 截图保存 `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/Unity_Trial/`，至少开场大/小尺寸、下划线、举高红墙、恢复姿势。若能用已有能力录制则可加短视频，不必安装包。
7. 结束停止 Play、清理临时输入，timeScale=1，仅保留 MainMenu，既有用户文件保持原字节。

## 回报与 Git

写 `Docs/Opening_Immersive_Cross_Raise_Unity_Handoff.md`，区分资源导入、编译、工具调用路径、真实键鼠、主观用户认可。写同目录 `Unity_Trial/result.json`，包括 checked_paths、failures、evidence、editor_compile、playmode、owner_acceptance。检查失败或无法连接时照实记录，不以文件存在/离线编译替代运行。

用户最新授权：休息期间可先推送当前源码、美术和发展记录等大文件，保持实机待验身份；运行检查完成后设计端再汇总回报、更新相关文档并push。当前源码checkpoint为 `cc815f8`。网络端可按明确任务文件allowlist本地提交修复/验收资料，排除4个保护文件；不要自行push。设计端读取此Handoff和result.json后继续同步。共享设计仓库只读，设计端负责自己的文档。无需自行向其他聊天发消息，反馈文件即可。
