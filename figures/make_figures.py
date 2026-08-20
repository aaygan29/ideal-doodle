"""Regenerate all figures from design (schematics) and results/*.json (result figures).

Rule: no figure is hand-edited. Schematic figures are built from the fixed design here;
result figures render only when their results JSON exists. Run: python figures/make_figures.py
"""
from __future__ import annotations

import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RESULTS = os.path.join(ROOT, "results")

# colorblind-safe (Okabe-Ito)
CB = {"blue": "#0072B2", "orange": "#E69F00", "green": "#009E73",
      "red": "#D55E00", "purple": "#CC79A7", "grey": "#999999", "black": "#000000"}


def _box(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
                                linewidth=1.5, edgecolor=CB["black"], facecolor=color, alpha=0.25))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9, wrap=True)


def _arrow(ax, x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                 mutation_scale=14, linewidth=1.4, color=CB["black"]))


def fig1_architecture():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); ax.axis("off")
    ax.set_title("Fig 1. AIM-DDM decision-phenotype estimator with honesty layer",
                 fontsize=12, weight="bold")
    _box(ax, 0.2, 3.9, 2.2, 1.1, "Event c\n(stakes, gain/loss,\nambiguity, threat,\ntime, reference)", CB["grey"])
    _box(ax, 0.2, 1.9, 2.2, 1.1, "Neural populations\nfMRI: NAcc/insula\nEEG: Cue-P3/CNV", CB["blue"])
    _box(ax, 3.0, 3.6, 2.4, 1.6, "Affective channel\n(rho_gain, lambda_loss,\nomega_threat)\nPOPULATION prior", CB["orange"])
    _box(ax, 3.0, 0.3, 2.4, 1.6, "Integrative channel\n(kappa_risk, delta_time,\ntau_consistency)\nPER-AGENT", CB["green"])
    _box(ax, 5.9, 2.1, 1.9, 1.4, "DDM likelihood\nV -> drift,\ncaution -> boundary", CB["purple"])
    _box(ax, 8.0, 2.1, 1.8, 1.4, "Honesty layer\nproper score +\nconformal set +\nMDES abstain", CB["red"])
    _arrow(ax, 2.4, 4.4, 3.0, 4.4)
    _arrow(ax, 2.4, 2.4, 3.0, 1.1)
    _arrow(ax, 2.4, 2.4, 3.0, 4.2)
    _arrow(ax, 5.4, 4.2, 6.85, 3.5)
    _arrow(ax, 5.4, 1.1, 6.85, 2.4)
    _arrow(ax, 7.8, 2.8, 8.0, 2.8)
    ax.text(8.9, 1.9, "predict OR abstain", ha="center", fontsize=8, style="italic", color=CB["red"])
    fig.tight_layout()
    out = os.path.join(HERE, "fig1_architecture.png")
    fig.savefig(out, dpi=150, bbox_inches="tight"); plt.close(fig)
    return out


def fig_claim_gate_map():
    claims = [
        ("C1 identifiable AIM-DDM phenotype", "T4/T5", "synthetic recovery", CB["green"]),
        ("C2 honest-by-construction (conformal+score+abstain)", "T4/T5", "math + sim", CB["green"]),
        ("C3 affective > behavioral transfer", "T3->T4", "NARPS + DEAP", CB["orange"]),
        ("C4 pooling lowers MDES", "T4", "joint fit", CB["orange"]),
        ("C5 predict-or-abstain on confounded targets", "T4", "public-figure corpus (prereg)", CB["red"]),
    ]
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, len(claims) + 0.5); ax.axis("off")
    ax.set_title("Claim -> evidence tier -> where tested (survivors of Council review)",
                 fontsize=12, weight="bold")
    for i, (name, tier, where, color) in enumerate(claims):
        y = len(claims) - i - 0.5
        _box(ax, 0.2, y, 5.6, 0.8, name, color)
        _box(ax, 6.0, y, 1.4, 0.8, tier, CB["grey"])
        _box(ax, 7.6, y, 2.3, 0.8, where, CB["blue"])
    fig.tight_layout()
    out = os.path.join(HERE, "fig_claim_gate_map.png")
    fig.savefig(out, dpi=150, bbox_inches="tight"); plt.close(fig)
    return out


def _result_figs():
    """Render result figures only for experiments whose JSON exists."""
    made = []
    # placeholder hooks; each renders when results/<name>.json appears
    mapping = {
        "e1_recovery.json": "fig2_recovery.png",
        "e2_coverage.json": "fig3_coverage.png",
        "e3_transfer_narps.json": "fig4_transfer.png",
        "e4_pooling.json": "fig5_pooling.png",
        "e5_abstention.json": "fig6_abstention.png",
    }
    for src, out in mapping.items():
        p = os.path.join(RESULTS, src)
        if os.path.exists(p):
            with open(p) as fh:
                json.load(fh)  # validated; per-figure renderers added as experiments land
            made.append(f"(result JSON present for {src}; renderer to be added with the experiment)")
    return made


if __name__ == "__main__":
    outs = [fig1_architecture(), fig_claim_gate_map()]
    outs += _result_figs()
    for o in outs:
        print("wrote", o)
