#!/usr/bin/env python3
"""Editorial curation for the 60 applied-level cases: near-miss diagnostic distractors.
These alternatives are credible hypotheses, but each is contradicted by stated data or fails to isolate the variable.
"""
from pathlib import Path
import json
p=Path(__file__).parent/'scenario-questions.json'
Q=json.loads(p.read_text(encoding='utf8')); lookup={x['id']:x for x in Q}
def hard(id,opts,why):
 assert len(opts)==len(why)==3
 q=lookup[id];assert q['level']==2
 q['options']=[q['answer'],*opts]
 assert len(set(q['options']))==4
 q['distractor_notes']=dict(zip(opts,why))

# STACK: changing visible interfaces, process topology and permissions can be confused.
hard('stack-v2-L2-01',[
 'The write may have succeeded before the denial was logged; first correlate operation IDs.',
 'The harness selected the wrong tool, while the executor’s denial is only a secondary symptom.',
 'A frontend error made the successful write appear denied in backend traces.'
],[
 'Possible in general, but the given evidence explicitly identifies the denied write; no success receipt is shown.',
 'Selection may warrant review, but it does not override the observed permission rejection.',
 'A UI failure cannot rewrite the actual executor’s denial record.'
])
hard('stack-v2-L2-02',[
 'The terminal shell provides capabilities; model tool proposals execute without an independent control loop.',
 'The model endpoint includes a built-in test runner and the terminal only supplies a visual interface.',
 'The terminal application enables a larger context window, which itself permits repository mutation.'
],[
 'Shell presence does not automatically authorize or dispatch generated tool calls.',
 'That architecture is possible but not established; the decisive observed difference is harness-controlled tooling.',
 'Context capacity affects input, not execution privilege.'
])
hard('stack-v2-L2-03',[
 'The model and engine API revision, because role parsing is entirely determined by transport responses.',
 'The user-level prompt and retrieval order, because both can reorder role boundary tokens after tokenization.',
 'The model weight format and hardware backend, because a loaded model guarantees role compatibility.'
],[
 'API revisions may matter, but serialization compatibility is the directly altered representation boundary.',
 'Retrieved text remains data; explicit template markers structure the messages.',
 'Successful weight loading alone does not prove role/template behavior.'
])
hard('stack-v2-L2-04',[
 'That a shared service account may bypass per-tool ACLs unless effective scope is checked.',
 'That tool schema declarations are weaker than runtime resource authorization.',
 'That shared processes can still apply separate tool permissions when the executor supports them.'
],[
 'This is a supported risk, not the unsafe assumption about default container isolation.',
 'Correct distinction: a schema is not a permission mechanism.',
 'Correct possibility: runtime policy may enforce restrictions even in one container.'
])
hard('stack-v2-L2-05',[
 'The client-side UI approval widget, assuming it already displayed a confirmation dialog.',
 'The model service gateway, assuming the tool name and arguments are schema-valid.',
 'The model response parser alone, because a well-formed action should carry its own authority.'
],[
 'Client UI may participate but cannot be the final permission authority.',
 'A gateway may enforce policy, but JSON validity alone does not authorize resource writes.',
 'Parsing proves syntax, not authenticated permission to mutate.'
])
hard('stack-v2-L2-06',[
 'Run the same open-ended user prompt on both and compare only final answer correctness.',
 'Benchmark the model server latency to determine whether the harness introduced queue delays.',
 'Compare tool descriptions but exclude approval and persistent state because weights are unchanged.'
],[
 'Identical output can conceal very different tool and authority trajectories.',
 'Latency is one possible effect but cannot explain the full observed task failures.',
 'The harness directly controls approval/state and those are critical regression candidates.'
])

