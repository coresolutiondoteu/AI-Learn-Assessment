# AI Systems Academy

**A self-paced course in AI systems engineering, with practical labs, guided architecture cases, and assessments. Runs locally in your browser.**

AI Systems Academy connects the parts of an AI system that are usually taught in isolation: hardware and compute, model weights, tokenization, inference, context, agent harnesses, tools, retrieval, security, evaluation, and production operations.

Use it to:

- **Understand the stack.** Identify what each layer does, how components interact, and where responsibility and trust boundaries sit.
- **Practice engineering decisions.** Follow request traces, work through controlled labs, and diagnose failures using observed evidence.
- **Check your understanding.** Review terminology, complete module checkpoints, and take randomized assessments with explanations linked to the relevant material.
- **Build evidence of competence.** Progress from foundational knowledge to architecture patterns, design trade-offs, and capstone projects.

The application is an educational environment, **not** a model runner or infrastructure automation tool.

## Why this exists

Using an AI assistant is straightforward. Understanding what happens between a prompt and a result is not.

Terms such as *model*, *tokenizer*, *runtime*, *kernel*, *agent*, *harness*, *TUI*, and *MCP* describe different parts of a larger system, yet are frequently conflated. A working demonstration rarely tells you which component made a decision, why performance changed, whether a tool call was authorized, or what would happen when something fails.

This project addresses that gap with a connected learning path. Concepts are introduced in dependency order, reinforced through vocabulary and examples, and revisited in scenarios where the learner must distinguish observations from assumptions and defend a technical choice.

## Download and run

