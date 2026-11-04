# Unity MainMenu Progress and Design Backlog

**Updated:** 2026-10-30  
**For:** Claude and Codex continuing The Fairy Hills on another computer in this network.

## Read first

Read `ART_HANDOFF.md` and `handoff.md` as directed by the heading and context block at the top of `TechnicalArt/MENU_UNITY_HANDOFF.md`, then read the menu handoff. That top block is context before numbered section 1. The menu handoff describes artwork and intended behavior; this note records what is currently implemented and what still needs design or asset work.

## Current Unity implementation

Unity project used on the authoring computer: `C:\Users\Administrator\Documents\UnityProject\TheFairyHill2D`. The Unity project files are local to that computer; this network note does not imply that the project checkout is present on every network computer.

- Scene: Assets/Scenes/MainMenu.unity is first in Build Settings, followed by Ch1_S1_Village and Ch1_S1b_ForestPath. The user deleted SampleScene on 2026-10-30; its stale Build Settings entry was removed.
- Art: menu PSD and source font/icon were copied into the Unity project; the named background, left darkening overlay and title plaque are separate scene sprites. Network source artwork was not changed.
- UI: English TextMeshPro menu labels use Fondamento. Continue is disabled; Settings opens a placeholder panel; Start loads `Ch1_S1_Village` when that scene is available in Build Settings; Quit calls `Application.Quit()`.
- Navigation: W/S and Up/Down change the selected option. Mouse hover changes selection; left-click invokes the hovered button action (Start, Settings, Quit); right/middle clicks remain disabled. Continue is skipped.
- Selection icon: fixed `(0, -14)` UI-unit offset from the focused row. It snaps into place; there is no easing or rotation.
- Audio: `Assets/_Project/Audio/UI/Menu_HoverChime.wav` is a short synthesized selection chime. It plays on selection changes after initial focus, at volume `0.35`, through a runtime 2D AudioSource. Repeated pointer updates over the same option are silent.
- MainMenu BGM: `Assets/_Project/Audio/Music/MENU_BGM_v1_loop.ogg` is imported as Streaming / Vorbis with preload disabled. A dedicated 2D `MainMenuMusic` AudioSource has Loop and Play On Awake enabled at volume `0.6`; it is separate from the hover chime source (`0.35`). The loop uses AudioSource Loop only; no crossfade script was added.
- The Main Camera has exactly one enabled AudioListener in the saved scene; the editor builder also adds one when it creates the camera.

## Validation state

The saved scene has one enabled AudioListener, and both the BGM and hover-chime scene references are present. Importer and AudioSource settings were verified in the Unity Editor. The user confirmed in Play Mode that BGM playback works and does not disturb the hover chime. Final visual review and a standalone player build remain unverified.

## Design and asset backlog

- [x] **Connect and verify MainMenu background music.** Added the approved seamless-loop OGG and configured the dedicated looping AudioSource. The user confirmed in Play Mode that playback works and the hover chime remains clear.
- [ ] **Review the menu selection chime.** The current short synthesized chime is a functional placeholder. Confirm it fits the desired sound identity or replace it with an approved designed sound.
- [ ] **Menu background separation and effects.** Separate the source art into the planned parallax layers, then design/build the Ogham particles, mist and doorway silhouette/light treatment as recorded in the art handoff.

## Append future design work here

Keep this list open for additions. Add new work as unchecked bullets under “Design and asset backlog”; do not remove completed history. When a task is completed, update the relevant `ART_HANDOFF.md` section 6 checkbox and append a dated entry in section 9. Update this note with implementation status and validation limits. Preserve the established rule that art-detail changes may be recorded directly, while story-meaning changes are first proposed in the root `DESIGN_CHANGES.md` for confirmation.