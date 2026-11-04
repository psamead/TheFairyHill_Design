# Task: Revision v3 — Batch A (slim): thin HUD frames + two-state Village gate (2026-11-01)

Shared folder = `Z:`. Batch A of 3. **All art and layout data are already in the project** (copies also in `Z:\TechnicalArt\unity_drop\v3_batchA\`). Your job is only: import settings, small C# changes, rebuild, report. Do not redesign, retune numbers, or touch anything not listed.

Last attempt was rolled back: (1) `Core_Persistent` was never rebuilt so the old green Celtic bar stayed; (2) Village → Forest stopped loading. Avoid both.

## Rules
- First: `git add -A && git commit -m "Before Revision v3 batch A"` (current tree includes the user's Niamh capsule — keep it: Size (0.23, 2.08) / Offset (0.08, 1.04)).
- Do NOT run automated tests or make a temp project copy. The user tests by hand.
- Do NOT edit `ChapterSceneLoader`, `LevelBootstrap`, `SpawnPoint`, the exit trigger, or the Forest scene.
- Copy only; never delete or overwrite the old gate PNGs (the three-piece files stay on disk, just unused).

## Steps
1. **Files are already in the project** (placed by Claude, not yet committed — include them in your "Before" commit): `Assets/_Project/Art/UI/HUD/UI_frame_thin.png`, `UI_panel_dark.png`; `Assets/_Project/Art/Backgrounds/S1_Village/props/S1_prop_gate_closed_v3.png`, `S1_prop_gate_open_v3.png`; `Assets/_Project/Data/Layouts/S1_Village_layout_v3.json`. Do not copy again. Set import: Sprite, PPU 100, no compression. `UI_frame_thin` / `UI_panel_dark` (96×96): 9-slice border 24 px all sides. Also delete the stray test file `_claude_write_test.txt` in the project root.
2. **Builder layout path**: in `Chapter1SceneBuilder.cs` change `VillageLayoutPath` to `S1_Village_layout_v3.json`.
3. **Gate data fields**: add to `Chapter1InteractData`: `sprite_open, image_x, image_w, image_h, sorting_order, blocker_x0, blocker_x1, blocker_h, range_x0, range_x1`.
4. **`CreateVillageGate`**: replace the three-part version. One SpriteRenderer (closed sprite) at x = `image_x` (left edge), bottom on y 0, scaled to `image_w × image_h`, sorting order `sorting_order` (behind Niamh). BoxCollider2D blocker covering `blocker_x0..x1`, height `blocker_h`. Trigger range covering `range_x0..range_x1`, height 8. `VillageGate`: E in range → sprite = open, blocker disabled; leaving range → sprite = closed, blocker enabled. Adapt `VillageGate.Configure` to take (renderer, closedSprite, openSprite, blocker).
5. **HUD in `Core_Persistent`**: controls hint top-left = `UI_panel_dark` (sliced, alpha ~0.6) behind the text + `UI_frame_thin` (sliced) around it, sized to the text with ~12 px padding. "Press E to …" prompt uses the same two images. Remove the stretched Celtic bar object from the HUD. Celtic frame stays only on the MainMenu Settings popup.
6. **Missing scripts**: remove components with missing scripts (`GameObjectUtility.RemoveMonoBehavioursWithMissingScript`) in Core_Persistent, S1_Village, S1b_ForestPath, MainMenu.
7. **Rebuild and SAVE both** `S1_Village` and `Core_Persistent` (open each scene, apply, `EditorSceneManager.SaveScene`). Confirm in your report that the `.unity` files changed on disk (git diff --stat).
8. **Don't break**: Build Settings scene list unchanged; exit trigger at x 37.8 still loads the Forest.

## Report
List changed files (git diff --stat), then ask the user to reopen Unity and check in Play Mode: (a) top-left hint has the thin frame and dark panel, no green bar; (b) the gate opens with E and closes when leaving; (c) walking to the right exit loads the Forest. Add a dated "Revision v3 — Batch A" section to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` and one line in §9 of `Z:\ART_HANDOFF.md`.
