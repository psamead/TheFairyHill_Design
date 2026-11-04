# The Fairy Hills · Design Repository

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

> Paths in the instructions: `Z:` = this repository's folder on the maintainer's machine, `W:` = the Unity project. Replace them with your own local paths.

## Folders

| Path | Contents |
|---|---|
| Root `*.md` | Specs and handoff notes for people and agents |
| `StoryDesign/` | Story, concept design, demo plan, market notes (Word) |
| `TechnicalArt/` | Technical / promotional art docs (Markdown + Word), fonts, tools (`tools/*.py`), Unity progress log, mock-ups |
| `MJ_ref/` | Concept art, generated images, the original designer's artwork (`AUTHOR_L7_66/`), `ASSETS.md` asset list |
| `TechArtAsset/` | Finished game assets (exported PNG, OGG, layout JSON) |
| `CommandForAgentToInitialRun/` | Step-by-step instructions given to Codex (dated) |
| `ForDesign/` | Screenshots from the Unity side for design review |
| `diagrams/` | Story diagrams |
| `_build_scripts/` | Node scripts that generate the Word documents |
| `deprecated/` | Superseded versions and process images (kept for visual history) |

## Licences

- Fonts: SIL Open Font License.
- Music generated with Google Lyria; sound effects synthesized in code (`TechnicalArt/tools/make_sfx.py`).
- All design documents and art are original work of this project (YiChun Jiang and collaborators), shared for course / project collaboration only. Please do not reuse them outside the course without permission.
