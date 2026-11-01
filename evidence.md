# Evidence

Run on 2026-11-01 (Asia/Saigon) from a local checkout; the repo is not published yet.

## Build and validation

```
WARN vietnamese-education-copy: description is 1808 chars (spec limit 1024)
WARN vietnamese-finance-copy: description is 1243 chars (spec limit 1024)
WARN vietnamese-healthcare-copy: description is 1219 chars (spec limit 1024)
WARN vietnamese-legal-contracts: description is 1487 chars (spec limit 1024)
ok: 32 skills, 4 warnings
```

Four Vietnamese skills have descriptions over the 1,024-character limit in the Agent Skills spec. They are copied unchanged from `jangtrinh/design-os-vietnamese`; shortening them is an upstream change. Some agents may truncate or reject them.

## install.sh (HOME set to a temp folder)

```
$ ./install.sh --codex --dry-run (HOME=tmp)
would copy line-art-motion
would copy motion-video-recreation
would copy product-designer
dry run: 16 skill(s), nothing written

$ ./install.sh --claude
copied motion-video-recreation
copied product-designer
done: 16 skill(s) installed to /tmp/tmp.S8bIjTcpIW/.claude/skills

$ ./install.sh --claude   (second run)
skip   motion-video-recreation (exists; use --force)
skip   product-designer (exists; use --force)
done: 0 skill(s) installed to /tmp/tmp.S8bIjTcpIW/.claude/skills

$ ./install.sh --cursor --skill design-os-figma-agent
target: /tmp/tmp.S8bIjTcpIW/.cursor/skills
copied design-os-figma-agent
done: 1 skill(s) installed to /tmp/tmp.S8bIjTcpIW/.cursor/skills

$ ./install.sh --codex --group all
copied vn-design-system-ux
done: 32 skill(s) installed to /tmp/tmp.S8bIjTcpIW/.agents/skills

$ ./install.sh --codex --skill nope
target: /tmp/tmp.S8bIjTcpIW/.agents/skills
no such skill: nope
exit=1

SKILL.md files under tmp home:
.agents/skills 32
.claude/skills 16
.cursor/skills 1
```

## Not tested

- Loading the installed skills inside Claude Code, Codex and Cursor (needs each app signed in on a desktop).
- `/plugin marketplace add jangtrinh/design-os-skills` (needs the repo to be public).
- Skills that call an external CLI (figma-agent, Blender, code2flow) were copied, not run.
