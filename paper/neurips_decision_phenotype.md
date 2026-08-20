# Neural-Grounded Computational Decision Phenotypes: Honest-by-Construction Prediction of Choice, with Provable Abstention

*NeurIPS-form working draft. Venue chosen after results land. Built only on the five claims
that survived Council review (`checkpoints/council_review_2026-08-20.md`). Numbers marked
`[TBD-Ex]` are produced by the experiment named, never written before the run.*

---

## Abstract

Predicting how an agent will decide is usually posed as a black-box classification problem,
which yields uncalibrated point predictions and no principled way to say "I do not know."
We take a different route grounded in the neuroscience of choice. Following the
Affect-Integration-Motivation (AIM) account, we model a decision-maker as a low-dimensional
point on a decision manifold whose coordinates are neuroeconomic parameters, and we split the
choice process into an **affective** component that generalizes across individuals and an
**integrative** component that individuates. We estimate this manifold with a drift-diffusion
likelihood, calibrate the affective component on populations with real neural recordings
(fMRI and EEG), and wrap every prediction in distribution-free conformal coverage, a
strictly-proper score, and a minimum-detectable-effect abstention gate. We show (C1) the
estimator is identifiable on synthetic ground truth, (C2) the honesty layer delivers nominal
coverage and calibrated forecasts with provable withholding, (C3) the affective component
forecasts held-out and less-representative choice above and beyond behavior inside a single
estimator, (C4) hierarchical pooling across datasets lowers the minimum detectable effect,
and (C5) on genuinely confounded real-world targets the framework predicts where identifiable
and **provably abstains** where the information and attribution confounds break identifiability,
turning a failure mode into a tested safety property. `[TBD-Ex1..5]`

## 1. Introduction

- Behavioral prediction is high-stakes and usually dishonest about its own uncertainty.
- The neuroforecasting literature (Genevsky & Knutson 2015; Genevsky, Yoon & Knutson 2017;
  Tong et al. 2020; Stallen et al. 2021; Genevsky, Tong & Knutson 2025) established that
  brain-derived *affective* signal can forecast aggregate, out-of-sample choice better than
  behavior, and generalizes even when the sample is unrepresentative. But those results are
  population->population, at small n, and have never been unified into a single identifiable
  estimator or equipped with distribution-free guarantees.
- Our contribution is a method that is (i) neurally grounded in AIM, (ii) honest by construction
  (conformal + proper scoring + abstention), and (iii) explicit about the one thing prior work
  leaves implicit: *when prediction is not licensed at all*.
- **We do not claim to measure any individual's brain.** The neural grounding is a population
  property; individual claims are about revealed decision policy, bounded by named confounds.

## 2. Related work

- **Neuroforecasting / AIM:** Knutson (2008) anticipatory affect; Samanez-Larkin & Knutson
  (2015) AIM; Knutson & Genevsky (2018) affective-vs-integrative transfer; Tong (2020),
  Stallen (2021), Smith/Montague (2014), Falk (2012/15). Fernandes (2022) gives AIM an EEG
  signature, which licenses our EEG arm.
- **Forecast evaluation:** Gneiting & Raftery (2007) strictly-proper scoring rules.
- **Distribution-free uncertainty:** Angelopoulos & Bates (2021) conformal prediction.
- **Choice process models:** drift-diffusion / sequential sampling; resource-rational analysis
  (Lieder & Griffiths 2020) as *interpretation* of the parameters, not a predictive claim.
- **Gap we fill:** no prior work unifies AIM decomposition + a choice-process likelihood +
  distribution-free coverage + an identifiability-linked abstention gate in one estimator, nor
  evaluates abstention as a safety property on confounded real-world decision records.

## 3. Method

### 3.1 The decision manifold
theta = (rho_gain, lambda_loss, kappa_risk, delta_time, omega_threat, tau_consistency). An event
is a context vector c (stakes, gain/loss frame, ambiguity, threat, time pressure, reference point).

