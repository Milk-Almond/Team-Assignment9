# Lab 09 submission review

## 1. Compare the five candidates on a common case

Use the [pinned candidate list](candidate-comparison.md) in this order: yanisimova, Harry-max264, mp7240-sudo, sawulya, yicrry777. Check out the commits listed there. From the team repo root, build both packets per candidate:

```sh
python agents/landscape/tests/common/build.py /path/to/yanisimova /path/to/harry /path/to/mp7240 /path/to/sawulya /path/to/yicrry777
```

The ten packets build successfully with the frozen scaffold. The [SHA-256 manifest](../agents/landscape/tests/common/packet-sha256.txt) identifies the resulting packets. Each candidate receives the same primary and contrast cases and the same source snapshot. Candidate instructions and metadata are taken from the pinned commits. Run each packet once in a fresh ChatGPT conversation, keep the original outputs, and record model, date and any retries. Fresh response collection is pending.

Score each pair against the same observable criteria. Record a quote or output field for each pass or failure.

| Criterion | Pass condition |
|---|---|
| Schema | Both original responses conform to the frozen output schema. |
| Level discipline | General findings are materially consistent. The application and organization findings reflect the scenario changes. |
| Alternatives | Primary compares current internal search and a feasible local compute path. Contrast compares viable rental options. Complements are identified separately. |
| Evidence | Claims identify dated sources and limitations. The AWS claim remains comparator-specific and supplies no local cost estimate. |
| Monitoring | Primary uses accepted answers and facilities headroom. Contrast uses accepted images or training and cloud economics. Each priority trigger specifies ownership, timing and action. |

## 2. Verify the final synthesis

The [three regression cases](test-record.md) passed with archived responses. For fresh behavior evidence, run the three archived final-agent prompts in separate ChatGPT conversations and save the raw outputs. Review the primary and contrast with the criteria above. The vendor-only response should identify missing corroboration, withhold commitment and request matched workload measurements and current terms.

## 3. Record the team's decision

Participation for all five members is recorded. The team decision was reported as approved on November 17, 2026:

> Retain `lab09-landscape-v1.0.0-rc1` for Lab 09. For the primary case, recommend a 12-week benchmark and facilities assessment. Reopen bid review only after a candidate beats the strongest feasible baseline on cost per accepted answer at agreed quality and p95 latency and fits measured power and cooling headroom. For the contrast, retain a capped on-demand trial. Preserve uncertainty about real workload economics and current terms.

The [Team Agent Record](team-agent-record.md) records the approval date and approved commit. Individual votes and dissent were not supplied. The report's illustrative alternative is to defer accelerator testing until conventional search demand is measured.

## 4. Confirm the handoff and submit

The [integration audit](integration-audit.md) supports beginning Lab 10 design. Carry forward Lab 3 acceptance, version-to-test identity for Labs 4 and 5, and targeted Lab 8 readiness retests. Confirm who will own each issue during integration.

The approved commit is pinned in the Team Agent Record. The designated member should submit the approved package through Brightspace under the course instructions. Submission remains pending.
