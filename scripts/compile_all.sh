#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
papers=(
  "papers/01-design-map"
  "papers/02-formal-dynamics"
  "papers/03-protocol-and-evaluation"
  "papers/04-sociotechnical-pilot"
)

for paper in "${papers[@]}"; do
  echo "Compiling ${paper}"
  (
    cd "${repo_root}/${paper}"
    mkdir -p build
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
  )
done