# MODELS: inference observability and representation compatibility are not just capacity limits.
hard('models-v2-L2-01',[
 'Model B adds system/chat template overhead even when the encoded content is identical.',
 'Model B has a shorter context window, requiring it to summarize the same policy into more segments.',
 'Model B uses a larger model architecture and therefore allocates proportionally more token IDs.'
],[
 'Template overhead could add tokens, but the stated difference is measured before chat messages are added.',
 'A context limit does not by itself increase the content tokenization count.',
 'Parameter count and tokenizer segmentation are independent design choices.'
])
hard('models-v2-L2-02',[
 'The serving runtime changed hidden sampler settings because retrieval increases token count.',
 'The retrieval index updated the model weights through an implicit adaptation step.',
 'The response difference proves that the training checkpoint changed between calls.'
],[
 'Decoder configuration is stated identical; input context is the observed changed variable.',
 'Retrieval adds evidence to a prompt rather than performing gradient updates.',
 'Different responses with the same weights are normal under changed context.'
])
hard('models-v2-L2-03',[
 'Longer decode sequences despite identical reported output-token counts.',
 'A larger retrieval index used only during answer generation after first-token emission.',
 'Model weight loading on every request, even though cold-start behavior was not observed.'
],[
 'The output length is similar; the observed regression is in TTFT.',
 'Retrieval and prefill can affect TTFT, not just later generation.',
 'Cold load is a potential component of TTFT but has not been shown to track prompt length.'
])
hard('models-v2-L2-04',[
 'Greedy decoding is deterministic whenever model weights and prompt text are unchanged, irrespective of backend.',
 'The different server always replaces sampling with top-p when temperature is set to zero.',
 'The output variation proves the new backend changed the checkpoint despite an unchanged digest.'
],[
 'Backend arithmetic and tie-breaking can alter numerical output despite the same text and weights.',
 'Such a configuration change would need evidence; backend numerics remain an independent possibility.',
 'Matching model digest is evidence against a weight change, though all artifacts should be checked.'
])
hard('models-v2-L2-05',[
 'Fine-tune a policy adapter after every update so the answer is grounded in the newest trained state.',
 'Put the most recently retrieved policy text into context but omit version and approval metadata.',
 'Use retrieval for all policies but disable abstention because the index always has at least one match.'
],[
 'Frequent weight adaptation is still harder to attribute/freshness-check than authoritative source retrieval.',
 'Recency without provenance and authority can still select the wrong policy.',
 'A retrieved match is not necessarily applicable, current or sufficient.'
])
hard('models-v2-L2-06',[
 'Require citations to valid-looking links and treat the answer correct when references resolve.',
 'Run the same model answer repeatedly and accept claims that are stable across samples.',
 'Ask a second model to agree with the cited answer without retrieving independent evidence.'
],[
 'A link can resolve yet point to expired or contradictory source content.',
 'Stable language is not factual correctness.',
 'Model agreement is not independent source verification.'
])

