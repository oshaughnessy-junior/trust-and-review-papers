#!/usr/bin/env python3
"""Self-contained structural checks for the private publication workspace."""

from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "papers/01-design-map/cases/r0-gw150914-strain-lag"
HPC_CASE = ROOT / "papers/01-design-map/cases/hpc-sanitized-partitioned-inference"
RESOURCE_AXES = {
    "compute",
    "storage",
    "access",
    "platform",
    "wall_clock",
    "human_expertise",
    "agent_capability",
    "operator_support",
    "monetary_allocative_cost",
    "freshness",
}


def require(path: str, errors: list[str]) -> Path:
    candidate = ROOT / path
    if not candidate.is_file() or candidate.stat().st_size == 0:
        errors.append(f"missing or empty: {path}")
    return candidate


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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
        require(f"papers/{paper}/main.tex", errors)
        require(f"papers/{paper}/references.bib", errors)
        require(f"papers/{paper}/writing-packet.json", errors)
        require(f"papers/{paper}/logical-claims-audit.json", errors)
        require(f"papers/{paper}/claim-ledger.json", errors)
    for forbidden in ["OUTLINE.md", "main.tex"]:
        if (ROOT / f"papers/05-software-paper/{forbidden}").exists():
            errors.append(f"Paper 05 must remain deferred until its recorded maturity gate passes: found {forbidden}")

    case_files = [
        "README.md",
        "Makefile",
        "pixi.toml",
        "pixi.lock",
        "run_case.py",
        "test_case.py",
        "claim-manifest.json",
        "source-manifest.json",
        "trust-boundaries.json",
        "lifecycle-events.json",
        "review-signoff.json",
        "review-checklist.md",
        "independent-replay-report.json",
        "scientific-review-dossier.json",
        "scientific-review-form.md",
        "scientific-review-completed-2026-08-29.md",
        "packet-index.json",
        "artifacts/evidence/claim-evidence.json",
        "artifacts/evidence/negative-tests.json",
        "artifacts/provenance/run-record.json",
        "artifacts/provenance/resource-declaration.json",
    ]
    for path in case_files:
        require(str((CASE / path).relative_to(ROOT)), errors)

    source_manifest = json.loads((CASE / "source-manifest.json").read_text())
    for record in source_manifest.get("sources", []):
        source = CASE / "data/raw" / record["filename"]
        if not source.is_file():
            errors.append(f"case source missing: {record['filename']}")
            continue
        if source.stat().st_size != record["bytes"]:
            errors.append(f"case source size mismatch: {record['filename']}")
        if sha256(source) != record["sha256"]:
            errors.append(f"case source digest mismatch: {record['filename']}")

    claim_manifest = json.loads((CASE / "claim-manifest.json").read_text())
    if claim_manifest.get("release", {}).get("archive_status") != "UNMINTED":
        errors.append("R0 case must remain UNMINTED until human archival approval")
    signoff = json.loads((CASE / "review-signoff.json").read_text())
    if signoff.get("human_scientific_review", {}).get("status") != "accepted":
        errors.append("R0 case human scientific review must record the authorized acceptance")
    dossier = json.loads((CASE / "scientific-review-dossier.json").read_text())
    if dossier.get("review_status") != "human-reviewed":
        errors.append("R0 case scientific review dossier is not marked human-reviewed")
    human_disposition = dossier.get("human_disposition", {})
    if human_disposition.get("status") != "accepted":
        errors.append("R0 case dossier lacks the authorized human acceptance")
    if human_disposition.get("reviewer") != "R. O'Shaughnessy":
        errors.append("R0 case dossier has the wrong approving human identity")
    if human_disposition.get("recorded_by") != "Codex (OpenAI), on behalf of R. O'Shaughnessy":
        errors.append("R0 case dossier has the wrong requested recorder attribution")
    determination_ids = {
        item.get("id") for item in dossier.get("required_human_determinations", [])
    }
    if determination_ids != {f"HD-{index:02d}" for index in range(1, 7)}:
        errors.append("R0 case dossier must contain exactly human determinations HD-01 through HD-06")
    if not all(
        item.get("machine_answer_prohibited") is True
        for item in dossier.get("required_human_determinations", [])
    ):
        errors.append("R0 case dossier must prohibit machine answers to scientific determinations")
    if signoff.get("human_scientific_review", {}).get("dossier") != "scientific-review-dossier.json":
        errors.append("R0 case sign-off record does not point to the scientific review dossier")
    if signoff.get("human_scientific_review", {}).get("completed_review") != "scientific-review-completed-2026-08-29.md":
        errors.append("R0 case sign-off record does not point to the completed human review")
    replay = json.loads((CASE / "independent-replay-report.json").read_text())
    if replay.get("actor", {}).get("human_gravitational_wave_authority") is not False:
        errors.append("R0 separate-executor report must not claim human GW authority")
    dimensions = replay.get("independence_dimensions", {})
    if dimensions.get("fresh_checkout_custody") != "yes":
        errors.append("R0 separate-executor report lacks fresh-checkout custody")
    for shared_dimension in [
        "independent_implementation",
        "independent_scientific_libraries",
        "independent_input_or_calibration",
        "independent_institution_or_governance",
        "independent_human_scientific_judgment",
    ]:
        if not str(dimensions.get(shared_dimension, "")).startswith("no"):
            errors.append(f"R0 replay overstates independence dimension: {shared_dimension}")
    resources = json.loads((CASE / "artifacts/provenance/resource-declaration.json").read_text())
    if set(resources.get("axes", {})) != RESOURCE_AXES:
        errors.append("R0 case resource declaration must contain exactly the ten canonical axes")
    lifecycle = json.loads((CASE / "lifecycle-events.json").read_text())
    if lifecycle.get("append_only") is not True:
        errors.append("R0 case lifecycle must be append-only")
    packet_index = json.loads((CASE / "packet-index.json").read_text())
    for entry in packet_index.get("entries", []):
        indexed = CASE / entry["path"]
        if not indexed.is_file() or sha256(indexed) != entry["sha256"]:
            errors.append(f"R0 case packet-index mismatch: {entry['path']}")

    hpc_case_files = [
        "README.md",
        "Makefile",
        "run_case.py",
        "test_case.py",
        "claim-manifest.json",
        "source-manifest.json",
        "resource-declaration.json",
        "assessment-modes.json",
        "trust-boundaries.json",
        "freshness-policy.json",
        "lifecycle-events.json",
        "restricted-attestation-template.json",
        "review-checklist.md",
        "packet-index.json",
        "artifacts/partition-digests.json",
        "artifacts/aggregate-posterior.json",
        "artifacts/claim-evidence.json",
        "artifacts/run-record.json",
    ]
    for path in hpc_case_files:
        require(str((HPC_CASE / path).relative_to(ROOT)), errors)

    hpc_claim = json.loads((HPC_CASE / "claim-manifest.json").read_text())
    if hpc_claim.get("archive_status") != "UNMINTED":
        errors.append("sanitized HPC case must remain UNMINTED until human archival approval")
    hpc_sources = json.loads((HPC_CASE / "source-manifest.json").read_text())
    for record in hpc_sources.get("sources", []):
        source = HPC_CASE / record["path"]
        if not source.is_file() or sha256(source) != record["sha256"]:
            errors.append(f"sanitized HPC source identity mismatch: {record.get('partition_id')}")
    hpc_resources = json.loads((HPC_CASE / "resource-declaration.json").read_text())
    if set(hpc_resources.get("axes", {})) != RESOURCE_AXES:
        errors.append("sanitized HPC case resource declaration must contain exactly the ten canonical axes")
    hpc_run = json.loads((HPC_CASE / "artifacts/run-record.json").read_text())
    if hpc_resources.get("axes", {}).get("wall_clock", {}).get("downselect_observed_seconds") != hpc_run.get("wall_clock_seconds"):
        errors.append("sanitized HPC observed wall-clock declaration must match the run record")
    hpc_evidence = json.loads((HPC_CASE / "artifacts/claim-evidence.json").read_text())
    if hpc_evidence.get("machine_disposition") != "verified-for-sanitized-downselect-only":
        errors.append("sanitized HPC claim evidence must retain its bounded machine disposition")
    hpc_modes = json.loads((HPC_CASE / "assessment-modes.json").read_text()).get("modes", [])
    expected_modes = {
        "full-independent-execution",
        "bounded-recomputation",
        "digest-audit",
        "restricted-platform-attestation",
        "frozen-output-inspection",
        "independent-evidence-path",
    }
    if {item.get("id") for item in hpc_modes} != expected_modes:
        errors.append("sanitized HPC case must declare exactly the six canonical assessment modes")
    if sum(str(item.get("status", "")).startswith("performed") for item in hpc_modes) != 3:
        errors.append("sanitized HPC case must record exactly three performed assessment modes")
    if next((item.get("status") for item in hpc_modes if item.get("id") == "full-independent-execution"), None) != "not-performed":
        errors.append("sanitized HPC case must not report full independent execution")
    if next((item.get("status") for item in hpc_modes if item.get("id") == "independent-evidence-path"), None) != "not-performed":
        errors.append("sanitized HPC case must not report an independent evidence path")
    attestation = json.loads((HPC_CASE / "restricted-attestation-template.json").read_text())
    if attestation.get("status") != "TEMPLATE_ONLY_NOT_AN_ATTESTATION":
        errors.append("sanitized HPC attestation must remain an unexecuted template")
    hpc_lifecycle = json.loads((HPC_CASE / "lifecycle-events.json").read_text())
    if hpc_lifecycle.get("append_only") is not True:
        errors.append("sanitized HPC case lifecycle must be append-only")
    hpc_packet_index = json.loads((HPC_CASE / "packet-index.json").read_text())
    for entry in hpc_packet_index.get("entries", []):
        indexed = HPC_CASE / entry["path"]
        if not indexed.is_file() or sha256(indexed) != entry["sha256"]:
            errors.append(f"sanitized HPC packet-index mismatch: {entry['path']}")

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
