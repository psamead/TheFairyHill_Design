# Midjourney prompting — lessons from Lantern Keeper and Fairy Hills

## 2026-11-20 Fairy Hills environment and listening trials

Current evidence is in [the dated production summary](TechnicalArt/OPENING_STORYBOARD_PROGRESS_2026-11-20.md), BG01/BG02 round records, and OP02_listening_2026-11-20. Earlier shared-project examples below retain their original dates.

1. Describe the visible spatial relationship before texture. “From the foot of the mound” produced a close view; an open meadow before a complete middle-distance hill produced more space. Check the selected image against the owner-marked outline.
2. Give each reference a job. OP01 supplies overall rendering, v3 supplies identity, BG02 r03 U4 supplies composition, and the grass crop supplies near-ground strokes. A grass-only crop contains little evidence for distant clouds or ridges.
3. Assess stroke strength at full size. Dense dark contours around distant hills and clouds became much stronger in single-image views than in grids. Describe nearby tapered grass, middle-distance light and shadow, and low-contrast distant shapes separately.
4. A three-colour shape guide can supply the hill outline while introducing smooth bands. Separate silhouette review from paint review, and record the influence of each reference. The resulting image prompt still allowed changes in hill scale and placement.
5. Erasing the whole mound in the tested V7 editor returned continuous meadow or distant slopes in all four outputs. Preserve that mask and output as a failed trial. Local upload and URL import of an external composite also failed in this session; record the specific surface and error.
6. OP02 repeatedly faced the viewer. Put the listening action and shoulder, head and eye direction first. The third prepared prompt changed cw 100 to 40, but the result screenshot omits settings, so the weight effect remains unverified. Costume drift continued.
7. Keep ready-to-submit text distinct from the actual submitted job. Save original downloads, dimensions, SHA-256, candidate index and reasons. Treat filename UUIDs as image identifiers until the parent job is verified. A retained candidate has a narrower evidence state than final approval.


Compiled 2026-11-18 for agents continuing these projects. Purpose: reuse the reasoning and evidence behind prompts, not blindly replay old parameter strings. This guide adds no new art decision and ran no generations.

## Before writing a prompt

1. Read the current handoff and approved asset. Identify the deliverable: pose reference, character concept, isolated prop, scene background, or storyboard. A useful pose reference need not be a finished game asset.
2. List what must stay fixed: identity, clothing, handedness, prop, view direction, palette, silhouette, and scene relationships. Choose one variable to explore in this batch.
3. Assign each reference an explicit job: identity, pose/composition, or rendering style. Verify that the actual submission includes the images in the intended slots. Mentioning an attachment in text does not establish that the job used it.
4. Check the selected model and interface before choosing parameters. The projects' Niji 6, `--cref`, `--cw`, `--sref`, `--sw`, and `--iw` records are version-specific experiments. Do not migrate a project model or translate weights automatically.

Official documentation checked on 2026-11-18 now describes an Edit model for V8.1/V8.2 with image references, and distinguishes descriptive generation prompts from instructional edit prompts. The former Character Reference documentation redirects there. That does not mean the historical Niji jobs used this newer workflow. Verify the active model's controls before reuse. [Edit model documentation](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)

## Writing the prompt

For ordinary generation, describe the desired visible image using concrete English phrases:

`subject + action/pose + view/composition + identity details that matter + medium/style + lighting/palette + background`

Keep only relevant fields. Put technical parameters separately at the end. Avoid adding conflicting style adjectives to an already established reference. Short, specific descriptions are a useful starting point; add detail to address an observed failure. [Official prompting basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)

Project conventions: describe the visual qualities rather than naming an artist or another game; use a consistent style phrase for related assets. For titles, retain controlled typography and use generation for visual treatment only as the project permits.

### Proposed templates — not previously tested prompts

**Single character pose reference:**

> One full-body character in strict side profile facing right, both arms raised above the head, clear shoulder-to-elbow-to-wrist connections, hands visible, [approved clothing and colour details], [approved painterly treatment], neutral lighting, plain background.

Attach the approved character for identity and a separately identified pose image when supported. Replace placeholders with actual details. These words do not guarantee correct hands; inspect the output. For Niamh, the existing game cross can be composited afterward rather than forcing a perfect generated prop.

**Isolated game prop:**

> One complete [object], [required shape and materials], [view appropriate to the current game scene], isolated on a plain background, [approved painted surface and palette], readable silhouette.

**Storyboard environment:**

> [Location and time], [one story beat], [placement of figures and important objects], [space needed for captions], [approved painted treatment], [specific lighting relationship].

For a supported edit workflow, instead state the limited change and what must remain unchanged. An edit instruction is still a proposal, not proof that pixels or identity were preserved.

## What the actual project trials teach

