"""Check exported file integrity, local links and selected disclosure patterns.

This is a bounded static check, not a comprehensive secret, privacy or rights audit.
"""
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re
import zipfile
import stat


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for k in ("href", "src"):
            if k in a:
                self.links.append(a[k])


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("duplicate JSON object key")
        obj[key] = value
    return obj


def safe_name(name):
    return (isinstance(name, str) and bool(name) and "\\" not in name
            and ":" not in name and not name.startswith("/")
            and ".." not in PurePosixPath(name).parts
            and str(PurePosixPath(name)) == name and name != ".")


def verify(root):
    if root.is_symlink():
        raise ValueError("export root is a symlink")
    root = root.resolve()
    manifest = json.loads((root / "export-manifest.json").read_text(), object_pairs_hook=unique_object)
    errors, skipped, pages = [], [], {}
    expected_names = set(manifest["files"]) | {"export-manifest.json", "mcrp-prototype-source.zip"}
    for p in root.rglob("*"):
        name = str(p.relative_to(root))
        if p.is_symlink():
            errors.append("symlink in export: " + name)
        elif p.is_file() and name not in expected_names:
            errors.append("unmanifested file: " + name)

    for name, expected in manifest["files"].items():
        if not safe_name(name):
            errors.append("unsafe manifest path: " + str(name))
            continue
        p = (root / name).resolve()
        if root not in p.parents:
            errors.append("unsafe manifest path: " + name)
            continue
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
            errors.append("missing or changed: " + name)
        if p.suffix == ".html" and p.is_file():
            parser = Links()
            parser.feed(p.read_text())
            pages[p] = parser
        if p.suffix in {".md", ".html", ".json", ".csv", ".py", ".js", ".txt"} and p.is_file():
            # Patterns are split to avoid flagging the checker's own source.
            patterns = [r"/" + r"Users/[^/\s]+/", r"/" + r"home/[^/\s]+/",
                        "-----BEGIN " + "PRIVATE KEY-----", r"ghp_" + r"[A-Za-z0-9]{30,}"]
            for pattern in patterns:
                if re.search(pattern, p.read_text()):
                    errors.append("disclosure pattern in: " + name)
    for path, parser in pages.items():
        for url in parser.links:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                skipped.append(url)
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if root not in target.parents and target != root:
                errors.append(f"link escapes export: {path.relative_to(root)} -> {url}")
            elif not target.exists():
                errors.append(f"broken link: {path.relative_to(root)} -> {url}")
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f"missing fragment: {path.relative_to(root)} -> {url}")
    file_map_digest = hashlib.sha256(json.dumps(manifest["files"], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if file_map_digest != manifest["file_map_sha256"]:
        errors.append("manifest file-map digest mismatch")
    validation_path = root / 'results/validation.json'
    if validation_path.exists():
        validation = json.loads(validation_path.read_text(), object_pairs_hook=unique_object)
        if validation.get('passed') is not True:
            errors.append('model validation does not report success')
        if validation.get('inputs_changed_during_run'):
            errors.append('source or fixture input changed during validation')
        hashes = {**validation.get('source_sha256', {}), **validation.get('table_sha256', {}),
                  **validation.get('tested_inputs_sha256', {}), **validation.get('evidence_sha256', {})}
        for group in validation.get('check_groups', []):
            hashes[group['log']] = group['log_sha256']
        for name, expected in hashes.items():
            if not safe_name(name) or name not in manifest['files']:
                errors.append('validation evidence absent from export: ' + str(name))
            elif hashlib.sha256((root/name).read_bytes()).hexdigest() != expected:
                errors.append('validation evidence hash mismatch: ' + name)
    # Source copy and optional figure lineage must agree with the actual export.
    source_manifest = root / "source-manifest.json"
    if source_manifest.exists():
        sources = json.loads(source_manifest.read_text(), object_pairs_hook=unique_object)
        for name, expected in sources.get("source_files_sha256", {}).items():
            if not safe_name(name) or name not in manifest["files"] or manifest["files"][name] != expected:
                errors.append("source-copy evidence mismatch: " + str(name))
    figure_manifest = root / "results/figures/manifest.json"
    if figure_manifest.exists():
        figures = json.loads(figure_manifest.read_text(), object_pairs_hook=unique_object)
        bound = dict(figures.get("inputs", {}))
        bound.update({"results/figures/" + name: expected for name, expected in figures.get("figures", {}).items()})
        for name, expected in bound.items():
            if not safe_name(name) or name not in manifest["files"] or manifest["files"][name] != expected:
                errors.append("figure lineage mismatch: " + str(name))
    brief_manifest = root / "results/brief-manifest.json"
    if brief_manifest.exists():
        brief = json.loads(brief_manifest.read_text(), object_pairs_hook=unique_object)
        for name, expected in {**brief.get("inputs", {}), **brief.get("artifacts", {})}.items():
            if not safe_name(name) or name not in manifest["files"] or manifest["files"][name] != expected:
                errors.append("brief lineage mismatch: " + str(name))
    archive = root / "mcrp-prototype-source.zip"
    if not archive.is_file():
        errors.append("missing download ZIP")
    else:
        try:
            with zipfile.ZipFile(archive) as z:
                members = z.namelist()
                if len(members) != len(set(members)):
                    errors.append("duplicate ZIP member names")
                wanted = {"mcrp-prototype/" + n for n in manifest["files"]} | {"mcrp-prototype/export-manifest.json"}
                if set(members) != wanted:
                    errors.append("ZIP member inventory mismatch")
                for name in members:
                    mode = z.getinfo(name).external_attr >> 16
                    if stat.S_IFMT(mode) not in (0, stat.S_IFREG):
                        errors.append("nonregular ZIP member: " + name)
                    if not safe_name(name):
                        errors.append("unsafe ZIP member: " + name)
                        continue
                    if name not in wanted:
                        continue
                    relative = name.removeprefix("mcrp-prototype/")
                    expected = (hashlib.sha256((root / "export-manifest.json").read_bytes()).hexdigest()
                                if relative == "export-manifest.json" else manifest["files"][relative])
                    if hashlib.sha256(z.read(name)).hexdigest() != expected:
                        errors.append("ZIP content mismatch: " + name)
        except (zipfile.BadZipFile, OSError, RuntimeError) as error:
            errors.append("unreadable ZIP: " + type(error).__name__)
    return {"passed": not errors, "checked_files": len(manifest["files"]),
            "html_pages": len(pages), "external_links_not_fetched": len(set(skipped)),
            "errors": sorted(set(errors)),
            "scope": "File inventory/hash, local link/fragment and four disclosure-pattern checks only"}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("root", type=Path)
    args = p.parse_args()
    result = verify(args.root)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
