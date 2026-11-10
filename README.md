# AI Systems Academy

**Learn how AI systems work, how to investigate them, and how to make better engineering decisions.**

AI Systems Academy is a self-paced learning application you can open in your browser. Its lessons connect model behavior with the systems around it: inference, context, retrieval, agent harnesses, tools, security, evaluation, and operations. You follow request traces, carry out guided experiments, and work through decisions where the available evidence matters more than a plausible answer.

The academy is for learners, developers, and technical practitioners who want to reason about the entire system. It does not run models, operate infrastructure, or execute agent-generated commands.

## Start learning

**[Download AI Systems Academy (ZIP, `main` branch)](https://github.com/coresolutiondoteu/AI-Learn-Assessment/archive/refs/heads/main.zip)**

1. Extract the ZIP, keeping its folder structure.
2. Open `AI_Systems_Academy/index.html` in a modern browser (inside the extracted repository folder).
3. Select **Begin module 1**. The **Assessment center** is available whenever you want to practise or take a scored exam.

You don't need an account, API key, model download, backend, database, or web server. The lessons and assessments run offline. External articles, videos, and documentation links still need internet access.

Your progress is saved in browser-local storage when the browser permits it. Before moving or updating the academy, use **My progress -> Export progress JSON** and keep the file somewhere safe. You can restore it with **Import progress JSON**.

[![AI Systems Academy video walkthrough](https://img.youtube.com/vi/ZzmACDsid8E/hqdefault.jpg)](https://youtu.be/ZzmACDsid8E)


## What you will actually do

A lesson introduces one part of the system and follows its role in a request. A controlled lab gives you something to observe for yourself. An engineering clinic then puts that knowledge under pressure: you have to decide what an observation proves, what remains uncertain, and which investigation or design choice is justified.

Each of the ten modules has six lessons. The learning path connects **concept, request trace, lab, engineering clinic, checkpoint, and review**. Clinic feedback explains the preferred choice and the shortcomings of alternatives; it is guided practice, not a scored exam.

You can use the shorter checkpoints to catch gaps as you go, or follow the 16-week study route toward the capstones. The field manual and opening guide provide the longer reference material when you need it.

### Inside the academy

| Material | Included in v2.0 |
| --- | --- |
| Curriculum | 10 modules, 60 linked lessons, and the interactive L0-L9 AI systems stack |
| Practical work | 10 lab runbooks; 10 engineering cases with 30 guided decisions |
| Design and projects | 11 architecture patterns, 4 capstones, and a 16-week study route |
| References | 99 glossary entries with review scheduling; 64 annotated references in the field manual |
| Assessment | 372 four-choice questions across foundational, applied, and engineering-judgment levels |
| Guides | AI Systems Engineering Field Manual, Opening Study Guide, and assessment/clinic design notes |

The material begins with computing and model fundamentals, including tokenization, prefill/decode, memory, and quantization. It then moves through local inference, context engineering, tool contracts and MCP, retrieval, evaluation, security, and operational trade-offs. The capstones cover an evidence-oriented assistant, a bounded tool agent, an evaluation-driven coding harness, and inference/agent performance work.

## Check what you've learned

The v2.0 bank contains **372 single-answer questions**, with four options per question. A scored exam selects questions and shuffles answer order; explanations and links to relevant material appear after submission.

| Level | Questions in bank | Share of scored exam | Tests |
| --- | ---: | ---: | --- |
| L1 - Foundations | 120 | 30% | Terminology and core responsibilities |
| L2 - Applied understanding | 192 | 50% | Traces, measurements, mechanisms, and diagnosis |
| L3 - Engineering judgment | 60 | 20% | Design choices under operational and security constraints |

Choose a **20-question module exam** or a comprehensive exam with **20, 30, or 40 questions**. The passing threshold is **80%**. For lower-pressure practice, there is also a ten-question guided challenge with optional hints, and five-question module checkpoints with immediate feedback.

An exam result reflects that attempt; **it is not a professional certification**. The question bank has not been psychometrically calibrated against real learner cohorts. Independent review of question difficulty and real learner testing remain future validation work.

## Progress and privacy

The academy operates in your browser. It does not require accounts, telemetry collection, or remote model calls. Learning history and notes are kept locally using the `ai-systems-academy-v1` storage key, with an optional field for clinic progress.

Some browsers restrict storage for `file://` pages, and progress may not follow you to another browser or file location. **Export your progress before upgrading.** Importing a progress file replaces the current browser record. That file can include your notes, so avoid putting credentials or sensitive production information into labs or exported records.
