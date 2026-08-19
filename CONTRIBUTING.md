# Contributing

Thanks for your interest in improving these cookbooks. This repo holds runnable
Pydantic AI examples that ground agents in current, cited web sources via the
You.com capabilities in `pydantic-ai-harness`.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then paste your YDC_API_KEY and OPENROUTER_API_KEY
make smoke             # verify imports and agent wiring without spending tokens
```

`make smoke` should end with `SMOKE OK`. It constructs every agent without
making network calls, so it is the fastest way to confirm your environment is
wired up.

## Running the examples

```bash
make run-health    # starters/healthcare_research.py  (Research API)
make run-edu       # starters/education_web_search.py (Web Search API)
make run-finance   # starters/finance_research.py     (Finance Research API)
make run-deal      # deal_desk.py                     (all three + SubAgents)
```

The `research`, `finance_research`, and deal-desk runs issue live calls and can
take minutes; `make run-edu` is the fastest first check.

## Before you open a pull request

- Run `make smoke` and make sure it prints `SMOKE OK`.
- If you change a script's output shape, regenerate the matching file under
  `examples/` from a real run so the saved outputs stay accurate.
- Keep keys out of code and commits. Everything secret lives in `.env`, which
  is gitignored. Never paste a real key into `.env.example` -- leave it blank.
- Match the existing style: docstrings on every module, typed models for
  structured outputs, and a source URL on every claim an agent returns.

## Proposing changes

Small fixes and improvements are welcome as pull requests against `main`. For
larger changes or new cookbook ideas, open an issue first so we can discuss
scope before you do the work.