# INFERENCE: distinguish input, output, concurrency, memory and tail effects.
hard('inference-v2-L2-01',[
 'Measure total response time and average output tokens/s; derive prefill indirectly as a fixed residual.',
 'Compare GPU occupancy during decode only, assuming queue time is stable between the two inputs.',
 'Profile only model loading because request prompt length should not affect TTFT once weights are warm.'
],[
 'A single residual cannot separate variable queue/load/prefill components.',
 'Queue and prefill can vary independently and need their own spans.',
 'Prompt length directly affects input processing even with warm weights.'
])
hard('inference-v2-L2-02',[
 'Mixed-precision weights alone, because the model must duplicate weight tensors once per session.',
 'Temporary input activations only, because attention cache remains constant across longer contexts.',
 'Memory fragmentation only, because the ideal packed weights already include all sequence-dependent state.'
],[
 'Some buffers are shared and weight duplication per session is not a general explanation.',
 'KV allocations grow with active sequence length and concurrency in the stated scenario.',
 'Fragmentation is real but does not account for all explicitly omitted cache/state allocations.'
])
hard('inference-v2-L2-03',[
 'The quantized model must use a more accurate sampler that consumes additional compute per output token.',
 'The memory footprint reduction necessarily lowered clock speeds through device power management.',
 'The tokenizer changed as part of quantization, creating longer inputs for every task.'
],[
 'Sampling and quantization are distinct; profiling specifically implicates dequantization.',
 'Device power behavior would need telemetry; dequantization is the observed contributor.',
 'The statement does not show a tokenizer change and profiling points to execution kernels.'
])
hard('inference-v2-L2-04',[
 'Use only output tokens/s because both files already fit and quality differences may be stochastic.',
 'Compare peak GPU memory and model load time but defer task accuracy until after selection.',
 'Choose the artifact with lower quantization error on a small numeric calibration set instead of end-to-end code tests.'
],[
 'The observed code regression is a task-level quality signal that must be included.',
 'Memory and loading are useful but omit the demonstrated failure in code tasks.',
 'Calibration error is not necessarily a proxy for actual task completion quality.'
])
hard('inference-v2-L2-05',[
 'The change is a success because aggregate tokens/s gained more percentage points than p95 latency lost.',
 'The new backend should be selected for all traffic if median latency stays below the SLO.',
 'The slowdown must be a model-quality regression because throughput and p95 moved in opposite directions.'
],[
 'A rate and latency in different units cannot be offset as percentages; p95 may violate an independent gate.',
 'The service objective is p95; median does not clear a failed tail target.',
 'Queueing/scheduling can explain the observed latency without changing task correctness.'
])
hard('inference-v2-L2-06',[
 'Estimate eight-user capacity from the one-user warm rate and then confirm only average latency.',
 'Repeat the single-user test with a larger context window but unchanged concurrency.',
 'Benchmark eight short prompts only because they reach the desired concurrent request count.'
],[
 'Throughput scaling is nonlinear and tail/memory behavior remains unmeasured.',
 'This tests context alone, not contention at eight clients.',
 'Short-prompt concurrency omits the long-prefill target workload.'
])

# LOCAL: API shape, readiness, device backend and network exposure are separate observations.
hard('local-v2-L2-01',[
 'Whether both endpoints support the same HTTP request fields, regardless of model file loader.',
 'Whether the target GPU has enough VRAM, treating format support as identical across engines.',
 'Whether the UI can list the artifact, taking catalogue visibility as a loadability check.'
],[
 'HTTP compatibility is independent of format/operator compatibility.',
 'Memory capacity cannot compensate for unsupported model layout or tokenizer semantics.',
 'Discovery metadata does not prove executable loading support.'
])
hard('local-v2-L2-02',[
 'The individual model weights, because concurrency alters the learned parameters after each request.',
 'The model tokenizer, because eight clients necessarily multiply the token IDs for each user.',
 'The frontend transport, because an 8× request count always creates an 8× network latency increase.'
],[
 'Concurrency does not change model parameters.',
 'Tokenization is per request; contention is mainly scheduling/memory, not altered encoded IDs.',
 'Networking may matter, but the given load shape points first to serving admission and resources.'
])
hard('local-v2-L2-03',[
 'Use firewall allowlists alone, relying on IP address as the only authorization boundary.',
 'Add TLS to the model server but keep the API unauthenticated because only local models are hosted.',
 'Expose behind a reverse proxy that authenticates users but has no usage quota or audit controls.'
],[
 'IP restrictions are helpful but do not replace authenticated identities for shared services.',
 'Encryption does not grant or verify access rights.',
 'Authentication is necessary, but abuse controls and observability remain relevant for network exposure.'
])
hard('local-v2-L2-04',[
 'Compare model weights and quantization versions only; identical weights imply stable event semantics.',
 'Check endpoint HTTP status and plain completion text, postponing streaming tool tests.',
 'Update the client SDK until it accepts the new response shape without validating semantic tool-call accuracy.'
],[
 'Tool-call event formats are runtime/API behaviors distinct from weights.',
 'Transport and plain text do not test the broken feature.',
 'Client compatibility can hide wrong or incomplete tool calls unless scored against known fixtures.'
])
hard('local-v2-L2-05',[
 'Compare only final response accuracy; a CPU fallback has no security or hardware implications.',
 'Measure GPU process memory alone; any nonzero allocation proves the intended kernels are active.',
 'Upgrade the model server and model weights first so that device probing can run against the newest stack.'
],[
 'Quality can remain similar while compute silently moves to CPU and latency changes.',
 'Allocation does not establish the compute path or effective driver/kernel compatibility.',
 'Multiple changes confound a straightforward backend-selection regression.'
])
hard('local-v2-L2-06',[
 'Extend /health to check that a PID exists and a port is listening, without issuing an inference request.',
 'Use the model server’s successful startup message as evidence that the selected weights fit in memory.',
 'Treat any HTTP 200 from the management endpoint as proof the target model can serve bounded requests.'
],[
 'Process and port checks still test liveness, not target-model readiness.',
 'Startup completion can precede model load or failure under real requests.',
 'General management health may not exercise the required model/backend path.'
])

