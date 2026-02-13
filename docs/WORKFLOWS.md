# Workflows

- Validate evidence JSON against schema:
  make validate-schema

- Validate graph + run queries:
  make graph-check

- Build a sample audit bundle (toy):
  . .venv/bin/activate
  python tools/bundle_build.py --out artifacts/out/sample_bundle --toy
