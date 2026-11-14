# Niamh motion v8 — Unity trial handoff

**Date:** 2026-11-14
**Project:** The Fairy Hills 2D
**Audience:** Project owner, students, artists, Unity developers, future Codex or other agents
**Current status (2026-11-14):** Unity imported the six parts, built a reversible trial prefab and seven Animator states, connected them to the persistent player, compiled, and observed motion in Village and Forest Play Mode. The owner tried it and said it was basically OK apart from some stutter. Stutter cause, run-speed capture, and individual gate checks remain open. This is a six-part trial, not the full 22-bone rig.

The implementation result and evidence are in Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md` and `Docs/References/Niamh_Motion_v8/Unity_Trial/` (published on Unity `main`; implementation commit `1374a0fa3b982491aa596a2897b25b9a7c8bc93b`). The sections below preserve the original constraints and method so future workers can understand the decision. Do not run the original task as though it were still pending.

## Start here

For this trial, use the six files under `parts/`, exported from the owner's `_m` Photoshop revision and stored at the common source canvas size of **327 × 699 px**. `previews/Niamh_motion_v8.gif` is an offline reference only; it is not a game animation asset. `motion_preview_spec.json` records the source pivots, intended timing, and known limits.

The Unity project is separate from this design repository. The six PNGs and JSON were copied, without editing the originals, to:

`Assets/_Project/Art/Characters/Niamh/Motion_v8_Source/`

**Transfer route for this task:** the files were copied into the Unity working tree over the shared network before the Unity integration task was handed off. Use the files already in the Unity project; do not fetch them from GitHub. If any staged file is missing or damaged, send the maintainer its exact design-repository relative path, intended Unity destination, and required format. The maintainer will stage the approved copy under `TechnicalArt/unity_drop/<date_task>/` and notify the Unity-side worker. Copy from the shared folder; never move or edit the source copy. Mapped drive letters and computer-specific absolute paths vary by workstation, so resolve the repository-relative path using the shared root available on that machine.

The GIF and contact sheet were copied to `Docs/References/Niamh_Motion_v8/` for review. The original, now executed task is archived at `CommandForAgentToInitialRun/2026-11-14_Niamh_Motion_v8_Unity_Trial.md` in the design repository. The Unity repository's `Docs/Niamh_Motion_v8_Unity_Handoff.md` contains the actual result below its original brief.

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

- **Imported and assembled:** six same-canvas PNGs; one derived far leg/boot; eight SpriteRenderers, prefab, seven Animator states, and a presentation component. The old static renderer remains as rollback.
- **Compiled:** Unity 6000.3.24f1 Editor compilation passed; no new trial Console errors were observed at inspection.
- **Play Mode observed:** Village idle, walk, jump phases, landing and the owner's later Village → Forest switch; Forest idle/walk/jump phases, landing and both facings. The first Forest load was invoked directly for inspection, so that action did not validate the exit trigger.
- **Owner feedback:** “已经试玩结束，除了些卡顿，可能是各种软件一起运行的问题，其他基本ok”. Treat this as basic trial acceptance with an unresolved stutter concern, not a measured diagnosis.
- **Still open:** 5.6u/s run was not independently captured; gate interaction, all collision routes, foot sliding and stutter cause were not fully verified. No standalone build or full rig was produced.
- **Published:** Unity `main` implementation commit `1374a0fa3b982491aa596a2897b25b9a7c8bc93b`; the Unity handoff holds the exact rollback and evidence list. Update this summary when later checks produce new evidence.
