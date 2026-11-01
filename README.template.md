# design-os-skills

{{COUNT}} agent skills from the DESIGN:OS suite, in one folder you can copy into Claude Code, Codex or Cursor. Free to use. Source-available under [PolyForm Shield 1.0.0](LICENSE).

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

## Core skills ({{CORE_COUNT}})

| Skill | What it does | Source |
| --- | --- | --- |
{{CORE_ROWS}}

## Vietnamese-language skills ({{VI_COUNT}})

Install with `--group vietnamese` or `--group all`.

| Skill | What it does | Source |
| --- | --- | --- |
{{VI_ROWS}}

## Keep it current

`scripts/build.py --src-root <folder with the source checkouts>` rebuilds `skills/`, `skills.json` and this index from `pack.json`, and fails if a skill's `name` does not match its folder or its description is missing, and warns when a description is over 1,024 characters. Test results are in [evidence.md](evidence.md).

## Licence

[PolyForm Shield 1.0.0](LICENSE) © 2026 Jang Trinh. Free to use and modify, including for paid client work. You may not resell it or build a competing product from it. Some skills carry their own `ATTRIBUTION.md`.

## Listed on

Not listed anywhere yet. Planned targets are in [LISTING-TARGETS.md](LISTING-TARGETS.md).
