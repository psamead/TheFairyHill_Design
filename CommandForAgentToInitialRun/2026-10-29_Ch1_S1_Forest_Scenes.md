# Task: Build playable Unity scenes for Chapter 1 — S1 Village and Forest Path (2026-10-29)

The shared folder is mapped as `Z:` on your computer. If your drive letter is different, use yours. This is also a classroom demo, so keep scripts small, readable and commented.

1. Read section 0 of `Z:\TechnicalArt\MENU_UNITY_HANDOFF.md` (environment rules), then all of `Z:\TechnicalArt\CH1_UNITY_HANDOFF.md` (this task), then sections 1–3 of `Z:\TechnicalArt\SCENE_SCALE_SPEC.md` (units and jump tuning).
2. Copy the art into the Unity project (copy only, do not move or edit the originals in `Z:`):
   - `Z:\TechArtAsset\Backgrounds\S1_Village\_work\S1_Village_L0…L4_*_wip.png` and `Z:\TechArtAsset\Backgrounds\S1_Village\props\S1_prop_wall_low.png`, `S1_prop_hay.png`, `S1_prop_wall_tall.png`, `S1_prop_gate.png` → `Assets/_Project/Art/Backgrounds/S1_Village/`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\_work\S1b_ForestPath_L0_Sky_wip.png`, `L1_Far_wip.png`, `L3_Walk_ditch_v2.png`, `L4_Fore_wip.png` and `props\F_prop_bramble.png`, `F_prop_cross.png`, `F_prop_thornwall.png` → `Assets/_Project/Art/Backgrounds/S1b_ForestPath/`
   - `Z:\TechArtAsset\Characters\Niamh\Niamh_side_static_v3.png` → `Assets/_Project/Art/Characters/Niamh/`
   - Layout data: `S1_Village_layout_v2.json`, `S1b_ForestPath_layout_v2.json` → `Assets/_Project/Data/Layouts/`
   - Do not copy `*_src.png`, `_ditch_fix`, `.mp4` previews or anything in `deprecated`.
3. Import settings and layer setup exactly as in `CH1_UNITY_HANDOFF.md` §1–2 (PPU 100, custom pivot `(0, 270/height)`, Max Size 8192, parallax factors, sorting orders).
4. Follow the build order in `CH1_UNITY_HANDOFF.md` §3: graybox colliders from the layout JSON → PlayerController with the tuning values → parallax layers → props and interactions (gate, iron cross pickup, thorn wall removed by IronPulse) → SceneLoader (MainMenu Start → S1 → Forest → back to menu or "to be continued").
5. Use placeholders for anything listed in §4 "暂时不做" (no skeletal animation, simple fade for the thorn wall).
6. When done:
   - Write progress to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` (new file): project paths, script names, final tuning values, what was checked in Play Mode, open problems.
   - In `Z:\ART_HANDOFF.md`, add a dated entry in section 9. Edit the current file on disk; do not overwrite other people's changes.
   - Tell the user what you verified in Play Mode (can Niamh clear the 1.2u wall, the 1.4u ditch by walking, the 2.6u ditch only by running; is the 3u thorn wall impassable before the pulse).