**[Download AI Systems Academy — ZIP of the `main` branch](https://github.com/coresolutiondoteu/AI-Learn-Assessment/archive/refs/heads/main.zip)**

1. Download the ZIP using the link above.
2. Extract it to a folder of your choice. Keep the directory structure intact.
3. Locate **`index.html`** in the extracted files (the packaged application places it in `AI_Systems_Academy/`) and open it in a modern browser.
4. Choose **Begin module 1** to start learning. Open **Assessment center** when you want to practice or take a scored exam.

There is **nothing to install to use the academy**: no backend, database, account, API key, model download, package manager, or running web server is required. The training content, checks, and exams work offline. Links to external articles, official documentation, GitHub repositories, and videos require an internet connection.

Your progress is stored in the browser when local-file storage is available. Use **My progress → Export progress JSON** to keep a backup, particularly before moving the files, changing browsers, or updating the application. You can restore it using **Import progress JSON**.

## Video walkthrough

[![Watch the AI Systems Academy fly-through](https://img.youtube.com/vi/ZzmACDsid8E/hqdefault.jpg)](https://youtu.be/ZzmACDsid8E)

[Watch the application fly-through on YouTube](https://youtu.be/ZzmACDsid8E)

---

## What's included

| Area | Content |
| --- | --- |
| Guided curriculum | **10 progressive modules**, **60 linked lessons**, and an interactive **L0–L9 system stack** |
| Practical learning | **10 lab runbooks**, with steps, safety constraints, and learner-recorded evidence |
| Engineering clinics | **10 cases** covering **30 guided decisions** built around observations, diagnosis, and architectural choices |
| Architecture | **11 reusable patterns**, **4 capstone projects**, and a **16-week study route** |
| Terminology and references | **99 glossary entries** with review scheduling, plus **64 annotated references** in the field manual |
| Assessment | **372 four-option questions** across foundations, application, and engineering judgment |
| Documentation | An **AI Systems Engineering Field Manual**, an **Opening Study Guide**, and the assessment/clinic design notes |

The material moves from basic computing and model concepts to local inference, context engineering, agent control loops, interfaces and MCP, RAG, evaluation, security, and production trade-offs. The PDF guides provide deeper reference material; the application connects it into shorter lessons and exercises.

### How the learning experience works

Each module follows a consistent sequence:

**Concept → Request trace → Lab → Engineering clinic → Knowledge checkpoint → Review**

A concept lesson explains what a component is, where it belongs, what it depends on, and what changes when it is replaced. The trace shows the component in an end-to-end request. The lab asks for a small, safe experiment and recorded observations. The clinic then presents a realistic situation with constraints and asks for three successive decisions:

1. **Observe:** What do the measurements establish, and what remains unknown?
2. **Diagnose:** Which boundary or hypothesis should be tested next?
3. **Decide:** Which approach best satisfies the constraints, and how would you verify it?

Clinic feedback explains the preferred option and why the alternatives are less suitable in that situation. Clinics are **guided practice**, not scored exams or proof of professional proficiency.

For a useful study cycle, complete the six lessons in a module, trace the example, perform the lab in a non-production environment, finish its clinic, take the checkpoint, and revisit any weak vocabulary before moving on.

## Assessments

The v2.0 question bank contains **372 distinct single-answer questions**, each with four choices. The difficulty levels separate recognition of terminology from applied diagnosis and engineering judgment.

| Level | Questions in bank | Share of a scored exam | Focus |
| --- | ---: | ---: | --- |
| **L1 — Foundations** | 120 | 30% | Terminology, responsibilities, core concepts, and basic processes |
| **L2 — Applied understanding** | 192 | 50% | Reading traces, interpreting measurements, diagnosing failures, and comparing mechanisms |
| **L3 — Engineering judgment** | 60 | 20% | Choosing and defending designs under operational, security, and reliability constraints |

### Exam formats

| Exam | Questions | L1 / L2 / L3 | Coverage |
| --- | ---: | --- | --- |
| Section exam | 20 | 6 / 10 / 4 | One selected module |
| Comprehensive | 20 | 6 / 10 / 4 | 2 questions from each module |
| Comprehensive | 30 | 9 / 15 / 6 | 3 questions from each module |
| Comprehensive | 40 | 12 / 20 / 8 | 4 questions from each module |

**Passing score: 80%.** Question selection and answer order are randomized for each attempt. Scored exams withhold answers and hints until submission, then provide a full review of both correct and incorrect responses, difficulty-level results, and links back to relevant lessons or clinics.

The academy also provides two unscored learning modes:

- **Guided learning challenge:** 10 questions across all modules, with optional hints and immediate explanations.
- **Module checkpoints:** 5 questions per attempt, with feedback for targeted practice.

An exam score reflects performance on that attempt; it is **not a professional certification**. The difficulty mix is implemented and logic-tested, but the question bank has not been psychometrically calibrated against real learner cohorts. The original 252 questions are retained from the earlier version; the 120 newer scenario questions and clinic stages received additional editorial work. Independent item review and learner testing remain important next steps.

## Study route

A recommended progression is to:

1. Map the full L0–L9 stack and explain the difference between the model, inference engine, harness, tools, and interface.
2. Learn tokenization, model behavior, prefill/decode, memory, quantization, and local serving.
3. Understand prompt and context assembly, tool contracts, bounded agent loops, and MCP boundaries.
4. Build and evaluate a small retrieval workflow with citations and access controls.
5. Investigate failure modes, prompt injection, state recovery, permissions, and production reliability.
6. Complete a capstone with reproducible tests, negative cases, a design decision record, and evidence of what actually worked.

The included **16-week plan** organizes these topics into weekly deliverables. The four capstones cover a local evidence assistant, a bounded tool agent with MCP, an evaluation-driven coding harness, and inference/agent performance engineering.

## Offline operation, privacy, and progress

The application runs entirely in the browser and does not require accounts, telemetry collection, external model calls, or a remote service. Learning history and notes are kept in browser-local storage, using the existing `ai-systems-academy-v1` storage key for compatibility with earlier releases. Engineering-clinic progress is stored as an additional optional field.

Some browsers restrict storage for `file://` pages; progress may also appear separate after changing the file path or browser. **Export progress before upgrading.** Importing a backup replaces the current browser record. Export files contain learning history and any notes you entered, so keep them private and do not place credentials or sensitive production data in lab records.

## Repository layout

The application distribution has the following structure:

```text
AI_Systems_Academy/
├── index.html                         # Standalone application
├── docs/
│   ├── AI_Systems_Field_Manual.pdf
│   ├── Opening_Study_Guide.pdf
│   └── ASSESSMENT_AND_CLINIC_DESIGN.md
├── source/
│   ├── template.html                  # HTML application source
│   ├── rebuild.py                     # Assemble standalone index.html
│   ├── modules.json                   # Lessons and modules
│   ├── question-bank.json             # Original assessment items
│   ├── scenario-questions.json        # Additional L2/L3 items
│   ├── engineering-clinics.json       # Engineering cases and decisions
│   └── ...                            # Glossary, patterns, references, study plan
├── tests/
│   ├── validate_content.py
│   └── assessment_flow.cjs
├── CHANGELOG.md
└── SHA256SUMS.txt
```

`index.html` is the standalone runtime. The `source/` files are provided for inspection, maintenance, and rebuilding; they are **not** needed when simply using the app.

### Edit and rebuild

From the unpacked `AI_Systems_Academy/` directory:

```sh
python3 source/rebuild.py
python3 tests/validate_content.py
node tests/assessment_flow.cjs
```

Python 3's standard library is sufficient to rebuild the application. Node.js is only required for the JavaScript regression suite, not for running the academy.

Edit `source/modules.json` for lessons, `source/question-bank.json` and `source/scenario-questions.json` for assessments, and `source/engineering-clinics.json` for clinic content. Keep lesson and question identifiers stable to preserve learner-progress references.

The authoring scripts (`expand_content.py`, `refine_question_bank.py`, `refine_level2.py`, `refine_level3.py`, and `build_clinics.py`) can regenerate curated content. Do **not** rerun them after hand-editing JSON unless you intend to overwrite those edits. `patch_app_v2.py` is historical migration code, not a normal build step.

See [`docs/ASSESSMENT_AND_CLINIC_DESIGN.md`](docs/ASSESSMENT_AND_CLINIC_DESIGN.md) for the assessment rubric and planned independent review, and [`CHANGELOG.md`](CHANGELOG.md) for release history.

## Scope and validation

This is a learning tool. It does not execute model-proposed commands, launch an inference server, access external systems, enforce authorization, or make production changes. Labs describe work for a learner to perform deliberately in an appropriate test environment.

For the v2.0 archive, content validation and offline JavaScript logic tests cover the 372 questions, distinct answer choices, domain/difficulty sampling, scoring, progress compatibility, clinic navigation/state, and the exam submission flow. **Graphical browser behavior, responsive layout, keyboard accessibility, and real-world assessment difficulty have not been independently validated for this version.** Those require separate browser testing and learner review.
