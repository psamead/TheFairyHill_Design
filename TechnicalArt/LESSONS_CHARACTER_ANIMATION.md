# Character animation lessons — The Fairy Hills

**Started:** 2026-11-14
**Audience:** Project owner, students, artists, Unity developers, future agents
**Scope:** Reusable lessons from preparing and testing Niamh's first user-reviewed cutout motion study. This is a growing experience log; it does not replace the art specification or live Unity progress.

## Trial 1 — Niamh motion v1–v8

### Context

The Unity game already used one static Niamh side-view Sprite. The owner wanted only actions needed by the existing Village and Forest Path scenes first: idle, walk, run, jump and land. The owner supplied and refined a layered Photoshop `_m` file, then reviewed motion studies with visual markups. The source parts in v8 were exported from that edited file and kept at a shared 327 × 699 px canvas.

### What worked in preparation

- Iterate using the owner's edited source and marked-up poses; each iteration kept its source snapshot, parameters, reference image, preview GIF, and README together.
- Preserve identical canvas dimensions and alignment for each transparent part. This made layered comparison and compositing predictable.
- Keep the jump poses staged: ascent with head up / legs behind / arm forward; descent with head down / arm behind / legs forward; then a small landing and recovery.
- Review the actual point of concern at named times. A contact sheet made it easier to compare the peak of the fall swing with the start and recovery.
- Remove exaggerated whole-body squash when it made the landing feel too heavy. Keep the feet visually grounded while upper parts settle.

### Limits found before Unity

- A GIF preview is useful for posing but cannot establish Unity import settings, Animator transitions, layering, collision alignment, movement synchronization, or performance in the actual scenes.
- Rotating whole `leg.png` and `arm.png` cannot create a knee or elbow bend. Duplicating one painted leg for the far side is only a mockup, not a final anatomical solution.
- Rigid dress and cape pixels can hide the arm's missing backdrop and obscure the hand arc. Check against magenta and game backgrounds at the actual 2.1u scale.
- Preview timing is an art reference, not gameplay timing. The preview's two-second jump loop is longer than the current physical jump. Bind poses to controller ground / vertical-velocity states, then retime in Play Mode.
- The user-edited `_m` file is authoritative. Export from a snapshot or duplicate; never repair it by painting over the source or reusing an old fill patch.

### What the Unity trial actually established

Unity imported the six PNGs, made a reversible eight-renderer puppet with a derived far leg/boot, built seven Animator states, and connected it to the persistent player without replacing its controls or collider. Editor compilation passed. Village and Forest Play Mode showed idle, walking, jump phases, landing and left/right facing; the owner tried the game and found it basically OK apart from some stutter. The cause of that stutter was not measured. Run at 5.6u/s, gate toggles and every collision route were not separately captured. The full evidence and rollback are in Unity `Docs/Niamh_Motion_v8_Unity_Handoff.md` and `Docs/References/Niamh_Motion_v8/Unity_Trial/` (implementation commit `1374a0fa3b982491aa596a2897b25b9a7c8bc93b`).

1. **Joint pivots.** Same-canvas pieces still shift if rotation uses the wrong origin. The Unity trial put each parent pivot at its converted landmark and offset child art back by the same amount; the static pose stayed aligned. The coordinates and 0.30 scale are specific to Niamh, so inspect each new character's pivots visually.
2. **Sorting.** Individual renderer orders can accidentally put limbs in front of the scenery. A `SortingGroup` held the puppet at the original actor order, while part orders worked inside the group. Check the foreground order in every level where the character appears.
3. **Facing.** Flipping individual pieces around separate joints can pull the assembly apart. The trial flipped the whole visual hierarchy and kept the hidden static renderer as the controller's facing reference and rollback. Review both directions in Play Mode.
4. **Floor contact.** Rotating boots changes the lowest visible pixel. The generator baked a vertical correction from the boot alpha edge into walk/run clips. This is not planted-foot IK; actual foot sliding still needs visual review.
5. **Preview capture.** A successful magenta image capture initially contained no puppet because the temporary camera lacked the preview scene's culling mask. Apply that mask and inspect the saved image rather than trusting capture success alone.
6. **Unrelated Editor changes.** TMP font caches can change during Editor work. Compare known dirty files before and after, leave unrelated changes unstaged, and report them. A cache change is not evidence that the animation changed.

For the next action, compare the trial at actual game scale, then decide what new art is required for push-door and cross-raise poses. Do not derive a bendable knee, independent cape or finished interaction animation from these six rigid images.

### Unity trial method

