# Chapter 1 Unity Progress — S1 Village and Forest Path

Date: 2026-10-30
Project: `C:\Users\Administrator\Documents\UnityProject\TheFairyHill2D`
Shared design source: `TechnicalArt/CH1_UNITY_HANDOFF.md`, `CommandForAgentToInitialRun/2026-10-29_Ch1_S1_Forest_Scenes.md`, and `TechnicalArt/SCENE_SCALE_SPEC.md`.

## Delivered

- Created `Assets/Scenes/Ch1_S1_Village.unity` and `Assets/Scenes/Ch1_S1b_ForestPath.unity`.
- MainMenu Start now loads `Ch1_S1_Village`; the village exit loads the forest; the forest endpoint shows a prompt and returns to MainMenu on E. All three routes were exercised in Play Mode.
- Added the 19 requested art/layout files by copy only. No source files, `_src`, `_ditch_fix`, previews, or `deprecated` material were copied or edited.
- Implemented JSON-driven ground and pit colliders, static Niamh, keyboard movement/jump, horizontal camera follow, parallax, village props/gate, Iron Cross pickup, thornwall and a smoke/fade IronPulse placeholder.
- Added both chapter scenes to Build Settings. SampleScene was present at initial delivery, then deleted by the user on 2026-10-30 and removed from Build Settings.

## Manual collision update — 2026-10-30

- The user manually refined the StoneWall_Tall_1.8u BoxCollider2D in Ch1_S1_Village. Its saved values are Offset (2.0378294, 0.9), Size (3.1901226, 1.8), with the GameObject at (16.8, 0, 0). This gives world bounds approximately X 17.2428–20.4329, Y 0–1.8; the collider is narrower than the 4.19u sprite to follow the visible wall shape.
- The scene asset on disk contains these values. The scene builder still creates a full-width collider from the layout block dimensions, so rebuilding Chapter 1 scenes will replace this manual override. Preserve/reapply these values or encode an explicit collider override in the builder before rebuilding.

## SampleScene removal — 2026-10-30

- The user deleted Assets/Scenes/SampleScene.unity. No runtime script directly references it. Its stale Build Settings entry was removed, and the project default scene now points to MainMenu.
- Both scene builders now skip Build Settings entries whose scene assets no longer exist, so rebuilding will not re-add a stale deleted-scene path.
## Scene and input settings

- PPU 100; background pivot `(0, 270 / source height)`; props bottom-left; Niamh bottom-center; Max Size 8192; compressed at quality 100.
- Camera orthographic size 5.4, fixed Y 2.7, horizontal follow; scene ground y=0.
- Walk 3.2 u/s, run 5.6 u/s, jump velocity 12, rising/falling gravity 30/45, coyote 0.10s, jump buffer 0.12s. Controls: A/D or arrows, Shift run, Space jump, E interact, Q IronPulse.
- Unity 6000.3.24f1 project did not have Cinemachine in `Packages/manifest.json`; used the small `ChapterCameraFollow` component to provide the documented fixed-Y horizontal camera behavior. No package was installed.
- TextMesh Pro dynamic font assets gained the left/right arrow glyphs and slash needed by the controls label; keep these imported glyph updates.
- Unity 6 requires custom sprite alignment/pivot to be applied through `TextureImporterSettings`; assigning `spritePivot` alone left sprites centered. The importer now sets Custom alignment and the requested pivot through importer settings. Nested ground coordinate arrays are parsed explicitly because Unity `JsonUtility` does not deserialize the raw jagged-array layout as expected.

## Play Mode checks

- 1.2u village wall: jump reached and landed on the top (x=12.33, y=1.20).
- 1.4u forest gap: walk-jump crossed (x=33.00, y=0.01).
- 2.6u forest gap: walk-jump did not clear and reached the pit floor; running jump crossed (x=48.68, y=0.00).
- 3u thornwall: blocked walking before IronPulse (player stopped at x=51.85).
- Iron Cross pickup succeeded; Q activated IronPulse, the wall faded and its collider disabled.
- MainMenu Start button callback loaded S1; the S1 exit loaded the forest; forest endpoint E returned to MainMenu.
- MainMenu, village, and forest each contain exactly one AudioListener. The chapter scenes each contain one player Rigidbody2D.

## Remaining design / production work

- Niamh uses the static image until the planned skeletal animation is ready.
- IronPulse uses a simple fade and dark particle smoke; final cold-light ring and thornwall crack treatment remain art/VFX work.
- The forest endpoint returns to MainMenu as the allowed temporary substitute while S2 is unavailable.
- No backpack/inventory UI was added; Iron Cross possession is held as a player state for this playable slice.
- The layout `lights` points and optional URP lighting/post-processing polish are not implemented yet.
- Build Settings and scene routing were checked in the Editor; no standalone PC player build was produced. MainMenu button callback was invoked directly during Play Mode, not tested with a physical mouse click.

## Code map

