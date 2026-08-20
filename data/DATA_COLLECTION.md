# Data collection — sources, provenance, licenses, access status

Every dataset used carries: id + version, access route, license, modality, what it grounds, and
one gotcha. Provenance stamps (id + version + split hash) go into every `results/*.json`.

## Neural datasets (ground the affective channel)

| id | route | license | modality | grounds | status |
|---|---|---|---|---|---|
| **NARPS ds001734** | OpenNeuro (public) | CC0 | fMRI, mixed-gambles reward | affective channel via NAcc/vmPFC/AIns betas; individual accept/reject | loader BUILT in harness (`io/narps.py`); not yet run on real download here |
| **DEAP** | licensed download (request) | academic EULA | EEG + peripheral + face + self-report | AIM-EEG affective features (Cue-P3, CNV per Fernandes 2022); YouTube view-count aggregate outcome | loader BUILT in harness (`io/deap.py`); download pending |

Gotchas (from harness docs, already handled): DEAP 4–45Hz bandpass (no delta), label order
valence/arousal/dominance/liking, latin1 Python-2 pickles, peripheral chans 33–40 not EEG; NARPS
economic baseline (gain/loss) dominates the aggregate arm by construction, so NARPS is an
individual-level fMRI check, not a brain-beats-behavior demo.

## Candidate additional neural data (via Google Dataset Search sweep)

Discovery tool: `https://datasetsearch.research.google.com/search?query=<terms>` (schema.org index
across OpenNeuro/NEMAR, OSF, Mendeley, Zenodo, figshare, HuggingFace). Candidates to evaluate for
the EEG arm and the AIM MID-task:
- **THINGS-EEG / THINGS-EEG2** (NEMAR/OSF) — 64-ch, large; visual, not reward, so secondary.
- **Monetary Incentive Delay (MID) task** datasets — the canonical Knutson gain/loss anticipation
  paradigm; search OpenNeuro for MID / reward anticipation. **Primary target for the affective prior.**
- Selection rule: prefer datasets with an explicit gain/loss anticipation contrast and released
  event timing; log license + n before use.

## Behavioral / decision corpora (fit the integrative channel for C5)

- **Public-figure decision records** (Trump term-1 2016–2020; Xi; one control figure). **Public
  record only.** Each decision coded into an event vector c (stakes, gain/loss frame, ambiguity,
  threat, time pressure, reference point) and an action class.
- **Coding protocol (Gate 8):** two independent blind coders; Cohen's kappa reported before any
  modeling; disagreements adjudicated by a written rubric, not by the modeler. Corpus + rubric +
  kappa land in `data/` before E5 runs.
- **Confounds stamped on every C5 result:** information confound (advisor-filtered outcomes),
  attribution confound (individual vs institution). Framing = office-level revealed policy.

## Literature (grounds the method; checked via Consensus/PubMed 2026-08-20)

- Knutson (2008) Anticipatory affect, Phil Trans R Soc B.
- Carter et al. (2009) NAcc/VTA motivational relevance, Front Behav Neurosci.
- Samanez-Larkin & Knutson (2015) AIM framework, Nat Rev Neurosci.
- Genevsky & Knutson (2015) microlending, Psych Science; 10.1177/0956797615588467.
- Genevsky, Yoon & Knutson (2017) crowdfunding "When Brain Beats Behavior", J Neurosci; 10.1523/JNEUROSCI.1633-16.2017.
- Knutson & Genevsky (2018) Neuroforecasting Aggregate Choice, Curr Dir Psych Sci; 10.1177/0963721417737877.
- Tong, Acikalin, Genevsky, Shiv & Knutson (2020) video engagement, PNAS; 10.1073/pnas.1905178117.
- Stallen et al. (2021) Brain Activity Foreshadows Stock Price Dynamics, J Neurosci (preregistered replication).
- Genevsky, Tong & Knutson (2025) generalizable components, PNAS Nexus; 10.1093/pnasnexus/pgaf029.
- Fernandes et al. (2022) AIM EEG registered report, NeuroImage.
- Falk, Berkman & Lieberman (2012) neural focus group, Psych Science; 10.1177/0956797611434964.
- Smith et al. (2014) market bubbles, PNAS.
- Gneiting & Raftery (2007) strictly proper scoring rules, JASA.
- Angelopoulos & Bates (2021) conformal prediction tutorial, arXiv:2107.07511.
- Lieder & Griffiths (2020) resource-rational analysis, Behav Brain Sci.

## Access status summary

- Public + wired: NARPS loader (needs the OpenNeuro fetch).
- Licensed + pending: DEAP (request the download).
- To acquire: a MID reward-anticipation dataset for the affective prior; the public-figure corpus (curate here).
- No neural data for any individual, by design and forever.
