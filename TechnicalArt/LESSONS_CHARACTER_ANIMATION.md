# Character animation lessons — The Fairy Hills

**Started:** 2026-11-14
**Audience:** Project owner, students, artists, Unity developers, future agents
**Scope:** Reusable lessons from preparing Niamh's first user-reviewed cutout motion study. This is a growing experience log; it does not replace the art specification or live Unity progress.

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
