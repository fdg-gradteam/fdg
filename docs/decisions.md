# Decision log

Each entry records a decision that affects more than one person. Newest at the bottom.
Format: date, decision, why, alternatives considered.

## D-001 — Team-owned GitHub organization, public repository (2026-11-23)
- **Why:** the project belongs to the team, not one account; branch protection is free on
  public repositories.
- **Alternatives:** private personal repository (branch protection not enforced on the free
  plan); Student Developer Pack being checked as a later option.

## D-002 — `uv` with `pyproject.toml` and `uv.lock` instead of pip and `requirements.txt` (2026-11-23)
- **Why:** one tool installs Python, creates the virtual environment and pins exact versions,
  so all six laptops and CI run the same packages.
- **Alternatives:** pip + venv + unpinned `requirements.txt` (versions drift between laptops).

## D-003 — Python 3.12 for everyone (2026-11-23)
- **Why:** a single version avoids "works on my machine"; 3.12 is expected to be supported by the
  heavy libraries. To be confirmed by the Tech Lead's install test (PaddleOCR, Prophet).

## D-004 — Git Bash as the standard terminal (2026-11-23)
- **Why:** the same commands work on every laptop and match the Linux CI.

## D-005 — Database and Docker decision postponed (2026-11-23)
- **Why:** not needed until the ledger work starts; decide with real requirements in hand.
