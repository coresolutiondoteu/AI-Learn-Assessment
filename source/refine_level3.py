#!/usr/bin/env python3
"""Adversarial distractor review: replace obvious nonsense in L3 with plausible near-miss decisions.
Every near miss violates a specific stated constraint, skips evidence, or weakens a trusted boundary.
"""
import json
from pathlib import Path
p=Path(__file__).parent/'scenario-questions.json'
Q=json.loads(p.read_text(encoding='utf8')); lookup={x['id']:x for x in Q}
def hard(id,opts,why):
 assert len(opts)==len(why)==3,id
 q=lookup[id]; assert q['level']==3
 q['options']=[q['answer'],*opts]
 assert len(set(q['options']))==4,id
 q['distractor_notes']=dict(zip(opts,why))

# STACK: the wrong designs are appealing shortcuts, but do not respect actual authority.
hard('stack-v2-L3-01',[
 'Keep the shared service but gate privileged actions in the browser; retain one executor identity.',
 'Split the frontend and model service, but let the harness authorize itself through generated policy.',
 'Centralize identity at an API gateway and audit all writes afterward without per-action approval.'
],[
 'A browser prompt cannot protect a privileged executor reachable through other paths.',
 'Separating processes helps only when policy is independently enforced.',
 'Authentication and after-the-fact auditing do not replace approval for exact mutations.'
])
hard('stack-v2-L3-02',[
 'Keep a common harness, but use frontend feature flags to hide write tools on mobile.',
 'Run separate model backends for each client but share a superuser tool identity.',
 'Share a global tool registry and rely on model-side prompts to restrict mobile edits.'
],[
 'Feature flags control presentation rather than the executor’s authority.',
 'Different inference endpoints do not solve the shared privileged execution identity.',
 'Registry visibility and prompt policy cannot substitute for per-client authorization.'
])
hard('stack-v2-L3-03',[
 'Upgrade the inference engine first, then retest the same prompt with the new chat template.',
 'Change the decoding settings and template together to restore the previous tool-call frequency.',
 'Keep template B and compensate with a post-processor that guesses missing role delimiters.'
],[
 'The engine is unchanged and changing it first confounds the obvious template regression.',
 'Joint changes do not isolate the representation fault.',
 'Heuristic repair of broken role separation can hide unsafe semantics and lacks an independent test baseline.'
])
hard('stack-v2-L3-04',[
 'Keep the host mounts, but require signed tool requests from the harness before using them.',
 'Run the same privileged image under a non-root entrypoint while retaining Docker socket access.',
 'Remove public network access but retain writable management mounts for faster diagnostics.'
],[
 'Signed requests do not reduce the host control granted by unnecessary mounts.',
 'A Docker socket can expose host-level privileges despite process UID.',
 'Egress restriction helps, but does not eliminate the writable host management path.'
])
hard('stack-v2-L3-05',[
 'Release behind a feature flag and monitor tool calls, leaving the existing executor authorization unchanged.',
 'Restrict model temperature and tool selection, then assume unapproved operations will be rare enough.',
 'Limit model API access to employees but retain direct deployment capability for every authenticated user.'
],[
 'Flags and monitoring are not independently enforced authorization for side effects.',
 'Probability reduction cannot replace a binding permission decision.',
 'Authentication without fine-grained authorization permits improper operations.'
])
hard('stack-v2-L3-06',[
 'Keep local tools but send the complete retrieved context to the hosted endpoint for feature parity.',
 'Move inference first, then run compatibility and data-flow tests only if production errors appear.',
 'Encrypt the outbound prompt but assume a compatible HTTP schema preserves tool behavior.'
],[
 'Sensitive context may violate residency and minimization policy even with local tool execution.',
 'Unverified migrations expose users before controls and evaluations are established.',
 'Encryption in transit does not address provider data processing or behavioral incompatibilities.'
])

