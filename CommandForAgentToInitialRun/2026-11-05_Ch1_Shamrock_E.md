# Task: Shamrock light collectibles — E (2026-11-05)

Run **after** "v3 fix D" is done. Shared folder = `Z:`. Spec: `Z:\TechnicalArt\CH1_UNITY_REVISION_v3_fix.md` section **E** only. Rules as before: `git commit -m "Before shamrock E"` first, no automated tests, keep all earlier fixes (no Point Lights for shamrocks — D2).

1. Copy `Z:\TechArtAsset\FX\Shamrock\` (`FX_shamrock_128.png`, `FX_shamrock_256.png`, `FX_shamrock_glow.png`) to `Assets/_Project/Art/FX/Shamrock/`. Sprite, PPU 100, centre pivot, no compression.
2. New `ShamrockLight` prefab/component built by the builder: icon 0.35u (order 11) + additive glow 1.0u behind it (order 10, colour via `_BaseColor` `#CFF0A0`, alpha breathing 0.6–0.85). Float ±0.08u ~2 s, sway ±8°, random phase. Trigger collider radius 0.3u.
3. Place one at every `lights` coordinate in the Village and Forest layouts.
4. On Niamh touch: fly to Niamh chest (local 0, 1.2) and shrink over 0.25 s, burst 12 green additive `FX_soft_dot` particles (0.06–0.12u, 1–2 u/s, life 0.4 s, xyz velocity curves same mode), then destroy; `GameState` shamrock count +1 (persist across the scene change). No sound yet. Existence +1 per 10 is NOT part of this task.
5. Rebuild + save Village and Forest; Core only if `GameState` needs a new field.

Report changed files; ask the user to check: shamrocks float along the jump arcs in both scenes, glow without lighting the background, collect with fly-in + sparkle, count persists Village → Forest. Add a dated "Shamrock E" section to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md`.
