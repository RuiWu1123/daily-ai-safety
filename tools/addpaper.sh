#!/bin/bash
# usage: addpaper.sh <textsdir> : for texts < 5000 bytes with an arXiv/PDF link, append full paper text (first 80KB)
d=$1; mkdir -p $d/pdfs
for f in $d/*.txt; do s=$(stat -c%s $f); if [ $s -lt 5000 ] && ! grep -q 'FULL PAPER TEXT' $f; then u=$(sed -n 4p $f | grep -oE 'https://(arxiv.org/(abs|pdf)/[0-9.v]+|[^ ]+\.pdf)' | head -1); id=$(basename $f .txt); if [ -n "$u" ]; then pu=$(echo $u | sed 's#arxiv.org/abs/#arxiv.org/pdf/#'); curl -sL -A 'Mozilla/5.0' "$pu" -o $d/pdfs/$id.pdf && pdftotext -q $d/pdfs/$id.pdf $d/pdfs/$id.txt && { printf '\n\n===== FULL PAPER TEXT (%s) =====\n' "$u"; head -c 80000 $d/pdfs/$id.txt; } >> $f && echo "$id +paper"; fi; fi; done
