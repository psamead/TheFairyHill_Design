# Opening, HUD hints and cross raise: Unity validation
Date: 2026-11-18. Baseline HEAD: `7bf4160`; implementation checkpoint: `cc815f8`.

## Status and evidence boundary
Resources imported, Editor compilation passed, and the checks below ran in the actual TheFairyHill2D Editor (6000.3.24f1). Screenshots are native Game view captures. No automated test framework, duplicate project, package installation, Recorder or push was used. Owner visual/audio acceptance is pending. The earlier v8 owner approval does not approve this new presentation.

This was tool-driven Play Mode: the menu's StartGame method, wired Next/Skip button callbacks and Input System queued keyboard states were exercised. No physical keyboard/pointer playtest is claimed. Forest travel used the existing scene loader and temporary runtime repositioning; the cross was acquired by its normal reveal/physics pickup trigger, without setting inventory. Full manual traversal from Village to the pickup remains unverified.

## Minimal repairs
- KeyHintUnderlines modified child UI graphics inside TMP's OnPreRenderText canvas rebuild, causing repeated “Trying to add Key Underline ... graphic rebuild loop” errors and missing lines. That callback now only requests a redraw; LateUpdate refreshes the mesh and draws outside the canvas rebuild. Font assets remain untouched.
- PlayerController2D used the wall root pivot for facing. The actual wall root is x=49.2 while its collider center is x=55.5. Facing now uses the existing collider center, with the pivot as fallback. Range, target selection, collision, timing and inventory rules are unchanged.

## Observed Play Mode results
- Opening: all three captions and Chapter I card captured at exactly 1920x1080 and 1280x720. Full screen cover, lower shade, no page counter/divider, readable captions and separate upper Next/Skip controls were observed. Space/Enter/Esc underlines rendered.
- Rapid repeated advance calls did not bypass the guard. Wired Skip went to card index 3, then wired Next reached Village. Held injected Enter left BlocksGameplay=true with CompletionCount=1; release allowed the normal Village spawn (3.5,0), one listener and BlocksGameplay=false.
- HUD: eight control links produced eight lines (A/D, arrows, Shift, Space, E/Q). A message containing E/Q produced two lines; replacing it with ordinary prose left zero enabled lines. Disable/re-enable restored control lines. All underline Images had raycastTarget=false.
- A dynamically added TMP/underline probe had four links and four enabled lines at its first rendered frame, with no raycast interception. The temporary probe was destroyed.
- Normal trigger pickup acquired the cross at (48.5,0). Missing-cross and no-target messages were captured.
- Injected Q directly enabled the raised sprite and hid every v8 part plus static fallback. During the pose, repeated Q plus movement/jump input left the feet at (50.3,0) and velocity zero. The unchanged 0.3-second glow and 1.6-second dissolve ran; the wall became dispersed and its collider disabled. Pose expiry restored all eight v8 parts and disabled the raised sprite. Subsequent movement/jump velocity was (3.2,11.4).
- Final clear pose captures approach the actual wall from x=49 and x=59.5. FacingLeft was false and true respectively; both walls completed with disabled colliders. The raised cross and restored idle are visible in the images.
- Disabling/re-enabling the presentation restored v8 with the raised renderer off. A separate tool-triggered presentation followed by a scene load expired normally with raisedEnabled=false; this interruption check was not a second normal Q/wall interaction.

## Console and limitations
The initial underline rebuild errors are historical failures fixed in this run. The final Console sample after 06:40 contains no Error entries and one Unity AI Account API accessibility warning. During loading there are informational “no audio listeners” messages before Core becomes ready; stable Village had exactly one. Audible continuity/mix, subjective readability, pose naturalness and frame-time performance require owner review. No performance diagnosis or audio signoff is claimed.

Evidence: `Docs/References/Opening_Immersive_Cross_Raise_2026-11-18/Unity_Trial/`. Prefer `cross_raise_right.png`, `cross_raise_left.png`, `cross_restore_right.png`, `cross_restore_left.png`, `hud_underlines.png`, `opening_0..3_1920.png` and corresponding `1280` images. `console_final.json` and `editor_runtime.log` retain the observation records; the text driver is an inspection aid outside Assets, not an installed test suite.

## Preservation and handoff
Play stopped, queued keys released, timeScale=1, MainMenu is the only open scene and is clean. All four protected files were byte-checked against the preflight hashes: AGENTS.md, Village scene and both font assets. No scene was rebuilt or saved. Shared design originals were not modified. The two script fixes and this local evidence are left for review; no local commit or push was made.

