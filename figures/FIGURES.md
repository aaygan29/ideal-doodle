# Figures — plan

All figures regenerate from `make_figures.py`. Schematic figures (1, and the claim map) are built
from the design; result figures (2–7) are built from `results/*.json` and only render once the
corresponding experiment has produced numbers. No figure is ever hand-edited. Each figure states
one takeaway in its caption (Gate F).

| Fig | Title | Source | Status |
|---|---|---|---|
| 1 | Architecture: AIM-DDM manifold + honesty layer | schematic | **generated** |
| — | Claim -> gate -> evidence-tier map | schematic | **generated** (`fig_claim_gate_map.png`) |
| 2 | Parameter recovery (recovered vs true theta, 20 seeds) | `results/e1_recovery.json` | pending E1 |
| 3 | Conformal coverage vs nominal + reliability diagram | `results/e2_coverage.json` | pending E2 |
| 4 | Affective vs behavioral forecast arms (ΔCRPS + CI), NARPS & DEAP | `results/e3_transfer_*.json` | pending E3 |
| 5 | Pooling buys power (MDES + posterior width, joint vs single) | `results/e4_pooling.json` | pending E4 |
| 6 | Abstention operating curve (coverage/accuracy vs abstention rate) on confounded targets | `results/e5_abstention.json` | pending E5 |
| 7 | State/role manifold (theta shifts for sad/angry; trader/cop/doctor) | `results/e6_manifold.json` | pending Step 5 |

Convention: chance/base-rate line always drawn; error bars always shown; colorblind-safe palette;
axes not truncated.
