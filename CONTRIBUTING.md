# Contributing

## Scope
This repository provides:
- Paper source (LaTeX)
- Evidence schemas (JSON/YAML)
- Toy threat–evidence–control graph
- Minimal tools to validate schemas and generate audit bundles

## How to contribute
1. Fork and create a feature branch.
2. Run tests / linters:
   - `make test`
   - `make lint`
3. Submit a PR with a clear description and references.

## Style
- Keep templates machine-readable.
- Avoid vendor-specific claims unless properly cited.
- Prefer additive changes; do not break schema compatibility lightly.