- Builder: `Assets/Editor/Chapter1/Chapter1SceneBuilder.cs` (Tools → The Fairy Hills → Build Chapter 1 Scenes)
- Gameplay: `Assets/_Project/Scripts/Gameplay/PlayerController2D.cs`, `PlayerInteractionTarget.cs`, `VillageGate.cs`, `IronCrossPickup.cs`, `ThornWall.cs`, `ChapterCameraFollow.cs`, `ParallaxLayer.cs`, `ChapterHUD.cs`, `ChapterSceneLoader.cs`, `ChapterSceneExit.cs`
- MainMenu destination: `Assets/_Project/Scripts/UI/MainMenu/MainMenuController.cs` and `Assets/Scenes/MainMenu.unity`

## Revision v2 implementation — 2026-10-30

Codex implemented the requested changes from `TechnicalArt/CH1_UNITY_REVISION_v2.md` and `CommandForAgentToInitialRun/2026-10-30_Ch1_Revision_v2.md` in `C:\Users\Administrator\Documents\UnityProject\TheFairyHill2D`.

- Added `Core_Persistent` for the sole player, camera/AudioListener, HUD/EventSystem, `GameState`, and scene loader. Village and Forest are level-only scenes with `LevelInfo`, spawn points, and standalone `LevelBootstrap`; SampleScene is removed from Build Settings.
- MainMenu Start now enters the selected first chapter scene; the level bootstrap adds Core and connects it to the already loaded chapter. Unity MCP Play Mode did not advance runtime frames (`Time.time` stayed 0), so completion of this bootstrap has not been visually confirmed in a normally advancing session.
- Split the Village gate render layers and added a reversible blocker that opens on interaction and closes when the player leaves the range.
- Applied the Celtic frame to Settings UI; added v2 foreground/prop art, forest grass edge, Iron Cross approach reveal and sparkle, and URP soft/additive particle materials.
- Applied Forest L4 alpha 0.55 / parallax 1.15, S1 L4 v2, and Forest L3b parallax 1.0 / sorting order -9.
- Stored manual collider overrides in layout data and kept the builder data-driven: tall wall Offset (2.0378294, 0.9), Size (3.1901226, 1.8); hay bale Offset (-0.15596342, 0.42), Size (1.3790255, 0.84).
- Unity scene generation and MCP script compilation succeeded; no compile errors were reported. Scene structure/collider values were inspected. A manual runtime scene query showed one Core player, one AudioListener, and one EventSystem. Full gameplay Play Mode acceptance remains pending because the connected MCP session did not advance frames. No player build, commit, or push was made.

Design/production follow-up: user visual comfort review of foreground/parallax; verify gate open/close, cross reveal/pickup and persistence, thornwall removal, and scene transitions in a normally advancing Play Mode; continue Niamh skeletal animation, final IronPulse VFX, and backpack/inventory UI.
## Hay bale sprite alignment — 2026-10-30

- The `HayBale_0.9u/Visual` child is offset left by 1.0 unit while the root remains at `(15, 0, 0)`. The BoxCollider2D stays at Offset `(-0.15596342, 0.42)`, Size `(1.3790255, 0.84)`. Current Unity bounds place the sprite center at `(14.86, 0.45)` and collider center at `(14.84, 0.42)`, aligned within 0.02 units horizontally.
- Added `visual_offset_x/y` to the Chapter 1 builder data and set the hay layout entry to `(-1.0, 0.0)`. Rebuilding the Village now keeps the visual adjustment and existing collider dimensions/offset; other blocks retain zero visual offset.
- No gameplay controller changes were needed. This was a focused data/builder/doc update; no scene rebuild or runtime test was performed.
## Niamh collision update — 2026-11-01

- The saved `Core_Persistent.unity` player uses a vertical CapsuleCollider2D with Offset `(0.08, 1.04)`, Size `(0.23, 2.08)`, and Is Trigger off. Niamh remains at `(3.5, 0, 0)`; the Rigidbody2D is Dynamic with Gravity Scale 0. The capsule bottom aligns with ground y=0.
- `Chapter1SceneBuilder.CreatePlayer` now creates this same capsule, preserving the user adjustment when Core is rebuilt. No gameplay-controller change was needed.
- Confirmed the serialized scene values on disk. No scene rebuild or Play Mode validation was run.

## Revision v3 rollback — 2026-11-01

- After the Revision v3 implementation attempt, the user reported a problem and requested a return to the pre-task project state. The v3-only scene, asset, script, test, and project-setting changes were rolled back; the earlier Niamh collider update and other pre-existing project changes were preserved.
- The problem's specific symptom and reproduction steps were not provided, so its cause was not diagnosed. Revision v3 implementation changes were not published to GitHub; the published update is the Niamh collision progress note only.

## Revision v3 — Batch A: Village UI (2026-11-01)

