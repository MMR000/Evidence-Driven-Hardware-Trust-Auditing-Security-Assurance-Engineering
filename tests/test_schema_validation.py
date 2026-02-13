import json
from jsonschema import Draft202012Validator

def test_evidence_schema_validates_example():
    with open("artifacts/schemas/evidence_item.schema.json", "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open("artifacts/examples/evidence_items.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    v = Draft202012Validator(schema)
    errors = list(v.iter_errors(data))
    assert errors == [], f"Schema errors: {[e.message for e in errors]}"
