"""Check exported file integrity, local links and selected disclosure patterns.

This is a bounded static check, not a comprehensive secret, privacy or rights audit.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re


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


def verify(root):
    root = root.resolve()
    manifest = json.loads((root / "export-manifest.json").read_text())
    errors, skipped, pages = [], [], {}
    for name, expected in manifest["files"].items():
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
        if p.suffix in {".md", ".html", ".json", ".csv", ".py", ".js"} and p.is_file():
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
