# Team Lab 09 · Emerging Technology Landscape Agent

**Version:** `lab09-landscape-v1.0.0-rc1` · **Status:** team approval reported November 17, 2026. See the Team Agent Record for the approved commit and trigger.

The agent maps current evidence, viable alternatives, complements and dependencies. It supplies decision triggers to the final mixture-of-experts system. The case study compares a facilities-gated on-premises accelerator benchmark with a reversible cloud accelerator trial.

| Deliverable | Location |
|---|---|
| Team Agent Record and report-out | [Team Agent Record](records/team-agent-record.md) |
| Five-candidate comparison and contribution lineage | [Candidate comparison](records/candidate-comparison.md) |
| Dated original sources | [Source register](agents/landscape/evidence/source-register.md) |
| Common cases, weakness and retest | [Test and failure record](records/test-record.md) |
| Seven specialists and Lab 10 issues | [Integration readiness audit](records/integration-audit.md) |

## Run the specialist

From the repository root, build the primary prompt, submit the packet in ChatGPT, and save the JSON response.

```sh
python agents/landscape/build_evidence_prompt.py \
  --case agents/landscape/cases/primary.json \
  --evidence agents/landscape/evidence/source-register.md \
  --out work/landscape-primary.txt
python tools/validate_response.py work/landscape-primary-response.json
```

Use `contrast_1.json` with the same evidence register, or `vendor_claim_only.json` with `vendor-only.md`. For a new case, supply a dated evidence register scoped to that case. The Python tools build and check the packet locally. ChatGPT is the interactive runtime.

To verify the saved demonstrations and frozen scaffold:

```sh
python -m pip install -r agents/landscape/tests/requirements.txt
python agents/landscape/tests/check.py
```