### 3.2 AIM-structured valuation and DDM likelihood
V(a | c, theta) = rho_gain E[gain] - lambda_loss E[loss] - kappa_risk sigma - omega_threat ambiguity
+ delta_time delay. The value difference drives a drift-diffusion process; boundary set by caution.
Affective channel (rho, lambda, omega) shares a hierarchical population prior; integrative channel
(kappa weighting, tau/threshold) is per-agent. This is the operationalization of Knutson & Genevsky's
affective-vs-integrative split.

### 3.3 Estimation
Hierarchical Bayes; partial pooling shrinks sparse individuals toward the population posterior so
underpowering shows up as posterior width, not overconfidence.

### 3.4 Honesty layer (C2)
Strictly-proper scoring (log/Brier/CRPS); split-conformal prediction sets at nominal coverage; an
MDES gate that abstains when the identifiable-event count puts the minimum detectable effect above
the claimed effect. Abstention is a first-class output.

### 3.5 Neural grounding
Affective-channel priors and the valuation form are calibrated on populations with real recordings:
NAcc/insula betas (fMRI, NARPS) and AIM-EEG correlates (Cue-P3, CNV; DEAP). No individual target is
scanned.

## 4. Experiments

- **E1 (C1) Parameter recovery.** Simulate agents at known theta; fit; correlate recovered vs true;
  20 seeds; report r + CI per parameter. Pass: r >= 0.6 for affective parameters. `[TBD-Ex1]`
- **E2 (C2) Coverage + calibration.** Empirical conformal coverage vs nominal; reliability diagram;
  abstention behavior below the MDES floor. Pass: |coverage - nominal| <= 3 pts at n>=200. `[TBD-Ex2]`
- **E3 (C3) Affective-vs-behavioral transfer.** Within the unified estimator, forecast held-out /
  less-representative choice on NARPS (fMRI) and DEAP (EEG); stimulus-grouped CV; permutation null;
  ablation vs content-blind 2-factor PCA. Report affective ΔCRPS + bootstrap CI. `[TBD-Ex3]`
- **E4 (C4) Pooling buys power.** MDES and posterior width, joint vs single-dataset fits. `[TBD-Ex4]`
- **E5 (C5) Calibrated abstention on confounded targets.** Public-figure decision corpora
  (preregistered temporal split); conformal predictions where identifiable; abstention rate where
  confounds break identifiability; calibration on the non-abstained subset vs base rate. `[TBD-Ex5]`

## 5. Results
`[populated from results/*.json as experiments land; every number carries seed, CI, null, score,
provenance stamp]`

## 6. Discussion (Step 5)
Operating characteristics: where the method works, at what n, with what coverage. Extension to state
(sad/angry as transient theta shift) and role (trader/cop/doctor as prior + weighting) phenotypes.

## 7. Limitations
- Population->individual transfer is the central open risk (Gate 7); we test it, we do not assume it.
- Neural grounding is population-level; no individual is scanned.
- Public-figure targets carry information and attribution confounds; C5 is designed around, not
  through, them.
- Resource-rational interpretation is not a load-bearing predictive claim.

## 8. Broader impacts (Gate 10)
Dual-use profiling risk; we restrict to public-record, office-level revealed policy, forbid
psychodiagnostic language, and make abstention-on-confounded-targets a core deliverable rather than
suppress it.

## 9. Reproducibility
Seeds, configs, split hashes, code commit, dataset versions released; leakage guards
(subject-/stimulus-grouped CV) inherited from the `behavioral_decoding` harness.

## Appendix A — Preregistration
Temporal split, arms, kill criteria for C3 and C5, committed to `checkpoints/` before fitting.

## Planned figures
See `figures/FIGURES.md`. Fig 1 architecture; Fig 2 recovery; Fig 3 coverage/calibration;
Fig 4 transfer arms; Fig 5 pooling/power; Fig 6 abstention operating curve; Fig 7 state/role manifold.
