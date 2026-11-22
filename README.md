# The Fairy Hills · Design Repository

2026-11-23 · [五页开场故事画与 OP03 手调 v4 接续](STORYBOARD_RESUME.md)。

**2026-11-20 story art handoff.** Read [the current production summary](TechnicalArt/OPENING_STORYBOARD_PROGRESS_2026-11-20.md) and [the illustrated Word handoff](TechnicalArt/OPENING_STORYBOARD_PROGRESS_2026-11-20.docx) for BG01, BG02, OP02, prompt trials and OP03 next steps. New media are retained locally for a later transfer; see TechnicalArt/STORYBOARD_PENDING_MEDIA_2026-11-20.json.


**2026-11-18 当前试装：** Immersive story frames/captions, underlined key hints and the direct raised-cross red-wall presentation are in the actual Unity project; offline C# type-check passed, Editor/Play Mode pending. Read the task in shared `CommandForAgentToInitialRun/2026-11-18_Opening_Immersive_Cross_Raise_Unity_Validation.md`; do not copy the task into Unity. See `TechnicalArt/OPENING_IMMERSIVE_CROSS_RAISE_TRIAL_2026-11-18.md`.

**English** | [简体中文](README.zh-CN.md)

Design and art documentation for **The Fairy Hills (妖精丘陵)**, a hand-painted 2D side-scrolling adventure demo based on Irish mythology: story, gameplay plan, art specs, Unity handoff notes, and finished art / audio assets.
Original designer: **YiChun Jiang**. Maintained by Psamead.
The Unity project lives in a separate repository: <https://github.com/psamead/TheFairyHill2D>

> This repository is **read-only** for collaborators and students: it is maintained and pushed by Psamead. Please do not edit it after pulling; send feedback to Psamead / YiChun instead.
>
> Most documents are written in Chinese. In-game text, titles and menus are English only.

## Get and update

```bash
# Recommended: clone next to the Unity project (sibling folder)
git clone https://github.com/psamead/TheFairyHill_Design.git
# Later updates
git pull
```

## Using these materials

**2026-11-14 evening update:** The owner approved the OP01 r04 U4 upscale for a temporary opening sequence and Chapter I cover. Character art remains provisional. Use [the new Unity task](CommandForAgentToInitialRun/2026-11-14_Opening_Chapter1_Placeholder_Unity_Trial.md), [knowledge base](TechnicalArt/STORYBOARD_KNOWLEDGE_BASE.md), and [next-chat entry point](STORYBOARD_RESUME.md). The readable current Word is `TechnicalArt/妖精丘陵_开场故事画与章节过渡交接_v2.docx`; v1 is historical. Assets are staged over the network; read the drop package dispatch status before claiming execution. The previously approved 23 movement sounds are also staged, with in-game integration awaiting feedback.

These materials support the project owner, students, production and layout designers, and any current or future agent. Read relevant sources for reference or layout work; follow the steps below when continuing development.

1. Clone this design repository next to the Unity repository. Read the Unity repository's root `AGENTS.md` first, then follow the task-specific reading list below. People and agents should use the same current sources.
2. In your own Unity checkout, run `git status --short` before editing. Check actual scenes, scripts, and Build Settings; distinguish the design goal from what is implemented.
3. The dated files in `CommandForAgentToInitialRun/` are records of past requests. Check the current project and later handoffs before reusing one. `TechnicalArt/LESSONS_SCENE_PIPELINE.md` explains problems encountered and how they were resolved.
4. For scope and story, use `DEMO_IMPLEMENTATION_PLAN.md` and `STORY_BIBLE.md`. For current implementation, inspect the Unity repository and its dated `Docs/` records, then this repository's `TechnicalArt/CH1_UNITY_PROGRESS.md`. “Asset ready,” “integrated,” “compiled,” “checked in Play Mode,” and “accepted by the user” are different states.
   The prompt collection in `StoryDesign/` records past model settings and experiments; check references, selected assets, model version, and the current goal before reusing a prompt.
