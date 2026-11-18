# Character animation lessons — The Fairy Hills

**2026-11-19 Unity反馈补记：** B直接举高接入现有红墙事件后，网络端的Editor工具检查确认左右朝向、触发、短暂停势、墙体消解和恢复路径均有证据。必须把“动作图已画”“Unity已接入”“工具模拟运行”“负责人实际游玩与审看”分开写。报告速度字段与最终Console日志冲突时不要沿用猜测值；按实际路线复测并保存日志。原始截图和报告入口见 `ForDesignScreenShot/2026-11-18_for-opening-cross-raise/README.md`。本轮未改变动作图、源PSD、Unity资源或代码。

**2026-11-18 预览补充：** 两张持势 GIF 保留。idle 到胸前的网格中间帧出现袖口变形、手臂衔接不自然，不能当作有效连续动作；按用户备选提供 idle 直接切胸前原稿版。第二种继续做，用户指定用第一张胸前抱持原稿替换此前两个变形的中间姿势，因此当前顺序是 idle → 胸前抱持 → 举高。先提供原画关键姿势切换，等待用户判断节奏；不把它称为平滑骨骼动画，也不增加第三张独立动作图。当前文件入口见 `TechArtAsset/Characters/Niamh/Cross_Actions/README.md`。



**2026-11-17 衣装一致性更新：** 第二稿新增金色前襟花纹已同步到胸前动作、基础 `Motion_v8/parts/body.png` 与静态备用图；两动作画布仍350×699，基础角色仍327×699，alpha保持。新增可编辑修订源和备份见 `TechArtAsset/Characters/Niamh/Motion_v8/appearance_front_ornament_v1/`。Unity实际身体和静态备用PNG已网络复制，`.meta`不变；本次未连接Editor或验证Play Mode。当前源用户PSD不覆盖，重导出基础身体须使用新增修订源。



**2026-11-17 晚间最新决定：两个动作足够，不再制作第三个动作。** 第一个 `cross_chest_local`（胸前）用于关卡内小怪、小障碍和小剧情；第二个 `cross_raised_story`（举起）用于剧情触发的大光线、湮灭大型障碍等事件。当前文件统一放 `TechArtAsset/Characters/Niamh/Cross_Actions/current/`，使用语义名 PSD/PNG；画布均为 350×699，保留左上原点与人物像素。用户原稿、旧试验和旧粗 GIF 已分类，路径变更及像素校验见该目录 `file_manifest.json`。

Agent 使用原则见 `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md`，人读说明见 `TechnicalArt/妮芙十字架双动作使用规则与制作交接_v1.docx`，机器规则见 `TechArtAsset/Characters/Niamh/Cross_Actions/action_usage_rules.json`。两张用户绘画已准备和整理；连续动画、大光线特效及 Unity 接入尚未完成。该使用原则不自动扩大当前 Demo 的战斗系统范围。以下较早的“等待第二姿势 / 制作高举或第三姿势 / 当前仅胸前”记录只作历史，不再是任务要求。



**Started:** 2026-11-14
**Audience:** Project owner, students, artists, Unity developers, future agents
**Scope:** Reusable lessons from preparing and testing Niamh's first user-reviewed cutout motion study. This is a growing experience log; it does not replace the art specification or live Unity progress.

**Current Niamh cross workflow:** see the final section, “2026-11-17 完整人物参考剪贴与用户手修工作流”. Earlier ImageGen integration notes are historical experiments.

## Trial 1 — Niamh motion v1–v8

### Context

The Unity game already used one static Niamh side-view Sprite. The owner wanted only actions needed by the existing Village and Forest Path scenes first: idle, walk, run, jump and land. The owner supplied and refined a layered Photoshop `_m` file, then reviewed motion studies with visual markups. The source parts in v8 were exported from that edited file and kept at a shared 327 × 699 px canvas.

### What worked in preparation

- Iterate using the owner's edited source and marked-up poses; each iteration kept its source snapshot, parameters, reference image, preview GIF, and README together.
- Preserve identical canvas dimensions and alignment for each transparent part. This made layered comparison and compositing predictable.
- Keep the jump poses staged: ascent with head up / legs behind / arm forward; descent with head down / arm behind / legs forward; then a small landing and recovery.
- Review the actual point of concern at named times. A contact sheet made it easier to compare the peak of the fall swing with the start and recovery.
- Remove exaggerated whole-body squash when it made the landing feel too heavy. Keep the feet visually grounded while upper parts settle.

### Limits found before Unity

