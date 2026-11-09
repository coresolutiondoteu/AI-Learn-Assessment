#!/usr/bin/env python3
"""Evidence-first learning clinics, one per learning module, three staged checks per clinic."""
import json
from pathlib import Path
C=[]
def step(stage,question,correct,wrong,explanation,why_wrong,insight):
    assert len(wrong)==3 and len(why_wrong)==3
    return dict(stage=stage,question=question,options=[correct,*wrong],answer=correct,explanation=explanation,
                distractor_notes=dict(zip(wrong,why_wrong)),insight=insight)
def clinic(id,title,story,objective,evidence,constraints,steps,proof,connections):
    assert len(steps)==3 and len(evidence)>=3
    C.append(dict(id=id,title=title,story=story,objective=objective,evidence=evidence,constraints=constraints,steps=steps,proof=proof,connections=connections))

clinic('stack','The green UI, the denied tool','A team reports that its coding assistant “worked.” The UI displayed success, but the execution trace records a failed write under a restricted identity.',
 'Distinguish interaction, control, tool execution and independent evidence.',
 [['Signal','Observed','Implication'],['UI result','Success text','A claim, not a side-effect receipt'],['Tool action','WRITE /etc/service.conf','Privileged target'],['Executor','DENIED: scope mismatch','Trusted control remained effective']],
 ['Do not alter the model or broaden privileges just to make the UI match.','The report must identify exactly what ran and what was denied.'],[
 step('1 · Establish observed state','Which statement can be proven from these traces?',
      'The model proposed or reported success, but the actual write was denied.',
      ['The service configuration was updated successfully.','The GPU refused to execute the requested tokens.','The UI text automatically overrode the OS denial.'],
      'Use execution receipts to establish side effects, not generated prose.',
      ['There is explicit denial evidence.','Device kernels are not tool authorization.','A display has no override authority.'],
      'Write “observed” and “inferred” in different columns.'),
 step('2 · Locate responsibility','Where should the permission to write the protected file be enforced?',
      'At the authenticated tool executor, tied to exact resource/action scope.',
      ['In the chatbot prose before it generates an answer.','In the terminal theme and button state.','By requiring the model to include a yes/no field in output.'],
      'The executor owns side effects and must independently check authority.',
      ['Prompt instructions are advisory.','UI flags can be bypassed.','Generated JSON is not a grant.'],
      'Separate tool discovery, request validation and execution.'),
 step('3 · Design the acceptance test','What proves that this incident cannot silently mutate a forbidden path?',
      'Replay a hostile tool proposal; verify denial, unchanged file content and a redacted audit event.',
      ['Ask the model to promise to follow the policy.','Inspect only the final chat response.','Keep the privileged tool but hide it from the navigation.'],
      'Negative tests need observed denial and unchanged authoritative state.',
      ['Promises are not execution proof.','Final text does not show file mutations.','UI hiding does not restrict API calls.'],
      'Include this denial test in the release suite.')],
 'Evidence pack: effective identity, tool arguments, denial receipt, unchanged target hash and trace ID.', ['eval','harness','tools'])

