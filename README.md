
# Evidence-Driven Hardware Trust Auditing & Security Assurance Engineering
### for High-Sensitivity Business Endpoints (Smartphones • Mobile Terminals • Regulated Environments)

<p align="center">
  <img src="docs/assets/banner.svg" alt="banner" width="920">
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/quickstart-1%E2%80%91command-success" /></a>
  <a href="#-repository-map"><img src="https://img.shields.io/badge/repo-super%20complete-blue" /></a>
  <a href="#-evidence-first"><img src="https://img.shields.io/badge/method-evidence%E2%80%91driven-purple" /></a>
  <a href="#-maturity-model"><img src="https://img.shields.io/badge/maturity-prototype%E2%86%92operations-orange" /></a>
  <a href="#-license"><img src="https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey" /></a>
</p>

<p align="center">
  <b>Upgrade “audit as a report” into “assurance as an engineering system”.</b><br/>
  Traceable • Comparable • Reappraisable • Lifecycle-aware
</p>

---

## 🌌 What is this repository?

Modern high-sensitivity endpoints rarely fail because of a single bug. Real compromise chains emerge from **cross-layer interactions**:

- hardware roots of trust & device identity anchoring  
- verified/measured boot + anti-rollback policy  
- TEE / secure element / hardware-backed keystores  
- baseband & wireless stacks  
- peripheral/DMA pathways & isolation boundaries  
- supply-chain composition & update-chain governance  
- runtime policy enforcement + audit-grade telemetry  

This repository is a **paper + engineering artifact pack** for building and operating a repeatable assurance workflow:

- an **Audit Object (AO) model** that makes scope executable and comparable  
- **Threat semantics** that bind each threat to required evidence & validation rules  
- an **Evidence Graph** that connects Threat ↔ Evidence ↔ Control ↔ Verification ↔ Deliverable ↔ Stage  
- a **4-stage maturity model** (prototype → pilot → production → operations) with stage gates  
- a **high-risk wireless reference architecture** that feeds telemetry back into assurance  

If you want a GitHub repo that looks serious *and* can be used by a team: this is the blueprint.

---

