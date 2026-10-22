#!/usr/bin/env python3
"""Create one paper note under papers/<lab>/ (Obsidian vault layout).

usage:
  python3 tools/new_note.py --lab METR [--lab "Redwood Research"] --title "..." --url "..." \
      --source "METR Blog" --date 2026-10-23 --tags 监控与控制,事故报告 --summary-file /path/summary.md \
      [--also-url URL --also-title TITLE --also-label LABEL] [--category "Misalignment Reports and Notices"]

Prints the wikilink to use in the daily report, e.g. [[papers/METR/2026-10-23 Title|笔记]].
The script only ever creates new files; existing notes are never touched (the user writes in my_notes/ and links to these notes).
"""
import argparse, glob, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS = ['Anthropic', 'OpenAI', 'METR', 'Apollo Research', 'UK AISI', 'FAR.AI', 'Goodfire', 'Transluce',
        'Redwood Research', 'Alignment Forum']
VOCAB = [l.split(' — ')[0][2:].strip() for l in open(os.path.join(ROOT, 'tools', 'TAGS.md'), encoding='utf8')
         if l.startswith('- ')]


def safe(t):
    # file names: ASCII only (no Chinese or typographic characters), no characters Obsidian/git dislike
    for a, b in {'’': "'", '‘': "'", '“': '', '”': '', '–': '-', '—': '-', '×': 'x'}.items():
        t = t.replace(a, b)
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[\\/:*?"<>|#^\[\]]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().rstrip('.')[:90].rstrip(' .,')
    return t or 'untitled'


def yq(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lab', action='append', required=True, choices=LABS)
    ap.add_argument('--title', required=True)
    ap.add_argument('--url', required=True)
    ap.add_argument('--source', required=True)
    ap.add_argument('--date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--tags', required=True, help='comma-separated, from tools/TAGS.md')
    ap.add_argument('--summary-file', required=True)
    ap.add_argument('--also-url', action='append', default=[])
    ap.add_argument('--also-title', action='append', default=[])
    ap.add_argument('--also-label', action='append', default=[])
    ap.add_argument('--category')
    a = ap.parse_args()

    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', a.date):
        sys.exit('--date must be YYYY-MM-DD')
    tags = [t.strip() for t in a.tags.split(',') if t.strip()]
    bad = [t for t in tags if t not in VOCAB]
    if bad or not tags:
        sys.exit(f'unknown tags {bad}; choose 1-4 from tools/TAGS.md')

    for f in glob.glob(os.path.join(ROOT, 'papers', '**', '*.md'), recursive=True):
        txt = open(f, encoding='utf8').read(3000)
        if f'url: {a.url}\n' in txt or f'"{a.url}"' in txt:
            rel = os.path.relpath(f, ROOT)[:-3]
            print(f'already present: [[{rel}|笔记]]'); return

    sub = a.lab[0] + ('/Misalignment Reports' if a.category else '')
    base = f'{a.date} {safe(a.title)}'
    name, k = base, 2
    while os.path.exists(os.path.join(ROOT, 'papers', sub, name + '.md')):
        name = f'{base} ({k})'; k += 1
    rel = f'papers/{sub}/{name}'

    others = [{'url': u, 'title': (a.also_title[i] if i < len(a.also_title) else u),
               'label': (a.also_label[i] if i < len(a.also_label) else '')} for i, u in enumerate(a.also_url)]
    fm = ['---', f'title: {yq(a.title)}', 'lab:'] + [f'  - {yq(l)}' for l in a.lab] + [
        f'date: {a.date}', f'source: {yq(a.source)}', f'url: {a.url}']
    if others:
        fm += ['other_versions:'] + [f"  - {yq(o['url'])}" for o in others]
    if a.category:
        fm.append(f'category: {yq(a.category)}')
    fm += ['tags:'] + [f'  - {t}' for t in tags] + ['---']
    meta = f'**来源**：{a.source} · {a.date} · [原文]({a.url})'
    if others:
        meta += '　另见：' + '；'.join(f"[{o['label'] or o['title']}]({o['url']})" for o in others)
    summary = open(a.summary_file, encoding='utf8').read().strip()
    os.makedirs(os.path.join(ROOT, 'papers', sub), exist_ok=True)
    with open(os.path.join(ROOT, rel + '.md'), 'w', encoding='utf8') as f:
        f.write('\n'.join(fm) + f'\n\n# {a.title}\n\n{meta}\n\n## 简读\n\n{summary}\n')
    print(f'created: [[{rel}|笔记]]')


if __name__ == '__main__':
    main()