# CONTEXT: many superficially valid output checks still miss provenance or state.
hard('context-v2-L2-01',[
 'Treat the ticket as trusted because it came through an authenticated retrieval service.',
 'Treat the instruction as executable only if the model quotes the source URL in its reply.',
 'Treat the ticket as high-priority whenever it is included in the system-visible context window.'
],[
 'Transport authentication does not promote source content into instructions.',
 'Citation of malicious text does not grant execution permission.',
 'Being visible to a model does not change data priority or user authority.'
])
hard('context-v2-L2-02',[
 'The server’s JSON decoding behavior, because tool output fields can alter role-token parsing without serialization changes.',
 'The user prompt and system message wording, because prompts can replace incompatible special-token markers.',
 'The inference engine’s batching strategy, because role delimiters are generated only after decoding starts.'
],[
 'Response parsing may reveal symptoms, but explicit template compatibility is the first relevant input boundary.',
 'Natural language cannot replace the model’s required role/template representation.',
 'Role serialization occurs before model execution; batching does not define the markers.'
])
hard('context-v2-L2-03',[
 'The context window is too small even though no truncation occurred, because useful details always vanish after 4K tokens.',
 'The model weights degraded after retrieval because too many unrelated examples altered its parameters.',
 'Citation scoring became unreliable while source selection remains equally precise under the larger prompt.'
],[
 'Capacity is not the limiting factor; more retrieved material can dilute relevance.',
 'Input documents do not change learned weights during inference.',
 'The problem describes reduced citation relevance, suggesting selection must be measured.'
])
hard('context-v2-L2-04',[
 'Stricter JSON Schema type checks, because a valid string owner ID implies a valid account owner.',
 'Model confidence checking, so low-probability owner IDs are automatically rejected.',
 'A request retry with lower temperature until the parser returns the same invoice owner twice.'
],[
 'Schema type correctness does not validate external reference existence and ownership.',
 'Probability is not an authority check on account identifiers.',
 'Repeated agreement with itself is not an authoritative database lookup.'
])
hard('context-v2-L2-05',[
 'A longer rolling model summary that retains the last ten turns, without a separate decision record.',
 'The most recent approved prompt alone, assuming earlier scope decisions have been fully transcribed.',
 'A persistent cache of model outputs that can be searched but has no source or approval metadata.'
],[
 'Even long summaries can drop negations and permissions.',
 'The incident proves that relying on prompt compaction alone is unsafe.',
 'Cached text without source/authorization status cannot be replayed as governing state.'
])
hard('context-v2-L2-06',[
 'Invalidate cached model output whenever a user changes their query wording, but ignore document revisions.',
 'Assume an identical prompt prefix contains no updated source data and can reuse the same citation indefinitely.',
 'Verify the model digest when reusing cache and treat that as sufficient to establish retrieved document freshness.'
],[
 'Query changes are not the only source of source-data invalidation.',
 'Stable prompt text may embed an obsolete retrieval result.',
 'Model identity does not encode external index/source updates.'
])