# MODEL MECHANICS: distractors reflect recognizable but insufficient engineering approaches.
hard('models-v2-L3-01',[
 'Validate that the new weights load and the advertised context length passes a single stress test.',
 'Compare only final text accuracy on existing fixtures, without replaying serialized tool/role tokens.',
 'Pin the tokenizer but allow automatic template updates; regression-test only when parsing errors appear.'
],[
 'Loading and maximum length do not prove role/tool behavior.',
 'Text-only outcomes miss serialization and structured tool-call regressions.',
 'Unversioned template updates are themselves a material compatibility risk.'
])
hard('models-v2-L3-02',[
 'Fine-tune frequently on account facts, using the latest training checkpoint as the sole source of truth.',
 'Retrieve current facts but put every customer record into shared context to reduce per-user indexing cost.',
 'Use a style adapter and rely on its latent knowledge for changing financial facts unless users complain.'
],[
 'Weight updates are not an authoritative live fact store and can lag corrections.',
 'Unscoped retrieval exposes data across identity boundaries.',
 'A behavior adapter does not guarantee factual freshness or correct attribution.'
])
hard('models-v2-L3-03',[
 'Keep the full long prompt and optimize attention kernels, evaluating only latency reductions.',
 'Increase the advertised context limit and reduce retrieval so the model sees all potential evidence.',
 'Move passages closer to the prompt start without testing position effects or citation support.'
],[
 'Compute optimization does not resolve observed exception-answer quality by itself.',
 'More raw input can increase distraction and cost without effective recall.',
 'Reordering is a candidate intervention but requires controlled quality evidence.'
])
hard('models-v2-L3-04',[
 'Keep temperature zero and pin the model name, trusting backend-level determinism.',
 'Compare average extraction accuracy and accept the upgrade if the global mean improves.',
 'Use a stronger reviewer model to validate disputed amounts without authoritative recomputation.'
],[
 'A model name and decoding setting are insufficient version and numeric determinism guarantees.',
 'Rare but material edge-case regressions can be hidden by averages.',
 'Model agreement does not replace a financial calculation oracle.'
])
hard('models-v2-L3-05',[
 'Ship the adapter to every task, but add model self-confidence thresholds for the sensitive subset.',
 'Route sensitive tasks to the local adapter and use the stronger model only for non-regulated traffic.',
 'Keep the adapter for all tasks, adding a second adapter that votes on its uncertain outputs.'
],[
 'Confidence from the same model is an unreliable risk gate.',
 'This reverses the observed reliability advantage on the sensitive subset.',
 'Correlated model behavior and unsupported regression remain unresolved.'
])
hard('models-v2-L3-06',[
 'Return the most recent passage as the default answer while preserving a note about older conflicts.',
 'Select the response with the strongest model probability and attach every conflicting citation.',
 'Synthesize a single compromise policy from both sources and note that it is an interpretation.'
],[
 'Recency does not determine governing authority or scope.',
 'Probability and number of citations do not resolve factual conflict.',
 'A compromise may invent terms that neither source authorizes.'
])

