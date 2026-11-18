# NYU Humanoid Robotics — seven-specialist evidence workflow

**Purpose:** repair the previously missing audit trail between the photographed classroom questions and a purported seven-expert answer. This folder is an **integration verification harness**, not proof of a completed MoE deployment or an NYU-approved robot trial.

## Reproducible procedure

1. Run `python integration/nyu_humanoid/verify_moe.py prepare` from the repo root. It constructs **seven distinct prompt packets** using the same case, evidence snapshot, frozen course instructions and each specialist's pinned, previously approved instructions + metadata. A manifest records source commits and SHA-256 content hashes.
2. Submit each packet in its **own fresh ChatGPT conversation** (no shared model history). Preserve complete, unchanged JSON replies as `integration/nyu_humanoid/runs/nyu-totes-2026-11-17/responses/<id>.json`. Record model, date, session evidence, operator and retries in `run-provenance.json`. No model execution is inferred from packet generation.
3. Run `python integration/nyu_humanoid/verify_moe.py verify`. It validates all seven response bodies against the frozen schema **and** the exact pinned `agent` metadata; confirms their JSON is stored unchanged; hashes the source inputs, packets and responses; and flags important disagreements or missing readiness proof. Outputs a machine-readable report and a human review checklist.
4. Human team members examine the original seven outputs. In `human-adjudication.md`, resolve or visibly preserve disagreements about breakthrough/Promethean classification, diffusion population, experiment-vs-defer scope, and safety/readiness. Include evidence IDs for every consequential claim. Do not treat the auto-generated checklist as a verified management decision.
5. Draft the final classroom answer ONLY after original responses and review exist. The decision remains human-owned. Keep the original answer and raw seven JSON records; the final synthesis must reference the seven filenames, pinned versions, source snapshot, dissent, and management gates.

## Current status

- **Done:** pinned seven existing specialist versions in `snapshots/`; common case and source register; deterministic prompt builder, response validator and conflict-screening protocol.
- **Not done / not claimed:** seven independent ChatGPT invocations, completed raw runtime outputs, human cross-expert adjudication, a fully verified integrated MoE answer, institutional permission for an actual NYU trial.
- **Scope:** a single concrete **staff-only stockroom tote-handling** proposal. The earlier separate library-reshelving answer is an alternate concept, not evidence from this same test.
- **Dependencies:** `python -m pip install jsonschema` for strict Draft 2020-12 validation; prompt preparation itself uses the standard library.
- **Frozen core:** all files under `core/` remain untouched.

## Approval / release criteria

The classroom answer may be called **seven-specialist-reviewed** only after seven valid, source-pinned raw outputs are present and any discrepancies are explicitly reviewed. It may be called **integrated validated MoE** only with preserved run logs and appropriate repeated tests proving orchestration, fallback and repeatability; this one-case exercise alone does not establish those broader claims.

## Pinning / ownership

The `roster.json` references source commits; its copies of `specialist_instructions.md` and `agent_metadata.json` are preserved byte-for-byte in `snapshots/`. Replace versions through a reviewed, logged change only; do not update approvals solely because a newer prompt exists. See `records/integration-audit.md` for known expert acceptance issues.

## How to run the included regression test

`python -m unittest integration.nyu_humanoid.test_verify_moe`
