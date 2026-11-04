# Task: Revision v3 — Batch A: thin UI frames (Core), Village gate (2026-11-01)

The shared folder is mapped as `Z:`. Read `Z:\TechnicalArt\UNITY_AGENT_RULES.md` §1 (environment rules) and the sections of `Z:\TechnicalArt\CH1_UNITY_REVISION_v3.md` listed below. This is batch A of 3 for Revision v3.

**Last attempt (all 10 changes at once) was rolled back by the user.** Symptoms: (1) the top-left controls hint still showed the old stretched Celtic bar — `Core_Persistent` was never updated; (2) after the change the player could no longer go from the Village into the Forest. Avoid both. Do not change anything outside this batch.

Rules for this batch:
- Before editing, commit the current working tree (`git add -A && git commit -m "Before Revision v3 batch A"`) so this batch can be rolled back alone.
- Do NOT run automated tests (the user will test by hand). Do not create a temporary project copy.
- Keep the user-tuned values: Niamh capsule Size (0.23, 2.08) / Offset (0.08, 1.04); tall wall and hay bale overrides in the layout data.
- If the Unity Editor is open, save nothing from memory over your file edits; when done, tell the user to close and reopen the project (or reload the scenes) before testing.

Sections: **1 + 3** (thin prompt frames) and **2 + 4** (gate), plus the missing-script cleanup row.

1. Copy (copy only): `Z:\TechArtAsset\UI\HUD\UI_frame_thin.png`, `UI_panel_dark.png`; `Z:\TechArtAsset\Backgrounds\S1_Village\props\S1_prop_gate.png` (closed) and `S1_prop_gate_open.png` (open).
2. In **`Core_Persistent`** (where the HUD lives): replace the stretched Celtic bar with dark panel + thin frame around the controls hint text itself, top-left. Same style for "Press E to …" prompts. Keep the Celtic frame only on the MainMenu Settings popup.
3. Village gate: two complete sprites swapped (closed / open), whole gate behind Niamh, blocker x 24.9–28.1, 8u high; E opens, leaving the range closes. Remove the v2 three-piece gate objects.
4. Remove components with missing scripts in all scenes.
5. Must still work: MainMenu → Start → Village → walk to the right exit → **Forest loads** → forest end returns to menu.
6. Report: what changed, file list, and ask the user to check: hint readable top-left, gate open/close, Village → Forest transition. Add a dated "Revision v3 — Batch A" section to `Z:\TechnicalArt\CH1_UNITY_PROGRESS.md` and a line in §9 of `Z:\ART_HANDOFF.md`.
