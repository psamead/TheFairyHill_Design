# Task: Revision v3 — Batch B: Forest visuals (2026-11-01)

The shared folder is mapped as `Z:`. Read `Z:\TechnicalArt\UNITY_AGENT_RULES.md` §1 (environment rules) and the sections of `Z:\TechnicalArt\CH1_UNITY_REVISION_v3.md` listed below. This is batch B of 3 for Revision v3.

**Last attempt (all 10 changes at once) was rolled back by the user.** Symptoms: (1) the top-left controls hint still showed the old stretched Celtic bar — `Core_Persistent` was never updated; (2) after the change the player could no longer go from the Village into the Forest. Avoid both. Do not change anything outside this batch.

Rules for this batch:
- Before editing, commit the current working tree (`git add -A && git commit -m "Before Revision v3 batch B"`) so this batch can be rolled back alone.
- Do NOT run automated tests (the user will test by hand). Do not create a temporary project copy.
- Keep the user-tuned values: Niamh capsule Size (0.23, 2.08) / Offset (0.08, 1.04); tall wall and hay bale overrides in the layout data.
- If the Unity Editor is open, save nothing from memory over your file edits; when done, tell the user to close and reopen the project (or reload the scenes) before testing.

Start only after the user confirms Batch A works. Sections: **5, 6, 7, 8, 9**. Change the Forest scene only (plus its layout data and builder code for the Forest); do not touch the scene loader, Core, or Village.

1. Copy (copy only): `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\_work\S1b_ForestPath_L2_Undergrowth.png`, `S1b_ForestPath_L3b_GrassEdge.png` (regenerated, replace), `S1b_ForestPath_L4_Fore_v2.png`; `props\F_prop_bramble_v3.png`, `F_prop_thornwall_v3.png`, `F_prop_thornwall_v3_glow.png`; `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\S1b_ForestPath_layout_v4.json`.
2. Apply sections 5–9 exactly (undergrowth 0.65 / order -20; grass edge continuous; L4_Fore_v2 alpha 1 / 1.15; bramble 3u in front of Niamh; thorn wall 9u with collider x 52.2–58.8, red glow + 2D point light; smoke burst; sparkles start after x 44.6 with a pulsing main star).
3. Keep the Forest exit working. If you move the exit to x 59.5, also update LevelInfo bounds to 60u.
4. Report as in Batch A; user checks: parallax comfort, stars, bramble/cross, glow, Q → smoke → wall gone → exit reachable.
