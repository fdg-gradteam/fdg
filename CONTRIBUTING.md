# Contributing to FDG

## 1. The daily loop

```bash
git switch main
git pull                                   # start from the latest main
git switch -c feature/compliance-vat-check # one branch per task
# ... write code and tests ...
uv run ruff check . && uv run pytest       # same checks CI will run
git add .
git commit -m "feat(compliance): add VAT arithmetic check"
git push -u origin feature/compliance-vat-check
gh pr create --fill                        # open the pull request
```

## 2. Rules

- **Nobody pushes to `main`.** Every change goes through a pull request with one approving review
  and green CI.
- **One task = one branch = one PR.** Small PRs get reviewed fast and break less.
- **Branch names:** `feature/<module>-<short-name>`, `fix/<short-name>`, `docs/<short-name>`,
  `chore/<short-name>`.
- **Commit messages** follow Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`,
  `refactor:`, `chore:`, optionally with a scope, e.g. `feat(capture): ...`.
- **Packages:** add with `uv add <package>` (or `uv add --dev <package>` for tools). Never use
  `pip install` in this project. Commit the updated `pyproject.toml` and `uv.lock` together.
- **Secrets and real data never enter Git.** Keys go in `.env`. If a key is ever committed,
  revoke it immediately, then tell the team.
- **Decisions that affect other people** go in `docs/decisions.md`.

## 3. Reviewing a PR

- Does it do what the linked issue asks, and nothing unrelated?
- Are there tests for the new logic, and do they test the edge cases?
- Is any money figure computed by code (never by the language model)?
- Would you understand this code in two months?

Approve only if you would be comfortable defending this code in front of the committee.

## 4. Definition of Done

A task is done when: the code is merged into `main`, CI is green, tests cover the new logic,
and any evaluation results are saved under `evaluation/`.
