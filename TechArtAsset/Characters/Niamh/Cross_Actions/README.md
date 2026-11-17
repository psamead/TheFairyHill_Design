# 妮芙十字架双动作

**2026-11-18 Unity当前试装：** 举高原画已接到原受控红墙Q事件，B直接举高，覆盖原1.9秒墙体反馈后恢复v8，无胸前中间停留；没有新增大光束。350像素新图沿用基础327像素角色的163.5px脚底原点。源码/资源已放实际工程，离线C#检查通过；Editor导入与Play Mode待验。任务单留共享设计目录 `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`。下文更早的“未接入”是历史记录。

2026-11-17。当前采用两个用户绘制的动作，不再制作第三个动作。以下是静态姿势与使用原则；连续动画、光束特效及 Unity 接入另行验收。

**前襟花纹同步：** 用户第二稿新增的金色花纹补片已加入胸前稿 `front_ornament_shared_from_raised_v1` 图层，同时同步基础 Motion_v8 身体和静态备用图；只改变前襟局部，人物轮廓 alpha 不变。当前胸前稿比最初用户胸前源稿多这一处经授权的衣装修订，下文「与源稿像素一致」指最初命名、分组与画幅整理时的校验。此次修订与 Unity 贴图复制记录见 `../Motion_v8/appearance_front_ornament_v1/sync_manifest.json`；Unity 编辑器导入和 Play Mode 外观未验证。

## 第二动作采用 B 直接举高（2026-11-18）

**当前采用：[B 直接举高](previews/raised_fast_v3/Niamh_raised_fast_direct_v3.gif)，idle 300ms → 举高1080ms → idle 620ms，共2秒，无胸前中间停留。** 用户要求全部版本保留作为发展记录。本轮新增两张 2 秒循环（上一版为 4.5 秒），不覆盖旧 GIF：

- [A 快速经过胸前再举高](previews/raised_fast_v3/Niamh_raised_fast_via_chest_v3.gif)：起手 idle 300ms，胸前仅 80ms，举高 1000ms，回落经过胸前 60ms，idle 560ms。
- [B 直接举高](previews/raised_fast_v3/Niamh_raised_fast_direct_v3.gif)：idle 300ms，直接举高 1080ms，idle 620ms。

两者均用用户原画关键姿势切换，不额外生成变形中间图，不含光线或游戏逻辑。旧版本内容校验未变，散列及精确时序见本轮 `preview_spec.json`；负责人已选择 B 直接举高，作为当前采用的起手方式与预览节奏；A 和所有旧版继续保留作发展记录。这是离线预览选择，不等于光线特效或 Unity 动作验收。

## 上一轮关键姿势预览（保留）

- [01 idle 直接切换为双手胸前抱持](previews/chest_review_v2/Niamh_idle_to_chest_direct_v2.gif)，3 秒。中间网格试做有袖口变形，按用户备选方案提供原稿直接切换版。
- [02 idle → 用户绘制的胸前抱持 → 举高](previews/raised_via_chest_v2/Niamh_idle_chest_raised_keyposes_v2.gif)，4.5 秒。用户明确允许继续第二种，要求把之前两个变形中间姿势换成已有的胸前抱持原稿。

这两张是原画关键姿势和节奏预览，暂用直接切换，没有平滑的中间肘腕动画或光线特效。只需现有两张用户动作图；第一张同时作为第二种举法的中间关键帧，不新增第三个独立绘制动作。两张原持势 GIF、早期网格试做及源 PSD 全部保留。当前脚本分别为 `tools/render_chest_direct_review.py`、`tools/render_raised_via_chest_review.py`。

## 历史网格过渡试做（保留，非当前推荐）

- [01 idle → 屈臂捧到胸前 → 保持 → 回落](previews/idle_to_actions_v1/Niamh_idle_to_chest_local_v1.gif)，4 秒。
- [02 idle → 抬臂举到额前 → 保持 → 回落](previews/idle_to_actions_v1/Niamh_idle_to_raised_story_v1.gif)，4.5 秒。

