# Project Structure (high-level)

- paper/                      LaTeX source for the review (MDPI-style skeleton)
- artifacts/
  - schemas/                  JSON schemas for evidence objects
  - templates/                YAML/JSON templates for audit bundles
  - examples/                 Example evidence items, control mappings, bundles
- graphs/
  - toy/                      Minimal threat–evidence–control graph in JSON + queries
- tools/                      Python utilities (schema validation, graph checks, bundle build)
- reports/                    Generated outputs (ignored by git)
- .github/                    CI workflows and issue templates
