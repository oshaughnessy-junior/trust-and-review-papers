#!/usr/bin/env python3
"""Sanitized partitioned-inference downselect fixture."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARTIFACTS = ROOT / "artifacts"


class CaseError(RuntimeError):
    pass


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict | list) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def logsumexp(values: list[float]) -> float:
    maximum = max(values)
    return maximum + math.log(sum(math.exp(value - maximum) for value in values))


def normalized(values: list[float]) -> list[float]:
    maximum = max(values)
    weights = [math.exp(value - maximum) for value in values]
    total = sum(weights)
    return [weight / total for weight in weights]


def load_partitions(source_manifest: dict, configuration: dict) -> list[dict]:
    expected_grid = configuration["theta_grid"]
    records = source_manifest["sources"]
    if len(records) != configuration["required_partition_count"]:
        raise CaseError("registered partition count mismatch")
    partitions = []
    seen = set()
    for record in records:
        path = ROOT / record["path"]
        if not path.is_file() or sha256(path) != record["sha256"]:
            raise CaseError(f"source identity failure: {record['partition_id']}")
        value = read_json(path)
        if value["partition_id"] != record["partition_id"] or value["partition_id"] in seen:
            raise CaseError("partition identity mismatch or duplicate")
        if value["theta"] != expected_grid or len(value["log_likelihood"]) != len(expected_grid):
            raise CaseError("theta grid or likelihood geometry mismatch")
        if not all(math.isfinite(float(item)) for item in value["log_likelihood"]):
            raise CaseError("non-finite likelihood")
        seen.add(value["partition_id"])
        partitions.append(value)
    return partitions


def evaluate(partitions: list[dict], configuration: dict) -> dict:
    theta = configuration["theta_grid"]
    aggregate = [sum(float(partition["log_likelihood"][i]) for partition in partitions) for i in range(len(theta))]
    probability = normalized(aggregate)
    map_theta = theta[max(range(len(theta)), key=lambda index: probability[index])]
    posterior_mean = sum(point * weight for point, weight in zip(theta, probability))
    low, high = configuration["central_theta_range"]
    central_probability = sum(weight for point, weight in zip(theta, probability) if low <= point <= high)

    halves = [partitions[: len(partitions) // 2], partitions[len(partitions) // 2 :]]
    half_means = []
    for half in halves:
        half_values = [sum(float(partition["log_likelihood"][i]) for partition in half) for i in range(len(theta))]
        half_probability = normalized(half_values)
        half_means.append(sum(point * weight for point, weight in zip(theta, half_probability)))
    split_difference = abs(half_means[0] - half_means[1])

    invariants = {
        "map_theta_matches_registered": map_theta == configuration["expected_map_theta"],
        "central_probability_above_floor": central_probability >= configuration["minimum_central_probability"],
        "split_half_mean_difference_below_ceiling": split_difference <= configuration["maximum_split_half_mean_difference"],
    }
    return {
        "theta": theta,
        "aggregate_log_likelihood": [round(value, 12) for value in aggregate],
        "posterior_probability": [round(value, 12) for value in probability],
        "map_theta": map_theta,
        "posterior_mean": round(posterior_mean, 12),
        "central_probability": round(central_probability, 12),
        "split_half_posterior_means": [round(value, 12) for value in half_means],
        "split_half_mean_difference": round(split_difference, 12),
        "invariants": invariants,
        "passed": all(invariants.values()),
    }


def partition_digests(partitions: list[dict], source_manifest: dict) -> list[dict]:
    source_by_id = {item["partition_id"]: item for item in source_manifest["sources"]}
    result = []
    for partition in partitions:
        likelihood = [float(value) for value in partition["log_likelihood"]]
        result.append({
            "partition_id": partition["partition_id"],
            "source_sha256": source_by_id[partition["partition_id"]]["sha256"],
            "argmax_theta": partition["theta"][max(range(len(likelihood)), key=lambda i: likelihood[i])],
            "log_likelihood_logsumexp": round(logsumexp(likelihood), 12),
            "digest_algorithm": "argmax plus stable logsumexp over registered theta grid",
        })
    return result


def execute(record: bool) -> dict:
    started = time.perf_counter()
    claim = read_json(ROOT / "claim-manifest.json")
    sources = read_json(ROOT / "source-manifest.json")
    partitions = load_partitions(sources, claim["configuration"])
    digests = partition_digests(partitions, sources)
    aggregate = evaluate(partitions, claim["configuration"])
    evidence = {
        "schema":"trustandreview.hpc-downselect.evidence.v0.1",
        "claim_id":claim["claim"]["id"],
        "machine_disposition":"verified-for-sanitized-downselect-only" if aggregate["passed"] else "failed",
        "strongest_warranted_conclusion":claim["claim"]["strongest_warranted_conclusion"],
        "full_scale_disposition":"not-performed",
        "restricted_attestation_disposition":"template-only",
        "result":aggregate,
    }
    run_record = {
        "schema":"trustandreview.hpc-downselect.run-record.v0.1",
        "workflow":"run_case.py",
        "platform":{"python":platform.python_version(),"system":platform.system(),"machine":platform.machine()},
        "input_digests":{item["partition_id"]:item["sha256"] for item in sources["sources"]},
        "configuration_sha256":sha256(ROOT / "claim-manifest.json"),
        "implementation_sha256":sha256(Path(__file__).resolve()),
        "randomness":"none",
        "wall_clock_seconds":round(time.perf_counter() - started, 9),
        "result":"pass" if aggregate["passed"] else "fail",
    }
    result = {"partition_digests":digests,"aggregate":aggregate,"evidence":evidence,"run_record":run_record}
    if record:
        write_json(ARTIFACTS / "partition-digests.json", digests)
        write_json(ARTIFACTS / "aggregate-posterior.json", aggregate)
        write_json(ARTIFACTS / "claim-evidence.json", evidence)
        write_json(ARTIFACTS / "run-record.json", run_record)
    return result


def verify() -> None:
    observed = execute(record=False)
    for key, filename in [
        ("partition_digests", "partition-digests.json"),
        ("aggregate", "aggregate-posterior.json"),
        ("evidence", "claim-evidence.json"),
    ]:
        if observed[key] != read_json(ARTIFACTS / filename):
            raise CaseError(f"committed {filename} differs from recomputation")
    committed_run = read_json(ARTIFACTS / "run-record.json")
    for key in ["workflow", "input_digests", "configuration_sha256", "implementation_sha256", "randomness", "result"]:
        if observed["run_record"][key] != committed_run[key]:
            raise CaseError(f"run-record identity mismatch: {key}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.record == args.verify:
        parser.error("choose exactly one of --record or --verify")
    if args.record:
        result = execute(record=True)
        if not result["aggregate"]["passed"]:
            raise CaseError("registered sanitized invariant failed")
        print("RECORDED: sanitized partition digests, aggregate posterior, evidence, and run record")
    else:
        verify()
        print("PASS: source identities, digest regeneration, aggregate invariants, and committed evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