5. Leave the next reader a dated record of the goal, source files, changes, observed checks, unverified items, and next step. For image prompts, save the model/version, references, parameters, exact prompt, selection reason, and output path. See `AGENT_PROCESS_GUIDELINES.md` under “接手材料写法.”

For layout, excerpts, and reuse, retain editable sources and their exported deliverables, source versions, image credits and captions, fonts, and known usage restrictions. Save derived outputs separately and preserve originals. See `AGENT_PROCESS_GUIDELINES.md` §5.7. The game remains an independently positioned demo with English in-game text.

## For agents: read first (in order, as needed)

1. `ART_HANDOFF.md` **§0 (how to use) and §9 (change log, newest at the bottom)** — where the project is now
2. `handoff.md` — project overview, demo scope, code conventions
3. `DEMO_IMPLEMENTATION_PLAN.md` — scenes, mechanics, implementation checklist
4. `STORY_BIBLE.md` — story and setting; `INVENTORY_SYSTEM_DESIGN.md` — backpack system
5. `TechnicalArt/SCENE_SCALE_SPEC.md` — character scale and jump metrics
6. `TechnicalArt/CH1_SCENE_PLAN.md` → `CH1_UNITY_HANDOFF.md` → `CH1_UNITY_REVISION_v2.md` / `v3.md` / **`v3_fix.md`** — Chapter 1 scenes from design to Unity, in order
7. `TechnicalArt/LESSONS_SCENE_PIPELINE.md` — lessons learned / pitfalls
8. `TechnicalArt/UNITY_AGENT_RULES.md` — Unity-side rules for agents
9. `DESIGN_CHANGES.md`, `AGENT_PROCESS_GUIDELINES.md` — how design changes are proposed and recorded

What happened recently: `ART_HANDOFF.md` §9, `TechnicalArt/CH1_UNITY_PROGRESS.md`, or `git log`.

> Paths in the instructions: `Z:` = this repository's folder on the maintainer's machine, `W:` = the Unity project. Replace them with your own local paths; the maintainer's network computer and drive letters are not prerequisites.

## Folders

| Path | Contents |
|---|---|
| Root `*.md` | Specs and handoff notes for people and agents |
| `StoryDesign/` | Story, concept design, demo plan, market notes (Word) |
| `TechnicalArt/` | Technical / promotional art docs (Markdown + Word), fonts, tools (`tools/*.py`), Unity progress log, mock-ups |
| `MJ_ref/` | Concept art, generated images, the original designer's artwork (`AUTHOR_L7_66/`), `ASSETS.md` asset list |
| `TechArtAsset/` | Finished game assets (exported PNG, OGG, layout JSON) |
| `CommandForAgentToInitialRun/` | Step-by-step instructions given to Codex (dated) |
| `ForDesignScreenShot/` | Play-test screenshots for design review, one folder per fix round (see its README) |
| `diagrams/` | Story diagrams |
| `_build_scripts/` | Node scripts that generate the Word documents |
| `deprecated/` | Superseded versions and process images (kept for visual history) |

## Licences

- Fonts: SIL Open Font License.
- Music generated with Google Lyria; sound effects synthesized in code (`TechnicalArt/tools/make_sfx.py`).
- All design documents and art are original work of this project (YiChun Jiang and collaborators), shared for course / project collaboration only. Please do not reuse them outside the course without permission.


## Imported context and lessons — 2026-11-18

[Claude context and reusable lessons](CLAUDE_CONTEXT_2026-11-18.md) preserves historical rationale and points to newer decisions in STORYBOARD_RESUME.md. It does not replace current design or validation rules. The shared Obsidian vault now has a separate TheFairyHill2D project index and a matching reference note.


For practical prompt writing, reference selection and iteration, read [Midjourney project lessons](MIDJOURNEY_PROJECT_LESSONS.md). It includes historical outcomes and clearly labelled untested templates.
