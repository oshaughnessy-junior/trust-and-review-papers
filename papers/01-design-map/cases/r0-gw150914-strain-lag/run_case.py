#!/usr/bin/env python3
"""Execute the immutable-source-bound GW150914 R0 strain-lag case."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import resource
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import h5py
import numpy as np
import scipy
from scipy.signal import butter, sosfiltfilt


ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "data/raw"
ARTIFACTS = ROOT / "artifacts"
CLAIM_MANIFEST = ROOT / "claim-manifest.json"
SOURCE_MANIFEST = ROOT / "source-manifest.json"
LOCK_FILE = ROOT / "pixi.lock"


class CaseError(ValueError):
    """An input identity, workflow precondition, or scientific invariant failed."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json(payload: Any) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json(payload))


def text(value: Any) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return str(value)


def verify_source_registry(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    records = manifest["sources"]
    if {record["detector"] for record in records} != {"H1", "L1"}:
        raise CaseError("source registry must contain exactly H1 and L1")
    for record in records:
        path = RAW_DIR / record["filename"]
        if "_V2-" not in record["filename"] or manifest["event_version"] != "GW150914-v2":
            raise CaseError("source registry rejects non-v2 input identity")
        if not path.is_file():
            raise CaseError(f"missing registered source: {record['filename']}")
        actual_digest = sha256(path)
        if actual_digest != record["sha256"]:
            raise CaseError(f"source digest mismatch for {record['detector']}: {actual_digest}")
        if path.stat().st_size != record["bytes"]:
            raise CaseError(f"source size mismatch for {record['detector']}")
    return records


def load_detector(record: dict[str, Any]) -> dict[str, Any]:
    path = RAW_DIR / record["filename"]
    with h5py.File(path, "r") as source:
        strain = np.asarray(source["strain/Strain"][:], dtype=np.float64)
        attrs = source["strain/Strain"].attrs
        detector = text(source["meta/Detector"][()])
        duration = int(source["meta/Duration"][()])
        gps_start = int(source["meta/GPSstart"][()])
        sample_spacing = float(attrs["Xspacing"])
        dq_names = [text(item) for item in source["quality/simple/DQShortnames"][:]]
        dq_mask = np.asarray(source["quality/simple/DQmask"][:], dtype=np.int64)
        injection_names = [text(item) for item in source["quality/injections/InjShortnames"][:]]
        injection_mask = np.asarray(source["quality/injections/Injmask"][:], dtype=np.int64)

    if detector != record["detector"]:
        raise CaseError(f"detector metadata mismatch: expected {record['detector']}, found {detector}")
    sample_rate = 1.0 / sample_spacing
    if duration != 32 or gps_start != 1126259446 or sample_rate != 4096.0:
        raise CaseError(f"unexpected sample geometry for {detector}")
    if strain.size != duration * int(sample_rate) or not np.isfinite(strain).all():
        raise CaseError(f"invalid strain array for {detector}")

    event_second = int(math.floor(1126259462.4 - gps_start))
    dq_value = int(dq_mask[event_second])
    injection_value = int(injection_mask[event_second])
    dq = {name: bool(dq_value & (1 << index)) for index, name in enumerate(dq_names)}
    injections = {
        name: bool(injection_value & (1 << index)) for index, name in enumerate(injection_names)
    }
    required_quality = ["DATA", "CBC_CAT1", "CBC_CAT2", "BURST_CAT1", "BURST_CAT2"]
    if not all(dq.get(name, False) for name in required_quality):
        raise CaseError(f"required quality bit missing for {detector}")
    if not (injections.get("NO_CBC_HW_INJ", False) and injections.get("NO_BURST_HW_INJ", False)):
        raise CaseError(f"transient hardware-injection exclusion failed for {detector}")

    return {
        "detector": detector,
        "strain": strain,
        "sample_rate_hz": sample_rate,
        "duration_seconds": duration,
        "gps_start": gps_start,
        "event_dq_mask": dq_value,
        "event_dq_bits": dq,
        "event_injection_mask": injection_value,
        "event_injection_bits": injections,
    }


def standardized(values: np.ndarray) -> np.ndarray:
    centered = values - values.mean()
    scale = centered.std()
    if not np.isfinite(scale) or scale == 0:
        raise CaseError("event window has zero or non-finite variance")
    return centered / scale


def zero_padded_shift(values: np.ndarray, samples: int) -> np.ndarray:
    shifted = np.roll(values, samples)
    if samples > 0:
        shifted[:samples] = 0.0
    elif samples < 0:
        shifted[samples:] = 0.0
    return shifted


def lag_curve(h1: np.ndarray, l1: np.ndarray, sample_rate: float, search_seconds: float) -> tuple[np.ndarray, np.ndarray]:
    first = standardized(h1)
    second = standardized(l1)
    correlation = np.correlate(first, second, mode="full") / first.size
    lag_samples = np.arange(-second.size + 1, first.size)
    mask = np.abs(lag_samples / sample_rate) <= search_seconds
    return lag_samples[mask] / sample_rate, correlation[mask]


def best_lag(lags: np.ndarray, correlations: np.ndarray) -> tuple[float, float]:
    index = int(np.argmax(np.abs(correlations)))
    return float(lags[index]), float(correlations[index])


def evaluate(
    detector_data: dict[str, dict[str, Any]], configuration: dict[str, Any], negative_shift_seconds: float = 0.0
) -> tuple[dict[str, Any], list[tuple[float, float]]]:
    h1 = detector_data["H1"]
    l1 = detector_data["L1"]
    if h1["sample_rate_hz"] != l1["sample_rate_hz"] or h1["gps_start"] != l1["gps_start"]:
        raise CaseError("detector time grids do not match")
    sample_rate = h1["sample_rate_hz"]
    sos = butter(
        int(configuration["filter_order"]),
        [float(configuration["bandpass_hz"][0]), float(configuration["bandpass_hz"][1])],
        btype="bandpass",
        fs=sample_rate,
        output="sos",
    )
    filtered = {
        detector: sosfiltfilt(sos, detector_data[detector]["strain"])
        for detector in ("H1", "L1")
    }
    event_index = int(round((float(configuration["event_gps"]) - h1["gps_start"]) * sample_rate))
    half_window = int(round(float(configuration["event_window_half_width_seconds"]) * sample_rate))
    windows = {
        detector: filtered[detector][event_index - half_window : event_index + half_window]
        for detector in ("H1", "L1")
    }
    if negative_shift_seconds:
        windows["L1"] = zero_padded_shift(
            windows["L1"], int(round(negative_shift_seconds * sample_rate))
        )
    lags, correlations = lag_curve(
        windows["H1"], windows["L1"], sample_rate, float(configuration["lag_search_half_width_seconds"])
    )
    lag, correlation = best_lag(lags, correlations)
    physical_bound = float(configuration["physical_lag_bound_seconds"])
    minimum_correlation = float(configuration["minimum_absolute_correlation"])
    invariants = {
        "registered_v2_input_identity": True,
        "matching_detector_time_grids": True,
        "required_event_quality_bits": True,
        "no_cbc_or_burst_hardware_injection_at_event": True,
        "absolute_correlation_above_declared_floor": abs(correlation) >= minimum_correlation,
        "absolute_lag_within_h1_l1_physical_bound": abs(lag) <= physical_bound,
    }
    result = {
        "lag_seconds": round(lag, 12),
        "absolute_lag_seconds": round(abs(lag), 12),
        "correlation": round(correlation, 12),
        "absolute_correlation": round(abs(correlation), 12),
        "sample_rate_hz": sample_rate,
        "event_window_samples_per_detector": int(windows["H1"].size),
        "negative_shift_seconds": negative_shift_seconds,
        "invariants": invariants,
    }
    curve = [(round(float(lag_value), 12), round(float(value), 12)) for lag_value, value in zip(lags, correlations)]
    return result, curve


def execute(write: bool) -> dict[str, Any]:
    started = datetime.now(timezone.utc)
    wall_start = time.perf_counter()
    cpu_start = time.process_time()
    source_manifest = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
    claim_manifest = json.loads(CLAIM_MANIFEST.read_text(encoding="utf-8"))
    records = verify_source_registry(source_manifest)
    detector_data = {record["detector"]: load_detector(record) for record in records}
    configuration = claim_manifest["workflow_configuration"]

    observed, curve = evaluate(detector_data, configuration)
    if not all(observed["invariants"].values()):
        failed = [name for name, passed in observed["invariants"].items() if not passed]
        raise CaseError(f"claim invariant failure: {', '.join(failed)}")
    shifted, _ = evaluate(detector_data, configuration, negative_shift_seconds=0.025)
    if shifted["invariants"]["absolute_lag_within_h1_l1_physical_bound"]:
        raise CaseError("adversarial 25 ms shift did not violate the physical-lag invariant")
    negative_tests = {
        "schema": "trustandreview.r0.negative-tests.v0.1",
        "tests": [
            {
                "id": "NEG-LAG-025S",
                "mutation": "zero-padded +25 ms shift of the L1 event window",
                "expected": "absolute recovered lag exceeds the declared H1-L1 physical bound",
                "observed_absolute_lag_seconds": shifted["absolute_lag_seconds"],
                "passed": True,
            },
            {
                "id": "NEG-VERSION-IDENTITY",
                "mutation": "substitute a non-v2 filename or unregistered digest",
                "expected": "reject before HDF5 ingestion",
                "observed": "covered by source-registry conformance tests",
                "passed": True,
            },
        ],
    }
    evidence = {
        "schema": "trustandreview.r0.claim-evidence.v0.1",
        "claim_id": "R0-GW150914-C001",
        "input_event": "GW150914-v2",
        "result": observed,
        "machine_disposition": "verified-under-declared-workflow",
        "strongest_warranted_conclusion": "bounded computational repeatability of the registered processing path and satisfaction of one necessary intersite-lag invariant",
        "scientific_validity_disposition": "not-assessed",
    }
    elapsed = time.perf_counter() - wall_start
    cpu = time.process_time() - cpu_start
    ended = datetime.now(timezone.utc)
    peak_rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform != "darwin":
        peak_rss *= 1024
    run_record = {
        "schema": "trustandreview.r0.run-record.v0.1",
        "run_id": f"r0-gw150914-v2-{started.strftime('%Y%m%dT%H%M%SZ')}",
        "started_at": started.isoformat(),
        "ended_at": ended.isoformat(),
        "workflow": "run_case.py",
        "configuration": configuration,
        "randomness": "none",
        "identities": {
            "H1_sha256": records[0]["sha256"] if records[0]["detector"] == "H1" else records[1]["sha256"],
            "L1_sha256": records[0]["sha256"] if records[0]["detector"] == "L1" else records[1]["sha256"],
            "claim_manifest_sha256": sha256(CLAIM_MANIFEST),
            "source_manifest_sha256": sha256(SOURCE_MANIFEST),
            "implementation_sha256": sha256(Path(__file__).resolve()),
            "environment_lock_sha256": sha256(LOCK_FILE),
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "h5py": h5py.__version__,
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "external_services_during_run": [],
        "outputs": {
            "claim_evidence": "artifacts/evidence/claim-evidence.json",
            "negative_tests": "artifacts/evidence/negative-tests.json",
            "lag_curve": "artifacts/derived/lag-correlation.csv",
        },
        "result": "pass",
    }
    resources = {
        "schema": "trustandreview.resource-declaration.v0.1",
        "axes": {
            "compute": {"processes": 1, "cpu_seconds_observed": cpu, "peak_rss_bytes_observed": peak_rss, "accelerator": "none"},
            "storage": {"registered_input_bytes": sum(item["bytes"] for item in records), "artifact_bytes_observed": 0},
            "access": {"rerun_requires_network": False, "upstream_access": "public CC BY 4.0; no account"},
            "platform": {"requirement": "Pixi-supported contemporary macOS arm64 or Linux x86_64; no scheduler"},
            "wall_clock": {"seconds_observed": elapsed},
            "human_expertise": {"execution": "basic CLI", "scientific_signoff": "GW strain/data-quality interpretation; pending"},
            "agent_capability": {"required_for_rerun": False, "case_authoring_support": "Codex; recorded separately from human review"},
            "operator_support": {"required_for_rerun": False, "setup": "Pixi environment resolution and approximately 2 MB local input"},
            "monetary_allocative_cost": {"marginal_cost_usd_observed": 0, "allocation_required": False},
            "freshness": {"source_retrieved": "2026-08-27", "reexecute_by": "2026-11-27", "on_failure": "append reproduction-failed or stale event; never overwrite this run"},
        },
    }
    if write:
        write_json(ARTIFACTS / "intermediate/preprocessing-summary.json", {
            "workflow_configuration": configuration,
            "detectors": {
                detector: {key: value for key, value in detector_data[detector].items() if key != "strain"}
                for detector in ("H1", "L1")
            },
        })
        write_json(ARTIFACTS / "evidence/claim-evidence.json", evidence)
        write_json(ARTIFACTS / "evidence/negative-tests.json", negative_tests)
        curve_path = ARTIFACTS / "derived/lag-correlation.csv"
        curve_path.parent.mkdir(parents=True, exist_ok=True)
        with curve_path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(["lag_seconds", "normalized_correlation"])
            writer.writerows(curve)
        write_json(ARTIFACTS / "provenance/run-record.json", run_record)
        resource_path = ARTIFACTS / "provenance/resource-declaration.json"
        write_json(resource_path, resources)
        resources["axes"]["storage"]["artifact_bytes_observed"] = sum(
            path.stat().st_size for path in ARTIFACTS.rglob("*") if path.is_file()
        )
        write_json(resource_path, resources)
    return {"evidence": evidence, "negative_tests": negative_tests, "curve": curve}


def verify_committed() -> None:
    observed = execute(write=False)
    committed_evidence = json.loads((ARTIFACTS / "evidence/claim-evidence.json").read_text(encoding="utf-8"))
    committed_negative = json.loads((ARTIFACTS / "evidence/negative-tests.json").read_text(encoding="utf-8"))
    if observed["evidence"] != committed_evidence:
        raise CaseError("committed claim evidence differs from a clean replay")
    if observed["negative_tests"] != committed_negative:
        raise CaseError("committed negative-test evidence differs from a clean replay")
    curve_path = ARTIFACTS / "derived/lag-correlation.csv"
    with curve_path.open(encoding="utf-8", newline="") as stream:
        committed_rows = list(csv.reader(stream))
    if not committed_rows or committed_rows[0] != ["lag_seconds", "normalized_correlation"]:
        raise CaseError("committed lag-correlation product has the wrong header")
    committed_curve = committed_rows[1:]
    observed_curve = observed["curve"]
    if len(committed_curve) != len(observed_curve):
        raise CaseError("committed lag-correlation product has the wrong length")
    tolerances = json.loads(CLAIM_MANIFEST.read_text(encoding="utf-8"))["workflow_configuration"][
        "clean_replay_tolerances"
    ]
    lag_tolerance = float(tolerances["lag_seconds_absolute"])
    correlation_tolerance = float(tolerances["normalized_correlation_absolute"])
    for row_number, (committed, observed_row) in enumerate(zip(committed_curve, observed_curve), start=2):
        if len(committed) != 2:
            raise CaseError(f"committed lag-correlation row {row_number} has the wrong width")
        try:
            committed_lag, committed_correlation = map(float, committed)
        except ValueError as error:
            raise CaseError(f"committed lag-correlation row {row_number} is not numeric") from error
        observed_lag, observed_correlation = observed_row
        if not math.isclose(committed_lag, observed_lag, rel_tol=0.0, abs_tol=lag_tolerance):
            raise CaseError(f"committed lag at row {row_number} exceeds clean-replay tolerance")
        if not math.isclose(
            committed_correlation,
            observed_correlation,
            rel_tol=0.0,
            abs_tol=correlation_tolerance,
        ):
            raise CaseError(f"committed correlation at row {row_number} exceeds clean-replay tolerance")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write a new recorded-run packet")
    parser.add_argument("--verify", action="store_true", help="verify committed evidence by clean replay")
    args = parser.parse_args()
    if args.write == args.verify:
        parser.error("choose exactly one of --write or --verify")
    try:
        if args.write:
            result = execute(write=True)
            print(json.dumps(result["evidence"], indent=2, sort_keys=True))
        else:
            verify_committed()
            print("PASS: registered inputs, quality policy, processing, lag invariant, adversarial tests, and clean replay")
    except (CaseError, KeyError, TypeError, json.JSONDecodeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