| Recorded outcome | How to reuse the lesson | Boundary |
| --- | --- | --- |
| Lantern Keeper's numeric age produced unwanted “11”; “cute” and three-head proportions reinforced a chibi look. | Specify the visible proportions/expression needed; omit nonessential numeric age in similar assets. | Observed project failure, not a universal ban on numbers. |
| Maela's clothing colours and lantern state changed even with a character reference. | Restate identity-critical colours, visible prop state, and handedness when they matter. | Check against the current approved artwork, not an old prompt row. |
| Strong character reference pulled side/back views toward front-facing character sheets. | Generate one view per image; isolate the view problem and adjust reference influence only on a compatible model. | The recorded `cw 40` side-view trial is not a default for every asset. |
| Heavy scene style references introduced scenery into isolated props; a lower style weight helped one chest trial. | Separate identity, composition, and style influences; judge object isolation independently. | Historical `sw 15` is one trial, not a universal recipe. |
| “Circle of light” produced halos/portals. | Describe the intended illumination relationship, such as soft light falling across one side of a room. | Preserve intentional magical geometry when the current design actually calls for it. |
| Fairy Hills' whole-person masks changed identity/orientation or removed Niamh; a proportions rewrite also changed the rendering style. | Change one objective per batch; retain acceptable backgrounds and protect the approved character. | The causes were not fully isolated; do not assert every model behaves this way. |
| Niamh's complete-character references supplied useful arms even when the cross was unusable. | Select for the reference's assigned purpose, composite only needed action regions onto original artwork, then use the existing game prop. | Do not replace the original character with the entire generated figure. |
| Vary(Subtle) helped an early Maela selection, but a Fairy Hills run offered no prompt-edit field. | Confirm what operation actually ran. Save changed prompt text only if it was submitted. | A proposed text revision is not a tested revision. |

## Keep the two projects distinct

**Lantern Keeper:** use the current Home art knowledge base and handoff over older prompt rows. The later Home decision accepts room perspective; old straight-on constraints are not universal. Retain Breton visual identity and the approved hand-painted treatment. Earlier triple-spiral prop wording conflicts with later separation from Fairy Hills motifs; do not reintroduce it just because it remains in the historical prompt table. Keep gameplay-changing props separate from backgrounds where the current design requires it.

**Fairy Hills:** the current Niamh method is complete-character pose reference → selected arms/sleeves onto original art → user correction → existing cross asset. Check both hands, thumb direction, grip, shoulder/elbow/wrist joins, clothing details, occlusion, and lighting after a flip. The November 17 archive records proposed Niji 6 / 1:2 / stylize 150 / character weight 100 and added image weight 2 for raised-pose trials; those are recorded instructions, not independently verified backend metadata. The November 18 direct-raise choice remains a preview decision, not Unity acceptance.

## Iteration and stopping

Compare a small batch against the stated objective. Record accept/reject reasons tied to a file. Change one main cause at a time: wording, reference role, reference strength, composition, or editing region. Do not repeatedly regenerate a whole accepted character to fix a prop or one sleeve. If useful reference material is already available, proceed with the project's compositing process when authorized.

After selection, verify the correct result and upscale/download original. Keep reference, candidate, selected art, cleaned asset, animation, and Unity-tested asset as separate states. A thumbnail, GIF, or tool success response does not establish delivery quality.

## Prompt record for the next agent

```text
Project / asset / date:
Goal and acceptance criteria:
Current approved baseline file + hash:
Generation or edit; model/version; website or Discord:
Reference files + hashes + assigned roles:
Exact submitted prompt:
Actual submitted parameters (unknown fields marked unknown):
Job ID / parent job / selected grid index / upscale ID:
Output original file, dimensions, hash:
Observed result; selection/rejection reason:
One next change and its reason:
Status: proposed / submitted / reference selected / asset prepared / integrated / tested
```

## Evidence to read in each design repository

- Lantern Keeper: `TechnicalArt/LESSONS_ART_PIPELINE.md` (prompt trials and later Home updates), `ForAgent/Design/ART_PROMPTS.md` (historical exact prompts), `TechnicalArt/HOME_ART_KNOWLEDGE_BASE.md` (current constraints).
- Fairy Hills: `AGENT_PROCESS_GUIDELINES.md` sections 5.3–5.8; `TechnicalArt/LESSONS_CHARACTER_ANIMATION.md` latest complete-character/compositing method; `TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md` failed edit/variation evidence; `MJ_ref/Characters/Niamh/Interaction_Study_2026-11-17/README.md` and `source_manifest.json`; `MJ_ref/Slideshow/Opening_v1/evidence/` for failed prompts/screenshots; `STORYBOARD_RESUME.md` for current decisions.

Do not present a newly composed template as an original tested prompt. Read the exact source record when reproducing a historical trial. This guide is shared between the two projects; paths above are relative to the named repository, not all present in both.
