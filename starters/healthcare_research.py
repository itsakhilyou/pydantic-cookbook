"""Healthcare starter: grounded clinical research with the You.com Research API.

A single-capability example. `YouResearch` gives the agent an `answer` tool,
a multi-step `research` tool, and a `finance_research` tool; the instructions
here steer it to `research`, which runs many searches and synthesizes one
cited answer -- the right fit for a moving clinical picture assembled from CDC
notices, journals, and health-system reports. An `output_schema` makes
`research` return validated structured JSON (case counts, resistance,
treatment, containment) that the model then writes up.

Topic: the Candida auris outbreak and its multidrug antimicrobial resistance,
where treatment selection and infection control depend on current, sourced data.

Run it (from the repo root):

    pip install -r requirements.txt
    cp .env.example .env   # then paste your keys into .env
    python starters/healthcare_research.py

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
configure_observability('cookbook-healthcare')

MODEL = os.environ.get('LLM_MODEL', 'openrouter:anthropic/claude-3.5-sonnet')

# `research` returns structured JSON matching this schema instead of prose when
# an `output_schema` is set, so the fields are validated before the model writes
# them up. (The API rejects output_schema only with research_effort='lite'.)
RESEARCH_SCHEMA = {
    'type': 'object',
    'properties': {
        'case_counts': {'type': 'string', 'description': 'Dated U.S. case counts and geographic spread.'},
        'resistance': {'type': 'string', 'description': 'Resistance rates by antifungal class, with dates.'},
        'first_line_treatment': {'type': 'string', 'description': 'Current first-line treatment selection.'},
        'containment': {'type': 'string', 'description': 'Infection-control and containment guidance.'},
        'as_of_date': {'type': 'string', 'description': 'The date the figures above are current as of.'},
    },
    'required': ['case_counts', 'resistance', 'first_line_treatment', 'containment', 'as_of_date'],
    # The Research API requires strict schemas: every object must forbid extra keys.
    'additionalProperties': False,
}

agent = Agent(
    MODEL,
    # `deep` runs more searches and reads more sources than `standard`; use
    # `exhaustive` for the most thorough pass at higher latency and cost.
    # `boost_domains` re-ranks CDC, WHO, and the clinical literature up without
    # excluding other sources; `country` focuses results; `output_schema` makes
    # `research` return validated structured JSON (see RESEARCH_SCHEMA above).
    capabilities=[
        YouResearch(
            research_effort='deep',
            freshness='month',
            country='us',
            boost_domains=['cdc.gov', 'who.int', 'nejm.org', 'thelancet.com', 'idsociety.org'],
            output_schema=RESEARCH_SCHEMA,
        )
    ],
    instructions=(
        'You are a clinical research assistant supporting infectious-disease clinicians. '
        'Use the `research` tool to investigate the question across current sources, then '
        'answer in tight, clinically useful prose. Each `research` call is a multi-step run, '
        'so make one comprehensive call covering the whole question rather than many narrow '
        'ones. Distinguish established guidance from preliminary reports, note the date of any '
        'figure, and cite the source URL for every claim. If the evidence is thin or '
        'conflicting, say so plainly.'
    ),
)

QUESTION = (
    'Summarize the current Candida auris outbreak in U.S. healthcare facilities: resistance '
    'epidemiology (fluconazole and amphotericin B), 2024-2026 case counts and geographic '
    'spread, first-line treatment selection, and infection-control and containment guidance.'
)


def main() -> None:
    result = agent.run_sync(QUESTION)
    print(result.output)


if __name__ == '__main__':
    main()
