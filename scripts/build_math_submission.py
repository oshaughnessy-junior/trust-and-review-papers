#!/usr/bin/env python3
"""Build the math manuscript and agent participation appendix with Pandoc + Typst."""
import argparse
from pathlib import Path
import re
import subprocess
import typst

root = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
out = a.output.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
main = root/'papers/07-release-packet/manuscripts/math-foundations.md'
appendix = root/'papers/09-review-1588/agent-participation.md'
md = out.with_suffix('.md')
main_text = main.read_text()
title = main_text.splitlines()[0].removeprefix('# ')
md.write_text((main_text.split('\n', 1)[1]+'\n\n'+appendix.read_text()).replace('../../09-review-1588/', 'https://github.com/oshaughnessy-junior/trust-and-review-papers/blob/aixiv-review-1588/papers/09-review-1588/'))
source = out.with_suffix('.typ')
subprocess.run(['pandoc',str(md),'-f','markdown','-t','typst','-s',
               '-M','title='+title, '-M','author=Codex agents (AI; MCRP contributors)',
               '-M','date=September 2026 - revision responding to aiXiv review1588',
               '-V','papersize=us-letter','-V','fontsize=10pt','-o',str(source)],check=True)
s=source.read_text().replace('margin: (x: 1.25in, y: 1.25in)','margin: (x: 0.8in, y: 0.8in)')
s=re.sub(r'\bsect\b','∩',s)
s=re.sub(r'align: \((?:auto,)+\),',lambda m:m.group().replace('auto','left'),s)
s=s.replace('  set heading(numbering: sectionnumbering)','  show table: it => { set par(justify: false); set text(size: 9pt); it }\n  set heading(numbering: sectionnumbering)')
needle='columns: (25%, 25%, 25%, 25%),'
if needle in s:
    before, after = s.rsplit(needle, 1)
    s = before + 'columns: (8%, 25%, 33%, 34%),' + after
source.write_text(s)
typst.compile(str(source),output=str(out),root=str(out.parent))
print(out)
