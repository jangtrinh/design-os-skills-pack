# design-os-skills

32 agent skills from the DESIGN:OS suite, in one folder you can copy into Claude Code, Codex or Cursor. Free to use. Source-available under [PolyForm Shield 1.0.0](LICENSE).

Each skill is a folder with a `SKILL.md` in the [Agent Skills](https://agentskills.io) format (`name` matches the folder, plus a `description`). The skills are copies of the files published in each source repo, and `skills.json` records the repo, path and commit they came from.

## Install

In Claude Code you can also add it as a plugin marketplace:

```text
/plugin marketplace add jangtrinh/design-os-skills
/plugin install design-os-skills@design-os-skills
```
Or from a clone, for any agent:

```bash
git clone https://github.com/jangtrinh/design-os-skills.git
cd design-os-skills
./install.sh --claude            # Claude Code  → ~/.claude/skills
./install.sh --codex             # Codex        → ~/.agents/skills
./install.sh --cursor            # Cursor       → ~/.cursor/skills
./install.sh --claude --group all            # also the Vietnamese-language skills
./install.sh --codex --skill design-os-figma-agent --dry-run
```
`--project` installs into the current repo (`./.claude/skills`, `./.agents/skills`, `./.cursor/skills`) instead of your home folder. Existing skills are skipped unless you pass `--force`. `--dry-run` prints the plan and writes nothing. The script only copies folders and never runs anything inside a skill.

Folders checked against the docs of each tool: [Cursor](https://cursor.com/docs/skills), [Codex](https://developers.openai.com/codex/skills), [Claude Code](https://code.claude.com/docs/en/skills).

## What a skill needs

Skills that drive a command-line tool need that tool installed first. For example `design-os-figma-agent` calls the `figma-agent` CLI from [design-os-figma-plugin](https://github.com/jangtrinh/design-os-figma-plugin), which also needs its plugin imported into Figma Desktop. Each skill's `SKILL.md` says what it expects. Nothing here sends data anywhere.

## Core skills (16)

| Skill | What it does | Source |
| --- | --- | --- |
| `blender-agent-core` | Core discipline for ANY Blender/bpy work — contract-first, purpose-first (render-only / print / both), knowledge routing, execute-verify-refine loop… | [design-os-3d-blender](https://github.com/jangtrinh/design-os-3d-blender) |
| `blender-image-to-3d` | Reconstruct assets in Blender from reference images using only native Blender geometry, local skills, and project workflows; includes fidelity… | [design-os-3d-blender](https://github.com/jangtrinh/design-os-3d-blender) |
| `blender-knowledge-workbench` | Retrieve and apply this Blender project's knowledge, engineering research and portable reference methods through a checked local catalog and bounded… | [design-os-3d-blender](https://github.com/jangtrinh/design-os-3d-blender) |
| `code2flow-answer-flow-questions` | Answer questions about a scanned app's user flows from Code2Flow's machine-readable outputs — "how does a user get from A to B", "which screens are… | [design-os-code2flow](https://github.com/jangtrinh/design-os-code2flow) |
| `code2flow-map-codebase` | Map a Next.js App Router repo into a Code2Flow user-flow canvas end to end (init → run → read the summary → report), respecting the fixed localhost… | [design-os-code2flow](https://github.com/jangtrinh/design-os-code2flow) |
| `code2flow-stories-from-prd` | Turn a PRD markdown into a Code2Flow Story Manifest (code2flow.stories.json v3, v2 structure plus optional audience captions, presenter notes, cues,… | [design-os-code2flow](https://github.com/jangtrinh/design-os-code2flow) |
| `design-os` | Use when working with DESIGN:OS CLI — Multi-runtime design operating system and CLI for Claude Code, OpenAI Codex, Gemini CLI, and Google Antigravity. | [design-os](https://github.com/jangtrinh/design-os) |
| `design-os-3d-blender` | Use when working with DESIGN:OS 3D Blender Agent — Parametric 3D mechanical parts generator, headless Blender Python (`bpy`) pipeline, and embedded… | [design-os-3d-blender](https://github.com/jangtrinh/design-os-3d-blender) |
| `design-os-code2flow` | Use when working with DESIGN:OS Code2Flow — Local-first AST codebase-to-user-flow mapper and 11-heuristic UX gap auditor across 7 frontend and mobile… | [design-os-code2flow](https://github.com/jangtrinh/design-os-code2flow) |
| `design-os-designer` | Use when shaping, implementing, critiquing, polishing, hardening or auditing rendered UI, then proving it with the ui gate and a three-width look. | [design-os](https://github.com/jangtrinh/design-os) |
| `design-os-figma-agent` | figma-agent — the CLI bridge to the Figma file already open in the designer's Figma desktop app, over a local WebSocket broker. SessionStart MAY have… | [design-os-figma-plugin](https://github.com/jangtrinh/design-os-figma-plugin) |
| `design-os-figma-craft` | Generic Figma canvas engineering discipline — the battle-tested workflow, laws, and Plugin-API failure-mode catalog for building/editing Figma files… | [design-os-figma-plugin](https://github.com/jangtrinh/design-os-figma-plugin) |
| `es-tutorial-video` | Use when turning a finished DESIGN:OS build folder into an A-to-Z tutorial video (16:9 + 9:16, evidence on screen, optional voice): storyboard, kit… | [design-os-svg-animation](https://github.com/jangtrinh/design-os-svg-animation) |
| `line-art-motion` | Turn one reference drawing (line art, logo, sketch) into a faithful, animated, interactive SVG page with video exports: centerline trace, part map,… | [design-os-svg-animation](https://github.com/jangtrinh/design-os-svg-animation) |
| `motion-video-recreation` | Recreate reference motion videos through HyperFrames v2, Motion IR, deterministic export, and source-to-output visual review. | [design-os-svg-animation](https://github.com/jangtrinh/design-os-svg-animation) |
| `product-designer` | EaseUI & Linear/Stripe-caliber Product Designer & Design Architect. MUST be called whenever creating or refining animations, UI elements, video… | [design-os-svg-animation](https://github.com/jangtrinh/design-os-svg-animation) |

## Vietnamese-language skills (16)

Install with `--group vietnamese` or `--group all`.

| Skill | What it does | Source |
| --- | --- | --- |
| `vietnamese-business-comms` | Authoritative Vietnamese omnichannel marketing and B2B commercial communications engineering skill for DESIGN:OS. Enforces strict linguistic… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-cybersecurity-infosec` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) cybersecurity incident communications, personal data breach notifications under Law… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-ecommerce-retail` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) e-commerce storefront copy, product detail pages (PDP), promotional flash sale… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-education-copy` | Writes, evaluates, and pedagogically audits native-quality Vietnamese (vi-VN) educational, academic, and EdTech communications across the full 7-tier… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-finance-copy` | Writes, localizes, and audits native-quality Vietnamese (vi-VN) financial, banking, accounting, and FinTech communications. Enforces statutory… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-government-public-service` | Drafts, localizes, and audits Vietnamese e-government communications, online public service portals (DVC toàn trình & một phần), administrative… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-healthcare-copy` | Writes, localizes, and audits native-quality Vietnamese (vi-VN) healthcare, medical, hospital, EMR, clinical, pharmacy, and dietary supplement (TPCN)… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-hospitality-travel` | Writes, localizes, and audits native-quality Vietnamese (vi-VN) hospitality, resort, civil aviation, culinary F&B, and tourism communications.… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-hr-recruitment` | Writes, localizes, and audits native-quality Vietnamese (vi-VN) human resources, talent acquisition, recruitment marketing, and employment compliance… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-insurance-insurtech` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) life insurance illustrations, general insurance policies, InsurTech digital… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-landing-copy` | Writes, optimizes, and audits high-converting native Vietnamese (vi-VN) landing pages and digital marketing copy across 6 critical verticals —… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-legal-contracts` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) civil and commercial agreements, corporate governance contracts, Terms of Service… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-media-journalism-pr` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) journalism copy, official press releases, press corrections and apologies under… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-real-estate-construction` | Drafts, localizes, and audits native-quality Vietnamese (vi-VN) real estate project communications, off-plan residential sales contracts, booking… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vietnamese-tech-writing` | Writes, edits, and audits native-quality Vietnamese (vi-VN) engineering, cloud, and product documentation — including commit subjects, PR reviews,… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |
| `vn-design-system-ux` | Vietnamese UI/UX microcopy, design systems, typography tokens, stacked-diacritic line-height gates, button/tab/badge/toast character caps, state copy… | [design-os-vietnamese](https://github.com/jangtrinh/design-os-vietnamese) |

## Keep it current

`scripts/build.py --src-root <folder with the source checkouts>` rebuilds `skills/`, `skills.json` and this index from `pack.json`, and fails if a skill's `name` does not match its folder or its description is missing, and warns when a description is over 1,024 characters. Test results are in [evidence.md](evidence.md).

## Licence

[PolyForm Shield 1.0.0](LICENSE) © 2026 Jang Trinh. Free to use and modify, including for paid client work. You may not resell it or build a competing product from it. Some skills carry their own `ATTRIBUTION.md`.

## Listed on

Not listed anywhere yet. Planned targets are in [LISTING-TARGETS.md](LISTING-TARGETS.md).