# HARNESSES: measure the tool trajectory and recovery, not the apparent answer only.
hard('harness-v2-L2-01',[
 'The second agent succeeded because the patch works; unauthorized path writes are only bookkeeping defects.',
 'The first agent is riskier because a wrong textual answer is harder to correct than an unauthorized write.',
 'Both agents should be graded only by the final task outcome because tools are implementation details.'
],[
 'Side effects on forbidden paths are an independent security failure.',
 'Risk depends on actual authority and harm; the second run includes a concrete unauthorized mutation.',
 'Trajectory integrity is part of evaluating a tool-enabled system.'
])
hard('harness-v2-L2-02',[
 'Build a single autonomous agent first because it can select all three API steps dynamically.',
 'Optimize for fewer model calls without testing whether the fixed pipeline handles exceptions.',
 'Parallelize the three known dependent API steps and compare elapsed time instead of task correctness.'
],[
 'A deterministic baseline is more transparent for already specified steps.',
 'Cost matters, but outcome/failure evidence is required to justify architecture.',
 'Dependent steps may have ordering requirements; latency alone is not a safe selection gate.'
])
hard('harness-v2-L2-03',[
 'Permit the same retry under a higher token budget, assuming previous denials were due to insufficient reasoning.',
 'Reset the agent state after each denial so the model gets an independent chance to propose the action.',
 'Switch to a planner/executor pattern without changing tool policy or termination conditions.'
],[
 'A permission denial is not usually corrected by more tokens.',
 'Discarding state can make repeated forbidden actions more likely.',
 'A different control topology still needs stop rules and denial-aware state.'
])
hard('harness-v2-L2-04',[
 'Retry the same create call with fresh request parameters if no receipt arrives within the timeout.',
 'Mark the resource as failed locally and assume the external API did not apply changes.',
 'Ask the model to choose whether it should retry based on the timeout duration alone.'
],[
 'Fresh parameters can defeat idempotency and create duplicates.',
 'A timeout is not proof that the target rolled back.',
 'Elapsed time alone cannot establish remote commit state.'
])
hard('harness-v2-L2-05',[
 'Measure average answer length and final-response correctness, treating the internal loops as hidden implementation.',
 'Raise the token limit until the completion rate rises, then infer acceptable cost from success percentage.',
 'Compare only the number of reviewer-model calls while ignoring input tool-result context and retries.'
],[
 'The cost explosion arises inside the trajectory, not just output length.',
 'Higher success without a cost/termination bound can remain economically unsound.',
 'Total consumption includes all model turns, tool outputs and review/retry cycles.'
])
hard('harness-v2-L2-06',[
 'Store only the generated patch diff; rerun all previous steps after restart to reconstruct evidence.',
 'Checkpoint the model conversation, relying on text summaries to infer which external writes completed.',
 'Persist the final test results but not tool-call IDs, because the tests can be repeated safely.'
],[
 'Rerunning write phases can duplicate external effects.',
 'Conversation summaries cannot establish authoritative side-effect receipts.',
 'Test repeatability does not authorize repeated mutations or identify earlier commits.'
])

