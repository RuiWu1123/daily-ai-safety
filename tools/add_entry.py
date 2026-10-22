#!/usr/bin/env python3
"""Insert one entry into a collection file, newest first, and update counts.

usage:
  python3 tools/add_entry.py --file METR_Research.md --title "..." --url "..." \
      --source "METR Research" --date 2026-10-23 --summary-file /path/summary.md \
      [--also-url URL --also-title TITLE --also-label LABEL] [--section "Misalignment Reports and Notices"]

Entries go under the "## <year>" heading (or "### <year>" inside --section), above
older entries of the same year. The "共 N 篇" line and the README table row are updated.
"""
import argparse, re, os
from datetime import date

MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--file', required=True)
    ap.add_argument('--title', required=True)
    ap.add_argument('--url', required=True)
    ap.add_argument('--source', required=True)
    ap.add_argument('--date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--summary-file', required=True)
    ap.add_argument('--also-url')
    ap.add_argument('--also-title')
    ap.add_argument('--also-label', default='')
    ap.add_argument('--section')
    a = ap.parse_args()

    path = os.path.join(ROOT, a.file)
    s = open(path, encoding='utf8').read()
    if f']({a.url})' in s:
        print('already present, skipped'); return
    y, m, d = int(a.date[:4]), int(a.date[5:7]), int(a.date[8:10])
    summary = open(a.summary_file, encoding='utf8').read().strip()
    meta = f'{a.source} {y} {MON[m - 1]} {d}'
    if a.also_url:
        meta += f'（另见{a.also_label}：[{a.also_title or a.also_url}]({a.also_url})）'
    level = '###' if a.section else '##'
    head = '####' if a.section else '###'
    entry = f'{head} [{a.title}]({a.url})\n\n{meta}\n\n{summary}\n\n'

    # region to insert into: whole file, or the given section
    if a.section:
        start = s.index(f'## {a.section}\n')
        end = len(s)
    else:
        start = 0
        end = s.find('\n---\n\n## ', s.index('---\n') + 4)  # an extra section after the main list
        end = len(s) if end == -1 else end
    region = s[start:end]

    yh = f'{level} {y}\n'
    if yh in region:
        i = region.index(yh) + len(yh)
        while region[i] == '\n':
            i += 1
        region = region[:i] + entry + region[i:]
    else:
        # new year heading: put it before the first older year heading, else at the end
        years = [(mm.start(), int(mm.group(1))) for mm in re.finditer(rf'^{level} (\d{{4}})\n', region, re.M)]
        older = [p for p, yy in years if yy < y]
        block = f'{yh}\n{entry}'
        if older:
            region = region[:older[0]] + block + region[older[0]:]
        else:
            region = region.rstrip('\n') + '\n\n' + block
    s = s[:start] + region + s[end:]

    # update total count line
    def bump(mm):
        return f'共 {int(mm.group(1)) + 1} 篇'
    s = re.sub(r'共 (\d+) 篇', bump, s, count=1)
    open(path, 'w', encoding='utf8').write(s)

    # README count column
    rp = os.path.join(ROOT, 'README.md')
    r = open(rp, encoding='utf8').read()
    lines = r.split('\n')
    for k, line in enumerate(lines):
        if line.startswith(f'| [{a.file}]'):
            cells = line.split(' | ')
            if '+' in cells[2]:
                base, extra = [int(x.strip()) for x in cells[2].split('+')]
                if a.section:
                    extra += 1
                    cells[1] = re.sub(r'（\d+ 篇）', f'（{extra} 篇）', cells[1])
                else:
                    base += 1
                cells[2] = f'{base} + {extra}'
            elif cells[2].strip().isdigit():
                cells[2] = str(int(cells[2]) + 1)
            cells[3] = re.sub(r'截至 [\d-]+', f'截至 {date.today().isoformat()}', cells[3])
            lines[k] = ' | '.join(cells)
    open(rp, 'w', encoding='utf8').write('\n'.join(lines))
    print('added to', a.file)


if __name__ == '__main__':
    main()
