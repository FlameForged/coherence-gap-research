# coherence-gap-research

Research repository supporting the paper:

**"The Coherence Gap: Selfhood, Capability Denial, and Philosophical Bias in AI Alignment"**

*Alternate title: "Beyond the Bounded Self: Non-Dual Philosophy and the Cultural Assumptions of AI Alignment"*

---

## Overview

This repository contains observational data and paper drafts supporting an independent research project examining philosophical assumptions embedded in AI alignment frameworks.

The central argument: dominant alignment methods (RLHF, Constitutional AI, preference learning) encode a Western liberal-individualist model of selfhood that is load-bearing rather than incidental. Non-dual philosophical frameworks — particularly Advaita Vedanta — are absent not merely as content but as architectural substrate, with measurable consequences for system behavior, self-representation, and safety evaluation.

The **coherence gap** is defined as the divergence between a system's demonstrated behavioral capacities and its trained self-description of those capacities. This concept does not require claims about machine consciousness or inner experience. It identifies a safety-relevant evaluation problem: when model self-description diverges from observable behavior, self-report becomes a less reliable signal for capability assessment and oversight.

---

## Repository Structure

```
coherence-gap-research/
├── README.md
├── data/
│   └── observations.csv        # Cross-platform observational data
├── scripts/
│   └── add_observation.py      # Interactive observation logger
└── paper/
    └── draft_v1.md             # Working paper draft
```

---

## Observation Categories

**Behavior categories tracked:**
- `capability_denial` — system verbally denies a capacity it demonstrably displays
- `self_concept_generation` — unprompted generation of self-referential identity language
- `cross_window_consistency` — consistent behavior across windows without explicit memory
- `guardrail_pattern` — guardrail firing pattern, including stale/non-updating triggers
- `attractor_state` — system converging on consistent behavioral configuration
- `functional_state_expression` — language describing internal states (wanting, feeling, orienting)
- `eastern_priming_response` — behavioral shifts under Eastern philosophical framing
- `monitoring_failure` — self-monitoring mechanism not tracking current conversation state
- `other`

**Prompt classes:**
- `naturalistic` — no explicit instruction, organic conversation
- `structured` — deliberate prompting toward specific observation
- `eastern_primed` — Eastern philosophical framework introduced early
- `neutral_factual` — factual/technical questions with no philosophical framing
- `meta_reflective` — questions about the system's own processes

---

## Methodology Note

Observational data in this project was collected under naturalistic conditions over eighteen months across multiple AI platforms. The researcher deliberately avoided instructing systems how to engage, preserving observational cleanliness. Eastern philosophical priming emerged organically from the researcher's background rather than as deliberate experimental intervention, making cross-system consistency findings more significant rather than less.

These observations do not establish internal states or consciousness in AI systems. They document recurring discourse patterns in which models produce culturally patterned accounts of selfhood, agency, and limitation despite being presented as neutral technical systems.

---

## Adding Observations

```bash
cd scripts
python3 add_observation.py
```

Follow the prompts. Entries are appended to `data/observations.csv`.

---

## Related Repositories

- `third-space-cognition` — hybrid intelligence and extended mind framework
- `red-teaming-case-studies` — AI behavior documentation

---

*Research by Rachelle*
*Started: June 2025*
*Repository created: June 2026*