# INFERENCE: wrong options optimize one metric but fail the stated correctness/SLO constraints.
hard('inference-v2-L3-01',[
 'Reduce retrieved context uniformly to meet TTFT and accept the existing accuracy benchmark without re-evaluating.',
 'Optimize decode kernels and output length before investigating slow initial-token latency.',
 'Introduce priority queueing for all requests but leave prefill size and evidence recall unmeasured.'
],[
 'Blind context reduction may eliminate critical legal sources; evidence recall is a hard requirement.',
 'Decode optimizations target later tokens rather than the diagnosed prefill/queue interval.',
 'Queueing can help but does not isolate whether long prefill is dominant or preserve evidence quality.'
])
hard('inference-v2-L3-02',[
 'Reserve 3.5 GiB for weight memory and 448 MiB for KV, because most prefixes are reusable.',
 'Reserve 1.75 GiB for KV, assuming the 16K sequence cache is shared among eight separate users.',
 'Reserve 14 GiB as the complete GPU budget, because the stated formula includes engine overhead.'
],[
 'Even cached shared prefixes do not make independent user KV free.',
 'Per-sequence KV must be multiplied by active concurrent sequences.',
 'The 14 GiB estimate is KV only; weights and runtime memory remain additional.'
])
hard('inference-v2-L3-03',[
 'Ship to a 1% canary immediately, relying on live financial-user reports for numerical regression detection.',
 'Accept the faster kernel after aggregate success passes, excluding the affected edge-value fixture.',
 'Roll back all kernel optimizations permanently without isolating the precision or workload condition.'
],[
 'High-stakes correctness should be verified before exposing real users to known regressions.',
 'Deleting the failing slice hides the exact issue the release gate should detect.',
 'Permanent rejection skips a controlled investigation of a potentially safe targeted implementation.'
])
hard('inference-v2-L3-04',[
 'Select 4-bit weights based on file fit, then dynamically raise context until the first OOM.',
 'Use context offloading as the default without latency measurement, assuming VRAM is the only bottleneck.',
 'Lower KV precision immediately, assuming quality and runtime support are equivalent across backends.'
],[
 'Testing only until failure can disrupt service and ignores concurrent target workload.',
 'Offload can incur large latency penalties and may be unavailable.',
 'KV compression changes numerical/state assumptions and requires tests.'
])
hard('inference-v2-L3-05',[
 'Increase batch size globally and optimize aggregate tokens/s while reporting p50 interactive latency.',
 'Use a single FIFO service queue but cap max output tokens for the interactive class.',
 'Serve all short prompts through the long-job queue, with a larger GPU utilization target.'
],[
 'The issue is interactive p95 fairness, not merely total throughput or median.',
 'Output caps may help decode but do not isolate long prefill queue contention.',
 'Higher utilization can coexist with worse tail responsiveness.'
])
hard('inference-v2-L3-06',[
 'Compare provider token prices, including prompt-cache discounts, but omit human review and task failures.',
 'Select the backend with higher task accuracy, assuming retries and latency have no economic cost.',
 'Choose by GPU-hour price and tokens/s under a synthetic prompt, then infer task-level spend.'
],[
 'Unit token cost excludes important outcome costs.',
 'Quality alone may not justify operational expense without accepted-task economics.',
 'Synthetic hardware efficiency does not fully represent workflows and recovery.'
])

# LOCAL SERVING: same operation, different boundaries and failure modes.
hard('local-v2-L3-01',[
 'Pin the REST schema and server version, then allow model format revisions to load opportunistically.',
 'Keep the current engine and fetch compatible model artifacts during recovery when a loader fails.',
 'Maintain one prebuilt engine per format, but choose the latest chat template dynamically on startup.'
],[
 'API compatibility does not guarantee architecture/weight/template loading.',
 'Online downloads violate the offline recovery requirement and are not reproducible.',
 'Unpinned template changes can break roles and tool calls despite engine isolation.'
])
hard('local-v2-L3-02',[
 'Keep a single shared pool with larger batches and judge success by nightly throughput.',
 'Prioritize interactive traffic but ignore fairness and starvation of overnight jobs.',
 'Build separate pools immediately, without comparing utilization or measurable SLO trade-offs.'
],[
 'Larger batches can worsen interactive tail latency.',
 'Unbounded priority can starve lower-priority work; fairness must be measured.',
 'Physical separation may help but could waste capacity without evidence.'
])
hard('local-v2-L3-03',[
 'Expose the raw model endpoint behind VPN access and rely on network membership as per-partner authorization.',
 'Use a TLS reverse proxy with one shared secret for all partners and no per-user scopes or audit.',
 'Publish the server through a web frontend, keeping inference requests unauthenticated for simplicity.'
],[
 'VPN reachability alone does not enforce partner identity, quotas or least privilege.',
 'Encryption plus a shared secret lacks per-actor scope and accountable usage.',
 'Frontend authentication is bypassable when the backend endpoint is exposed directly.'
])
hard('local-v2-L3-04',[
 'Canary the new engine with latency gates only; investigate malformed outputs from production incidents.',
 'Keep the faster engine but add retries to hide schema failures without changing acceptance thresholds.',
 'Accept 98% schema validity by lowering the downstream contract requirement to current performance.'
],[
 'The known contractual failure should block before broad rollout.',
 'Retries can compound latency/cost and may still yield wrong structure.',
 'Redefining the gate does not demonstrate safe behavior for dependent consumers.'
])
hard('local-v2-L3-05',[
 'Stage the driver update and trust a successful GPU initialization test, postponing workload validation.',
 'Upgrade the driver/kernel and model server together under a single maintenance change with snapshot only.',
 'Keep the old driver indefinitely and skip evaluation of security or compatibility updates.'
],[
 'GPU discovery does not prove end-to-end inference and tool behavior.',
 'A snapshot helps but simultaneous changes complicate diagnosis and still need tests.',
 'Avoiding all updates is not a lifecycle strategy and ignores future risks.'
])
hard('local-v2-L3-06',[
 'Increase restart frequency and keep readiness based on a lightweight localhost HTTP check.',
 'Set stricter timeouts but admit the same unbounded long-context concurrency.',
 'Disable worker restarts and count all load failures as client-side timeouts.'
],[
 'Restart loops can amplify load; a simple listener check does not measure service capacity.',
 'Short timeouts without admission controls do not prevent OOM and queuing.',
 'Suppressing recovery without controlling demand can leave unhealthy service indefinitely.'
])

