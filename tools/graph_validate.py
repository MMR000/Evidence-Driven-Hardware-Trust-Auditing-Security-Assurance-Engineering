#!/usr/bin/env python3
import argparse
import json
import sys
import yaml
from jsonschema import Draft202012Validator
from rich.console import Console

console = Console()

def load_schema(path: str):
  with open(path, "r", encoding="utf-8") as f:
    return json.load(f)

def validate_json(schema, obj, name="object"):
  v = Draft202012Validator(schema)
  errors = sorted(v.iter_errors(obj), key=lambda e: e.path)
  if errors:
    console.print(f"[red]{name} schema validation failed[/red]")
    for e in errors:
      console.print(f"- path={list(e.path)} msg={e.message}")
    raise SystemExit(1)

def index_nodes(nodes):
  m = {}
  for n in nodes:
    m[n["id"]] = n
  return m

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--graph", required=True)
  ap.add_argument("--queries", required=True)
  args = ap.parse_args()

  with open(args.graph, "r", encoding="utf-8") as f:
    graph = json.load(f)
  with open("artifacts/schemas/graph.schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

  validate_json(schema, graph, name="graph")

  nodes = graph["nodes"]
  edges = graph["edges"]
  node_by_id = index_nodes(nodes)

  # Basic referential integrity
  for e in edges:
    if e["src"] not in node_by_id and not e["src"].endswith(".json"):
      console.print(f"[red]Edge src not found:[/red] {e}")
      sys.exit(1)
    if e["dst"] not in node_by_id and not isinstance(e["dst"], str):
      console.print(f"[red]Edge dst not found:[/red] {e}")
      sys.exit(1)

  with open(args.queries, "r", encoding="utf-8") as f:
    q = yaml.safe_load(f)

  # Execute minimal query types
  for item in q.get("queries", []):
    name = item.get("name", "unnamed")
    qtype = item.get("type")
    if qtype == "node_filter":
      kind = item.get("kind")
      hits = [n for n in nodes if n.get("kind") == kind]
      console.print(f"[cyan]{name}[/cyan]: {len(hits)} nodes kind={kind}")
      for n in hits:
        console.print(f"  - {n['id']}: {n['name']}")
    elif qtype == "graph_rule":
      rule = item.get("rule", "")
      ok = True
      if "THREAT" in rule and "mitigated_by" in rule:
        for t in [n for n in nodes if n["kind"] == "THREAT"]:
          has = any(e for e in edges if e["src"] == t["id"] and e["rel"] == "mitigated_by"
                    and node_by_id.get(e["dst"], {}).get("kind") == "CONTROL")
          if not has:
            ok = False
            console.print(f"[red]Rule fail[/red] threat {t['id']} missing mitigated_by CONTROL")
      if "THREAT" in rule and "supported_by" in rule:
        for t in [n for n in nodes if n["kind"] == "THREAT"]:
          has = any(e for e in edges if e["src"] == t["id"] and e["rel"] == "supported_by"
                    and node_by_id.get(e["dst"], {}).get("kind") == "EVIDENCE_INSTANCE")
          if not has:
            ok = False
            console.print(f"[red]Rule fail[/red] threat {t['id']} missing supported_by EVIDENCE_INSTANCE")
      console.print(f"[green]{name}[/green]: {'OK' if ok else 'FAIL'}")
      if not ok:
        sys.exit(1)
    else:
      console.print(f"[yellow]Skipping unknown query type[/yellow]: {qtype}")

  console.print("[green]Graph checks OK[/green]")

if __name__ == "__main__":
  main()