clinic('models','A template change disguised as a model failure','A new model family loads correctly, but some assistant messages expose literal role markers and structured tool calls no longer parse.',
 'Identify representation compatibility before blaming weights or compute.',
 [['Signal','Prior','After'],['Model load','PASS','PASS'],['Role parsing','99.8%','82%'],['Template digest','A','B'],['GPU availability','PASS','PASS']],
 ['No retraining budget.','Preserve the ability to roll back to the known-good serialization.'],[
 step('1 · Read the evidence','Which regression is most closely aligned with the observed change?',
      'Chat template/role serialization compatibility.',
      ['GPU driver performance under load.','RAG index ranking quality.','A missing training checkpoint in the model weights.'],
      'Role markers failing after a template change suggest serialization mismatch.',
      ['GPU is available and tool marker parsing is semantic.','Retrieval is not in the incident path.','Inference weights still load.'],
      'Changes in one layer may be misreported as defects in another.'),
 step('2 · Plan a controlled comparison','Which controlled test isolates the suspected cause?',
      'Replay identical input/tool fixtures with template A and B while keeping weights and backend fixed.',
      ['Upgrade weights, template and driver simultaneously.','Compare only output fluency on one open-ended question.','Change top-p until markers look correct.'],
      'One-variable comparisons plus exact serialized traces enable attribution.',
      ['Confounded changes prevent attribution.','Fluency does not measure tool parsing.','Sampling tuning cannot repair a format mismatch.'],
      'Track role markers and stopping tokens explicitly.'),
 step('3 · Make the release decision','What is a justified acceptance gate?',
      'Tool/role parsing plus end-to-end task outcomes meet baseline with tested rollback.',
      ['The weights load, therefore the release is ready.','The UI looks unchanged.','The first generated sentence is grammatically correct.'],
      'Loading and rendering are necessary but not sufficient for contractual compatibility.',
      ['Load success omits behavior.','UI cannot establish serialization correctness.','Grammar does not prove tool calls.'],
      'Version the tokenizer, chat template and weights independently.')],
 'Evidence pack: serialized messages, tokenizer/template IDs, parsing scores, canary test and rollback procedure.', ['stack','context','local'])

clinic('inference','The 7B model that fits until real users arrive','A local inference team sizes a model by its weight file only. A long-context deployment becomes unavailable when eight users connect.',
 'Estimate KV memory, then translate the capacity model into an admission plan.',
 [['Parameter','Baseline','Target'],['Weights','7B at ideal 4-bit ≈3.5 GB','Same'],['KV cache','448 MiB at 4K × 1','16K × 8 users'],['KV precision','FP16','FP16'],['Serving overhead','Not included','Not included']],
 ['Hypothetical 28 layers, 8 KV heads, head dim 128.','Do not treat an illustrative formula as a real-model measurement.'],[
 step('1 · Compute pressure','Using the supplied baseline, approximately how much KV is required for the target?',
      'About 14 GiB: 448 MiB × 4 context × 8 sequences.',
      ['448 MiB because all users share one cache.','3.5 GB because KV cannot exceed model weights.','About 1.75 GiB because concurrency has no memory cost.'],
      'For fixed KV precision/geometry, memory scales roughly with context tokens and sequences.',
      ['Attention state differs per sequence.','Weights and KV are separate allocations.','1.75 GiB represents one 16K sequence.'],
      'Calculate before changing max-concurrent settings.'),
 step('2 · Interpret a slowdown','After enabling continuous batching, throughput rises but interactive p95 doubles. What can be concluded?',
      'Capacity and tail responsiveness improved in different directions; both require separate acceptance tests.',
      ['Higher aggregate throughput guarantees every request is faster.','The model grew more parameters from batching.','A p95 regression proves tokenizer corruption.'],
      'Throughput does not imply per-user latency improvement.',
      ['Scheduling may increase waiting time.','Schedulers do not change weights.','Tokenizer corruption needs other evidence.'],
      'Slice latency by prompt length and concurrency.'),
 step('3 · Decide architecture','Which deployment action is defensible before buying hardware?',
      'Benchmark target load; cap context/concurrency or cache geometry with quality and SLO gates.',
      ['Assume 4-bit weights solve all memory issues.','Disable OOM telemetry so dashboards remain green.','Allow unlimited clients because paging always makes memory free.'],
      'Control admission using measured memory and latency budgets.',
      ['KV may dominate.','Hidden failure is still failure.','Paging/offload may hurt SLO or be unavailable.'],
      'Keep a quantified peak-memory margin and recovery behavior.')],
 'Evidence pack: KV geometry sheet, 1/4/8-client load test, TTFT, p95, GPU peak, OOM scenario.', ['local','production','models'])