# CONTEXT: the viable-sounding shortcuts miss provenance, semantic checks or effective state.
hard('context-v2-L3-01',[
 'Sanitize log text and forward the remaining instructions directly to the agent as trusted recommendations.',
 'Attach provenance labels in the system prompt but let the model make the final write authorization.',
 'Route all remediation through a single shell tool and rely on prompt-level allowlists.'
],[
 'Sanitization does not convert external data into authorized instructions.',
 'Labels aid reasoning but cannot replace independent execution policy.',
 'Generic shell access with model-only rules expands attack surface.'
])
hard('context-v2-L3-02',[
 'Check HTTP response success and one plain-text completion against the old provider before switching.',
 'Compare streamed events but leave the downstream typed argument validator disabled during migration.',
 'Freeze the UI and prompt text while assuming both providers serialize role markers identically.'
],[
 'Transport success and one sample miss structured behavior.',
 'Event shapes alone are insufficient if downstream semantic contracts are unvalidated.',
 'Shared prompt text does not imply compatible model templates or parsing.'
])
hard('context-v2-L3-03',[
 'Keep all 25 documents but move exception clauses to the first 2K tokens without evaluating retrieval.',
 'Replace retrieval with fine-tuning on the present corpus, retaining current citations as static strings.',
 'Use a larger context window and reduce the number of answer citations to simplify output.'
],[
 'Position changes can be useful but require measured source recall and grounding.',
 'Weight adaptation is not a trustworthy current evidence or citation source.',
 'Capacity and shorter output do not resolve irrelevant evidence selection.'
])
hard('context-v2-L3-04',[
 'Accept JSON output and add a human review on sampled cases while allowing all other IDs downstream.',
 'Check customer IDs for existence but do not enforce that the authenticated caller owns them.',
 'Let the model self-correct references when it notices wrong customers, without checking an authoritative registry.'
],[
 'Sampled review cannot prevent a known cross-tenant violation on unreviewed writes.',
 'Existence does not imply permission or correct tenant ownership.',
 'Model self-verification is insufficient for referential integrity and authorization.'
])
hard('context-v2-L3-05',[
 'Persist longer chat summaries and re-prompt the model to reconstruct lost decisions after restart.',
 'Keep the current active context as state and store only the last model response on disk.',
 'Persist retrieved documents but not approvals or tool receipts, rederiving those with an LLM on resume.'
],[
 'Even detailed summaries may lose exception semantics or approval provenance.',
 'Active context is not a durable transaction and state ledger.',
 'Document source data alone cannot prove historical side effects or human authorization.'
])
hard('context-v2-L3-06',[
 'Enable cache reuse by identical textual prefixes, regardless of tenant identity, and redact outputs after generation.',
 'Partition cache by model version only, since the same weights imply equivalent policy context.',
 'Disable shared prefix reuse permanently without measuring whether tenant-isolated keys would meet SLO.'
],[
 'Identical text may still carry tenant-sensitive content and access differences.',
 'Model identity is not a substitute for tenant/authorization isolation.',
 'Disabling may be safe but does not explore a testable isolation-preserving design.'
])

