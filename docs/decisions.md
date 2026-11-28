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


## D-006 — PostgreSQL 16 in Docker as the database, Alembic for migrations (2026-11-28)
- **Status:** Proposed (to confirm in team meeting 2026-11-28)
- **Why:** database-level read-only role protects NL-to-SQL; same version on every laptop
  and in CI; one command to start or reset; schema changes are versioned and reviewed.
- **Alternatives:** SQLite (simpler, but no user roles and a different SQL dialect);
  Supabase (free projects pause after inactivity); native Windows install (kept as fallback).
- **Later:** a hosted copy on Neon for the demo.

## D-007 — PydanticAI for the advisor agent (2026-11-28)
- **Status:** Proposed (to confirm in team meeting 2026-11-28)
- **Why:** tools and results are Pydantic models we already use; works with Gemini and
  Ollama (provider swap); test model allows agent tests without API quota.
- **Alternatives:** Gemini SDK directly (more hand-written code); LangGraph (built for
  complex multi-step workflows, too heavy for one agent); AutoGen (not recommended for new projects).
- **Safeguard:** version pinned in uv.lock; agent wrapped inside src/fdg/advisor/ so the
  framework can be swapped in one place.