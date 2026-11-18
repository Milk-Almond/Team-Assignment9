"""Synthetic harness regression tests. These do NOT run or evaluate real LLM experts."""
import json
import tempfile
import unittest
from pathlib import Path

from integration.nyu_humanoid import verify_moe as m


def fake_response(meta, recommendation="MONITOR: await evidence"):
    return {
        "agent": meta,
        "analytical_question": "Synthetic parser-only unit test",
        "general_et_finding": "Synthetic; not evidence",
        "application_finding": "Synthetic; not evidence",
        "organization_specific_finding": "Synthetic; not evidence",
        "evidence": [],
        "contrary_evidence_or_limitations": ["Synthetic; not evidence"],
        "confidence_and_uncertainty": "No real test was performed",
        "value_opportunity_implication": "Synthetic",
        "risk_governance_implication": "Synthetic",
        "recommendation_management_implication": recommendation,
        "change_monitoring_triggers": [],
        "abstention_or_more_information_needed": [],
    }


class TestPinnedMoEVerification(unittest.TestCase):
    def test_prepare_creates_seven_distinct_packets(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            m.prepare(folder)
            manifest = m.read_json(folder / "manifest.json")
            self.assertEqual(len(manifest["experts"]), 7)
            self.assertEqual(len({x["prompt_sha256"] for x in manifest["experts"]}), 7)
            self.assertEqual(manifest["status"], "PROMPTS_READY_NOT_EXECUTED")
            self.assertEqual(len(list((folder / "responses").glob("*.json"))), 0)

    def test_no_responses_is_incomplete(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            m.prepare(folder)
            report = m.validate(folder)
            self.assertEqual(report["status"], "INCOMPLETE")
            self.assertEqual(report["valid_expert_responses"], 0)
            self.assertTrue(any("original raw JSON response not supplied" in e for e in report["errors"]))

    def test_synthetic_versions_and_conflicts_require_human_review(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            m.prepare(folder)
            for exp in m.roster():
                meta = m.read_json(m.ROOT / exp["metadata_path"])
                rec = "MONITOR: watch the external market"
                if exp["id"] == "05_adoption":
                    rec = "BOUNDED_EXPERIMENT: conditional trial only"
                if exp["id"] == "06_organizational":
                    rec = "REQUEST EVIDENCE: no NYU safety authorization shown"
                m.write_json(folder / "responses" / (exp["id"] + ".json"), fake_response(meta, rec))
            report = m.validate(folder)
            self.assertEqual(report["status"], "REVIEW_REQUIRED")
            self.assertEqual(report["valid_expert_responses"], 7)
            self.assertTrue(any("SCOPE TENSION" in w for w in report["review_flags"]))
            self.assertEqual(report["human_signoff"], "PENDING")

    def test_mismatched_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            m.prepare(folder)
            for exp in m.roster():
                meta = m.read_json(m.ROOT / exp["metadata_path"])
                if exp["id"] == "03_promethean":
                    meta["version"] = "unapproved-version"
                m.write_json(folder / "responses" / (exp["id"] + ".json"), fake_response(meta))
            report = m.validate(folder)
            self.assertEqual(report["status"], "INCOMPLETE")
            self.assertEqual(report["valid_expert_responses"], 6)
            self.assertTrue(any("identity/version mismatch" in e for e in report["errors"]))

    def test_tampered_packet_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            m.prepare(folder)
            packet = folder / "prompts" / "02_innovation.txt"
            packet.write_text(packet.read_text(encoding="utf-8") + "tampered", encoding="utf-8")
            report = m.validate(folder)
            self.assertTrue(any("altered prepared prompt" in e for e in report["errors"]))


if __name__ == "__main__":
    unittest.main()
