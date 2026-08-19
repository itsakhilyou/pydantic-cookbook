"""Finance starter: market analysis with the You.com Finance Research API.

A single-capability example. `YouResearch` exposes `answer`, `research`, and
`finance_research`; the instructions here steer it to `finance_research`, the
finance-tuned endpoint for company, market, and instrument analysis. It reads
across deal-flow data, fund performance, default statistics, and manager
commentary and returns one cited synthesis.

Topic: the maturation and mounting stress of the private credit market --
valuation scrutiny, credit-quality deterioration, and systemic interconnection.

Run it (from the repo root):

    pip install -r requirements.txt
    cp .env.example .env   # then paste your keys into .env
    python starters/finance_research.py

Keys live in `.env` (gitignored): `YDC_API_KEY` from https://api.you.com and
`OPENROUTER_API_KEY` from https://openrouter.ai. `LLM_MODEL` defaults to an
OpenRouter model; set it to any Pydantic AI model string to change providers.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from pydantic_ai import Agent

from pydantic_ai_harness import YouResearch

# Repo root on sys.path so `observability` is importable from starters/.
_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
from observability import configure_observability  # noqa: E402

# Load vars from .env and wire Logfire tracing before the agent runs.
load_dotenv(_ROOT / '.env')
configure_observability('cookbook-finance')

MODEL = os.environ.get('LLM_MODEL', 'openrouter:anthropic/claude-3.5-sonnet')

agent = Agent(
    MODEL,
    # `finance_effort` accepts `deep` or `exhaustive`. `deep` (the default here)
    # runs in roughly a minute or two; `exhaustive` reads more widely at
    # noticeably higher latency and cost, so reserve it for full due diligence.
    # Unlike `research`, `finance_research` runs on You.com's curated finance
    # index (SEC filings, earnings transcripts, analyst coverage, fundamentals,
    # financial news), so it takes no domain filters or output_schema -- the
    # pre-curated corpus is the control. Reach for `research` with include/boost
    # domains when you need domain-pinned or structured output.
    capabilities=[YouResearch(finance_effort='deep')],
    instructions=(
        'You are a credit strategist writing a desk note for portfolio managers. '
        'Use the `finance_research` tool to analyze the question, then write a concise, '
        'decision-useful note. Each `finance_research` call is a full multi-step research '
        'run that takes a minute or two and is metered per call, so make one comprehensive '
        'call covering the whole question rather than fanning out many narrow ones. '
        'Lead with the market signal, quantify with dated figures, name the specific stress '
        'points and their transmission channels, and cite the source URL for every number. '
        'Flag where the data is stale or contested.'
    ),
)

QUESTION = (
    'Assess the current state of the private credit market: size and growth, the stress signals '
    'entering 2026, valuation and mark transparency concerns, credit-quality deterioration and '
    'notable defaults, systemic interconnection with banks and insurers, and the shift toward '
    'asset-backed finance. What should credit investors watch next?'
)


def main() -> None:
    result = agent.run_sync(QUESTION)
    print(result.output)


if __name__ == '__main__':
    main()
