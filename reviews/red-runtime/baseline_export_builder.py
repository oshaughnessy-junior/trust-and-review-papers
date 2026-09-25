"""Build a self-contained, reviewable static export. Does not publish anything.

Pandoc is required for Markdown/MathML rendering. Python runtime demos otherwise
use only the standard library. No remote assets, analytics or network calls.
"""
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {".md", ".py", ".json", ".csv", ".js", ".css", ".in"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def shell(title, content, prefix="", toc=""):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="MCRP research prototype: scoped reliance, mathematical models, and toy agents.">
<title>{html.escape(title)} · MCRP</title><link rel="stylesheet" href="{prefix}surfaces/site.css"></head>
<body><header><a href="{prefix}index.html">MCRP / Research prototype</a>
<nav aria-label="Main"><a href="{prefix}publication/blog-introduction.html">Introduction</a>
<a href="{prefix}domains/README.html">Domain cases</a><a href="{prefix}reviews/COLLECTIVE.html">Red-team review</a></nav></header>
<main>{content}</main><footer>Release candidate · Synthetic models · Substantial AI contribution disclosed.
No external peer review or operational certification. <a href="{prefix}publication/release-assessment.html">Release assessment</a> ·
<a href="{prefix}export-manifest.json">File manifest</a></footer></body></html>'''


def remap(text, relative):
    # Public export stands alone; private-history references become background.
    prefix = "../" * len(relative.parent.parts)
    text = re.sub(r"\]\([^)]*06-mcrp-hardening[^)]*\)",
                  "](" + prefix + "publication/background.md)", text)
    return re.sub(r"\]\((?!https?://)([^)\s]+)\.md([#)][^)]*)?",
                  lambda m: "](" + m.group(1) + ".html" + (m.group(2) or ""), text)


def build(output):
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("export must be outside the source packet")
    output.mkdir(parents=True, exist_ok=True)
    old = output / "export-manifest.json"
    if old.exists():
        prior = json.loads(old.read_text())
        for name in prior.get("files", {}):
            p = (output / name).resolve()
            if output not in p.parents:
                raise ValueError("unsafe prior manifest path")
            if p.is_file():
                p.unlink()
    source_hashes, transforms = {}, []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in ALLOWED or "__pycache__" in path.parts:
            continue
        rel = path.relative_to(ROOT)
        dest = output / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        source_hashes[str(rel)] = sha(data)
        dest.write_bytes(data)
        if path.suffix == ".md":
            text = path.read_text()
            mapped = remap(text, rel)
            if mapped != text:
                transforms.append(str(rel))
            result = subprocess.run(["pandoc", "--from", "markdown+tex_math_dollars+tex_math_single_backslash",
                                     "--to", "html5", "--mathml", "--toc", "--toc-depth=2"],
                                    input=mapped, text=True, capture_output=True, check=True)
            if result.stderr.strip():
                raise RuntimeError(f"Pandoc warning for {rel}: {result.stderr}")
            headings = re.findall(r"^#\s+(.+)$", text, re.M)
            title = headings[0] if headings else path.stem
            prefix = "../" * len(rel.parent.parts)
            content = '<article>' + result.stdout + '</article>'
            dest.with_suffix(".html").write_text(shell(title, content, prefix))
    # Embed traces as inert JSON; escape '<' to avoid script termination.
    demo = json.loads((ROOT / "toy_agents/results/demo.json").read_text())
    trace = json.dumps(demo["scenarios"]["release_cycle"], sort_keys=True).replace("<", "\\u003c")
    portal = (ROOT / "surfaces/portal.html.in").read_text().replace("__TRACE_JSON__", trace)
    (output / "index.html").write_text(shell("What can we rely on?", portal))
    (output / "source-manifest.json").write_text(json.dumps({
        "schema": "mcrp.public-candidate-source.v1", "source_files_sha256": source_hashes,
        "rendering": "Pandoc MathML; relative Markdown links rewritten to HTML; private-history links mapped to public background",
        "transformed_markdown": transforms, "license_status": "proposed, not adopted",
        "public_release_status": "not published; exact candidate approval pending"}, indent=2) + "\n")
    files = {str(p.relative_to(output)): sha(p.read_bytes()) for p in sorted(output.rglob("*"))
             if p.is_file() and p.name not in {"export-manifest.json", "mcrp-prototype-source.zip"}}
    content_digest = sha(json.dumps(files, sort_keys=True, separators=(",", ":")).encode())
    (output / "export-manifest.json").write_text(json.dumps({
        "schema": "mcrp.public-candidate-export.v1", "release_candidate": "2026-09-25-rc1",
        "files": files, "file_map_sha256": content_digest,
        "scope": "Integrity inventory, not a signature or approval; excludes this manifest and download ZIP"}, indent=2) + "\n")
    # Zip has fixed metadata; no private Git history, absolute paths or symlinks.
    with zipfile.ZipFile(output / "mcrp-prototype-source.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(files) + ["export-manifest.json"]:
            info = zipfile.ZipInfo("mcrp-prototype/" + name, (2026, 9, 25, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, (output / name).read_bytes())
    return {"files": len(files), "file_map_sha256": content_digest,
            "zip_sha256": sha((output / "mcrp-prototype-source.zip").read_bytes())}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