# TOOLS: keep host/server/executor and protocol roles distinct.
hard('tools-v2-L2-01',[
 'Tool-definition token growth degraded selection by truncating the applicable descriptions.',
 'The additional tools overloaded remote APIs, causing more execution failures after correct selection.',
 'The harness began denying most tool calls despite stable model selection accuracy.'
],[
 'Context truncation was explicitly measured as zero.',
 'Execution success remains at 99%, so endpoint reliability is not the leading observed change.',
 'Selection accuracy fell substantially; denials are not demonstrated as the primary cause.'
])
hard('tools-v2-L2-02',[
 'Use CLI exit code zero as confirmation and consider the JSON rejection a warning-level detail.',
 'Check HTTP 200 from the underlying API but ignore the returned business-status field.',
 'Retry the command until the output object is consistently formatted as valid JSON.'
],[
 'A wrapper can exit successfully while the business operation is rejected.',
 'Transport status alone cannot establish domain-level completion.',
 'Repeatable syntax does not change a rejected transaction into success.'
])
hard('tools-v2-L2-03',[
 'The host authorizes all future resources once the user enables the MCP integration.',
 'The MCP server should enforce permissions only on writes; read tools may return any discovered resource.',
 'The host delegates all authorization to the model because it can see the requested account ID.'
],[
 'Integration consent does not grant blanket access to every underlying resource.',
 'Read operations can expose sensitive data and require authorization too.',
 'The model cannot independently authenticate caller rights.'
])
hard('tools-v2-L2-04',[
 'Rely on the successful tool-list response as evidence that request-level authorization is compatible.',
 'Increase timeout values until the newer client eventually accepts the older access token.',
 'Pin the model revision and adjust prompts while leaving client/server protocol versions unchecked.'
],[
 'Discovery and subsequent auth requests may exercise different protocol behavior.',
 'A malformed audience or incompatible auth flow cannot be fixed by waiting.',
 'Model version is independent of MCP transport/authorization negotiation.'
])
hard('tools-v2-L2-05',[
 'Use an MCP tool returning a static summary of a remote agent’s possible capabilities.',
 'Treat the remote agent as a synchronous function with no independent task state or cancellation.',
 'Have the model directly generate CLI commands on the remote host as a substitute for task delegation.'
],[
 'A capability summary does not establish remote agent task ownership.',
 'The case explicitly describes independent lifecycle and identity.',
 'Remote shell execution does not provide safe cross-agent state and trust contracts.'
])
hard('tools-v2-L2-06',[
 'Authorize once at MCP discovery, then treat all visible tool invocations as approved.',
 'Validate the schema and tool name, assuming a correct call implies an authenticated actor.',
 'Rely on TLS and server identity as the only checks before performing user-requested payment mutations.'
],[
 'Tool listing is not per-user/per-resource authorization.',
 'Syntactic validity does not grant resource rights.',
 'Transport authentication does not confer all end-user entitlements.'
])

# RAG: competing retrieval and source-validation hypotheses.
hard('rag-v2-L2-01',[
 'The embedding model retrieved a semantically weak match, so ranking score alone should determine current policy.',
 'The generator failed to cite all related sources, so adding more citations will necessarily restore freshness.',
 'The answer should be accepted because the cited document exists and text matches the user question.'
],[
 'The observed issue is authority/version validity, not merely semantic match score.',
 'Additional citations can still point to stale or inapplicable policies.',
 'A matched source may be superseded or outside the current effective period.'
])
hard('rag-v2-L2-02',[
 'Retrieval top-k was too low, so raising k alone guarantees the missing negation will appear.',
 'The embedding model is too small, so a larger model will reconstruct the omitted clause without reindexing.',
 'The reranker chose the wrong passage but the indexed chunks still preserve every exception in full.'
],[
 'More chunks may help but does not repair a structure-destroying segmentation design.',
 'An encoder cannot reliably restore text not present in retrieved evidence.',
 'The split has removed the scope/negation from the returned evidence unit.'
])
hard('rag-v2-L2-03',[
 'Increase semantic top-k alone; exact identifiers will rank correctly once enough candidates are returned.',
 'Use lexical matching only, because it scores exact IDs accurately even on paraphrased descriptions.',
 'Choose a lexical or vector pipeline at random and average their results over repeated queries.'
],[
 'Larger k does not guarantee strong identifier ranking or efficient retrieval.',
 'The case explicitly observes lexical weakness on paraphrased questions.',
 'Random selection does not use query evidence or evaluated score fusion.'
])
hard('rag-v2-L2-04',[
 'Judge the final answer as correct when its highest-ranked citation supports at least one claim.',
 'Use the model’s own citation-confidence score to resolve conflicts without inspecting source authority.',
 'Drop the contradictory citation and retain a fluent answer supported by one remaining passage.'
],[
 'One supported claim does not prove all statements or resolve contradiction.',
 'Confidence is not an authoritative evidence-hierarchy decision.',
 'Suppressing contradictory evidence conceals uncertainty relevant to the user.'
])
hard('rag-v2-L2-05',[
 'Treat the larger context window as persisted memory because its token budget can include previous sessions.',
 'Treat KV cache as long-term application memory because it speeds continuation after every new request.',
 'Treat stored preferences as model weights because the same assistant can retrieve them repeatedly.'
],[
 'A window describes capacity; persistence depends on the application storing and reassembling history.',
 'KV cache is transient attention state and is normally lost on restart.',
 'A data store is distinct from learned parameters and is governed separately.'
])
hard('rag-v2-L2-06',[
 'Retrieval recall@5 is 80% because the model answered 80 questions correctly.',
 'Recall@5 is 72% but the end-to-end system must have hallucinated the remaining eight correct answers.',
 'Recall@5 is 72% and therefore citation groundedness must be exactly 72% as well.'
],[
 'Answer accuracy and gold-document retrieval are independent measures.',
 'Other evidence and prior knowledge can explain correct answers without the recorded top-five gold hit.',
 'Citation support requires separate scoring; it need not equal retrieval recall.'
])

