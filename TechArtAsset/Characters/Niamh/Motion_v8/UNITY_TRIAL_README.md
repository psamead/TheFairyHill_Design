# Niamh motion v8 — Unity trial handoff

**Date:** 2026-11-14
**Project:** The Fairy Hills 2D
**Audience:** Project owner, students, artists, Unity developers, future Codex or other agents
**Status:** Motion study and source parts prepared; copied into the Unity repository. Unity rig, Animator, live player hookup, compilation, Play Mode review, and user acceptance are still pending.

## Start here

For this trial, use the six files under `parts/`, exported from the owner's `_m` Photoshop revision and stored at the common source canvas size of **327 × 699 px**. `previews/Niamh_motion_v8.gif` is an offline reference only; it is not a game animation asset. `motion_preview_spec.json` records the source pivots, intended timing, and known limits.

The Unity project is separate from this design repository. The six PNGs and JSON were copied, without editing the originals, to:

`Assets/_Project/Art/Characters/Niamh/Motion_v8_Source/`

The GIF and contact sheet were copied to `Docs/References/Niamh_Motion_v8/` for review. The executable task is `CommandForAgentToInitialRun/2026-11-14_Niamh_Motion_v8_Unity_Trial.md` in the design repository. The same task is included in the Unity repository at `Docs/Niamh_Motion_v8_Unity_Handoff.md`.

## What this trial should prove

Make an isolated layered character prefab and connect it to the existing player for a reversible in-game trial. Preserve the persistent player's root, movement, interaction, collider, camera, and scene routing. The six source layers support only a simple transform rig: separate head, back hair, torso/dress/cape, one arm, one complete leg, and one boot. A far-side leg can be made as a Unity-side duplicate of the leg and boot with a darker tint. This is **not** the detailed 22-bone rig in `TechnicalArt/NIAMH_RIG_PARTS.md`; the source does not have separate upper/lower limbs, joints, cape panels, or hair segments.

The preview was composed by rotating whole layers around the approximate source-canvas pivots below. Unity can use these as starting landmarks, then adjust after visual inspection. Coordinates in the JSON use a top-left origin. Convert to bottom-left coordinates with `yUnityPx = 699 - yJsonPx`.

| Part / joint | Preview pivot, top-left px | Converted y, bottom-left px |
|---|---:|---:|
| Head | (180, 214) | 485 |
| Arm / shoulder | (219, 323) | 376 |
| Hip | (187, 532) | 167 |
| Knee / boot | (185, 579) | 120 |

All pieces share the same canvas, so preserve their alignment and bottom-center origin. Existing static Niamh is 327 × 699 px, imported at 100 PPU, and displayed at 0.30 scale (about 2.1 Unity units high). Use the same displayed height and compare at the game's actual camera size. The current capsule on the persistent player is 0.23 × 2.08 units with offset (0.08, 1.04); keep it unchanged.

## Motion intent from the user's review

- Idle: quiet breathing and a small head / arm response.
- Walk: about 0.8 s per loop; run: about 0.5 s per loop. Keep the rigid dress/cape readable and avoid over-rotating large pieces.
- Jump ascent / apex: legs swing backward, arm reaches forward with a wider arc, and head tips slightly upward.
- Descent: head looks down, arm swings backward, and legs lift forward. The stronger swing peaks near 1.025 s in the offline reference, opening around 0.8 s and returning by 1.25 s.
- Landing: feet stay on the ground; body / back hair settle by about 3 px, head / arm by about 4 px, then recover gently. The previous large whole-body squash was removed.

The GIF uses a 2-second repeating jump-study timeline for side-by-side inspection. Do not assume the game's physical jump takes two seconds: map ascent and descent poses to the existing controller's grounded state and vertical velocity, and let the controller remain authoritative for movement. The actual jump is shorter. Re-time the poses to the real jump after Play Mode review while preserving their order and relative intent.

## Source and decision history

- Editable source: `Motion_v8/Niamh_user_revision_source.psd`, a snapshot of the user-edited `_m` file. Earlier user edits repaired the head, hair, body/shoulder area, legs, and boots; retain them.
- Layer exports: `Motion_v8/parts/{head,hair_back,body,arm,leg,boot}.png`.
- Preview renderer and numeric values: `Motion_v8/tools/render_preview.py` and `Motion_v8/motion_preview_spec.json`.
- User pose references: `Motion_v8/references/`.
- The older full rig plan is still a future target; this trial intentionally measures what can be achieved with the current six pieces before requesting additional Photoshop or Midjourney art.

## Known risks and review points

1. The arm may reveal missing or differently painted pixels behind it when it swings; inspect on a bright magenta background and at the in-game character size.
2. The whole leg cannot bend at the knee with the current export. The boot can rotate separately at the approximate knee pivot, but this may expose seams.
3. The far leg is derived from the near-leg art and may have imperfect overlap, shape, or value. Keep the experiment reversible and show it in both Village and Forest lighting.
4. The dress/cape remains one rigid piece. Do not imply that the v8 preview proves cape or hair secondary animation.
5. The source export is a preview puppet assembled from same-canvas images, not a Unity-ready PSB. Import the PNGs as individual Sprites; do not overwrite or re-slice the source PSD.

## Completion record

Update this section only after the Unity task is run. Record separately: assets imported, prefab / clips created, player connected, editor compilation, Play Mode locations and actions reviewed, user feedback, unresolved defects, and the Git commit. Until then, Unity-side items remain pending.
