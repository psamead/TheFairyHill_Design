# Task: Revision v3 — Batch C: music and sound effects (2026-11-01)

The shared folder is mapped as `Z:`. Read `Z:\TechnicalArt\UNITY_AGENT_RULES.md` §1 (environment rules) and the sections of `Z:\TechnicalArt\CH1_UNITY_REVISION_v3.md` listed below. This is batch C of 3 for Revision v3.

**Last attempt (all 10 changes at once) was rolled back by the user.** Symptoms: (1) the top-left controls hint still showed the old stretched Celtic bar — `Core_Persistent` was never updated; (2) after the change the player could no longer go from the Village into the Forest. Avoid both. Do not change anything outside this batch.

Rules for this batch:
- Before editing, commit the current working tree (`git add -A && git commit -m "Before Revision v3 batch C"`) so this batch can be rolled back alone.
- Do NOT run automated tests (the user will test by hand). Do not create a temporary project copy.
- Keep the user-tuned values: Niamh capsule Size (0.23, 2.08) / Offset (0.08, 1.04); tall wall and hay bale overrides in the layout data.
- If the Unity Editor is open, save nothing from memory over your file edits; when done, tell the user to close and reopen the project (or reload the scenes) before testing.

Start only after the user confirms Batch B works. Section: **10**. Last time the Village → Forest transition broke in the same change set that added per-level music crossfades to the scene loader, so be careful here.

1. Copy (copy only, `.ogg` only): `Z:\TechArtAsset\Audio\S1_VILLAGE_BGM_v1_loop.ogg`, `S1b_FOREST_BGM_v1_loop.ogg`, and the four files in `Z:\TechArtAsset\Audio\SFX`.
2. Put one looping AudioSource in each **level** scene (Village / Forest), volume 0.5, Play On Awake. Do **not** add crossfade logic to `ChapterSceneLoader` in this batch; a simple start/stop with the level scene is enough. If you want a fade, put it in a separate small component on the level's music object.
3. One-shot SFX on the gate (open / close), the iron cross (pickup, duck music 0.5 s), and the thorn wall (banish, starts with the smoke).
4. Keep exactly one AudioListener (in Core). MainMenu music must still stop when the game starts.
5. Report as before; user checks: music in both levels, seam not audible, four SFX, Village → Forest still works.
