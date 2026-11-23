# FDG — Financial Decision Guard

An Arabic-first, agentic decision-support assistant that helps Egyptian small businesses check
invoices and tax position, forecast cash, and evaluate financial decisions before committing.

Graduation project, Faculty of Computer Science and AI, Menoufia National University, 2026–2027.

> FDG is decision support, not legal or tax advice.

## Quick start (Windows, Git Bash)

Prerequisites: Git for Windows, VS Code, `uv`, GitHub CLI (see `CONTRIBUTING.md`).

```bash
git clone https://github.com/fdg-gradteam/fdg.git
cd fdg
uv sync                      # creates .venv and installs the exact locked versions
uv run pre-commit install    # turns on the automatic checks before each commit
cp .env.example .env         # then put your own keys in .env
uv run pytest                # should end with "passed"
```

## Repository layout

| Path | What lives there |
|---|---|
| `src/fdg/` | All application code, one package per module |
| `tests/` | Pytest tests, mirroring `src/fdg/` |
| `rules/` | Dated, sourced tax rules (YAML), kept apart from code |
| `evaluation/` | Evaluation scripts and results |
| `data/` | Data notes only. Real data goes in `data/raw/`, which Git ignores |
| `docs/` | Decision log, meeting notes, design documents |

## How we work

Read `CONTRIBUTING.md` before your first pull request.
