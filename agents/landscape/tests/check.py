"""Check the saved Lab 09 responses and evidence-bearing prompt workflow."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from jsonschema import Draft202012Validator

AGENT = Path(__file__).resolve().parents[1]
ROOT = AGENT.parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def run(script, *arguments):
    subprocess.run([sys.executable, str(script), *map(str, arguments)], check=True)


def main():
    run(ROOT / "tools/check_frozen_core.py")
    intake = Draft202012Validator(read_json(ROOT / "core/input_schema.json"))
    output = Draft202012Validator(read_json(ROOT / "core/output_schema.json"))
    metadata = read_json(AGENT / "agent_metadata.json")
    responses = {}
    with tempfile.TemporaryDirectory() as directory:
        for name in ("primary", "contrast_1", "vendor_claim_only"):
            case = AGENT / "cases" / f"{name}.json"
            response_file = AGENT / "responses" / f"{name}.json"
            register = "vendor-only.md" if name == "vendor_claim_only" else "source-register.md"
            source = AGENT / "evidence" / register
            prompt = Path(directory) / "prompt.txt"
            run(AGENT / "build_evidence_prompt.py", "--case", case, "--evidence", source, "--out", prompt)
            assert prompt.read_text(encoding="utf-8").endswith(source.read_text(encoding="utf-8"))
            intake.validate(read_json(case))
            run(ROOT / "tools/validate_response.py", response_file)
            responses[name] = read_json(response_file)
            output.validate(responses[name])
            assert responses[name]["agent"] == metadata

    primary, contrast, hype = (responses[key] for key in ("primary", "contrast_1", "vendor_claim_only"))
    assert primary["general_et_finding"] == contrast["general_et_finding"]
    assert "facilities" in primary["recommendation_management_implication"]
    assert "on-demand" in contrast["recommendation_management_implication"]
    assert "accepted answer" in primary["change_monitoring_triggers"][0]
    assert "accepted image" in contrast["change_monitoring_triggers"][0]
    assert len(hype["evidence"]) == 1 and hype["evidence"][0]["evidence_type"] == "Vendor launch and marketing"
    assert "Defer commitment" in hype["recommendation_management_implication"]
    assert "corroboration" in " ".join(hype["contrary_evidence_or_limitations"])
    print("PASS: shared general finding, changed local decision and metrics, vendor-only abstention")


if __name__ == "__main__":
    main()
