# LaTeX drafting conventions

Each manuscript lane owns its `papers/NN-name/` directory and must create:

- `main.tex`: compile-ready private first draft;
- `references.bib`: only sources actually cited by that paper, with identifiers or authoritative URLs;
- `writing-packet.json` and `logical-claims-audit.json` following the shared scientific-writing schemas;
- `claim-ledger.json` following `openclaw.claim-ledger.v1`;
- `README.md`: exact compile command, maturity, and first unmet evidence gate;
- `build/`: ignored generated PDF/log artifacts.

Use `\input{../../latex/common-preamble.tex}` after `\documentclass`. Cite with `natbib` and finish with:

```tex
\bibliographystyle{plainnat}
\bibliography{references}
```

Required status language:

- `\draftstatus{...}` on page 1;
- `\designchoice{...}` for protocol/model choices;
- `\openhypothesis{...}` for untested propositions;
- `\implementationobservation{...}` only for versioned local evidence;
- `evidencegate` blocks where a claim, result, privacy property, or field conclusion cannot yet be promoted.

Do not write mock result prose. A planned Results section may state estimands, table shells, decision rules, and the exact artifacts required before population.

Compile from a paper directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Then summarize `build/main.log`, render `build/main.pdf` with `pdftoppm`, and inspect the images. Generated build products remain uncommitted.
