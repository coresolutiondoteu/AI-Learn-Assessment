# Assessment & Engineering Clinic Design — v2.0

## Intended outcome

The academy moves from **term recognition** to **causal interpretation** to **defensible engineering judgment**. The exam is formative and local. Learners should understand why a decision is right, why another is tempting, what evidence is insufficient, and what changes would invalidate their conclusion.

The operational progression is:

1. **Foundations (L1):** Define the entity or boundary, identify which component owns an operation, and distinguish terms that sound similar.
2. **Applied understanding (L2):** Read a trace or evidence table, recognize a confounder, infer a likely failure boundary, choose an isolation test. Avoid claiming more than the data support.
3. **Engineering judgment (L3):** Select an architecture under explicit cost, access, reliability and ownership constraints; argue what remains unproven and how the change can be validated/rolled back.

## Scoring blueprint

| Exam | Level 1 (30%) | Level 2 (50%) | Level 3 (20%) | Total | Pass |
|---|---:|---:|---:|---:|---:|
| Full 20 | 6 | 10 | 4 | 20 | 16 |
| Full 30 | 9 | 15 | 6 | 30 | 24 |
| Full 40 | 12 | 20 | 8 | 40 | 32 |
| Per-module 20 | 6 | 10 | 4 | 20 | 16 |

Full examinations draw uniformly across the ten competencies; source item counts need not match exam percentage. Section examinations use the selected domain only. The basic observation that 30% + 50% = 80% is a **marking property**: perfect foundation and applied responses can pass without Level 3. It does not guarantee that passing requires such perfection, since an individual may earn some L3 points and miss easier questions. Every wrong or unanswered choice counts as incorrect; scores are not weighted after selection because the exam quota already provides the weighting.

Correct answer positions are randomized. Hints, answer explanations and individual alternative rationales are deferred until *after* scored exam submission. An unscored guided challenge and clinics reveal feedback immediately to support learning. Repeated attempts may encounter questions again; this is useful for rehearsal but should not be interpreted as an independent proficiency certification.

## Question writing and reviewing rubric

For an advanced item to be retained, reviewers should check:

- **One decision:** Clear question with a bounded meaning of *best*, *most directly supported* or *first diagnostic step*. Where multiple answers could be defensible, add a constraint or change the stem.
- **Evidence before claim:** Use observed state, relevant context and numbers when the learner must infer causes. Do not infer root cause from a mere correlation. If evidence is inconclusive, make selecting an isolation experiment the correct action.
- **Plausible alternatives:** Every wrong choice represents a specific engineering misconception or legitimate competing approach that fails *under the scenario constraints*, not an unrelated technology or a cartoonishly bad security practice.
- **Comparable grammar and length:** Choices should have similar specificity, syntax and approximate verbosity, with no giveaway words like *always*, *never*, or *obviously* reserved only for wrong options. Random option ordering is not a substitute for editorial balance.
- **One defensible key:** Correctness must follow from stated facts plus taught principles, not a reviewer’s unstated preferred stack/tool. Specialist reviewers should check both the key and the distractors.
- **Feedback teaches:** Explain why the best option meets the goal; why each alternative is less suitable; what concept/term would help; what measurement or test would verify it in a real system.
- **Technical safety:** Do not advise bypassing tool authorization, treating LLM content as an approval, leaking secrets, or performing destructive external actions as part of an exercise.
- **Traceability:** Preserve stable item ID, module, level, concept/term mapping, and evidence link. Keep changed items and reviewer notes versioned.

### Example: tools and orchestration

**Situation:** A harness grows from 8 to 48 tools. Task success decreases 94% → 76%. Tool-selection accuracy falls 97% → 79%, tool execution reliability remains 99%, input tokens increase 3,200 → 8,900 and context truncation is 0% before and after.

**L1:** Distinguish a tool call from the actual authorized execution of a tool.

**L2:** Infer the failure boundary most consistent with evidence: selection ambiguity is growing while the tools themselves remain reliable. More tokens may raise cost/latency, but zero truncation does not support the claim that instructions are being lost to context overflow. This is not proof that tool selection is the *sole* cause; test against matched tasks.

**L3:** With business functionality fixed and the model unchanged, propose task-aware discovery that provides only a relevant, identity-scoped tool subset per request. **Discovery is not authorization**: every chosen call still requires independent policy checks and bounded execution. Record tool-selection quality, task success, latency and authorization-denial outcomes for a fair A/B comparison.

This pattern is general: measured observation → discriminating diagnosis → controlled architectural response → independent validation.

## Engineering clinic teaching contract

Every one of the ten modules has a three-stage local clinic:

- **Observe:** Determine what the facts show and what remains unknown.
- **Diagnose:** Identify the next test or isolate a component/authority boundary.
- **Decide:** Choose the safest architecture or recovery action under explicit constraints, explaining rejected alternatives.

A completed 3/3 indicator means all three questions were *attempted*, **not** that engineering proficiency is certified. Learners are encouraged to run corresponding labs in controlled environments, retain traces, and explain limitations in a short design record. The clinic is designed to lead naturally into that lab evidence.

## Calibration and pilot testing (not yet conducted)

1. Ask beginners, experienced AI engineers, and independent security/platform reviewers to complete the same fixed set **without answer keys**. Collect item-level selection, duration, confidence and feedback, without collecting private data unnecessarily.
2. Calculate percent correct by level, the distribution of overall scores, and *item discrimination*: whether higher-scoring learners disproportionately choose the keyed answer. Flag items solved by easy distractor elimination.
3. Inspect option-choice frequencies. A distractor never chosen may be implausible; a distractor preferred by experts may indicate ambiguous wording or an incorrectly keyed answer.
4. Measure learning gain on unseen but equivalent scenarios after lessons and clinics, rather than on repeated identical questions alone.
5. Set targets from measured data, revise problematic items with specialist review, freeze a sample for future comparisons, and rerun tests after every item-bank change.
6. For a public release, perform real desktop/mobile browser QA, keyboard-only navigation, assistive-technology checks, local backup/import and installation-free offline smoke tests. Automated GUI QA could not be completed in the managed build environment.

Do not claim that 80% is demonstrably challenging or that 100% is objectively difficult until actual learner score distributions support those descriptions.

## Existing material preserved and remaining debt

The 46-page field manual and two-page opening companion have not been rewritten in this release. Their original content and historical assessment outline remain companion resources; **this file and the v2.0 application are authoritative for the revised scoring blueprint**. Existing 252 questions remain intact in the canonical `source/question-bank.json`; original advanced questions map to L2, so some may still have straightforward distractors. The 120 new questions and 30 clinic stages received deeper curation. A future release should editorially refresh the full legacy bank, integrate the deeper clinics into the PDFs, introduce independent reviewer and learner feedback, and perform real browser QA.
