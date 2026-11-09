# AI Systems Academy - Offline AI Engineering Learning & Assessment

**Version:** 2.0 · **Build date:** 2026-11-08 · **Language:** English · **Format:** self-contained offline HTML app + companion PDFs + editable sources

Download the app: https://github.com/coresolutiondoteu/AI-Learn-Assessment/archive/refs/heads/main.zip

## Run it

1. Unzip the archive, preserving the `AI_Systems_Academy/` folder.
2. Open **`index.html`** in a modern desktop browser. No installation, account, API keys, internet connection, running server, or external packages are needed to use the embedded training and assessments.
3. Select **Begin module 1**. Learn the concept, examine the trace, record a safe lab, then open **Engineering clinic** to practice evidence-based decisions.
4. Use **Assessment center** for the unscored learning challenge, topic exams, or full 20-, 30- and 40-question assessments. Use **My progress → Export progress JSON** to back up your work.

The local HTML app and PDF manuals are usable without internet. Links to official documentation, papers and repositories need internet access. Some browsers restrict storage when opening `file://` pages: export progress periodically and import it after changing browsers/paths.

## Check the video fly-through first

[![Watch the video](https://img.youtube.com/vi/ZzmACDsid8E/hqdefault.jpg)](https://www.youtube.com/watch?v=ZzmACDsid8E)   

## What is included

| Component | Coverage |
|---|---|
| Connected learning modules | **10** competency domains, foundations to production engineering |
| Core concept lessons | **60** lessons, now including an *Engineering lens* on failures, decisions, evidence and transfer |
| Engineering clinics | **10** in-depth case studies with observed evidence, constraints, **30** stepwise decision exercises, feedback and proof targets |
| Four-option assessment bank | **372** distinct questions: **120 Level 1**, **192 Level 2**, **60 Level 3** |
| New question content | **120** scenario-driven questions (60 applied, 60 engineering-judgment); individually curated incorrect-option rationales and explanatory notes |
| Lab/runbook guidance | 10 exercises, checklists and learner-entered evidence; **not** automatic external-system execution |
| Architecture and capstone tools | Interactive L0-L9 stack, 11 architecture patterns, four capstones, 16-week path |
| Vocabulary and references | 99 glossary entries with review scheduling; 64 annotated manual references and module reading links |
| Companion manuals | 46-page **AI Systems Engineering Field Manual** and two-page **Opening Study Guide**, included unchanged |

### How the deeper training works

Each module now connects a progression rather than only a reading passage:

**Concept → Request trace → Hands-on lab → Engineering clinic → Knowledge checkpoint → Reflective review**

The ten engineering clinics illustrate how a practitioner isolates evidence, diagnoses a failure boundary, and chooses an architecture under constraints. Each clinic has a coherent situation, measured signals or observations, safety/operational constraints, and three guided decisions. After each choice, the learner sees the best answer, its justification, and explanations for each alternative. Clinics and the guided challenge are **unscored learning**, not certifications.

In the assessment bank, questions may include an engineering incident, a measurable before/after comparison, trace observations, or explicit constraints. New advanced alternatives are engineered as plausible competing decisions or diagnoses, rather than arbitrary wrong statements. A question's answer review explains both the choice and the relevant misconception, then links back to its concept or clinic.

## Three-level assessment contract

| Level | Share of each scored exam | What it assesses | Example |
|---|---:|---|---|
| **1 — Foundations** | **30%** | Vocabulary, conceptual ownership, key distinctions, basic processes | Distinguish model, inference engine, harness and user interface |
| **2 — Applied understanding** | **50%** | Interpret evidence, diagnose symptoms, compare mechanisms, follow a trace | Explain a drop in tool-selection accuracy when tool execution still succeeds |
| **3 — Engineering judgment** | **20%** | Choose justified designs under constraints, handle security and uncertainty | Preserve fifty capabilities while designing scoped tool discovery and authorization |

The exam draws **6/10/4** questions at 20 items, **9/15/6** at 30, or **12/20/8** at 40. The full exam covers each of the ten modules equally: two, three, or four questions from each. A section exam contains 20 questions from that specific module with the same 6/10/4 allocation. Questions and the position of the correct alternative are randomized for each attempt.

**Pass threshold: 80%.** In a perfectly answered Level 1 + Level 2 attempt, the candidate has exactly 80%; reaching 100% necessarily requires getting Level 3 questions right. This **score architecture** is implemented and regression-tested. Whether 80% proves challenging and 100% exceptionally hard for real learners remains a **pilot-testing hypothesis**, not a proven psychometric claim. Scores are formative, not proctored, normed, or a professional certification.

The app keeps scored exam answers and hints hidden until submission, then shows **all** answer explanations (including correct responses), difficulty-level performance, misconceptions, and links to a matching clinic or lesson. The final item has an explicit **Submit exam** control instead of a disabled Next button.

### Learning modes (not graded like the exam)

- **Guided learning challenge:** Ten cross-domain questions, balanced 3 × Level 1 / 5 × Level 2 / 2 × Level 3, with optional hints, immediate reasoning and alternative explanations.
- **Module knowledge checkpoints:** Five questions drawn across levels (1 foundation, 3 applied, 1 judgment), followed by educational feedback; aim for 80%, but treat this as practice evidence.
- **Engineering clinics:** Three stage-by-stage decisions per domain. Revisit an attempt or reset clinic responses without changing scored exam history.

## Recommended route

1. **Map:** Use the opening guide and the L0–L9 explorer to locate owners and trust boundaries.
2. **Understand:** Work through the six lessons in a module; articulate inputs, outputs, failure modes and trade-offs.
3. **Trace and build:** Follow the module's request trace, perform the lab safely on a non-production environment, and retain evidence outside the app where appropriate.
4. **Reason:** Complete the three-stage engineering clinic *before* attempting a high-stakes style exam.
5. **Check:** Take the five-question checkpoint. Inspect explanations even for correct responses, and review related vocabulary.
6. **Assess:** Attempt an unscored guided challenge and a section exam. Move to the full exam after covering multiple domains.
7. **Prove:** Complete a capstone with a reproducible test, negative cases, design rationale and evidence; a high quiz score alone is insufficient.

## Progress and privacy

The app uses a browser-local storage record under the existing key **`ai-systems-academy-v1`**, deliberately preserving the v1/v1.1 storage schema and prior lesson/lab/vocabulary/exam progress. New engineering-clinic state is an optional `clinics` field; older exported records continue to import. Opening the app at a new local path or changing browsers may expose different browser-local storage. Export a progress JSON backup before upgrading or clearing browser data. An import **replaces** the current browser record with the chosen backup.

No login, tracking, remote collection, model calls, or external services are required for the app. Exported progress files can contain your learning history and notes: handle them as personal data. Do not paste secrets or actual credentials into lab evidence.

## Editable source and maintenance

`index.html` is a standalone distributable generated from `source/template.html` plus JSON sources. To edit content and rebuild from the unpacked root:

```sh
python3 source/rebuild.py
python3 tests/validate_content.py
node tests/assessment_flow.cjs
```

Python 3 standard library is sufficient for **building**. Node.js is optional, needed only for the JS regression tests. To edit the new expanded content, edit `source/scenario-questions.json` and `source/engineering-clinics.json` directly; existing questions live in `source/question-bank.json`, lessons in `source/modules.json`. The remaining JSON files cover vocabulary, references, patterns, capstones and the study plan. Keep stable IDs for previous question/lesson references and learner-progress continuity.

The `source/expand_content.py`, `source/refine_question_bank.py`, `source/refine_level2.py`, `source/refine_level3.py`, and `source/build_clinics.py` are **authoring/regeneration scripts**, not browser runtime dependencies. These scripts may replace curated JSON: do not rerun them after manual editing unless that regeneration is intended. `source/patch_app_v2.py` documents the one-time v1.1→v2 migration of the HTML template and is **not** part of the normal build.

See **`docs/ASSESSMENT_AND_CLINIC_DESIGN.md`** for the item-writing rubric, calibration plan, and remaining limitations. `SHA256SUMS.txt` provides checksums for the unpacked deliverable.

## Safety, scope, and testing status

The academy does **not** execute tools, start local inference, run a model, deploy infrastructure, or enforce production security. It explains and asks you to verify such operations in a controlled environment. No part of the assessment is a substitute for live system testing, credential management, authorization checks, or expert review. The manuals' links and release references were compiled for 2026-11-08; verify them before operational use.

**Validated for this build:** source JSON/schema, all 372 questions, uniqueness and answer mapping, per-domain three-level supply, 30/50/20 question sampling, domain balance, scoring boundaries, result breakdown, HTML/JS compilation, legacy-progress load, 10 engineering clinics and offline Node-based logic regressions. **Not validated in a real graphical browser:** visual presentation, mobile behavior, keyboard/accessibility and full browser interaction, because managed-browser policy blocked the headless-browser test in the build environment. Review locally before any public launch.

## Package layout

- `index.html` — standalone HTML academy app
- `docs/AI_Systems_Field_Manual.pdf` — original 46-page companion reference
- `docs/Opening_Study_Guide.pdf` — original two-page reading guide
- `docs/ASSESSMENT_AND_CLINIC_DESIGN.md` — pedagogy and item-quality/calibration plan
- `source/*.json` — editable content
- `source/template.html` / `source/rebuild.py` — offline app source and build
- `source/*.py` — optional authoring/migration scripts
- `tests/` — offline source and regression tests
- `CHANGELOG.md` — version history
- `SHA256SUMS.txt` — file-by-file integrity evidence