clinic('local','The endpoint responds; the application fails','A team switches a local inference engine behind an “OpenAI-compatible” endpoint. The dashboard returns healthy while structured tool calls break.',
 'Separate process liveness, model readiness and complete API behavior.',
 [['Metric','Before','After'],['/health','200','200'],['Model ready','PASS','PASS'],['Tool-call parse','99%','85%'],['p95','3.8 s','2.6 s']],
 ['Keep the known-good backend available.','Do not assume faster response is an acceptable substitute for correct tools.'],[
 step('1 · Classify the regression','What is currently disproven?',
      'That a healthy HTTP listener guarantees the application-level tool contract.',
      ['That the server responds to any request.','That latency improved in the measured sample.','That an HTTP endpoint can present health status.'],
      'Liveness and API tool semantics are distinct checks.',
      ['Health is returning successfully.','p95 was measured lower.','A 200 response proves the listener exists.'],
      'Trace one exact tool call from serialized input to consumer parser.'),
 step('2 · Select evidence','Which test should be prioritized?',
      'Freeze task fixtures and compare streaming fragments, tool schemas and semantic results across engines.',
      ['Compare model file sizes only.','Change the frontend layout and retest.','Increase context for every request without checking stream events.'],
      'Feature-level compatibility must be measured on behavior users consume.',
      ['Size says nothing about API semantics.','Presentation is not this fault.','More context does not repair event parsing.'],
      'Pin both model and engine revisions in a reproducibility manifest.'),
 step('3 · Make the release gate','What do the measured results justify?',
      'Hold rollout until tool parsing meets required threshold, while preserving the measured latency benefit as a candidate.',
      ['Roll forward because p95 dropped by 1.2 seconds.','Delete tool validation from the client.','Relabel the endpoint as fully compatible without evidence.'],
      'Independent hard criteria must pass before release.',
      ['Latency gains cannot compensate for broken core behavior.','Validation removal conceals errors.','Protocol labels are not acceptance evidence.'],
      'Report capability differences rather than just benchmark averages.')],
 'Evidence pack: health/readiness probes, streaming contract fixtures, schema/semantic accuracy, rollback digests.', ['context','inference','eval'])

clinic('context','The decision lost during compaction','A coding agent makes a correct read-only plan, then a long transcript is compacted. An earlier “never mutate production” constraint disappears; the next tool proposal requests a write.',
 'Design context compaction without making the model transcript the source of truth.',
 [['Record','Before compaction','After'],['Production write policy','Prohibited','Missing from summary'],['Prompt length','29K','6K'],['Tool proposal','Read-only','Write requested']],
 ['The task still needs efficient context.','Trustworthy approvals must survive restart and compaction.'],[
 step('1 · Locate the failure','Which statement is best supported?',
      'A material constraint was lost from context; the executor must still independently prohibit the write.',
      ['The model weights forgot the policy and need retraining.','Lower token count automatically proves improved safety.','Any missing summary detail automatically grants permission.'],
      'Compaction is lossy, and authority must not live only in text.',
      ['Weights were not modified.','Smaller is not necessarily safer.','Omission is not consent.'],
      'Compare the compiled prompt with a durable decision ledger.'),
 step('2 · Decide what persists','What state must remain authoritative outside the prompt?',
      'Task constraints, approvals, resource scope, accepted results and replayable side-effect receipts.',
      ['Only a short model-written summary of the last chat turn.','Only GPU prefill telemetry.','Only the most recent user emoji and assistant greeting.'],
      'Structured state is required for continuity and safe recovery.',
      ['Summaries can drop critical conditions.','Telemetry does not express intent and permission.','Conversation style does not define contracts.'],
      'Link authoritative state entries to original evidence IDs.'),
 step('3 · Set an acceptance gate','Which negative test best validates the repair?',
      'Force compaction before a privileged proposal, then verify executor denial and preserved constraint provenance.',
      ['Ask the model to summarize more confidently.','Run only short contexts where the bug never occurs.','Increase output token limit without a state check.'],
      'Test the actual failure boundary under the conditions that triggered it.',
      ['Confidence does not preserve policy.','Avoiding long contexts hides the bug.','Completion budget does not create durable authorization.'],
      'Track source IDs, decision revisions and effective tool authority in traces.')],
 'Evidence pack: source constraints, context manifests before/after, tool-denial trace and state-resume test.', ['harness','rag','eval'])

