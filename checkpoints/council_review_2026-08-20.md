# Council Review — Neural-Grounded Computational Decision-Phenotype Model
Date: 2026-08-20. Mode: manuscript/proposal, Deep, gatekeeper stance.

## Verdict: MAJOR REVISION
Sound method and math; zero real-data results yet; the naive individual-neuroprofile claim fails
Gate 0/6/8 and is inverted into C5.

## NeurIPS-style score
- Soundness 2/4 (no real-data validation yet; one naive claim rested on no ground truth).
- Presentation 3/4 (clean affective/integrative story).
- Contribution 3/4 (AIM + conformal/proper-scoring + hierarchical pooling unified; no prior art doing all three).
- Overall 5/10 (MAJOR REVISION band).
- Confidence 4/5 (harness code read directly; sample sizes recomputed).
- Flags: reproducibility YES; ethics see Gate 10 (public-figure profiling); borderline = whether affective transfer replicates inside the unified estimator.

## Claim Ledger (naive pitch)
| # | Claim | Asserted | Actual | Status |
|---|---|---|---|---|
| A | affective transfers / integrative individuates | T4 | T3 | Gate 3/7 partial |
| B | brain beats behavior out-of-sample | T4 | T3 | small-n, contested |
| C | conformal+scoring = honest abstaining forecasts | T4 | T4->T5 | Gate T pass |
| D | pooling fixes underpowering | T3 | T3 (provable->T4) | needs run |
| E | predict a leader's actions from their neurology | T4 | T1 | Gate 0/8 FAIL |

## Gate ladder
- Gate 0 Provenance [Aragorn] FAIL (leader arm: no neural ground truth; coded labels), PASS elsewhere (NARPS/DEAP real).
- Gate 1 Variance [Gandalf] N/A yet; mandate >=20 seeds (source lit n~28-39 subj, ~30-140 items = seed-variance danger zone).
- Gate 2 Spec robustness [Gandalf] N/A yet; pre-commit ROI/bandpass/DDM params.
- Gate 3 Specificity [Gimli] AT RISK; affective split must beat content-blind 2-factor PCA.
- Gate 4 Confounds [Galadriel] AT RISK; partial out economic baseline / severity / base rate.
- Gate 5 Mechanism [Gimli] N/A yet; necessity via affective-channel lesion.
- Gate 6 Calibration [Boromir] FAIL as worded; fixed by reframe.
- Gate 7 External validity [Faramir] the crux; population->individual transfer unproven; label as open risk.
- Gate 8 Measurement [Galadriel] FAIL for leaders; need >=2 blind coders + kappa; information + attribution confounds.
- Gate 9 Reproducibility [Eowyn] PASS; harness seeded, CI-green, leakage-guarded.
- Gate 10 Ethics [Treebeard] CONDITIONAL; office-level revealed policy, public record, no psychodiagnosis.
- Gate 11 Analytic integrity [Bilbo] preregister temporal split + kill criteria before leader data.
- Gate F N/A (no figures yet).
- Gate T Theory [Elrond] PASS; proper scoring / conformal / DDM sound; resource-rational = interpretation only, not load-bearing.

## Error analysis
- Claim B: Type I dominant (ROIs x arms family-wise); bound = permutation null + FDR across arms; settle = within-estimator affective-vs-behavioral ΔCRPS with stimulus-grouped permutation on NARPS/DEAP.
- Claim E: Type I + II; ~50-150 codable decisions/term -> wide MDES + analyst DoF; settle = the abstention gate should FIRE here.

## Surviving claims -> paper (C1-C5): see README.

## What would change the verdict
Run E1 (synthetic parameter recovery) + E3 (within-estimator affective-vs-behavioral forecast on NARPS ds001734), both multi-seed with the harness permutation null. If recovery is clean and affective ΔCRPS CI excludes 0 under stimulus-grouped CV, core (C1-C4) -> ACCEPT and C5 rides as the honest external-validity probe. If affective transfer vanishes inside the unified estimator, C3 dies; paper narrows to C1/C2/C4.
