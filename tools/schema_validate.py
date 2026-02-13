#!/usr/bin/env python3
import argparse
import json
from jsonschema import Draft202012Validator
from rich.console import Console

console = Console()

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--schema", required=True)
  ap.add_argument("--data", required=True)
  args = ap.parse_args()

  with open(args.schema, "r", encoding="utf-8") as f:
    schema = json.load(f)
  with open(args.data, "r", encoding="utf-8") as f:
    data = json.load(f)

  v = Draft202012Validator(schema)
  errors = sorted(v.iter_errors(data), key=lambda e: e.path)

  if errors:
    console.print("[red]Schema validation failed[/red]")
    for e in errors:
      console.print(f"- path={list(e.path)} msg={e.message}")
    raise SystemExit(1)

  console.print("[green]Schema validation OK[/green]")

if __name__ == "__main__":
  main()