- Imported the two v3 gate sprites and HUD sprites as single sprites at 100 PPU with uncompressed texture data. Set 24 px 9-slice borders on the two 96×96 HUD sprites.
- Updated the builder to read `S1_Village_layout_v3.json`, create one closed/open gate sprite with JSON-driven blocker/range, and create fitted dark-backed thin-frame HUD panels. The controls hint and interaction/message panels use 12 px padding; Core has no Celtic HUD frame. The MainMenu Settings frame remains unchanged.
- Rebuilt and saved only `Core_Persistent` and `Ch1_S1_Village`. Preserved Niamh's capsule (Size `(0.23, 2.08)`, Offset `(0.08, 1.04)`). Build Settings stayed at four scenes; the exit at x=37.8 still targets `Ch1_S1b_ForestPath`. Forest and MainMenu scene files were not changed.
- Missing-script scan found 0 components in Core, Village, Forest, and MainMenu. Unity Editor compilation and scene generation succeeded. The first build attempt exposed a duplicated `props/` path; it was corrected and the rebuild succeeded. No automated tests were run per the Batch A rule. Manual Play Mode checks remain pending for HUD appearance, gate open/close, and the Village-to-Forest transition.

## Revision v3 — Batch B: Forest visuals (2026-11-01)

- Imported Forest v4 layers and v3 props as single sprites at 100 PPU with uncompressed textures. The 1335 px layers use pivot `(0, 270/1335)`. Copied `F_prop_thornwall_v3.png` from the shared folder; earlier art files remain intact.
- Updated `Chapter1SceneBuilder` to read `S1b_ForestPath_layout_v4.json`. Forest layers now use L2 undergrowth at 0.65 / order -20, continuous L3b v3 at 1.0 / order -9, and L4 Fore v2 at alpha 1.0 / parallax 1.15. Bramble is decorative at order 12; the cross is order 11.
- Added post-gap cross stars (activated after x=44.6; scattered stars reduce on reveal while the main star remains until pickup). Added the additive B0202A thorn glow and radius-6 Point Light. IronPulse turns the light off over 0.3 s, emits the configured 80 + 40/s smoke with red ember sub-emitter, fades the wall over 0.6 s, then disables its blocker.
- Rebuilt and saved only `Ch1_S1b_ForestPath`. The exit remains at x=59.5 in a 60-unit level and returns to MainMenu. No automated tests were run per the Batch B rule. Unity compilation, builder execution, sprite import settings, and scene structure were inspected; Play Mode visual/gameplay checks remain for the user.

## User review of Batch A / B — 2026-11-01

- Batch A accepted except one change: only the gate's **right post** should render in front of Niamh (fix A1).
- Batch B issues: thorn-wall glow renders as grey-white haze (fix B1, material colour path); Forest starts black because the new red Point Light enables 2D lighting (fix B2, lighting plan).
- Spec: `TechnicalArt/CH1_UNITY_REVISION_v3_fix.md`. A1 + B1 sent to Codex (`CommandForAgentToInitialRun/2026-11-01_Ch1_v3_Fix_A1_B1.md`); B2 after A1/B1 are accepted; Batch C (audio) on hold.

## Revision v3 Fix A1/B1 — 2026-11-01

- A1: Added the supplied gate front-post art without overwriting the source PNG. The supplied 414×240 PNG contains both posts despite the spec describing only the right post, so the builder now derives a right-post-only Sprite asset from the right-hand 114 px of that image. It overlays the gate back at sorting order 11; the closed/open gate renderer remains at -5. Niamh is order 10, so 11 is used instead of the spec's order 5 to actually render in front. Gate collider, range, and open/close logic are unchanged.
- B1: ThornWall now applies `#B0202A` tint and pulse alpha through a `MaterialPropertyBlock` `_BaseColor`; the SpriteRenderer stays white. The additive material defaults to `#B0202A` at 0.5 alpha. Existing red point-light fading and Q → smoke → wall removal behavior are unchanged.
- Updated the builder with a focused A1/B1 rebuild command and saved targeted changes to the Village and Forest scenes. Niamh capsule and Village wall/hay-bale collider overrides were preserved. B2 lighting was not changed.
- Unity Editor source compilation and scene save completed. No automated tests were run, per task instructions. Play Mode appearance and interaction need the user's manual check.

## Village Gate Right Post Alignment — 2026-11-01

- Recorded the user's saved Scene-view placement for `Gate_PostR_Front` at local position `(0.99, 0, 0)` under `Village Gate` (world X `27.4`). The Inspector screenshot showed X `0.988`; Unity reports the serialized Transform as `0.99`.
- Updated `Chapter1SceneBuilder.CreateVillageGate` to use the same position so a Village rebuild will retain the alignment. Kept sorting order 11 and left the gate backing, collider, interaction range, and behavior unchanged.
- The Village scene was already saved at this position and was left untouched in this follow-up. No Play Mode/gameplay test was run.

## User review of fix A1/B1 — 2026-11-04

- A1 (gate right post in front) and B1 (thorn glow colour) accepted.
- New: IronPulse smoke invisible with 739 `Particle Velocity curves must all be in the same mode` errors (fix B3). A Global Light 2D placed under Niamh lights the whole Forest like daytime; replaced by the B2 dark-forest plan (Deepnest-style, revised 2026-11-04). Command: `CommandForAgentToInitialRun/2026-11-04_Ch1_v3_Fix_B2_B3.md`.
