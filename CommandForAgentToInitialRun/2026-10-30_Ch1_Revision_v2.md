# Task: Chapter 1 revision v2 — persistent Core scene, gate split, parallax comfort, forest props (2026-10-30)

The shared folder is mapped as `Z:`. Same environment rules as before (`Z:\TechnicalArt\MENU_UNITY_HANDOFF.md` §0): copy art into the project, never edit or move files in `Z:`. Keep scripts small, readable and commented — this is a classroom demo.

1. Read `Z:\TechnicalArt\CH1_UNITY_REVISION_v2.md` in full. It lists 7 changes, the reason for each, and the exact files, positions, sorting orders and parallax values. Your own v1 notes are in `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md`.
2. Before rebuilding anything, read section 7b: the user hand-tuned the `StoneWall_Tall_1.8u` collider. Move that override into data (layout JSON fields or a builder override table) so a rebuild keeps it. Then do the architecture change (section 7): create `Core_Persistent` (Niamh, camera + follow, the only AudioListener, HUD/UI canvas + EventSystem, `GameState` singleton, `SceneLoader`); make the two chapter scenes additive level scenes with `SpawnPoint` and `LevelInfo`; add `LevelBootstrap` so a level scene opened alone in the Editor still runs. Remove the per-scene Niamh/camera/listener/EventSystem from the level scenes. MainMenu Start → load Core + `Ch1_S1_Village`.
3. Copy the new art (copy only):
   - `Z:\TechArtAsset\Backgrounds\S1_Village\props\S1_prop_gate_post_L.png`, `S1_prop_gate_boards.png`, `S1_prop_gate_post_R.png`
   - `Z:\TechArtAsset\Backgrounds\S1_Village\_work\S1_Village_L4_Fore_v2.png`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\_work\S1b_ForestPath_L3b_GrassEdge.png`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\props\F_prop_bramble_v2.png`, `F_prop_cross_v2.png`, `F_prop_thornwall_v2.png`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\S1b_ForestPath_layout_v3.json`
   - `Z:\TechArtAsset\FX\FX_sparkle_star.png`, `FX_soft_dot.png`
   - `Z:\TechArtAsset\UI\Frame\UI_frame_celtic.png` (transparent, main) and `UI_frame_celtic_stone.png` (with stone fill). Set them up exactly as in section 2 (210 px borders, Image Type = Tiled).
4. Apply sections 1–6 of the revision document (gate split + tall invisible wall that opens on E by hiding the boards and closes again when Niamh leaves the gate trigger area; UI frame or placeholder; enlarged forest props from layout v3 and the iron-cross sparkle/reveal; URP particle material `M_FX_SoftParticle` to fix the pink smoke; forest L4 alpha 0.55 / factor 1.15; S1 L4 v2; forest grass-edge layer at factor 1.0, order -9). Keep the v1 jump checks passing. Layout blocks may now carry `collider_x` / `collider_w` (and the tall wall override from 7b): when present, use them for the collider instead of the sprite bounds.
5. When done:
   - Update `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` with a new dated "Revision v2" section: what changed, new script names, the scene list and load flow, what you checked in Play Mode, and anything not done.
   - Add a dated entry in section 9 of `Z:\ART_HANDOFF.md`. Edit the current file on disk; do not overwrite other people's changes.
   - Tell the user what you verified in Play Mode, using the checklist in section 8 of the revision document.