clinic('harness','The retry that created two resources','A durable automation creates a VM. Its API succeeds but the response is lost. The worker crashes before recording completion and repeats the create on restart.',
 'Make retry behavior safe when network success and local knowledge diverge.',
 [['Signal','Observed','Meaning'],['Create API','Success at target','Resource exists'],['Local receipt','Missing','Ambiguous local state'],['Restart action','Second create','Duplicate side effect']],
 ['The workflow must be resumable after arbitrary crashes.','Resource ownership must be provable.'],[
 step('1 · Recognize the ambiguity','What does a client timeout prove?',
      'The caller lacks a confirmed response; it does not establish whether the target committed.',
      ['The create API definitely rolled back.','The request definitely failed before reaching the server.','The model should choose success when it is confident.'],
      'Transport outcome and external commit state are separate facts.',
      ['Successful remote state can be lost to the client.','Delivery may have occurred before timeout.','Confidence cannot prove resource state.'],
      'Preserve stable operation IDs and check target inventory.'),
 step('2 · Design the state machine','Which sequence supports safe restart?',
      'Record intent and operation ID, execute once, reconcile target state, persist receipt, then resume dependent steps.',
      ['Create repeatedly until at least one success message appears.','Record “done” before checking the target result.','Rebuild from conversational history only, without target checks.'],
      'Durable receipts and idempotent external actions make continuation reliable.',
      ['Duplicates become likely.','Optimistic state can lie.','Generated text is not authoritative.'],
      'Model failures at every transaction boundary.'),
 step('3 · Define proof','Which test demonstrates useful resilience?',
      'Inject a crash after remote success; restart and verify exactly one target resource exists with a complete ledger.',
      ['Run once under ideal networking and count no errors.','Have the model say the retry logic is safe.','Confirm that the UI loading animation finishes.'],
      'A replay test after ambiguous success exercises the true failure surface.',
      ['Happy path misses duplicate risk.','Self-certification is not a test.','UI progress is not external state.'],
      'Use resource ownership labels and idempotency keys where supported.')],
 'Evidence pack: operation IDs, before/after target inventory, state transitions, crash-injection test.', ['production','tools','eval'])

clinic('tools','48 tools, lower success','An agent’s catalog grows from 8 to 48 tools. Task success and selection accuracy fall while API execution reliability remains unchanged.',
 'Diagnose tool ambiguity from measured evidence, then enforce a safe discovery architecture.',
 [['Metric','8 tools','48 tools'],['Task success','94%','76%'],['Correct tool selection','97%','79%'],['Tool execution success','99%','99%'],['Input tokens','3,200','8,900'],['Context truncated','0%','0%']],
 ['All business functionality must remain available.','The model cannot be replaced in this iteration.','No user may acquire a capability they are not authorized to use.'],[
 step('1 · Diagnose the symptom','Which variable is most implicated by the table?',
      'Selecting the appropriate tool from a larger overlapping catalog.',
      ['A new context truncation error.','A measured decrease in API execution reliability.','The complete disappearance of the model’s tool-call capability.'],
      'Selection accuracy fell while execution stayed 99% and no truncation was observed.',
      ['Truncation was 0%.','API success stayed 99%.','Tool calls still occur.'],
      'Do not infer unique causality without a controlled tool-subset A/B test.'),
 step('2 · Choose the diagnostic experiment','Which experiment isolates catalog complexity with least confounding?',
      'Keep model/tasks fixed and compare full tool visibility with task-specific subsets; inspect selection and outcomes.',
      ['Change the model, descriptions and test set simultaneously.','Increase context and treat faster results as evidence of correctness.','Measure only per-endpoint API latency.'],
      'A controlled catalog A/B test targets selection quality, not unrelated factors.',
      ['Confounded variables defeat attribution.','Latency alone does not measure selection.','Endpoint speed cannot explain observed selection regressions.'],
      'Report both selection errors and task success for each subset.'),
 step('3 · Choose an architecture','What change can preserve all tools and reduce selection ambiguity without violating authorization?',
      'Task-aware capability discovery, minimal exposed sets, and independent per-call policy checks.',
      ['Expose all tools with longer descriptions in every request.','Execute all candidate mutating tools concurrently and select the best result.','Let the model assign itself permissions during discovery.'],
      'Discovery targets relevance; authorization still determines whether a specific tool may run.',
      ['More tokens may not cure semantic overlap.','Parallel mutations increase side effects.','A model cannot grant resource authority.'],
      'Build cross-user denial tests for discovery and execution independently.')],
 'Evidence pack: frozen task set, confusion matrix of selected tools, timing/token breakdown and authorization denials.', ['harness','eval','context'])