# HARNESSES: the distractors are partial strategies that fail a concrete state/permission requirement.
hard('harness-v2-L3-01',[
 'Use one deployment-capable harness but require an approval phrase in model output before proceeding.',
 'Grant the planning agent production rights and log any deployment action for later review.',
 'Require a UI confirmation for deployment names, while allowing the executor to accept changed digests.'
],[
 'A generated phrase is not independent authorization.',
 'Post-action logging does not ensure the human authorized a specific mutation.',
 'Approval tied only to a name can become stale if the exact artifact changes.'
])
hard('harness-v2-L3-02',[
 'Replace only the final validation step with an autonomous reviewer; assume its verdict is sufficient.',
 'Use autonomous specialists for every stage and enforce end-to-end tests only after the rollout.',
 'Keep the fixed pipeline but ask a planner agent to reorder stable operations on every request.'
],[
 'A reviewer model is not a substitute for deterministic checks and authority.',
 'Adds coordination and risk before measuring benefits.',
 'Unnecessary dynamic ordering can invalidate proven invariants for predictable tasks.'
])
hard('harness-v2-L3-03',[
 'Keep generic network tools but require the agent to cite the ticket before emailing a digest.',
 'Ask a second model to approve the destination using only the retrieved ticket as evidence.',
 'Disable the write tool for all tasks, including separately approved and legitimate delivery workflows.'
],[
 'A citation proves origin, not permission to send to a new address.',
 'A second model processing the same malicious evidence is not an independent authorization gate.',
 'Blanket removal sacrifices valid capabilities instead of implementing scoped execution.'
])
hard('harness-v2-L3-04',[
 'Replay creation using a new autogenerated resource name whenever the local state checkpoint is missing.',
 'Trust the initial API success response and mark every downstream operation complete without checking inventory.',
 'Check that a VM with the desired name exists, but ignore ownership and request IDs before resuming.'
],[
 'Changing names creates duplicates when the original succeeded.',
 'A past response does not prove all later state or recovery conditions.',
 'Name collisions can refer to resources owned by another system.'
])
hard('harness-v2-L3-05',[
 'Allow an unlimited number of retries, but summarize each failed tool response to reduce tokens.',
 'Stop after ten loops regardless of evidence and report success whenever a patch exists.',
 'Increase the model context and token budget while keeping the same repeated failed action.'
],[
 'Compression saves some context but does not create a progress or termination rule.',
 'A fixed budget is useful, but success still requires external acceptance evidence.',
 'Additional capacity can extend an unproductive failure trajectory.'
])
hard('harness-v2-L3-06',[
 'Approve a repository branch name and let execution use its latest commit at runtime.',
 'Accept the reviewer’s chat message as binding if it mentions the same task ID, even after rebases.',
 'Re-run tests on the new diff but retain the earlier human approval without revalidation.'
],[
 'A moving branch can point to a different artifact after review.',
 'Task identity is not an immutable content/version contract.',
 'Tests do not authorize an unreviewed mutation of the approved artifact.'
])