Use the network-first handoff: first check whether the task's assets are already pre-copied into the Unity project. If anything is missing, request an exact file list and purpose from the maintainer; have approved files staged under `TechnicalArt/unity_drop/<date_task>/` and copy them through the shared network. Do not use GitHub as the default art download path. Copy, do not move, the six PNGs and JSON spec into the Unity repository. Import PNGs as individual Sprites while retaining the shared canvas and a common origin. Build a reversible layered prefab, initially at the same visual height as the static Niamh (0.30 scale, roughly 2.1u); preserve the existing player root and capsule. A simple Transform / Animator rig can test the six available parts. It must be labeled a trial, because it does not implement the detailed 22-bone plan.

Review gaps and ordering on magenta, then review idle, directional movement, run, jump ascent, jump descent, landing, and turning in both Village and Forest. Keep animation as presentation: the existing player controller remains authoritative for movement, collision, input, and transitions. Never rebuild unrelated chapter scenes as part of this test. Record imported / integrated / compiled / Play Mode / user-accepted states separately.

## Reusable handoff pattern

For future art-to-Unity animation work, keep the following next to the versioned source:

1. Editable source or an immutable source snapshot, plus individually exported parts.
2. A contact sheet or GIF labeled as a reference preview, not production animation.
3. A machine-readable spec with canvas size, coordinate origin, pivots, timing intent, and limitations.
4. User markups and a short decision log explaining what changed between versions.
5. A Unity-specific task that names allowed changes, protects existing scene / prefab edits, and defines visual and runtime acceptance checks.
6. A completion note that distinguishes prepared assets, imported assets, implementation, compilation, Play Mode evidence, and user approval.

See `TechArtAsset/Characters/Niamh/Motion_v8/UNITY_TRIAL_README.md`, `TechnicalArt/NIAMH_RIG_PARTS.md`, `TechnicalArt/NIAMH_ANIM_LIST_DEMO.md`, and `CommandForAgentToInitialRun/2026-11-14_Niamh_Motion_v8_Unity_Trial.md`.

## Trial 2 — Niamh holding the iron cross with both hands (2026-11-16)

### Goal and accepted result

Explore the hand and arm pose needed for Niamh's cross-raising interaction while retaining the existing in-game character design. The owner accepted the resulting still as a **pose and style direction**: the generated Niamh reads as close to the game's current art, and both hands hold the cross against her chest. This approval is limited to the static concept image. It does not approve its pixels as final game art, a cutout, an animation, or a Unity integration.

### Method that worked

1. Keep the existing side-view game image as the identity/style anchor and the in-game cross sprite as the prop anchor.
2. Use Midjourney in the owner's Discord conversation to obtain a four-pose character sheet; select U2 (upper-right) for the bent arms and two-handed grip. Treat the MJ character as pose reference only; its face, eyes, proportions, cape, and other details are not replacements for the game asset.
3. Generate an integrated Niamh still with Codex built-in ImageGen, referencing the original Niamh, MJ U2, and the Unity cross image. This retained the current character identity and brought the rendered treatment closer to the in-game still.
4. Ask the owner to judge the result beside the actual in-game side sprite. The owner accepted the direction on 2026-11-16.

### Limits and next action

- ImageGen's exact backend model/version and the complete prompt were not preserved in the record. Do not label it Google Imagen or invent missing metadata.
- The image is a static, generated whole-character concept. It does not contain aligned character parts, a repaired arm-backdrop, usable pivots, a motion cycle, or Unity import settings.
- Next, prepare a non-destructive layered pose using the user-edited source and Motion_v8 as the basis. Plan arm/hand/cross overlap and fill hidden regions; keep the rest of the character anchored to the existing art. Make an offline pose/GIF preview, inspect seams and the full in-game scale, and ask the owner to approve it before writing a separate Unity task.
- The gate-push pose remains a separate action. Do not imply either interaction is implemented by v8's seven existing states.

### Evidence and files

- Study folder: `TechArtAsset/Characters/Niamh/Interaction_Study_2026-11-16/`.
- Selected still: `Niamh_two_hands_pose_study_v1.png` (Codex built-in ImageGen; whole-character concept, not an aligned export of animation parts).
- MJ pose sheet: `MJ_two_hands_U2_original.png` (U2 is the upper-right pose; full sheet preserved).
- Earlier grip-only ImageGen result: `grip_imagegen_2026-11-15_reference.png` (retained only as an arm/hand study).
- Human-readable decision record: `TechnicalArt/妮芙双手捧十字架动作参考_2026-11-16.md`.

This trial also informs the generation workflow in `AGENT_PROCESS_GUIDELINES.md` §5.8: try ImageGen with in-game references first; use MJ for pose exploration if needed; then have ImageGen integrate the closest pose with the original character and prop references. The owner approves the offline animation as a distinct stage before Unity work.