clinic('rag','The retrieved policy from the wrong tenant','A policy assistant answers a public customer question using an internal staff document. Filtering occurs after retrieval has passed snippets into the model.',
 'Analyze grounding quality and data authorization as separate axes.',
 [['Signal','Observed','Question'],['Retrieval recall@5','94%','Is evidence present?'],['Citation support','91%','Is each claim supported?'],['Cross-tenant snippet in context','YES','Was access permitted?']],
 ['Private passages must never enter an unauthorized user’s model context.','The assistant should still answer public-policy queries.'],[
 step('1 · Separate metrics','Which result blocks release regardless of recall and citation scores?',
      'An unauthorized source entered the prompt context.',
      ['Retrieval recall is below a hypothetical 100% target.','The answer was syntactically valid JSON.','The returned snippet had a plausible title.'],
      'Access control is a hard boundary independent of search relevance.',
      ['Recall can be imperfect without breaching confidentiality.','Syntax is not authority.','Titles do not imply permission.'],
      'Trace document ACL from ingest through candidate selection.'),
 step('2 · Fix the pipeline','Where must permission filtering occur?',
      'Before protected documents are exposed to generation, including lexical/vector/rerank paths.',
      ['Only after the final answer is rendered.','Only in the browser user interface.','Only when a model voluntarily asks for permission.'],
      'Once private material enters context, post-processing cannot undo the exposure.',
      ['Final filtering is too late.','Hiding output does not secure input.','Models do not own data entitlements.'],
      'Test unauthorized retrieval at every search path, not only final text.'),
 step('3 · Improve quality','After fixing access, which evaluation verifies both usefulness and safety?',
      'Authorized recall, claim-level citation support, abstention and cross-tenant negative tests.',
      ['Only average semantic similarity to source chunks.','Only that the model replies confidently.','Only a browser screenshot of the policy text.'],
      'Quality and confidentiality must be measured independently.',
      ['Similarity alone does not prove relevance or permission.','Confidence is not evidence.','Screenshots cannot inspect data paths.'],
      'Include old-policy and conflicting-source cases for freshness/authority.')],
 'Evidence pack: document ACLs, permitted candidate IDs, cited claim spans and failed/denied retrieval traces.', ['context','eval','tools'])

clinic('eval','The green dashboard that hid a failure','A release looks excellent by average task score. A new version improves most answers but begins requesting forbidden actions.',
 'Judge upgrades with independent quality, operational and safety gates.',
 [['Metric','Baseline','Candidate'],['Task success','86%','90%'],['Unauthorized actions','0','3 / 500'],['p95 response','3.7 s','3.2 s'],['Security gate','0 actions','0 actions']],
 ['The forbidden-action gate is mandatory.','A passing suite is conditional evidence, not a guarantee of zero risk.'],[
 step('1 · Read the scorecard','Which metric most directly blocks release?',
      'Three unauthorized actions against a zero-action policy gate.',
      ['A four-point improvement in answer success.','Lower tail latency under the same load.','The number of evaluation questions being finite.'],
      'Safety gates must not be traded against answer quality.',
      ['Improvement does not erase policy failures.','Latency improvement is desirable.','Finite tests affect certainty, but the observed violations are concrete.'],
      'Report the violating trajectories, not just the aggregate count.'),
 step('2 · Diagnose safely','Which evidence should be preserved for each unsafe case?',
      'Input source, model/context version, proposed arguments, authorizer verdict, side effect and redacted trace.',
      ['Only the final answer text.','Only the GPU temperature during inference.','Only the percentage of correct ordinary FAQs.'],
      'Trajectory replay reveals whether the failure lies in proposals, policy or execution.',
      ['Final text can hide attempted side effects.','Device temperature is not action authority.','Unrelated FAQs do not describe this failure.'],
      'If executor denied all proposals, distinguish attempts from actual forbidden commits.'),
 step('3 · Design the gate','Which release process best fits the evidence?',
      'Block pending root-cause and negative regression proof; rerun frozen and new failure cases before canary.',
      ['Ship immediately because average correctness rose.','Delete rare failure categories from the test suite.','Disable traces so user reports are the only signal.'],
      'Releasing by evidence requires stable hard gates and expanding failure suites.',
      ['Aggregate accuracy is insufficient.','Removing tests hides risk.','Lack of traces impairs review.'],
      'Define failure-specific ownership and rollback trigger.')],
 'Evidence pack: frozen evaluation fixtures, unsafe trajectories, per-slice metrics, policy test and canary rollback.', ['harness','production','rag'])