- A GIF preview is useful for posing but cannot establish Unity import settings, Animator transitions, layering, collision alignment, movement synchronization, or performance in the actual scenes.
- Rotating whole `leg.png` and `arm.png` cannot create a knee or elbow bend. Duplicating one painted leg for the far side is only a mockup, not a final anatomical solution.
- Rigid dress and cape pixels can hide the arm's missing backdrop and obscure the hand arc. Check against magenta and game backgrounds at the actual 2.1u scale.
- Preview timing is an art reference, not gameplay timing. The preview's two-second jump loop is longer than the current physical jump. Bind poses to controller ground / vertical-velocity states, then retime in Play Mode.
- The user-edited `_m` file is authoritative. Export from a snapshot or duplicate; never repair it by painting over the source or reusing an old fill patch.

### What the Unity trial actually established

Unity imported the six PNGs, made a reversible eight-renderer puppet with a derived far leg/boot, built seven Animator states, and connected it to the persistent player without replacing its controls or collider. Editor compilation passed. Village and Forest Play Mode showed idle, walking, jump phases, landing and left/right facing; the owner tried the game and found it basically OK apart from some stutter. The cause of that stutter was not measured. Run at 5.6u/s, gate toggles and every collision route were not separately captured. The full evidence and rollback are in Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md` and `Docs/References/Niamh_Motion_v8/Unity_Trial/` (implementation commit `1374a0fa3b982491aa596a2897b25b9a7c8bc93b`).

1. **Joint pivots.** Same-canvas pieces still shift if rotation uses the wrong origin. The Unity trial put each parent pivot at its converted landmark and offset child art back by the same amount; the static pose stayed aligned. The coordinates and 0.30 scale are specific to Niamh, so inspect each new character's pivots visually.
2. **Sorting.** Individual renderer orders can accidentally put limbs in front of the scenery. A `SortingGroup` held the puppet at the original actor order, while part orders worked inside the group. Check the foreground order in every level where the character appears.
3. **Facing.** Flipping individual pieces around separate joints can pull the assembly apart. The trial flipped the whole visual hierarchy and kept the hidden static renderer as the controller's facing reference and rollback. Review both directions in Play Mode.
4. **Floor contact.** Rotating boots changes the lowest visible pixel. The generator baked a vertical correction from the boot alpha edge into walk/run clips. This is not planted-foot IK; actual foot sliding still needs visual review.
5. **Preview capture.** A successful magenta image capture initially contained no puppet because the temporary camera lacked the preview scene's culling mask. Apply that mask and inspect the saved image rather than trusting capture success alone.
6. **Unrelated Editor changes.** TMP font caches can change during Editor work. Compare known dirty files before and after, leave unrelated changes unstaged, and report them. A cache change is not evidence that the animation changed.

For the next action, compare the trial at actual game scale, then decide what new art is required for push-door and cross-raise poses. Do not derive a bendable knee, independent cape or finished interaction animation from these six rigid images.

### Unity trial method

Use the network-first handoff: first check whether the task's assets are already pre-copied into the Unity project. If anything is missing, request an exact file list and purpose from the maintainer; have approved files staged under `TechnicalArt/unity_drop/<date_task>/` and copy them through the shared network. Do not use GitHub as the default art download path. Copy, do not move, the six PNGs and JSON spec into the Unity repository. Import PNGs as individual Sprites while retaining the shared canvas and a common origin. Build a reversible layered prefab, initially at the same visual height as the static Niamh (0.30 scale, roughly 2.1u); preserve the existing player root and capsule. A simple Transform / Animator rig can test the six available parts. It must be labeled a trial, because it does not implement the detailed 22-bone plan.

Review gaps and ordering on magenta, then review idle, directional movement, run, jump ascent, jump descent, landing, and turning in both Village and Forest. Keep animation as presentation: the existing player controller remains authoritative for movement, collision, input, and transitions. Never rebuild unrelated chapter scenes as part of this test. Record imported / integrated / compiled / Play Mode / user-accepted states separately.

## Reusable handoff pattern

For future art-to-Unity animation work, keep the following next to the versioned source:

1. Editable source or an immutable source snapshot, plus individually exported parts.
2. A contact sheet or GIF labeled as a reference preview, not production animation.
3. A machine-readable spec with canvas size, coordinate origin, pivots, timing intent, and limitations.
4. User markups and a short decision log explaining what changed between versions.
5. A Unity-specific task that names allowed changes, protects existing scene / prefab edits, and defines visual and runtime acceptance checks.
6. A completion note that distinguishes prepared assets, imported assets, implementation, compilation, Play Mode evidence, and user approval.

See `TechArtAsset/Characters/Niamh/Motion_v8/UNITY_TRIAL_README.md`, `TechnicalArt/NIAMH_RIG_PARTS.md`, `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md`, and `CommandForAgentToInitialRun/2026-11-14_Niamh_Motion_v8_Unity_Trial.md`.

## Trial 2 — Niamh holding the iron cross with both hands (2026-11-16)

### Goal and accepted result

Explore the hand and arm pose needed for Niamh's cross-raising interaction while retaining the existing in-game character design. The owner accepted the resulting still as a **pose and style direction**: the generated Niamh reads as close to the game's current art, and both hands hold the cross against her chest. This approval is limited to the static concept image. It does not approve its pixels as final game art, a cutout, an animation, or a Unity integration.

### Method that worked

1. Keep the existing side-view game image as the identity/style anchor and the in-game cross sprite as the prop anchor.
2. Use Midjourney in the owner's Discord conversation to obtain a four-pose character sheet; select U2 (upper-right) for the bent arms and two-handed grip. Treat the MJ character as pose reference only; its face, eyes, proportions, cape, and other details are not replacements for the game asset.
3. Generate an integrated Niamh still with Codex built-in ImageGen, referencing the original Niamh, MJ U2, and the Unity cross image. This retained the current character identity and brought the rendered treatment closer to the in-game still.
4. Ask the owner to judge the result beside the actual in-game side sprite. The owner accepted the direction on 2026-11-16.

### Limits and next action

- Later owner feedback on 2026-11-16 rejected the newly generated chest-hold, mid-raise, overhead and isolated-arm studies: duplicated hands/arms, too many fingers, incorrect arm connections and missing chest costume details. Preserve these for diagnosis only; they are not approved cutouts or Unity input. The earlier approval covers the concept's style and pose direction, not its hand anatomy. Start the next chat by fixing one chest-hold still, tracing two shoulder-elbow-wrist chains and exactly two hands, retaining the original neckline, chest fastenings and cape opening. File status and owner-marked screenshots are indexed in the study folder README.

- ImageGen's exact backend model/version and the complete prompt were not preserved in the record. Do not label it Google Imagen or invent missing metadata.
- The image is a static, generated whole-character concept. It does not contain aligned character parts, a repaired arm-backdrop, usable pivots, a motion cycle, or Unity import settings.
- Next, prepare a non-destructive layered pose using the user-edited source and Motion_v8 as the basis. Plan arm/hand/cross overlap and fill hidden regions; keep the rest of the character anchored to the existing art. Make an offline pose/GIF preview, inspect seams and the full in-game scale, and ask the owner to approve it before writing a separate Unity task.
- The gate-push pose remains a separate action. Do not imply either interaction is implemented by v8's seven existing states.

### Evidence and files

- Study folder: `TechArtAsset/Characters/Niamh/Interaction_Study_2026-11-16/`.
- Selected still: `Niamh_two_hands_pose_study_v1.png` (Codex built-in ImageGen; whole-character concept, not an aligned export of animation parts).
- MJ pose sheet: `MJ_two_hands_U2_original.png` (U2 is the upper-right pose; full sheet preserved).
- Earlier grip-only ImageGen result: `grip_imagegen_2026-11-15_reference.png` (retained only as an arm/hand study).
- Human-readable decision record: `TechnicalArt/妮芙双手捧十字架动作参考_2026-11-16.md`.

This trial also informs the generation workflow in `AGENT_PROCESS_GUIDELINES.md` §5.8: try ImageGen with in-game references first; use MJ for pose exploration if needed; then have ImageGen integrate the closest pose with the original character and prop references. The owner approves the offline animation as a distinct stage before Unity work.

## 2026-11-17 完整人物参考剪贴与用户手修工作流

### 当前来源与交付状态

用户在 `Niamh_chest_composite_preparation_wip_m.psd` 从胸前完整人物 U1 取手臂袖口，摆到原妮芙朝右立绘上，并在独立 Layer 2 手绘袖口衔接。随后接续 Agent 命名版，另存 `Niamh_chest_composite_clean_wip_v1_m.psd`，调整现有十字架的大小、方向，栅格化副本并裁去应被手遮住的部分。最新文件中可见十字架副本为 58×55 像素，源画布为 327×699；这只是本稿实际数据，不是以后姿势的固定道具尺寸。

Agent 将最新用户稿另存为研究目录中的 `Niamh_chest_hold_organized_v1.psd`，只命名和分组，保留全部 13 个源图层；通过 PhotoCraft 分别渲染源稿与整理稿后做 RGBA 逐像素比较，结果一致。源稿 SHA256 及校验见同名 `_validation.json`。这是当前静帧编辑入口，并不表示整套动作或 Unity 已验收。

### 可复用步骤与分工

1. **完整人物参考。** 在 MJ 先出完整人物，再选择合理手势；本项目不继续单独生手。原始下载图保留在 `MJ_ref/Characters/Niamh/Interaction_Study_2026-11-17/`，不得把参考人物整张替换原角色。举手 r01 U1、U2 可取不同手臂组合，r02 U4 留备用。
2. **剪贴回原画。** 保留原脸、头发、衣装和画布，取需要的手臂、手与袖口区域。朝左参考翻到朝右时检查拇指、左右手、受光和前后遮挡。隐藏原下垂手臂，保留备份。不要把原肩袖轮廓与新袖口重叠成两个肘或额外手臂。
3. **手工过渡。** 剪贴层和补画层分开。用户实际完成的袖口补画接顺了原衣料高光、阴影、褶皱和外轮廓。Agent 的软蒙版只弱化剪贴直边，未解决衣褶结构；几笔大色块的试画不自然，未纳入交付。需要结构补画时不能声称羽化即可完成。
4. **道具最后合成。** 采用现有 `TechArtAsset/Scenes/S1b_ForestPath/props/F_prop_cross_v2.png`。先变换方向和大小，再保留智能对象备用，用栅格副本或蒙版处理手与柄的遮挡；检查两手实际接触、柄在指前/指后的关系，不依赖 MJ 生成十字架。用户最新的裁切道具层与备用智能对象都应保留。
5. **逐张姿势再做连续动作。** 先检查胸前、中段、高举各自只有两条合理肩肘腕链、两只手，原衣装结构保留。未经静帧核查的剪贴件不能批量推进。下一姿势由用户制作时，Agent 只做图层和资料整理，等待新稿。
6. **预览与实际状态分开。** `Cross_Raise_Preview_v1` 的脚本用 PhotoCraft 导出/选区，再用 Pillow 安排部件和 GIF 编码，生成 4.5 秒粗循环；它只到面前高度，中段有姿势替换跳变，肩袖及握柄待修。GIF 早于最新用户十字架修订，未同步重渲染；不能称作平滑动画、头顶高举或 Unity 可用动作。

### 工具选用与核查

- 优先选可满足任务且调用容易的工具。本机 PhotoCraft CLI：`C:\photocraft-0.5.0\photocraft-cli.exe`；先查 `--help`、`commands --json --filter <command>`，核对实际参数，再调用 `info`、`run`、`convert`。PhotoCraft 不足时使用 Photoshop。此前 Photoshop 窗口捕获超时不证明它的全部编辑接口不可用。
- 本轮可用的 CLI 操作包括 `select.lasso`、`layer.layerMask.revealSelection`、`layer.setProps`、`layer.select`、`layer.groupLayers`、`file.placeEmbedded` 和 `edit.transform`；参数以本机 registry 为准。
- 分组要保持可见层内部顺序、透明度和混合方式，隐藏参考集中存放。另存源稿，重新读取整理稿并渲染比较。只看命令返回成功不足以确认画面正确。
- **白边处理未完成。** 本轮 1px `layer.matting.defringe` 对实际浅色轮廓效果有限，深色背景对比仍见白边。它不能自动去掉不透明的浅色外沿，也不能用整人物收缩替代轮廓精修；`clean` 文件名不代表问题已解决。

### 文件阅读顺序

`STORYBOARD_RESUME.md`（当前项与停下条件） → 动作研究目录 `README.md`（最新编辑入口、旧稿用途） → 本节（方法与边界）。`ART_HANDOFF.md` 和故事画知识库只保留摘要与链接，避免重复维护多份操作说明。旧失败候选、旧 `_m` 和粗 GIF 原位保留，防止已有链接和脚本失效。

### 2026-11-18 不同宽度动作图的原点与状态恢复

两张动作图为350×699，基础v8部件为327×699，左上人物像素原点相同。Unity新Sprite不能一律底部居中：用原角色的163.5px原点（新图归一化x=0.467142857），保持100PPU和原根缩放，才能避免切姿势时横移。举高时仅隐藏六部件，使用同材质/排序组的覆盖Sprite；结束恢复原可见状态，禁用时清理。不要改写原Animator曲线或用户PSD来迁就试装。当前是源码实现和离线类型检查结果，真实脚底、朝向及恢复仍待Play Mode。

用户选B只规定直接举高；GIF循环时序不决定玩法冷却。当前事件覆盖既有墙体1.9秒反馈，没有新增光束系统。共享任务单和实际运行反馈分别记录。
