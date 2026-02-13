import json
from jsonschema import Draft202012Validator

def test_graph_schema_validates_toy_graph():
    with open("artifacts/schemas/graph.schema.json", "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open("graphs/toy/toy_graph.json", "r", encoding="utf-8") as f:
        graph = json.load(f)
    v = Draft202012Validator(schema)
    errors = list(v.iter_errors(graph))
    assert errors == [], f"Graph schema errors: {[e.message for e in errors]}"
