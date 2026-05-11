# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

Python 3.14.2 via Homebrew. Virtual environment lives at `env/` (already created).

```bash
source env/bin/activate        # activate venv
python <file>.py               # run any script
```

## Linting

CI runs `flake8` on every PR to `main`. Run locally before pushing:

```bash
flake8 .
```

`ruff` is also installed in the venv (same cache lives at `.ruff_cache/`).

## Repository Structure

Each student has their own top-level directory (`akash/`, `keerthi/`, `karthik/`). All work stays scoped to that directory. New students get a new directory named after them.

- `Questions/` — curriculum docs: practice problems, sprint plans, mini-project specs
- `DSA-4Week.md` — 4-week FAANG prep plan (Arrays → Strings → Hashmaps → Two Pointers → Sliding Window → Binary Search → Stack → Linked Lists → Trees), tracking via `[ ]` checkboxes
- `Git.md` — Git reference doc for students

## project_context_extractor.py

Located at `akash/project_context_extractor.py`. Reads project update JSON files and formats them into structured summaries.

**Input format** — JSON files must follow this schema:
```json
{ "data": [ { "update": "<html or plain text>", ... }, ... ] }
```

**Usage:**
```bash
cd akash
python project_context_extractor.py <person>_project.json
```

Outputs `<person>_project_summary.txt` in the current directory. Optionally uses `facebook/bart-large-cnn` via HuggingFace `transformers` for AI summarization; falls back to regex extraction if `transformers`/`torch` are not installed.

## Calculator module (akash/calculator/)

`main.py` imports `add` and `sub` using bare module names (`from add import add`). Run it from inside the directory:

```bash
cd akash/calculator
python main.py
```

Running it from the repo root will fail with an `ImportError` because there is no `__init__.py` and the directory is not on `sys.path`.

## Linting config

`.flake8` at the repo root sets `max-line-length = 110` and adds per-file-ignores for two known structural issues in `akash/`:
- `venkatesh_project.json.py` — JSON content with the wrong file extension; F821/E501/W292 are suppressed there.
- `project_context_extractor.py` — logging style uses empty f-strings (F541) and one unused variable (F841); suppressed there.

All other Python files are linted with default rules at 110-char max.

## Student directories — read only

`akash/`, `keerthi/`, and `karthik/` are student submission directories. Students submit code by opening a PR that targets only their own directory. Do not create, edit, or delete files inside these directories. All curriculum content lives at the repo root or in `Questions/`.

## Branch workflow

- Each student works on their own branch (e.g. `akash_branch`)
- PRs target `main`; scope of each PR is strictly the student's own directory
- Do not push directly to `main`