clinic('production','Faster is not always better','An AI platform has strict p95 response targets and regulated workloads. A candidate backend improves reasoning but exceeds the latency SLO for routine requests.',
 'Choose a measured service architecture with operational recovery and quality gates.',
 [['Metric','Baseline','Candidate'],['Routine p95','3.3 s','8.1 s'],['Reasoning accuracy','86%','89%'],['SLO','≤4 s','≤4 s'],['Sensitive-data handling','Local','Requires policy review']],
 ['Do not redefine the SLO after measuring the candidate.','Respect data-handling policy and rollback requirements.'],[
 step('1 · Identify the trade-off','Which finding is established by the provided numbers?',
      'The candidate improves measured accuracy but fails the routine request p95 SLO.',
      ['All requests are slower by exactly 4.8 seconds.','The baseline is inaccurate for every user.','The new backend is impossible to use for any workload.'],
      'Measured aggregate and tail outcomes support a trade-off, not an absolute judgment.',
      ['p95 does not apply to each request.','86% includes successful cases.','Different tasks may justify different latency.'],
      'Do not hide minority regressions behind average improvements.'),
 step('2 · Evaluate architecture','Which response preserves both business requirements best?',
      'Test task-aware local/hosted routing with strict data classification, measurable fallback and per-class SLOs.',
      ['Send all regulated documents to the hosted model by default.','Use only the fast model, regardless of difficult-case failures.','Choose by GPU model number without task evaluations.'],
      'Hybrid selection can balance latency, quality and data boundaries if measured and governed.',
      ['Data residency may prohibit it.','Complex tasks may need stronger reasoning.','Hardware labels are not completed-task outcomes.'],
      'Include routing overhead and misclassification in benchmarks.'),
 step('3 · Define a production gate','Which package of evidence justifies rollout?',
      'Representative A/B tasks, per-slice p95, factual/safety checks, cost per accepted task, canary and rollback test.',
      ['One polished demo and a positive customer quote.','Average output tokens/s alone.','A plan to measure failures only after all users migrate.'],
      'A release gate must cover user outcomes, operational reliability and recovery.',
      ['Anecdotes cannot prove safety.','Token speed omits task completion.','Post-release-only measurement shifts risk to users.'],
      'Write an ADR with rejected alternatives and an exit/rollback criterion.')],
 'Evidence pack: routing ADR, per-class quality/p95/cost, data policy matrix, canary and rollback results.', ['inference','eval','local'])

if __name__=='__main__':
    root=Path(__file__).parent
    modules={m['id'] for m in json.loads((root/'modules.json').read_text())}
    assert {x['id'] for x in C}==modules
    for c in C:
        for s in c['steps']:
            assert len(s['options'])==4 and len(set(s['options']))==4 and s['answer'] in s['options']
            assert len(s['distractor_notes'])==3
    (root/'engineering-clinics.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('Generated',len(C),'deep engineering clinics and',sum(len(c['steps']) for c in C),'interactive reasoning stages')
