#!/usr/bin/env python3
"""Self-contained structural checks for the private publication workspace."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(path: str, errors: list[str]) -> Path:
    candidate = ROOT / path
    if not candidate.is_file() or candidate.stat().st_size == 0:
        errors.append(f"missing or empty: {path}")
    return candidate


def main() -> int:
    errors: list[str] = []
    for path in [
        "README.md",
        "PUBLICATION_PROGRAM.md",
        "SCIENCE_WRITING_PACKET.md",
        "SCIENCE_WRITER_REVIEW.md",
        "science-writing/writing-packet.json",
        "science-writing/logical-claims-audit.json",
        "science-writing/claim-ledger.json",
    ]:
        require(path, errors)
    for paper in [
        "01-design-map",
        "02-formal-dynamics",
        "03-protocol-and-evaluation",
        "04-sociotechnical-pilot",
    ]:
        require(f"papers/{paper}/OUTLINE.md", errors)
        require(f"papers/{paper}/CLAIMS.md", errors)
    if (ROOT / "papers/05-software-paper/OUTLINE.md").exists():
        errors.append("Paper 05 must remain deferred until its recorded maturity gate passes")

    packet = json.loads(require("science-writing/writing-packet.json", errors).read_text())
    if packet.get("schema") != "openclaw.scientific-writing.packet.v1":
        errors.append("writing packet schema mismatch")
    audit = json.loads(require("science-writing/logical-claims-audit.json", errors).read_text())
    if audit.get("schema") != "openclaw.scientific-writing.audit.v1" or not audit.get("claims"):
        errors.append("logical claims audit missing schema or claims")
    ledger = json.loads(require("science-writing/claim-ledger.json", errors).read_text())
    if ledger.get("schema") != "openclaw.claim-ledger.v1" or not ledger.get("claims"):
        errors.append("claim ledger missing schema or claims")
    for claim in ledger.get("claims", []):
        if claim.get("disposition") not in {"verified", "human-asserted", "blocked"}:
            errors.append(f"invalid disposition for {claim.get('id', '<unknown>')}")
        if claim.get("consequence_level") in {"medium", "high"} and claim.get("disposition") == "blocked":
            if claim.get("human_required") is not True:
                errors.append(f"blocked consequential claim lacks human_required: {claim.get('id')}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID: publication structure, maturity gate, and science-writing artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
