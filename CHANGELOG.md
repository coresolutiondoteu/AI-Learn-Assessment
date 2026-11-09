# AI Systems Academy — changelog

## v2.0 · 2026-11-08 · Engineering mastery expansion

**Motivation:** Reviewers found several older assessment questions answerable by eliminating obviously wrong choices. More authentic engineering decisions, diagnostic evidence, deeper explanations and a meaningful path from beginner-level understanding to advanced mastery were requested.

### Training expansion

- Added **10 evidence-driven engineering clinics**, one per competency domain: each includes scenario, observed facts/metrics, limits and constraints, three staged reasoning tasks and justification of the alternatives (**30 guided decisions**).
- Added **Engineering clinic** as a fifth tab in all ten modules, plus a global **Engineering clinics** casebook for cross-domain practice.
- Expanded each of the **60 existing lessons** with an *Engineering lens* connecting typical failure, diagnostic evidence, and architectural reasoning; retained existing concept, trace and lab structure.
- Connected questions and answer reviews to their vocabulary, concept lesson and clinic. Existing PDFs remain included and unchanged.

### Assessment expansion

- Expanded from **252 to 372 distinct four-option questions**: retained the 252-item original bank and added **60 applied (Level 2)** and **60 engineering-judgment (Level 3)** scenario questions.
- Introduced levels **1 Foundations / 2 Applied understanding / 3 Engineering judgment**. Existing foundation questions map to Level 1, existing advanced questions to Level 2. New L2/L3 have curated misconception-based alternatives with individual explanation notes.
- Redesigned 20/30/40-question full exams and 20-question module exams to use **30% / 50% / 20%** quotas, with ten-domain balance in comprehensive exams.
- Randomized question selection and alternative order; improved the misleading **correct answer is longest** pattern by editorially balancing new-option length.
- Exposed level-by-level score breakdown, all-question explanations, deeper learning notes and direct remediation links.
- Updated the unscored guided challenge to include three levels in a 3/5/2 mix; changed five-question topic checkpoints to 1/3/1.
- Kept the **80%** pass threshold and provided a precise, tested scoring design: all Level 1 + Level 2 correct equals 80%, with Level 3 mastery necessary for 100%.

### Compatibility, reliability and checks

- Preserved v1/v1.1 browser storage key and schema; new clinic progress lives in an optional field. Existing lesson/lab/vocabulary/exam records still load.
- Extended offline schema checks and Node VM logic regression tests to cover all questions, 10 clinics, sampling, levels, last-question submission and scoring.
- Rebuild remains Python-standard-library-only and creates a single locally usable HTML document.
- Browser policy prevented graphical browser QA in the build environment. Cross-browser responsive, accessibility and real learner-difficulty testing are **not yet verified**; a pilot-test plan is supplied in `docs/ASSESSMENT_AND_CLINIC_DESIGN.md`.

**Important limitation:** The 30/50/20 distribution is a design, not an evidence-backed promise that 80% will be objectively difficult. Pilot data, reviewer disagreement and item discrimination should guide future item revisions. Older baseline questions may still contain simplistic distractors and deserve a full editorial pass.

## v1.1 · 2026-11-08 · First external learner feedback

- Fixed the final-question navigation by showing **Submit exam** instead of a disabled **Next question** button.
- Introduced the 10-question unscored guided learning challenge with hints and immediate feedback.
- Added stronger explanations and cross-topic prompts to results, including selected curated case notes and memory arithmetic.
- Made full answer review the default, not just wrong-answer review.
- Added offline content validation and Node logic tests.
- Retained 252 questions, 10 modules, 80% passing threshold, PDF companions and compatible local progress records.

## v1.0 · 2026-11-08 · First private academy

- Offline HTML learning application connected to the AI Systems Engineering field manual and opening study guide, with 10 modules, lessons, labs, glossary, reference links and four-option assessments.
