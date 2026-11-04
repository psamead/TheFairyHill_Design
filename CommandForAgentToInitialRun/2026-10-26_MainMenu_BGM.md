# Task: Add background music to the Unity MainMenu (2026-10-26)

The shared folder is mapped as `Z:` on your computer. If your drive letter is different, use yours.

1. Read section 0 of `Z:\TechnicalArt\MENU_UNITY_HANDOFF.md` (environment rules), then section 5 of `Z:\TechnicalArt\AUDIO_PIPELINE.md` (Unity import settings).
2. Copy **only** `Z:\TechArtAsset\Audio\MENU_BGM_v1_loop.ogg` into the Unity project at `Assets/_Project/Audio/Music/`. Do **not** copy the `.wav` file; it is the master backup and stays in the shared folder.
3. Use it as the MainMenu background music:
   - Import settings: Load Type = Streaming, Compression = Vorbis, Preload Audio Data off.
   - AudioSource: Loop on, Play On Awake on, volume about 0.6. The existing selection chime (0.35) must stay clearly audible over the music.
   - The file is already a seamless loop. Do not add a crossfade script; AudioSource Loop is enough.
4. Do not modify, move or delete anything else in the shared folder.
5. When done:
   - Update `Z:\TechnicalArt\MENU_UNITY_PROGRESS_AND_DESIGN_BACKLOG.md` (implementation status and what is still unverified).
   - In `Z:\ART_HANDOFF.md`, update the menu BGM line in section 6 and add a dated entry in section 9. Edit the current file on disk; do not overwrite other people's changes.
   - Tell the user whether you checked the music in Play Mode.
