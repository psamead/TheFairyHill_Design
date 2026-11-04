# Task: Chapter 1 revision v3 — thin UI frames, gate swap, forest comfort & drama, audio (2026-11-01)

The shared folder is mapped as `Z:`. First read `Z:\TechnicalArt\UNITY_AGENT_RULES.md` (environment rules + when to write automated tests); it replaces the old "§0" reference. Keep scripts small and commented — this is a classroom demo.

1. Read `Z:\TechnicalArt\CH1_UNITY_REVISION_v3.md` in full (9 changes + audio + missing-script cleanup). v2 rules still apply where v3 is silent. Keep the user's hand-tuned values (Niamh capsule, tall wall, hay bale) data-driven so a rebuild keeps them.
2. Copy the new files (copy only):
   - `Z:\TechArtAsset\UI\HUD\UI_frame_thin.png`, `UI_panel_dark.png`
   - `Z:\TechArtAsset\Backgrounds\S1_Village\props\S1_prop_gate.png` (closed) and `S1_prop_gate_open.png` (open)
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\_work\S1b_ForestPath_L2_Undergrowth.png`, `S1b_ForestPath_L3b_GrassEdge.png` (regenerated), `S1b_ForestPath_L4_Fore_v2.png`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\props\F_prop_bramble_v3.png`, `F_prop_thornwall_v3.png`, `F_prop_thornwall_v3_glow.png`
   - `Z:\TechArtAsset\Backgrounds\S1b_ForestPath\S1b_ForestPath_layout_v4.json`
   - `Z:\TechArtAsset\Audio\S1_VILLAGE_BGM_v1_loop.ogg`, `S1b_FOREST_BGM_v1_loop.ogg`, and everything in `Z:\TechArtAsset\Audio\SFX\` (`.ogg` only; never the `.wav` masters)
   - All files above are ready (2026-11-01). If any is missing on your side, use a placeholder and list it in your report.
3. Apply sections 1–10 of the revision document. Remove the v2 three-piece gate. Remove components with missing scripts so the Console has no "referenced script (Unknown)" warnings.
4. Testing (see `UNITY_AGENT_RULES.md` §2–3): turn on Run In Background. This task changes gameplay (gate blocker, iron-cross trigger, thorn wall, scene flow), so add PlayMode tests for at least: v1 jump checks (1.2u wall, 1.4u walk-jump, 2.6u run-jump only), gate closed blocks / opens on E / closes after leaving range, sparkles start only after crossing x 44.6, iron cross pickup persists across scenes, thorn wall collider off after IronPulse, one player / one AudioListener after scene changes. Run them from the command line and fix failures before reporting.
5. When done:
   - Add a dated "Revision v3" section to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` (changes, scripts, values, what you checked, what is not done).
   - Add a dated entry in section 9 of `Z:\ART_HANDOFF.md` (edit the current file on disk, keep other changes).
   - Tell the user what you verified in Play Mode, using the checklist at the end of the revision document. If Play Mode still does not advance frames through MCP, say so plainly and list what the user must check by hand.
