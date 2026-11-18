# Team Agent Record · Landscape

| Field | Record |
|---|---|
| Course / specialty | MASY1-GC 1800 · Team Lab 09 · SubAgent 7 |
| Status / version | Proposed synthesis for team approval · `lab09-landscape-v1.0.0-rc1` |
| Evidence cutoff | 2026-11-17 |
| Governing question | Where does the technology sit among alternatives, complements and external signals, and what should management monitor next? |
| Authority | Intelligence and bounded evaluation. Management owns funding and deployment. The security owner controls access and data transfer. |
| Evidence | [Source register](../agents/landscape/evidence/source-register.md) · [Context tests](test-record.md) · [Candidate lineage](candidate-comparison.md) |

## Landscape and proposed decision

**General ET.** Data-center GPUs are an established class with competing GPU and rented ASIC options. Runtime, memory, storage, networking, power and cooling determine deployability. Benchmark submissions and issuer revenue give directional signals about the ecosystem. Claims about local price/performance, independent deployment prevalence, current capacity and applicable formal standards remain qualified.

**Application.** For internal document RAG, compare current internal search and manual review with a modest local RAG baseline and a larger on-premises GPU running the same acceptance set. For bursty vision training and inference, start with a small rented GPU and measure a larger on-demand GPU or portable ASIC on the same workload. Both need comparable quality, latency and total cost. The business unit of value changes from accepted answers to accepted images and training runs.

**Organization.** Propose a 12-week benchmark and facilities assessment for the fictional life-sciences company. Existing CUDA skills help, but limited power and restricted data constrain the shortlist. For the startup, propose a capped on-demand trial with a GPU fallback in approved cloud regions. Low capital and bursty demand make reversibility valuable.

## Monitoring and decision log

| Priority | Owner and review point | Signal and management action |
|---|---|---|
| 1 · Primary | ML platform and facilities, week 12 | Enter bid review only after improved cost per accepted answer at agreed quality and p95 latency against the strongest feasible baseline, within measured power and cooling headroom. |
| 1 · Contrast | Startup ML lead, every two weeks | Extend an alternative only if it improves cost per accepted image at comparable quality and latency after porting effort, while meeting the training deadline. |
| 2 · External | Procurement monthly and before bids, cloud operations weekly during the startup trial | Refresh benchmark results, quotes, lead times or regional quotas. Reopen the shortlist or switch to fallback when a verified change threatens the agreed operating target. |
| 3 · Governance | Security and finance on a data, hosting-terms or commitment change | Reassess data permissions and contract terms before changing hosting or making a commitment. |

Approve these gates before gathering results. No numerical service threshold has been approved. A credible alternative view is to start with manual search and defer accelerator trials until demand is measured. Reopen the pilot decision if that baseline satisfies the agreed service level or if facilities make the shortlisted configurations infeasible. The alternative is an analytical dissent for review. No member position is attributed.

The dated AWS comparison is scoped to EC2 P5e/P5en and remains vendor evidence. A representative paired benchmark and current terms are required to promote it to a local economic claim.

## AI use, verification and Lab 10 handoff

Codex compared pinned candidate artifacts, checked original publishers, adapted the cases, drafted the synthesis and authored three saved model demonstrations in this conversation. Local checks covered frozen core integrity, prompt assembly and schema conformance. Human approval, workshop timing and individual verifier assignments require the team's record. The first Lab 10 question is which exact versions the orchestrator should route to when historically approved prompts and later retests differ. See the [seven-agent audit](integration-audit.md).