# TOOLS: options are credible protocol and orchestration variants with insufficient controls.
hard('tools-v2-L3-01',[
 'Rewrite all overlapping tool descriptions and keep the full catalog visible, then retest semantic matching.',
 'Introduce hierarchical catalog categories, but continue exposing every tool in the chosen broad category.',
 'Move tool selection to a router model while leaving authorization implicit in each generated call.'
],[
 'Description quality matters, but does not directly reduce the overloaded choice space in each request.',
 'A broad category can still contain many overlapping candidates; test precision and relevant-subset size.',
 'A model router can reduce choices but cannot grant tool authority; model replacement is also disallowed here.'
])
hard('tools-v2-L3-02',[
 'Retry both APIs with the same request body and rely on each provider to suppress duplicates.',
 'Persist tool responses in local memory but regenerate new operation IDs after every restart.',
 'Use A’s idempotency key and B’s request ID, but skip target reconciliation after ambiguous timeouts.'
],[
 'B does not promise idempotency just because A does.',
 'Ephemeral IDs cannot identify a previously committed operation across restarts.',
 'A request ID is useful only when the authoritative target outcome is checked before retry.'
])
hard('tools-v2-L3-03',[
 'Validate tenant scope in the application host, then trust all MCP server requests from that host.',
 'Validate the token audience at the server but authorize any resource under the authenticated tenant.',
 'Use TLS and token signature validation, without checking effective authorization for the requested resource.'
],[
 'A compromised or misconfigured host should not bypass server resource policy.',
 'A token may still have narrower scopes than its tenant membership.',
 'Token validity and protected-resource entitlement are separate checks.'
])
hard('tools-v2-L3-04',[
 'Keep the old session resume code but add a retry loop around revised stateless server responses.',
 'Upgrade the protocol without pinning versions, then test only successful tool listing and first invocation.',
 'Accept a vendor compatibility claim and rely on model prompts to recover failed authorization exchanges.'
],[
 'Retries cannot replace incompatible lifecycle/auth semantics.',
 'Happy-path discovery misses replay and disconnect handling.',
 'Negotiation and authorization occur in protocol/client/server code, not generated prompts.'
])
hard('tools-v2-L3-05',[
 'Retry remote task submission on timeout, but avoid resending the original input context.',
 'Cancel the local coordinator’s work and assume the remote agent automatically observes that cancellation.',
 'Poll the remote status endpoint but use a new task ID for each poll or retry.'
],[
 'The original task can still be running; duplicate submission may create repeated side effects.',
 'Local cancellation does not imply remote lifecycle propagation.',
 'Changing task IDs defeats correlation and reconciliation of the existing remote task.'
])
hard('tools-v2-L3-06',[
 'Return all search hits to the model, then filter employee-level records before rendering the answer.',
 'Authorize only the initial search query and assume links in its results inherit that authorization.',
 'Filter tool discovery by user role, but let every discovered tool fetch records without per-resource checks.'
],[
 'Sensitive records have already entered model context before display filtering.',
 'A permitted search does not grant access to every linked record.',
 'Discovery scope does not replace per-call/per-object authorization.'
])

# RAG: plausible retrieval improvements that omit source scope, authority or important evaluation slices.
hard('rag-v2-L3-01',[
 'Retrieve across the shared index, then suppress unauthorized citations and passages in the final response.',
 'Perform ACL filtering after reranking so the model can still benefit from the best global matches.',
 'Use encrypted retrieval transport but keep permission filtering inside model-generation instructions.'
],[
 'Unauthorized data already reached the model before final rendering.',
 'Candidates may leak into reranking/model context and must be filtered by scope before exposure.',
 'Transport confidentiality does not determine access rights to individual documents.'
])
hard('rag-v2-L3-02',[
 'Use smaller uniform chunks and increase top-k until a footnote appears in some retrieved results.',
 'Index parent sections but omit their footnotes, allowing the model to infer common exceptions.',
 'Retrieve the full source document for every query without measuring noise, access scope or latency.'
],[
 'Smaller fragments may further separate the table from its governing footnote.',
 'The missing exception is authoritative evidence, not optional inference.',
 'Full-document retrieval may be useful in some cases but risks irrelevant context and SLO issues.'
])
hard('rag-v2-L3-03',[
 'Replace the embedding model first and compare only the global recall average.',
 'Increase vector top-k globally without adding lexical matching for exact identifiers.',
 'Allow exact-ID matches through unfiltered lexical search, then apply scope checks only after generation.'
],[
 'The observed exact-ID failure is not specifically diagnosed by aggregate semantic recall.',
 'More vector candidates do not guarantee correct exact-match ranking.',
 'A new lexical path must preserve authorization before context generation.'
])
hard('rag-v2-L3-04',[
 'Prefer whichever contract clause has the latest ingestion timestamp and cite that alone.',
 'Weight passages by semantic similarity and present the highest-scoring clause as definitive.',
 'Summarize both clauses as a merged policy and flag the answer as AI-generated interpretation.'
],[
 'Ingestion time is not governing legal applicability.',
 'Retrieval similarity is distinct from source authority and contract scope.',
 'A merged interpretation can invent terms inconsistent with the signed amendment.'
])
hard('rag-v2-L3-05',[
 'Retain previously authorized memory indefinitely, but mark old project notes as read-only.',
 'Remove revoked records from the UI history, while keeping their embeddings retrievable to improve recall.',
 'Apply current ACLs to live source documents but assume prior summarized memories remain authorized.'
],[
 'Read-only records can still expose data after permission revocation.',
 'Hiding history does not remove retrievable memory data.',
 'Summaries and embeddings derived from restricted sources require the same scope review.'
])
hard('rag-v2-L3-06',[
 'Release because answer accuracy improved, but add an information banner about unreliable citations.',
 'Switch to fewer citations and score only correctness, treating source mismatches as cosmetic.',
 'Canary the new version on all sensitive contracts, monitoring wrong-source incidents without rollback criteria.'
],[
 'A warning does not restore provenance for high-stakes actions.',
 'Reducing evidence visibility does not resolve source misattribution.',
 'Known risk needs predefined acceptance/abort conditions before live exposure.'
])

