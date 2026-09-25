"""Reproduce the release packet from its root, including an extracted export.

Run: python3 run_checks.py
No network, credentials or third-party Python packages are required.
"""
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_input_inventory(root=ROOT):
    """Inputs that must remain unchanged throughout a reproduction run."""
    paths = {p for p in root.rglob("*.py") if not any(part in {"build", "__pycache__"} for part in p.relative_to(root).parts)}
    paths.update(p for p in (root / "adapters/fixtures").glob("*") if p.is_file())
    for name in ("domains/fixtures/scenarios.json", "reviews/red-math/original_completion.json"):
        fixture = root / name
        if fixture.is_file():
            paths.add(fixture)
    if any(p.is_symlink() for p in paths):
        raise ValueError("source/input symlink is not a frozen input")
    return {str(p.relative_to(root)): sha(p) for p in sorted(paths)}


def evidence_inventory(root=ROOT):
    """Bind saved evidence, without treating a hash as proof of its meaning."""
    paths = set()
    for folder in ("toy_agents", "models", "domains/fixtures", "adapters", "results"):
        for p in (root / folder).rglob("*"):
            if p.is_file() and p.suffix in {".json", ".csv", ".svg", ".png", ".pdf"} and p != root / "results/validation.json":
                paths.add(p)
    return {str(p.relative_to(root)): sha(p) for p in sorted(paths)}


def main():
    RESULTS.mkdir(exist_ok=True)
    logs = RESULTS / "check-logs"
    logs.mkdir(exist_ok=True)
    suites = [
        ("toy-protocol", "toy_agents/tests", "test_*.py"),
        ("release-cycle", "models", "test_release_cycle.py"),
        ("conditional-math", "models/math", "test_*.py"),
        ("domain-cases", "domains/fixtures", "test_*.py"),
        ("runtime-red-regressions", "reviews/red-runtime", "test_*.py"),
        ("legacy-adapter", "adapters/tests", "test_*.py"),
    ]
    for name, folder in [("coupled-agents", "models/coupled"), ("local-rule-ecology", "models/ecology/tests"), ("human-interface-design", "models/human_pilot"), ("funded-audit-delivery", "models/funded_audits")]:
        if (ROOT / folder).is_dir():
            suites.append((name, folder, "test_*.py"))
    commands = [(n, ["-m", "unittest", "discover", "-s", folder, "-p", pattern, "-v"], None)
                for n, folder, pattern in suites]
    commands.append(("ecology-sweeps", ["-m", "models.ecology.run"], None))
    commands.append(("correction-game", ["-m", "models.ecology.correction_game"], None))
    commands.append(("legacy-adapter-demo", ["-m", "adapters.demo"], None))
    if (ROOT / "models/human_pilot/run_design.py").is_file():
        commands.append(("human-design-calculations", ["models/human_pilot/run_design.py"], None))
    commands += [
        ("toy-traces", ["-m", "toy_agents.run"], None),
        ("release-trace", ["models/release_cycle.py", "--output", "results/release-cycle.json"], None),
        ("math-sweeps", ["models/math/run_experiments.py"], None),
        ("domain-oracles", ["domains/fixtures/domain_models.py"], "domains/fixtures/oracle-results.json"),
        ("domain-replays", ["domains/fixtures/replay_receipts.py"], "domains/fixtures/replay-results.json"),
        ("adversarial-math", ["reviews/red-math/probes.py"], "results/adversarial-math.json"),
        ("adversarial-domain", ["reviews/red-domains-law/counterexamples.py"], "results/adversarial-domain.json"),
    ]
    for name, folder in [("coupled-sweeps", "models/coupled"), ("ecology-sweeps", "models/ecology"), ("funded-audit-sweeps", "models/funded_audits")]:
        if (ROOT / folder / "run_experiments.py").is_file():
            commands.append((name, [folder + "/run_experiments.py"], None))
    before = source_input_inventory()
    records, tests = [], 0
    for name, args, destination in commands:
        result = subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True)
        combined = (result.stdout + result.stderr).replace(str(ROOT), "<packet>")
        log = logs / (name + ".txt")
        log.write_text(combined)
        passed = result.returncode == 0
        found = re.search(r"Ran (\d+) tests? in", combined)
        count = int(found.group(1)) if found else 0
        tests += count
        if destination and passed:
            # Refuse to record non-JSON text as a machine result.
            parsed = json.loads(result.stdout)
            (ROOT / destination).write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n")
        records.append({"name": name, "args": args, "passed": passed,
                        "test_methods": count, "log": str(log.relative_to(ROOT)), "log_sha256": sha(log)})
        print(name + (": PASS" if passed else ": FAIL"), flush=True)
        if not passed:
            print(combined, file=sys.stderr)
            break
    # Refresh domain provenance using packet-relative paths valid in the export.
    domain_files = list((ROOT / "domains/fixtures").glob("*.py")) + [
        ROOT / "domains/fixtures/scenarios.json", ROOT / "domains/fixtures/oracle-results.json",
        ROOT / "domains/fixtures/replay-results.json", ROOT / "toy_agents/protocol.py"]
    (ROOT / "domains/fixtures/run-manifest.json").write_text(json.dumps({
        "schema": "mcrp-domain-run/2", "synthetic_only": True,
        "python": platform.python_version(),
        "sha256": {str(p.relative_to(ROOT)): sha(p) for p in sorted(domain_files)},
        "commands": [r["args"] for r in records if r["name"] in {"domain-cases", "domain-oracles", "domain-replays"}]}, indent=2) + "\n")
    after = source_input_inventory()
    changed = sorted(name for name in set(before) | set(after) if before.get(name) != after.get(name))
    source = {name: value for name, value in before.items() if name.endswith(".py")}
    tables = {str(p.relative_to(ROOT)): sha(p) for p in sorted(ROOT.rglob("*.csv"))}
    ok = len(records) == len(commands) and all(r["passed"] for r in records) and not changed
    manifest = {"schema": "mcrp.release-packet-validation.v1", "passed": ok,
                "python": platform.python_version(), "test_methods": tests,
                "check_groups": records, "source_sha256": source, "table_sha256": tables,
                "tested_inputs_sha256": before, "inputs_changed_during_run": changed,
                "evidence_sha256": evidence_inventory(),
                "scope": "Synthetic/model tests and adversarial probes; no live service or human efficacy validation"}
    (RESULTS / "validation.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"{tests} test methods; {len(records)} check groups; passed={ok}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