两版从同一个放下手的 idle 开始，采用不同的肘腕路径，终点保持用户当前 PSD 的原画，脚底不动。预览增加运动留白，源 PSD 的 350×699 画幅未改。中间帧由两段手臂网格与服装补画插值形成，手型有短暂的对齐混合，属于离线粗动作研究，尚非生产骨骼动画；未加光线特效或接入 Unity。脚本 `tools/render_idle_to_actions.py`，源稿 SHA256、时序及验证见对应 `preview_spec.json`。

## 原独立持势 GIF（保留）

- [01 胸前局部使用](previews/hold_loops_v1/Niamh_cross_chest_local_hold_v1.gif)
- [02 举起剧情释放](previews/hold_loops_v1/Niamh_cross_raised_story_hold_v1.gif)

两张均从当前 PSD 导出，包含最新前襟花纹；各 3 秒、20 fps，为连续微呼吸和轻摆的独立持势循环，脚底固定。未制作起手/收手、攻击判定、光束特效或 Unity 动作接入，不能把持势循环当成完整技能动画。源文件 SHA256 和时序见同目录 `preview_spec.json`，脚本为 `tools/render_separate_hold_gifs.py`。

## 当前静帧

| 动作 | PSD 和同名透明 PNG | 使用范围 |
| --- | --- | --- |
| 01 胸前局部使用 `cross_chest_local` | [Niamh_cross_chest_local_v1.psd](current/Niamh_cross_chest_local_v1.psd) | 关卡内对付小怪、小障碍物及小剧情互动。具体战斗规则与数值另行设计。 |
| 02 举起剧情释放 `cross_raised_story` | [Niamh_cross_raised_story_v1.psd](current/Niamh_cross_raised_story_v1.psd) | 剧情触发的大光线、湮灭大型障碍物等关键事件。大光线属于后续特效设计，当前 PSD 未包含该特效。 |

统一画布 **350×699**，左上原点不变，人物未缩放或平移。第一稿从 327 扩至 350，新增右侧透明区；第二稿从 450 裁至 350，右侧被裁区域全透明，原可见范围最大 x 为 337（右开区间）。两稿与用户源图在同画布下 RGBA 像素一致。静帧不代表已经有骨骼、平滑过渡或游戏内效果。

## 图层与文件夹

- `current/`：仅放两个当前动作的命名整理 PSD 和透明 PNG。PSD 的 `01_..._current` 是当前动作与用户修补层，`02_CHARACTER_base` 是原人物，`90_REFERENCES_BACKUPS_hidden` 是隐藏参考及旧部件。第二稿原有手绘组保留为嵌套组，不合并绘画层。
- `sources/user/`：保留用户原始 PSD 内容，只按动作语义重命名；包括胸前稿、第二个举起稿及较早衔接稿。原尺寸保留。
- `archive/psd_trials/`：旧准备稿、命名稿、蒙版试验及其旧导出和校验。历史，不作当前编辑入口。
- `archive/Cross_Raise_Preview_v1/`：较早粗 GIF 和脚本，早于用户第二个动作，未采用最新两姿势；禁止作为当前动作或大光线效果的验收依据。
- `evidence/`：整理时的源稿渲染，仅供校验。路径与 SHA256、画幅裁切和像素验证记录在 `file_manifest.json`。
- 较早失败概念图保留在邻接目录 `../Interaction_Study_2026-11-16/`；完整 MJ 原图仍在 `MJ_ref/Characters/Niamh/Interaction_Study_2026-11-17/`。它们属于参考或历史类别，不与当前 PSD 混放。

## 规则和交接

Agent 主规则见 `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md` 的双动作使用原则，机器可读数据见 `action_usage_rules.json`；人读说明为 `TechnicalArt/妮芙十字架双动作使用规则与制作交接_v1.docx`。制作经验见 `TechnicalArt/LESSONS_CHARACTER_ANIMATION.md`。以上以 ShareWorkFolder 为根。

当前完成图层、画幅、命名、归类和使用原则整理。下一步按负责人安排，不补画第三个动作，不因本使用范围自动新增 Demo 战斗系统或改动 Unity。白边此前仅做去边试验，未确认完全清除。
