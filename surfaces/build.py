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
import os
import tempfile
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {".md", ".py", ".json", ".csv", ".js", ".css", ".in", ".txt", ".svg", ".png", ".pdf"}


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
<main>{content}</main><footer>Agent-first research prototype · Synthetic models · Substantial AI contribution disclosed.
No external peer review or operational certification. <a href="{prefix}publication/launch.html">Launch and contribution terms</a> ·
<a href="{prefix}export-manifest.json">File manifest</a></footer></body></html>'''


def remap(text, relative):
    # Public export stands alone; private-history references become background.
    prefix = "../" * len(relative.parent.parts)
    text = re.sub(r"\]\([^)]*06-mcrp-hardening[^)]*\)",
                  "](" + prefix + "publication/background.md)", text)
    return re.sub(r"\]\((?!https?://)([^)\s]+)\.md([#)][^)]*)?",
                  lambda m: "](" + m.group(1) + ".html" + (m.group(2) or ""), text)


def _build_staged(output):
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("export must be outside the source packet")
    output.mkdir(parents=True, exist_ok=True)
    source_hashes, transforms = {}, []
    created = set()
    for path in sorted(ROOT.rglob("*")):
        if path.is_symlink():
            raise ValueError("symlink in source packet: " + str(path.relative_to(ROOT)))
        if not path.is_file() or path.suffix not in ALLOWED or any(part in {"__pycache__", "build"} for part in path.relative_to(ROOT).parts):
            continue
        rel = path.relative_to(ROOT)
        dest = output / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        source_hashes[str(rel)] = sha(data)
        dest.write_bytes(data)
        created.add(str(rel))
        if path.suffix == ".md":
            text = data.decode("utf-8")
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
            created.add(str(rel.with_suffix(".html")))
    # Embed traces as inert JSON; escape '<' to avoid script termination.
    demo = json.loads((output / "toy_agents/results/demo.json").read_text())
    trace = json.dumps(demo["scenarios"]["release_cycle"], sort_keys=True).replace("<", "\\u003c")
    portal = (output / "surfaces/portal.html.in").read_text().replace("__TRACE_JSON__", trace)
    (output / "index.html").write_text(shell("What can we rely on?", portal))
    (output / "source-manifest.json").write_text(json.dumps({
        "schema": "mcrp.public-candidate-source.v1", "source_files_sha256": source_hashes,
        "rendering": "Pandoc MathML; relative Markdown links rewritten to HTML; private-history links mapped to public background",
        "transformed_markdown": transforms, "license_status": "MIT code/fixtures; CC BY 4.0 original prose/figures; retained third-party terms; see LICENSE.md",
        "public_release_status": "maintainer-authorized agent-first launch; live delivery observation recorded separately"}, indent=2) + "\n")
    (output / ".nojekyll").write_bytes(b"")
    created.update({"index.html", "source-manifest.json", ".nojekyll"})
    files = {name: sha((output / name).read_bytes()) for name in sorted(created)}
    content_digest = sha(json.dumps(files, sort_keys=True, separators=(",", ":")).encode())
    (output / "export-manifest.json").write_text(json.dumps({
        "schema": "mcrp.public-candidate-export.v1", "release_candidate": "2026-09-25-agent-v1",
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


def build(output):
    output = Path(output)
    if output.is_symlink():
        raise ValueError("export directory cannot be a symlink")
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        raise ValueError("export must be outside the source packet")
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and any(output.iterdir()):
        old = output / "export-manifest.json"
        if not old.is_file() or old.is_symlink():
            raise ValueError("nonempty output lacks a regular prior export manifest")
        prior = json.loads(old.read_text())
        names = set(prior["files"]) | {"export-manifest.json", "mcrp-prototype-source.zip"}
        allowed_dirs = {str(parent) for name in names for parent in Path(name).parents if str(parent) != "."}
        for name in names:
            p = output / name
            if output not in p.resolve().parents or p.is_symlink():
                raise ValueError("unsafe prior manifest entry")
        for p in output.rglob("*"):
            rel = str(p.relative_to(output))
            if p.is_symlink() or (p.is_file() and rel not in names) or (p.is_dir() and rel not in allowed_dirs):
                raise ValueError("untracked or symlink output entry: " + rel)
        for name, expected in prior["files"].items():
            p = output / name
            if not p.is_file() or sha(p.read_bytes()) != expected:
                raise ValueError("prior generated file changed: " + name)
    with tempfile.TemporaryDirectory(prefix="." + output.name + "-stage-", dir=output.parent) as tmp:
        stage = Path(tmp) / "candidate"
        result = _build_staged(stage)
        backup = Path(tmp) / "previous"
        if output.exists():
            os.replace(output, backup)
        try:
            os.replace(stage, output)
        except BaseException:
            if backup.exists():
                os.replace(backup, output)
            raise
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.output), indent=2))
