"""Optional publication figures from saved synthetic results; requires Matplotlib.

Run from the packet root: python3 surfaces/make_figures.py
The core reproduction suite does not import this optional dependency.
"""
from pathlib import Path
import hashlib
import json
import os

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "build/matplotlib-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = ROOT / "results/figures"
COLORS = {"group_first": "#087f82", "naive": "#a84c32", "A_only": "#575394",
          "uniform": "#5c6b74", "bounded": "#087f82", "prestige": "#a84c32"}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.fonttype": "none", "svg.hashsalt": "mcrp-release-2026-09-25",
                         "figure.facecolor": "white", "axes.labelcolor": "#23373a",
                         "text.color": "#23373a", "axes.titleweight": "bold"})
    coupled_path = ROOT / "models/coupled/results/summary.json"
    ecology_path = ROOT / "models/ecology/results/summary.json"
    coupled = json.loads(coupled_path.read_text())
    ecology = json.loads(ecology_path.read_text())
    stages = ["initial", "selected", "reserved", "completed", "relied"]
    rows = coupled["scenario_results"]
    selected = {}
    for policy, reliance, label in [("group_first", "all", "Group-first"),
                                    ("naive", "all", "Representative-first"),
                                    ("group_first", "A_only", "Group-first + A-only reliance")]:
        candidates = [r for r in rows if r["policy"] == policy and r["retry"] == "reroll"
                      and r["clones"] == 100 and r["capacity"] == 20
                      and not r["reserve_repair"] and not r["hidden_control"]
                      and r["reliance_filter"] == reliance]
        assert len(candidates) == 1
        selected[label] = candidates[0]
    fig, ax = plt.subplots(figsize=(8, 4.6), layout="constrained")
    for (label, row), key in zip(selected.items(), ["group_first", "naive", "A_only"]):
        values = [row["A_" + stage + "_share"] for stage in stages]
        ax.plot(range(5), values, marker="o", label=label, color=COLORS[key], linewidth=2,
                linestyle="--" if key == "A_only" else "-")
    ax.axhline(2/3, color="#adb8ba", linewidth=1, linestyle=":")
    ax.set(xticks=range(5), xticklabels=["Initial panel", "All selections", "Reserved", "Completed", "Relied"],
           ylim=(0, 1.06), ylabel="Share of panels containing declared group A",
           title="An invitation rule does not bind later selection")
    ax.legend(loc="lower left", frameon=False, fontsize=9)
    fig.text(.01, -.035, "Synthetic: 100 replicates × 12 requests; 100 A labels; reroll retries; 20 hours/person.\nPooled stage shares are descriptive; requests compete for capacity. Dotted line: 2/3 group-first initial probability.", fontsize=8)
    save(fig, "selection-through-stages")
    lookup = {(r["regime"], r["policy"]): r for r in ecology["aggregate"]}
    policies = ["uniform", "bounded", "prestige"]
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.2), layout="constrained")
    specs = [("overload", "minimum_group_coverage", "Coverage of the least-served group", (0, 1)),
             ("overload", "correct_checks_per_offer", "Correct checks per offered task", (0, 1)),
             ("blind_common_cause", "defect_detection_fraction", "Detection with shared blindness", (0, 1))]
    chart_data = []
    for ax, (regime, metric, title, limits) in zip(axes, specs):
        for i, policy in enumerate(policies):
            values = lookup[regime, policy]["summaries"][metric]
            ax.errorbar(i, values["mean"], yerr=[[values["mean"]-values["min"]], [values["max"]-values["mean"]]],
                        fmt="o", markersize=7, capsize=5, color=COLORS[policy], linewidth=1.7)
            chart_data.append({"regime": regime, "policy": policy, "metric": metric, **values})
        ax.set(xticks=range(3), xticklabels=["Uniform", "Bounded\ncredit", "Prestige"], ylim=limits,
               title=title, ylabel="Fraction")
        ax.grid(axis="y", color="#e3e8e7", linewidth=.6)
        ax.set_axisbelow(True)
    fig.text(.01, -.045, "Synthetic attention ecology: 8 paired seeds, 80 periods. Points: seed means; whiskers: seed min–max, not confidence intervals.\nDifferent metrics favor different choices. Defect rates and behavior are stipulated, not learned from people.", fontsize=8)
    save(fig, "ecology-tradeoffs")
    manifest = {"schema": "mcrp.figure-evidence.v1", "matplotlib": matplotlib.__version__,
                "inputs": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in [coupled_path, ecology_path, Path(__file__)]},
                "selection_rows": selected, "ecology_points": chart_data,
                "figures": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted(OUT.iterdir()) if p.suffix in {".svg", ".png"}}}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"figures": sorted(manifest["figures"]), "matplotlib": matplotlib.__version__}))


def save(fig, name):
    fig.savefig(OUT / (name + ".svg"), bbox_inches="tight", metadata={"Date": None})
    fig.savefig(OUT / (name + ".png"), bbox_inches="tight", dpi=180, metadata={"Software": "Matplotlib"})
    plt.close(fig)


if __name__ == "__main__":
    main()