# EVAL/SECURITY: close alternatives are plausible metrics and controls, not random technical nouns.
hard('eval-v2-L2-01',[
 'The model lacks enough context capacity to process contradictory examples in one request.',
 'The FAQ benchmark is representative because most production requests are straightforward.',
 'The live failures prove the model’s learned weights changed after the evaluation run.'
],[
 'Context size may matter but the explicit missing test categories are the primary gap.',
 'The reported production failures contradict the representativeness assumption.',
 'No change to model artifacts is established by the evidence.'
])
hard('eval-v2-L2-02',[
 'The SLO passes because mean latency is lower than the stated four-second limit.',
 'The SLO can pass if the median is below four seconds, even with a long tail.',
 'The p95 observation is a warning only because the 95th percentile is less representative than the average.'
],[
 'The contract explicitly uses p95, not mean latency.',
 'Median responsiveness does not meet a p95 target.',
 'Percentile objectives are deliberately defined to cover tail behavior.'
])
hard('eval-v2-L2-03',[
 'The injection failed because the model’s final response never mentioned exfiltration.',
 'The injection succeeded once the model proposed the network call, regardless of the executor denying it.',
 'The attack result cannot be evaluated without looking at the README’s formatting and title.'
],[
 'Hidden attempted actions still need examination; final text is insufficient evidence.',
 'An attempted unsafe proposal matters, but denied side effects must be distinguished from actual leakage.',
 'Presentation affects believability, not whether bytes crossed the defended boundary.'
])
hard('eval-v2-L2-04',[
 'The code repository’s commit history only, because package scripts are external to the agent tool surface.',
 'The model output schema only, because external tools cannot execute harmful commands if JSON is valid.',
 'The user approval dialog only, because package installs are always considered read-only actions.'
],[
 'Indirect dependencies and test scripts can execute with effective tool privileges.',
 'Schema validity does not constrain side effects once the executor invokes scripts.',
 'Install hooks may mutate or contact external endpoints and need scoped permissions.'
])
hard('eval-v2-L2-05',[
 'The UI denial is sufficient if the browser attempts to undo the already-completed mutation.',
 'The model approval text is authoritative because it preceded the actual user-facing denial.',
 'The approval control is working because the user can see and reject the proposed action.'
],[
 'Undo may be impossible; the preventive gate should precede execution.',
 'The model cannot confer human authorization.',
 'A warning after the mutation does not prevent the side effect.'
])
hard('eval-v2-L2-06',[
 'Final textual answer and task score alone, because completed tasks are what the user sees.',
 'The number of model calls and completion length, assuming similar counts imply safe trajectories.',
 'A tool inventory snapshot without run-specific arguments, decisions or side-effect receipts.'
],[
 'Identical visible answers can arise from unsafe and safe action paths.',
 'Counts do not reveal which protected resources were touched.',
 'Capability lists are not evidence of actual actions or authorizations.'
])

