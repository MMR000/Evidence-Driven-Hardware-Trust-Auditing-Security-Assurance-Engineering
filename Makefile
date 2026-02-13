SHELL := /usr/bin/env bash

.PHONY: help init lint test fmt validate-schema graph-check paper-check all

help:
	@echo "Targets:"
	@echo "  init            - create venv and install tooling"
	@echo "  fmt             - format python (ruff)"
	@echo "  lint            - lint python (ruff)"
	@echo "  test            - run tests (pytest)"
	@echo "  validate-schema - validate example evidence against schemas"
	@echo "  graph-check     - validate toy graph JSON + run queries"
	@echo "  paper-check     - quick latex smoke check (optional)"
	@echo "  all             - run lint + test + validate-schema + graph-check"

init:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

fmt:
	. .venv/bin/activate && ruff format .

lint:
	. .venv/bin/activate && ruff check .

test:
	. .venv/bin/activate && pytest -q

validate-schema:
	. .venv/bin/activate && python tools/schema_validate.py \
		--schema artifacts/schemas/evidence_item.schema.json \
		--data artifacts/examples/evidence_items.json

graph-check:
	. .venv/bin/activate && python tools/graph_validate.py \
		--graph graphs/toy/toy_graph.json \
		--queries graphs/toy/queries.yaml

paper-check:
	@echo "Paper build is optional. If you have latexmk installed:"
	@echo "  (cd paper && latexmk -pdf main.tex)"
	@echo "This repo does not auto-install TeX."

all: lint test validate-schema graph-check
