#!/usr/bin/env bash
# Install design-os-skills into an agent's skills folder. Copies folders only; never runs skill scripts.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
usage() { cat <<U
Usage: ./install.sh (--claude | --codex | --cursor | --agents | --dir PATH) [options]
  --claude        ~/.claude/skills   (Claude Code)
  --codex         ~/.agents/skills   (Codex user skills)
  --cursor        ~/.cursor/skills   (Cursor)
  --agents        ~/.agents/skills   (any agent that reads the shared folder)
  --dir PATH      any other folder
Options:
  --group NAME    core | vietnamese | all   (default: core)
  --skill NAME    install one skill (repeatable); overrides --group
  --project       use ./<agent folder> in the current directory instead of \$HOME
  --force         overwrite a skill folder that already exists
  --dry-run       print what would be copied and exit
  --list          list skills and exit
U
}
dest=""; group="core"; skills=(); force=0; dry=0; project=0; list=0
while [ $# -gt 0 ]; do
  case "$1" in
    --claude) dest=".claude/skills"; home=1;;
    --codex|--agents) dest=".agents/skills"; home=1;;
    --cursor) dest=".cursor/skills"; home=1;;
    --dir) dest="$2"; home=0; shift;;
    --group) group="$2"; shift;;
    --skill) skills+=("$2"); shift;;
    --project) project=1;;
    --force) force=1;;
    --dry-run) dry=1;;
    --list) list=1;;
    -h|--help) usage; exit 0;;
    *) echo "unknown option: $1" >&2; usage >&2; exit 2;;
  esac; shift
done
names_for_group() { python3 - "$HERE/skills.json" "$1" <<'P'
import json,sys
d=json.load(open(sys.argv[1]))
for s in d['skills']:
    if sys.argv[2]=='all' or s['group']==sys.argv[2]: print(s['name'])
P
}
if [ "$list" = 1 ]; then names_for_group all; exit 0; fi
[ -n "$dest" ] || { usage >&2; exit 2; }
if [ "${home:-0}" = 1 ]; then
  if [ "$project" = 1 ]; then dest="$PWD/$dest"; else dest="$HOME/$dest"; fi
fi
if [ ${#skills[@]} -eq 0 ]; then
  case "$group" in core|vietnamese|all) ;; *) echo "bad --group: $group" >&2; exit 2;; esac
  while IFS= read -r n; do skills+=("$n"); done < <(names_for_group "$group")
fi
echo "target: $dest"
count=0
for n in "${skills[@]}"; do
  src="$HERE/skills/$n"
  [ -f "$src/SKILL.md" ] || { echo "no such skill: $n" >&2; exit 1; }
  if [ -e "$dest/$n" ] && [ "$force" = 0 ]; then echo "skip   $n (exists; use --force)"; continue; fi
  if [ "$dry" = 1 ]; then echo "would copy $n"; else
    mkdir -p "$dest"; rm -rf "$dest/$n"; cp -R "$src" "$dest/$n"; echo "copied $n"
  fi
  count=$((count+1))
done
[ "$dry" = 1 ] && echo "dry run: $count skill(s), nothing written" || echo "done: $count skill(s) installed to $dest"
