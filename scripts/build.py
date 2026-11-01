#!/usr/bin/env python3
"""Rebuild skills/, skills.json and the README index from pack.json.

Usage: scripts/build.py [--src-root DIR]   (DIR holds local checkouts named in pack.json)
Fails on: name != folder, missing description, duplicate names. Warns on description > 1024 chars.
"""
import glob, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_root = sys.argv[sys.argv.index('--src-root') + 1] if '--src-root' in sys.argv else os.path.join(ROOT, '..')
pack = json.load(open(os.path.join(ROOT, 'pack.json')))

def frontmatter(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    if not m: raise SystemExit(f'no frontmatter: {path}')
    out = {}
    for line in m.group(1).split('\n'):
        k = re.match(r'^(name|description):\s*(.*)$', line)
        if k:
            v = k.group(2).strip()
            if v and v[0] in '>|': raise SystemExit(f'block scalar not supported: {path}')
            if len(v) > 1 and v[0] == v[-1] and v[0] in '"\'': v = v[1:-1]
            out[k.group(1)] = v
    return out

shutil.rmtree(os.path.join(ROOT, 'skills'), ignore_errors=True)
os.makedirs(os.path.join(ROOT, 'skills'))
entries, seen, warnings = [], set(), []
for s in pack['sources']:
    base = os.path.join(src_root, s['local'])
    head = subprocess.run(['git', '-C', base, 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
    for pat in s['paths']:
        for d in sorted(glob.glob(os.path.join(base, pat))):
            if not os.path.isfile(os.path.join(d, 'SKILL.md')): continue
            name = os.path.basename(d)
            fm = frontmatter(os.path.join(d, 'SKILL.md'))
            assert fm.get('name') == name, f'name mismatch {name} vs {fm.get("name")}'
            assert fm.get('description'), f'no description {name}'
            if len(fm['description']) > 1024: warnings.append(f"{name}: description is {len(fm['description'])} chars (spec limit 1024)")
            assert name not in seen, f'duplicate {name}'
            seen.add(name)
            shutil.copytree(d, os.path.join(ROOT, 'skills', name), ignore=shutil.ignore_patterns('node_modules', '.git', '.DS_Store'))
            rel = os.path.relpath(d, base)
            entries.append({'name': name, 'group': s['group'], 'description': fm['description'],
                            'source_repo': s['repo'], 'source_path': rel, 'source_commit': head})
entries.sort(key=lambda e: (e['group'], e['name']))
json.dump({'name': pack['name'], 'count': len(entries), 'skills': entries}, open(os.path.join(ROOT, 'skills.json'), 'w'), indent=2, ensure_ascii=False)

def short(d, n=150):
    d = re.sub(r'\s+', ' ', d).replace('|', '/')
    return d if len(d) <= n else d[:n].rsplit(' ', 1)[0] + '…'
rows = lambda g: '\n'.join(f"| `{e['name']}` | {short(e['description'])} | [{e['source_repo'].split('/')[1]}](https://github.com/{e['source_repo']}) |" for e in entries if e['group'] == g)
readme = open(os.path.join(ROOT, 'README.template.md'), encoding='utf-8').read()
readme = readme.replace('{{CORE_ROWS}}', rows('core')).replace('{{VI_ROWS}}', rows('vietnamese'))
readme = readme.replace('{{COUNT}}', str(len(entries))).replace('{{CORE_COUNT}}', str(sum(e['group']=='core' for e in entries))).replace('{{VI_COUNT}}', str(sum(e['group']=='vietnamese' for e in entries)))
open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8').write(readme)
for w in warnings: print('WARN', w)
print(f'ok: {len(entries)} skills, {len(warnings)} warnings')
