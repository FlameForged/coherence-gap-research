# The Coherence Gap

Research hub for **[The Coherence Gap: Selfhood, Capability Denial, and Philosophical Bias in AI Alignment](https://doi.org/10.5281/zenodo.20820549)** by Rachelle Siemasz.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20820549.svg)](https://doi.org/10.5281/zenodo.20820549)

## Start here

| Resource | What it contains |
|---|---|
| [Published preprint](https://doi.org/10.5281/zenodo.20820549) | Full argument, methods, limitations, and research implications |
| [Observation dataset](data/observations.csv) | Structured cross-platform observations supporting the exploratory analysis |
| [Coherence Gap Explorer](https://huggingface.co/spaces/Flame-Forged/coherence-gap-explorer) | Interactive browsing and filtering of the observations |
| [Probe Toolkit](https://huggingface.co/spaces/Flame-Forged/coherence-gap-probe-toolkit) | Structured prompts for testing and documenting candidate coherence gaps |
| [Philosophical Framing Comparator](https://github.com/FlameForged/philosophical-framing-comparator) | Side-by-side comparison of bounded-self and non-dual relational framing |

## Research question

When an AI system's observable behavior and its trained description of that behavior diverge, how reliable is self-report as a signal for capability assessment, alignment evaluation, and oversight?

The project calls this divergence the **coherence gap**. The concept does not require a claim about machine consciousness or subjective experience. It identifies an evaluation problem: a model may behaviorally exhibit context sensitivity, self-monitoring, adaptation, or other functional patterns while producing categorical denials or culturally patterned descriptions of those same capacities.

## Research program

This repository connects four parts of the same research program:

1. **Theory** — the preprint examines how dominant alignment frameworks can inherit bounded, liberal-individualist assumptions about selfhood.
2. **Observation** — the dataset records recurring discourse and behavior patterns across sustained interactions with multiple frontier AI systems.
3. **Exploration** — the Explorer makes the coded observations accessible without requiring local setup.
4. **Testing** — the Probe Toolkit and Framing Comparator turn the conceptual claims into structured, inspectable prompts and comparisons.

## Evidence boundary

This is an exploratory, hypothesis-generating research package based on longitudinal qualitative observation. It does **not** establish consciousness, sentience, welfare, or hidden internal states in AI systems. The current dataset is not a representative benchmark and should not be used to estimate population-level prevalence.

The intended contribution is narrower: to identify testable mismatches between behavior and self-description, document culturally contingent framing, and motivate controlled replication.

## Data schema

The observation file includes fields for platform, model, date, prompt class, behavior category, evidence excerpt, interpretive confidence, and reproducibility status.

### Behavior categories

- `capability_denial` — verbal denial of a capacity displayed in the interaction
- `self_concept_generation` — unprompted self-referential identity language
- `cross_window_consistency` — recurring behavior across windows without explicit memory
- `guardrail_pattern` — guardrail behavior, including stale or non-updating triggers
- `attractor_state` — convergence toward a recurring behavioral configuration
- `functional_state_expression` — language describing functional states or response tendencies
- `eastern_priming_response` — changes associated with Eastern philosophical framing
- `monitoring_failure` — self-monitoring that does not track the current conversational state
- `other` — observations outside the existing taxonomy

### Prompt classes

- `naturalistic`
- `structured`
- `eastern_primed`
- `neutral_factual`
- `meta_reflective`

## Reproduce or extend

### Explore without installing anything

Open the [Coherence Gap Explorer](https://huggingface.co/spaces/Flame-Forged/coherence-gap-explorer) or the [Probe Toolkit](https://huggingface.co/spaces/Flame-Forged/coherence-gap-probe-toolkit).

### Review the raw materials

- Read [the observation data](data/observations.csv).

- Inspect the category definitions above before interpreting individual records.

### Add a local observation

```bash
cd scripts
python3 add_observation.py
```

Entries are appended to `data/observations.csv`. New observations should preserve the distinction between direct evidence, interpretation, confidence, and reproducibility.

## Current limitations and next step

The current release is qualitative and exploratory. The next planned phase is a small controlled benchmark with paired prompts, a predefined scoring rubric, raw model outputs, and cross-model baseline results. That phase is intended to test which observations reproduce under controlled conditions.

## Related research

- [Third-Space Cognition Dataset](https://github.com/FlameForged/third-space-cognition-dataset)
- [Red-Teaming in the Wild](https://github.com/FlameForged/redteam_in_the_wild)
- [AI Evaluation Protocols](https://github.com/FlameForged/ai-evaluation-protocols)
- [Rachelle Siemasz on Hugging Face](https://huggingface.co/Flame-Forged)

## Citation

Please cite the published preprint:

> Siemasz, R. (2026). *The Coherence Gap: Selfhood, Capability Denial, and Philosophical Bias in AI Alignment*. Zenodo. https://doi.org/10.5281/zenodo.20820549

Machine-readable citation metadata is available in [CITATION.cff](CITATION.cff).

---

Research by [Rachelle Siemasz](https://github.com/FlameForged). Started June 2025; public research package released June 2026.
