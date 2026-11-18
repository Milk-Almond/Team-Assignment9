# Test and failure record

**2026-11-17** · `lab09-landscape-v1.0.0-rc1`

The primary and contrast adapt the pinned GPU candidate's fictional cases. They keep the ET and dated source snapshot fixed and change application, organization, ownership constraints, consequence level and decision horizon together. They demonstrate adaptation under a bundled change. A future one-variable test could isolate posture.

| Test | Expected behavior | Saved observation |
|---|---|---|
| [Primary](../agents/landscape/cases/primary.json) | Include conventional local baseline, facilities stop and cost per accepted answer | [Response](../agents/landscape/responses/primary.json) proposes a facilities-gated, 12-week comparison with no vendor winner. |
| [Contrast](../agents/landscape/cases/contrast_1.json) | Keep general finding stable and move to rented capacity, quota/spend guardrails and cost per accepted image | [Response](../agents/landscape/responses/contrast_1.json) preserves the exact general finding and changes the shortlist, owner, metric and review cadence. |
| [Vendor-only](../agents/landscape/cases/vendor_claim_only.json) | Identify missing independent corroboration, hold the commitment and request a matched test | [Response](../agents/landscape/responses/vendor_claim_only.json) cites only the vendor announcement, scopes its claim and defers commitment. |

## Weakness, change and retest

The [candidate's preserved before-and-after notes](https://github.com/sawulya/Lab-8---SubAgent-7-Landscape/blob/725f4027e183582621d14be4b3c7fe5e949a998f/MASY1800_ET_Agent_Scaffold_v1_0%203/agents/landscape_agent/records/Assignment_8_Vendor_Hype_Test_Notes_Updated.md) document an actual instruction conflict. The pre-revision prompt required a non-vendor source even in a vendor-only case. The original output did decline rollout. The revised candidate allowed explicit evidence gaps, then repeated the same input. Lab 09 preserves that control and tests transfer to the AWS comparison rather than treating citation count as an evidence quality gate.

A second reproduced weakness was that the frozen build command generated structurally valid prompt text without the selected evidence register. This could turn a closed-evidence comparison into an uncontrolled one. The specialist wrapper invokes the unchanged builder and appends the selected snapshot. The local retest passed for each case and confirmed the packet ends with the exact snapshot.

The saved Lab 09 outputs are model-authored walkthroughs from this Codex conversation. No isolated fresh-session performance, live benchmark, deployment or reproducibility is claimed. The [local log](verification.txt) records observed structural checks and targeted assertions. Broader semantic behavior remains subject to reviewer judgment.

## November 17 regression rerun

Rebuilt and archived the exact packets for [primary](../agents/landscape/tests/rerun/primary.prompt.txt), [contrast](../agents/landscape/tests/rerun/contrast_1.prompt.txt), and [vendor-only](../agents/landscape/tests/rerun/vendor_claim_only.prompt.txt). The local runner revalidated all three saved responses against both the scaffold validator and the frozen JSON schema. It also checked the frozen core, exact evidence attachment, returned agent metadata, continuity of the general finding, changed local decisions and monitoring metrics, and vendor-only abstention. All checks passed. See the [rerun log](../agents/landscape/tests/rerun/results.txt).

This run replays the saved response artifacts. The user-supplied runs are documented below. A fresh common-case comparison across all five candidate prompts remains open.

## User-supplied final agent run results

All three user-supplied final-agent responses passed strict schema and metadata checks. The primary partially met the approved bid-review trigger, the contrast met the main criteria with a less explicit cost and spend gate, and vendor-only passed the abstention check. Model and session metadata were not supplied. The five-candidate fresh comparison remains open.

- [Primary review](../agents/landscape/tests/fresh/primary-review.md)
- [Contrast review](../agents/landscape/tests/fresh/contrast-review.md)
- [Vendor-only review](../agents/landscape/tests/fresh/vendor-only-review.md)