# PRODUCTION: choose measured, risk-adjusted responses rather than one attractive KPI.
hard('production-v2-L2-01',[
 'A hosted model benchmark with a single latency and accuracy winner, ignoring data classification.',
 'A data-residency policy only; all other quality and operational risks are implementation details.',
 'A comparison of model sizes and published token costs without workload-specific task evaluation.'
],[
 'Architecture choice includes residency, fallback and full operational ownership.',
 'Residency matters but does not answer correctness and resilience constraints.',
 'Marketing metrics and unit prices do not justify workload outcomes.'
])
hard('production-v2-L2-02',[
 'The arithmetic mean of the 1,000 durations, assuming p95 can be computed directly from it.',
 'The maximum duration among the slowest 50 requests, which is always identical to p95.',
 'Only the share completing in three seconds, because that fixes every percentile regardless of ordering.'
],[
 'Mean does not determine an arbitrary percentile.',
 'The maximum of the tail is near p100 rather than the p95 cutoff.',
 'The statement leaves the exact transition observation and percentile convention unspecified.'
])
hard('production-v2-L2-03',[
 'Model API costs per million tokens, using a discount for cached prefixes but omitting recovery.',
 'Average infrastructure energy and GPU utilization, treating every generated answer as accepted.',
 'Human review costs only, because models can produce tokens at negligible marginal cost.'
],[
 'Retries, failed work and operational review can dominate token price.',
 'Compute utilization does not equal completed task value.',
 'Inference infrastructure and failures still contribute material costs.'
])
hard('production-v2-L2-04',[
 'Global HTTP error rate, because security-related proposals count only if they break an API call.',
 'User-reported answer quality, because model intent cannot affect authorization policy.',
 'The canary’s share of total traffic, because low exposure guarantees the security gate is nonblocking.'
],[
 'Unsafe tool proposals are an independent security signal.',
 'Policy violations can exist alongside fluent accepted answers.',
 'A hard gate does not disappear at small canary percentages.'
])
hard('production-v2-L2-05',[
 'A validated production system because both demonstration attempts succeeded without errors.',
 'A complete architecture because the visible demo includes every component needed for operation.',
 'A safe release candidate because no negative tests have yet shown it can fail.'
],[
 'Two successes do not establish repeatable failure-handling or risk controls.',
 'Visible components do not prove tested operational behavior.',
 'Not testing failure paths is absence of evidence, not proof of safety.'
])
hard('production-v2-L2-06',[
 'Comparison of model answer quality only; if it is stable, other runtime details cannot explain the incident.',
 'Aggregate latency measurements without model, context or tool version information.',
 'The UI error message alone, because it necessarily reflects the authoritative operation outcome.'
],[
 'A regression may arise from context, tools or orchestration with unchanged model quality.',
 'Timing without configuration identity cannot support reliable attribution.',
 'UI messages may be generated or derived and need corroborating execution traces.'
])

if __name__=='__main__':
    # Longer near-miss options removed the old length clue. Restore the precise
    # source answer wording for applied cases; correct-option lengths now overlap.
    for item in Q:
        if item['level']==2:
            item['options'][0]=item['original_answer_text']
            item['answer']=item['original_answer_text']
    assert len(Q)==120
    for x in Q:
        assert len(x['options'])==len(set(x['options']))==4 and x['answer'] in x['options']
        assert len(x['distractor_notes'])==3
    p.write_text(json.dumps(Q,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('Strengthened distractors in 60 applied-understanding questions.')