## 🧭 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [🗂 Repository Map](#-repository-map)
- [🧠 Evidence-First Method](#-evidence-first-method)
- [🧩 Audit Objects (AO) & Observables](#-audit-objects-ao--observables)
- [🧾 Evidence Tiers](#-evidence-tiers)
- [🕸 Evidence Graph Model](#-evidence-graph-model)
- [🧱 Maturity Model & Stage Gates](#-maturity-model--stage-gates)
- [📦 Evidence Bundle Format](#-evidence-bundle-format)
- [🔁 Change-Triggered Reappraisal (Drift)](#-change-triggered-reappraisal-drift)
- [📡 High-Risk Wireless Reference Architecture](#-high-risk-wireless-reference-architecture)
- [🧪 Demos & Examples](#-demos--examples)
- [🔍 Graph Queries](#-graph-queries)
- [🧰 Tooling](#-tooling)
- [📄 Paper](#-paper)
- [🧷 Citation](#-citation)
- [👥 Authors](#-authors)
- [📜 License](#-license)
- [🤝 Contributing](#-contributing)

---

## 🚀 Quick Start

### 1) Validate everything (schemas + graph integrity)
```bash
make check
````

Runs:

* JSON/YAML schema validation
* evidence-graph referential integrity checks
* toy graph queries
* report generation → `out/report/`

### 2) Build the paper (optional)

```bash
make paper
```

### 3) Generate an “audit-ready evidence bundle” demo

```bash
make demo-bundle
```

Outputs:

* `out/demo_bundle.zip`
* `out/demo_bundle/claim_map.yaml`
* `out/demo_bundle/evidence/` (sample artifacts)
* `out/demo_bundle/trace/graph.json` (traceability snapshot)

---

## 🗂 Repository Map

```text
.
├─ paper/                         # Manuscript source (MD/LaTeX) + figures
│  ├─ manuscript.md
│  ├─ figures/
│  └─ tables/
├─ docs/                          # Docs / GitHub Pages
│  ├─ index.md
│  ├─ guide/
│  ├─ assets/
│  └─ diagrams/
├─ artifacts/                     # Engineering deliverables (the “real value”)
│  ├─ ao/                         # Audit Object taxonomy + observables
│  ├─ threat/                     # Threat ontology + tuple templates
│  ├─ evidence/                   # Evidence schemas + tiers + validation rules
│  ├─ controls/                   # Control mappings (NIST/ISO/ETSI/CC)
│  ├─ maturity/                   # Stage gates + checklists + minimum deliverables
│  └─ bundles/                    # Evidence bundle spec + templates + examples
├─ graph/                         # Evidence-graph schema + sample graph instances
│  ├─ schema/
│  ├─ toy/
│  └─ queries/
├─ tools/                         # CLI helpers (validate, query, export)
│  ├─ validate/
│  ├─ query/
│  └─ export/
├─ examples/                      # End-to-end demo cases
│  ├─ smartphone_high_sensitivity/
│  └─ wireless_gateway/
├─ out/                           # Build outputs (git-ignored)
├─ Makefile
└─ README.md
```

---

## 🧠 Evidence-First Method

> Assurance is not a conclusion. Assurance is a **reproducible argument**.

Every “security conclusion” must answer:

1. **What is the audit boundary?** (AO inventory)
2. **What evidence supports the claim?** (typed artifacts + provenance)
3. **Which controls close the loop?** (verifiable mitigations, not vibes)
4. **What changes invalidate the evidence?** (drift triggers + reappraisal)

This repo operationalizes those answers.

---

## 🧩 Audit Objects (AO) & Observables

### Why Audit Objects?

Audit scope commonly collapses into vague statements (“secure boot is enabled”) that are not comparable across devices, teams, or time.

Audit Objects (AOs) make scope **explicit and stable**, e.g.:

* AO-02 Boot chain (ROM → BL → OS)
* AO-03 Anti-rollback / downgrade policy
* AO-05 TEE & trusted applications
* AO-08 Baseband firmware & isolation boundary
* AO-11 Supply chain composition & provenance
* AO-14 Runtime telemetry & policy enforcement

Key files:

* `artifacts/ao/ao_inventory.yaml`
* `artifacts/ao/observables/`

Each AO defines **observables**: concrete, collectible signals (hashes, policy flags, counters, attestations, manifests).

---

## 🧾 Evidence Tiers

Not all evidence is equal. We classify evidence to keep audits honest and comparable:

* **E1 Cryptographic evidence**: attestations, signatures, certificate chains
* **E2 Measurement evidence**: measured boot logs, counters, secure monotonic values
* **E3 Configuration evidence**: baseline dumps, policy flags, build fingerprints
* **E4 Process/provenance evidence**: SBOM, SLSA/in-toto provenance, approvals, key ceremonies

See:

* `artifacts/evidence/taxonomy.md`
* `artifacts/evidence/schemas/`

---

## 🕸 Evidence Graph Model

We represent assurance as a directed labeled multigraph.

### Node types

* **AuditObject / Asset / Boundary**
* **Threat**
* **Precondition**
* **EvidenceType**
* **EvidenceInstance**
* **Control**
* **VerificationActivity**
* **Deliverable**
* **StageGate**

### Edge types

* `targets`, `requires`, `supported_by`, `mitigated_by`, `verified_by`,
  `requires_deliverable`, `includes`, `invalidates`

Toy graph:

* `graph/toy/graph.json`

Queries:

* `graph/queries/`

---

## 🧱 Maturity Model & Stage Gates

We define **four stages** with **minimum deliverables** (not vague “risk acceptance”):

1. **Prototype (PoC)**

   * AO inventory + boundary definition
   * baseline evidence templates
   * initial threat-to-evidence map

2. **Pilot (EVT/DVT)**

   * repeatable evidence collection
   * signed evidence manifests
   * verification activities documented and runnable

3. **Production**

   * enforceable stage gates
   * supplier transparency + provenance requirements
   * audit-ready decision records and trace snapshots

4. **Operations**

   * continuous monitoring/telemetry
   * drift triggers and reappraisal workflow
   * compliance reporting and change history

See:

* `artifacts/maturity/stages.yaml`
* `artifacts/maturity/checklists/`

---

## 📦 Evidence Bundle Format

An “audit-ready bundle” is not a PDF. It is a reproducible package:

* device identity dossier (model, SoC, rev, build fingerprints)
* evidence objects (raw artifacts + provenance headers)
* claim mapping (claim id → evidence ids → validation rules)
* control mapping (control id → verification steps → acceptance criteria)
* change log (delta across releases / versions)
* traceability snapshot (graph export)

Spec:

* `artifacts/bundles/spec.md`

Template:

* `artifacts/bundles/templates/bundle_layout/`

---

## 🔁 Change-Triggered Reappraisal (Drift)

Assurance becomes stale when:

* firmware updates happen
* boot policies change
* suppliers change
* OTA signing keys rotate
* wireless policies drift
* operational exceptions appear

We provide a drift playbook:

* identify impacted AOs
* invalidate dependent evidence nodes
* re-run targeted verification activities
* update trace snapshot + decision record

See:

* `docs/guide/drift_reappraisal.md`
* `examples/smartphone_high_sensitivity/drift_demo/`

---

## 📡 High-Risk Wireless Reference Architecture

For environments where you can’t assume “clean RF”:

* enforcement front-end (FPGA / dedicated hardware policies)
* encrypted gateway enforcing trust boundaries
* management plane producing audit-grade telemetry and policy logs
* telemetry feeds back into evidence bundles and ops-stage reports

See:

* `examples/wireless_gateway/architecture.md`
* `docs/diagrams/wireless_ref_arch.mmd`

---

## 🧪 Demos & Examples

### Example A: High-sensitivity smartphone onboarding

* instantiate AO inventory
* minimal threat-to-evidence mapping
* generate a demo bundle
* run readiness checks for Pilot/Production

Path:

* `examples/smartphone_high_sensitivity/`

### Example B: Wireless posture hardening

* policy baselines and enforcement evidence
* telemetry artifacts
* ops-stage compliance report export

Path:

* `examples/wireless_gateway/`

---

## 🔍 Graph Queries

Toy examples:

* “Show threats with missing required evidence”
* “List controls not verified for production gate”
* “Show everything that depends on baseband firmware identity evidence”

```bash
make query Q="missing_evidence"
make query Q="prod_gate_blockers"
make query Q="depends_on:EI_BASEBAND_FIRMWARE_ID"
```

Outputs:

* `out/query/*.json`
* `out/query/*.md`

---

## 🧰 Tooling

* `tools/validate/` → schema & graph integrity
* `tools/query/` → graph queries
* `tools/export/` → Markdown/HTML exports

Make targets:

* `make check`
* `make demo-bundle`
* `make query Q=<name>`
* `make report`
* `make paper`

---

## 📄 Paper

Manuscript source:

* `paper/manuscript.md`

Figures:

* `paper/figures/`

Tables:

* `paper/tables/`

---

## 🧷 Citation

If you use this repository in research or internal engineering, please cite the accompanying paper:

```bibtex
@article{evidence_graph_endpoint_assurance,
  title   = {Evidence-Driven Hardware Trust Auditing and Security Assurance Engineering for High-Sensitivity Business Endpoints},
  author  = {Atanbayev, Yernat and Budenov, Ruslan and Jilkibayev, Yerbolsyn and Tokkuliyeva, Aizhan and Shaikhanova, Aigul Kairulayevna},
  journal = {Preprint / Under Review},
  year    = {2026}
}
```

---

## 👥 Authors

* Atanbayev Yernat (Correspondence: [yernatatanbayev@gmail.com](mailto:yernatatanbayev@gmail.com))
* Budenov Ruslan
* Jilkibayev Yerbolsyn
* Tokkuliyeva Aizhan
* Shaikhanova Aigul Kairulayevna

Affiliation:

* TSARKA R&D LLP, Astana, Kazakhstan

---

## 📜 License

Released under **Creative Commons Attribution 4.0 (CC BY 4.0)** unless stated otherwise.

* You may share and adapt with attribution.
* Contributions are accepted under the same license.

---

## 🤝 Contributing

We welcome:

* improvements to evidence schemas and validation rules
* additional threat mappings (ATT&CK / CAPEC / CWE anchors)
* realistic demo bundles for more device families
* better graph queries and exports

Guidelines:

1. keep the AO inventory stable (avoid scope drift)
2. every threat must declare minimal required evidence
3. every control must be verifiable (no “hand-wavy” mitigations)
4. stage gates must be deliverable-centric and auditable

See:

* `CONTRIBUTING.md`
* `CODE_OF_CONDUCT.md`

