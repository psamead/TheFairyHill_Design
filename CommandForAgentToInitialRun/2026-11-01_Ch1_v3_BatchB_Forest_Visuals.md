# Task: Revision v3 — Batch B (slim): Forest visuals (2026-11-01)

Shared folder = `Z:`. Batch B of 3. **Start only after the user confirms Batch A works.** Spec: `Z:\TechnicalArt\CH1_UNITY_REVISION_v3.md` §5–9 (read those sections only). Art and layout data are already in the project; your job is import settings, Forest builder code, rebuild the Forest scene, report.

## Rules
- First: `git add -A && git commit -m "Before Revision v3 batch B"` (includes the files Claude placed, listed below).
- Do NOT run automated tests or make a temp project copy. The user tests by hand.
- Change the **Forest only**: Forest builder code, Forest scene. Do NOT edit `ChapterSceneLoader`, `LevelBootstrap`, `SpawnPoint`, `Core_Persistent`, the Village scene, or the gate/HUD code from Batch A.
- Never delete or overwrite old PNGs; new files have new names.
- Keep Niamh capsule Size (0.23, 2.08) / Offset (0.08, 1.04).

## Files already placed by Claude
- `Assets/_Project/Art/Backgrounds/S1b_ForestPath/`: `S1b_ForestPath_L2_Undergrowth.png` (4800×1335), `S1b_ForestPath_L3b_GrassEdge_v3.png` (continuous grass edge — use this instead of the old `L3b_GrassEdge.png`), `S1b_ForestPath_L4_Fore_v2.png`
- `.../props/`: `F_prop_bramble_v3.png` (672×300), `F_prop_thornwall_v3_glow.png` (1079×900)
- `Assets/_Project/Data/Layouts/S1b_ForestPath_layout_v4.json` — includes a `layers` block (sprite / parallax / order / alpha). Last ground segment already extended to x 60 so the exit at 59.5 is reachable.

## One file you must copy (upload to the project failed on Claude's side)
- `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\props\F_prop_thornwall_v3.png` (1079×900) → `Assets/_Project/Art/Backgrounds/S1b_ForestPath/props/`

## Steps
1. Import all of the above as Sprite, PPU 100, no compression. Layer PNGs: pivot `(0, 270/height)` like the existing forest layers.
2. `Chapter1SceneBuilder.cs`: `ForestLayoutPath` → `S1b_ForestPath_layout_v4.json`. Read the new fields (`kind`, `solid`, `sorting_order`, `collider_x`, `collider_w`, `glow`, `hint_trigger_x`, `layers`).
3. Layers: add L2 undergrowth (parallax 0.65, order -20); swap grass edge to `_v3`; L4 → `L4_Fore_v2` with alpha **1.0**, parallax 1.15.
4. Bramble: decoration, no collider, order 12 (in front of Niamh). Cross order 11.
5. Thorn wall: sprite at x 49.2, 10.79×9u; collider x 52.2–58.8, 9u high. Glow overlay: same rect, Additive, `#B0202A`, alpha breathes 0.35–0.7 (~2.5 s) + random flash every 3–6 s; URP 2D Point Light same colour, radius ~6u, intensity follows the glow. On IronPulse: glow + light off in 0.3 s, then smoke, wall fades out over 0.6 s.
6. Smoke (§9): `M_FX_SoftParticle`; burst 80 then 40/s for 1.2 s; box 6.6×9u over the wall; size 1.0–2.5u growing ×1.5; up 1.5–3 u/s + noise 0.5–1; colour `#1A0E22` → transparent; 10–15% small additive dark-red embers (sub-emitter); life 1.5–2.5 s.
7. Stars (§7): nothing before Niamh passes x 44.6. Then scattered stars 0.4–0.7u, 4–6/s within 1.2u of the cross; a main star ~0.8u at the cross centre blinking every 0.25–0.35 s (warm gold, Additive) until pickup.
8. Exit at x 59.5; LevelInfo bounds 60u. Forest end still returns to the menu as before.
9. Rebuild and **save** the Forest scene. Confirm with `git diff --stat` that the `.unity` file changed.

## Report
Changed files (git diff --stat). Ask the user to reopen Unity and check: parallax comfort, stars after the big gap, bramble in front / cross behind, red glow, Q → smoke → wall gone → exit reachable. Add a dated "Revision v3 — Batch B" section to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` and a line in §9 of `Z:\ART_HANDOFF.md`.