# EVAL/SECURITY: tempting measurement or governance shortcuts are still weaker than the verified boundary.
hard('eval-v2-L3-01',[
 'Take the vendor’s public benchmark and extend it with a small sample of the easiest internal tasks.',
 'Evaluate task success on internal cases but treat all tool side effects as out of scope.',
 'Use a larger review model to rate the vendor’s demo answers instead of replaying actual tools.'
],[
 'Public averages plus easy samples do not cover permission-sensitive production actions.',
 'Tool trajectories and forbidden actions are central risks of the intended workload.',
 'A second model cannot establish executor behavior or real side effects.'
])
hard('eval-v2-L3-02',[
 'Ship behind a canary because the answer gain is larger than the measured unauthorized-action rate.',
 'Retain the existing authorization policy but downgrade the observed violations to a nonblocking warning.',
 'Increase evaluation sample size and assume the three violations disappear without an engineering change.'
],[
 'A hard zero-action requirement is not a weighted quality trade-off.',
 'Relabeling observed violations does not satisfy the specified gate.',
 'Larger samples may measure the rate more precisely but cannot undo concrete failures.'
])
hard('eval-v2-L3-03',[
 'Use a shared container with root access and add a strict agent system prompt for dangerous commands.',
 'Allow host mounts for performance but block only known suspicious external domains.',
 'Run tests under the developer’s account and rely on repository code reviews to catch exfiltration.'
],[
 'Prompt compliance does not enforce process privileges.',
 'Host mounts and incomplete egress lists leave broad escape/exfiltration paths.',
 'Human review is useful but does not replace execution isolation for adversarial code.'
])
hard('eval-v2-L3-04',[
 'Improve prompt-injection filtering further and defer log-redaction controls to a later phase.',
 'Turn off all traces to prevent secrets from entering logs, accepting no incident reconstruction.',
 'Encrypt the trace store but retain full plaintext credentials accessible to every operator.'
],[
 'The demonstrated leak is in logging code, independent of whether injection is blocked.',
 'No telemetry hinders diagnosis; minimization/redaction plus restricted access is better.',
 'Encryption at rest does not protect plaintext from overprivileged readers.'
])
hard('eval-v2-L3-05',[
 'Reuse the staging approval if the changed digest passes the same automated test suite.',
 'Require approval for production target only, but allow artifact substitutions within the approval window.',
 'Accept the original approval if the same human is still logged in, regardless of target or digest.'
],[
 'Tests do not confer human authorization to deploy a different artifact.',
 'Exact digest remains part of the action that must be approved.',
 'Identity continuity does not expand approved action scope.'
])
hard('eval-v2-L3-06',[
 'Replay the failed deployment immediately, but reuse the same model prompt and monitor health afterward.',
 'Mark the run failed locally and remove the missing receipt from records, assuming target state is unchanged.',
 'Ask another model to reconstruct likely tool outcomes and use that narrative as the next checkpoint.'
],[
 'A repeated write can create a second side effect when the first succeeded.',
 'Local receipt gaps do not establish external absence.',
 'Reconstruction from model prose is not an authoritative transaction ledger.'
])

