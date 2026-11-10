## Repository and maintenance

The runnable academy is `AI_Systems_Academy/index.html`. The other files make the learning content inspectable and allow maintainers to rebuild and validate the application. They are not required for ordinary study.

```text
AI_Systems_Academy/
├── index.html
├── docs/                    # Field manual, study guide, design notes
├── source/                  # Application template, content, build scripts
├── tests/                   # Content and assessment logic tests
├── CHANGELOG.md
└── SHA256SUMS.txt
```

To work on the application, run these commands **from the `AI_Systems_Academy/` directory**:

```sh
python3 source/rebuild.py
python3 tests/validate_content.py
node tests/assessment_flow.cjs
```

Python 3's standard library is sufficient for the rebuild. Node.js is needed for the JavaScript regression suite, not for studying with the academy.

Lessons live in `source/modules.json`; assessment items are in `source/question-bank.json` and `source/scenario-questions.json`; engineering cases are in `source/engineering-clinics.json`. Keep their identifiers stable to preserve progress references. The content-generation scripts can overwrite hand-edited JSON if rerun without care, while `patch_app_v2.py` is historical migration code rather than a normal build step.

See [`docs/ASSESSMENT_AND_CLINIC_DESIGN.md`](docs/ASSESSMENT_AND_CLINIC_DESIGN.md) for the assessment rubric and [`CHANGELOG.md`](CHANGELOG.md) for release history.

### What has been validated

For v2.0, content validation and offline JavaScript logic tests cover the question bank, answer choices, selection and scoring, progress compatibility, clinic state, and exam submission. **Those checks do not establish real-world assessment difficulty or full interface quality.** Graphical browser behavior, responsive layout, keyboard accessibility, and learner-cohort performance still need independent validation.

The labs are instructions for work in an appropriate non-production environment. The application itself does not launch infrastructure or perform those experiments on your behalf.
