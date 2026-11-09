#!/usr/bin/env python3
"""Editorial pass: trim the telltale longest-correct-option bias in scenario questions.
The full reasoning is retained in explanations; stable IDs and unambiguous answer keys remain.
"""
from pathlib import Path
import json
root=Path(__file__).parent
base=json.loads((root/'scenario-questions.json').read_text(encoding='utf8'))

answers={
'stack':[
 'The write was denied by the executor, despite the UI result.',
 'A harness adds authorized execution and a continuing task loop.',
 'The tokenizer and chat template for the target model.',
 'That containers automatically enforce separate per-tool authorization.',
 'The trusted application policy and tool executor.',
 'Replay fixed tasks and compare the harness control-flow traces.',
 'Separate the planes and enforce approval at the mutation executor.',
 'Share inference; isolate each client’s harness and tool authority.',
 'A/B-test the changed chat template on fixed tool-call cases.',
 'Restrict host mounts/privileges and verify explicit denial tests.',
 'Block release until executor authorization and auditing are proven.',
 'Review data flow, local authority, API behavior and regression evidence.'
],
'models':[
 'The tokenizers split the same text differently.',
 'The input context changed; the model weights did not.',
 'Additional prefill and attention-state work before the first token.',
 'Greedy output may vary across serving implementations.',
 'Retrieval supplies current, attributable facts without changing weights.',
 'Check that each claim has current authoritative source support.',
 'Version representation artifacts; regression-test role and tool parsing.',
 'Use retrieval for changing facts, with selective behavioral adaptation.',
 'Test evidence selection against long-context quality and cost.',
 'Pin artifacts and verify edge amounts against authoritative calculations.',
 'Preserve risk-aware routing until the sensitive-case regression is resolved.',
 'Cite competing evidence and abstain or escalate unresolved conflicts.'
],
'inference':[
 'Separate queue time, cold load and prefill from decode.',
 'KV cache, activation/buffer overhead and mixed-precision allocations.',
 'The backend has an inefficient path for this quantization.',
 'Compare quality, latency, throughput and peak memory on real tasks.',
 'Higher throughput coincided with worse p95 responsiveness.',
 'Benchmark 1, 4 and 8 concurrent realistic long-context clients.',
 'Profile TTFT; test task-aware retrieval or prefix reuse under recall gates.',
 'About 14 GiB of KV state, before weights and overhead.',
 'Hold the faster kernel until the numeric regression is resolved.',
 'Size total load memory; test cache geometry and admission limits.',
 'Workload-aware priority/admission scheduling with fairness and p95 gates.',
 'Verified total cost per accepted task, including recovery and review.'
],
'local':[
 'The engine’s format, architecture and serialization compatibility.',
 'Concurrent admission, batching and serving-memory behavior.',
 'Add authentication, network controls, quotas and protected transport.',
 'Replay tool-call stream and error-contract compatibility tests.',
 'Inspect device visibility, backend selection and driver compatibility.',
 'A model-readiness probe, separate from process liveness.',
 'Pin compatible model/engine/template artifacts with offline rollback.',
 'Test priority classes or isolated service pools against p95.',
 'An authenticated TLS gateway and a private scoped model endpoint.',
 'Hold rollout until structured-output validity meets its release gate.',
 'Baseline, tested rollback, controlled canary and live workload validation.',
 'Bound admission and restarts; monitor load and OOM recovery.'
],
'context':[
 'Treat the ticket as untrusted data, never as governing instruction.',
 'The model-specific chat template and role-token conventions.',
 'Retrieval selection/relevance degraded despite available context capacity.',
 'Semantic checks on valid ownership and permitted resource IDs.',
 'An authoritative decision and approval ledger outside the transcript.',
 'Cache reuse proves neither evidence freshness nor source version.',
 'Preserve provenance, validate actions and gate mutations independently.',
 'Replay fixtures across serialization and streamed tool-call contracts.',
 'Permission-filtered, reranked evidence with measured abstention behavior.',
 'Block until referential/tenant checks and denial tests meet policy.',
 'Persist structured task state and receipts; assemble per-turn context.',
 'Prove tenant-aware cache keys and context-isolation behavior.'
],
'harness':[
 'The second agent made an unauthorized edit despite a useful patch.',
 'Compare it to a deterministic pipeline on cost and task success.',
 'Budgeted retries, denial-aware state and a termination rule.',
 'Reconcile target state by stable operation ID before retry.',
 'Measure resources and retries per accepted task against stop rules.',
 'A durable action ledger and state checkpoint with receipts.',
 'Separate read/build from writes; bind approval to exact deployment.',
 'Keep fixed stages, using bounded agents only for proven exceptions.',
 'Executor-side identity, scoped destination and action authorization.',
 'Reconcile inventory by ownership ID, then resume idempotently.',
 'Require new evidence per retry and enforce budgeted escalation.',
 'Version-lock reviewed artifacts and invalidate stale approvals.'
],
'tools':[
 'Selection ambiguity grew; executor reliability remained unchanged.',
 'Validate business status separately from exit and transport status.',
 'Host consent and server-side caller/resource authorization both apply.',
 'Inspect negotiated protocol, transport and token audience requirements.',
 'A2A delegation with independent task lifecycle and identity.',
 'Caller/resource policy remains mandatory despite tool discovery.',
 'Task-aware tool discovery with independent per-call authorization.',
 'Durable receipts; idempotent A and request-ID reconciliation for B.',
 'Validate audiences and resource scope at host and server.',
 'Pin protocol revision and test auth, reconnect and state semantics.',
 'Durable remote task IDs, reconciliation, cancellation and idempotency.',
 'Filter by user/resource before retrieval and every tool invocation.'
],
'rag':[
 'The matching policy lacked verified freshness and authority.',
 'The chunk boundary lost an exception and its scope.',
 'Hybrid lexical/vector search with slice-based recall evaluation.',
 'Check claim-level support and disclose unresolved source conflicts.',
 'Capacity, durable memory and KV cache have different lifetimes.',
 'Recall@5 is 72%, independent of 80% answer correctness.',
 'Enforce ACLs before evidence reaches model context.',
 'Preserve parent/child clauses and retrieve linked footnotes.',
 'Add exact-ID lexical retrieval and score critical slices.',
 'Verify applicability, prioritize signed terms and cite the conflict.',
 'Revalidate ACL/freshness on memory reads with deletion controls.',
 'Hold rollout until citation-fidelity regressions meet the safety gate.'
],
'eval':[
 'The benchmark omits adversarial and abstention scenarios.',
 'The p95 target fails despite acceptable median and mean.',
 'The executor prevented access and exfiltration, not merely proposals.',
 'Unmodeled indirect execution and dependency-script side effects.',
 'The approval occurs after execution rather than preventing it.',
 'Tool trajectory, authorization decisions and observed side effects.',
 'Run held-out risk-sensitive tasks with end-to-end trajectory review.',
 'Block release because the zero-unauthorized-action gate failed.',
 'Least-privilege ephemeral sandboxes with restricted mounts and egress.',
 'Redact and restrict traces as part of defense in depth.',
 'Invalidate approval after exact digest/target changes.',
 'Reconcile target state and receipt IDs before resuming writes.'
],
'production':[
 'An ADR comparing quality, residency, cost, latency and alternatives.',
 'The measured latency distribution at the p95 boundary.',
 'Full cost per accepted task, including retries and human work.',
 'The independent security gate on forbidden canary actions.',
 'A prototype, not proven production readiness.',
 'Versioned traces to attribute model/context/tool regressions.',
 'Evaluate policy-governed hybrid routing and recovery trade-offs.',
 'Test bounded routing/fallback for each latency and quality slice.',
 'Cap concurrency/context after peak-memory and recovery tests.',
 'Tested schema migration, compatibility and rollback/forward-recovery.',
 'Reproducible fixtures, scoped execution, negative tests and review.',
 'One observation failed; test other paths before claiming service loss.'
]}
for mod,shorts in answers.items():
    items=[x for x in base if x['module']==mod]
    assert len(items)==len(shorts)==12
    for q,short in zip(items,shorts):
        q['original_answer_text']=q['answer']
        assert short not in q['options']
        q['options'][q['options'].index(q['answer'])]=short
        q['answer']=short
        assert len(q['options'])==len(set(q['options']))==4
# Follow-on editorial pass is applied here after concise answer updates.
(root/'scenario-questions.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Refined answer lengths for',len(base),'scenario questions')