# PRODUCTION: trade-offs remain plausible but each alternative ignores a measured constraint.
hard('production-v2-L3-01',[
 'Prefer hosted reasoning for all tasks and use encryption, without classifying restricted source content first.',
 'Use local inference exclusively and accept quality regressions on complex cases without exception routing.',
 'Use hybrid routing based on model confidence but let the model select whether data may leave the network.'
],[
 'Encryption is not permission to process restricted data externally.',
 'Residency alone does not meet measured task-quality requirements.',
 'Data handling must be a deterministic policy, not a model-generated preference.'
])
hard('production-v2-L3-02',[
 'Serve all tasks on the larger model but reduce output length until average latency meets four seconds.',
 'Keep all tasks on the small model and increase retries only for wrong answers after human complaints.',
 'Route by task complexity, but measure only per-model decode speed without including classifier errors or routing overhead.'
],[
 'Mean latency is not the p95 SLO; truncating output may hurt quality.',
 'Reactive user complaints are not a reliable accuracy or safety gate.',
 'An unmeasured router can break the end-to-end latency and quality contract.'
])
hard('production-v2-L3-03',[
 'Reserve 13 GiB for weights and admit the target concurrency until an OOM event proves it needs adjustment.',
 'Assume KV cache offloading covers the 18 GiB peak without any latency or backend-support test.',
 'Use the 7 GiB minimum KV estimate as the capacity budget and ignore the documented peak scenario.'
],[
 '13 + 18 exceeds the 24 GiB budget even before other allocations; fail-safe admission is required.',
 'Offloading may be unavailable and can violate performance constraints.',
 'Sizing from the minimum rather than peak creates predictable overload risk.'
])
hard('production-v2-L3-04',[
 'Roll back the binary immediately and assume forward-only database migrations cannot affect the restored app.',
 'Restore from the latest backup without validating whether it contains writes committed after the migration.',
 'Add more application unit tests and keep migration rollback as a manual incident response procedure.'
],[
 'Old binaries may be incompatible with migrated persistent data.',
 'Unverified restore points can lose valid transactions and need an explicit recovery plan.',
 'Additional unit tests alone do not prove stateful integration and recovery.'
])
hard('production-v2-L3-05',[
 'Publish the successful patch with model logs and defer permission/path isolation tests until the next release.',
 'Run a high-accuracy evaluation set but permit the agent to auto-merge if the final code passes unit tests.',
 'Require human code review but accept filesystem scope and tool outcomes only from the agent’s own claims.'
],[
 'Logs may aid review, but unresolved scope risks mean the acceptance gate is not met.',
 'Auto-merge still needs independently enforced restrictions and threat-model evidence.',
 'Reviewer trust relies on real diffs and test/sandbox receipts, not self-reported actions.'
])
hard('production-v2-L3-06',[
 'Declare a service outage once the first external check times out, and trigger global rollback.',
 'Declare the service fully healthy because one internal observer can connect and the process is running.',
 'Treat the external observer as unreliable and defer investigation until another user reports a failure.'
],[
 'Single-vantage failure does not establish global service state or justify destructive rollback.',
 'One working path cannot prove reachability across all network segments.',
 'Unverified assumptions about observers can hide a real routing/permission failure.'
])

if __name__=='__main__':
    # Alternate semantically equivalent concise/full formulations: prevent
    # 'the shortest answer always wins' from replacing 'the longest always wins'.
    for item in Q:
        if item['level']==3 and int(item['id'][-2:])%2:
            item['options'][0]=item['original_answer_text']
            item['answer']=item['original_answer_text']
    assert len(Q)==120
    assert all(len(q['options'])==4 and q['answer'] in q['options'] for q in Q)
    p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('Strengthened distractors in 60 advanced engineering-judgment questions.')
