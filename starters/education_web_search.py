"""Education starter: current-evidence survey with the You.com Web Search API.

A single-capability example. `YouSearch` gives the agent two tools:
`web_search`, which returns several results with query-relevant excerpts, and
`get_page`, which reads a specific URL in full. The agent surveys broadly, then
reads the most promising pages before answering -- the right shape for a topic
whose evidence base shifts monthly across district reports, labor data, and
education research.

Topic: K-12 teacher burnout, retention, and workload, and which interventions
the recent evidence actually supports.

Run it (from the repo root):

    pip install -r requirements.txt
    cp .env.example .env   # then paste your keys into .env
    python starters/education_web_search.py

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

from pydantic_ai_harness import YouSearch

# Repo root on sys.path so `observability` is importable from starters/.
_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
from observability import configure_observability  # noqa: E402

# Load vars from .env and wire Logfire tracing before the agent runs.
load_dotenv(_ROOT / '.env')
configure_observability('cookbook-education')

MODEL = os.environ.get('LLM_MODEL', 'openrouter:anthropic/claude-3.5-sonnet')

agent = Agent(
    MODEL,
    # `freshness='month'` keeps results recent; raise `num_results` to survey
    # more sources per search (1 to 20). `country` focuses results, and the
    # domain controls shape the corpus without a second fetch: `exclude_domains`
    # drops low-signal aggregators, while `boost_domains` re-ranks authoritative
    # sources up without excluding the rest of the web.
    capabilities=[
        YouSearch(
            num_results=10,
            freshness='month',
            country='us',
            exclude_domains=['pinterest.com', 'reddit.com', 'quora.com'],
            boost_domains=['rand.org', 'nces.ed.gov', 'oecd.org', 'pewresearch.org', 'edweek.org'],
        )
    ],
    instructions=(
        'You are an education-policy analyst briefing a district leadership team. '
        'Search broadly, read the most relevant sources in full, and synthesize what '
        'the current evidence supports. Separate well-established findings from single '
        'studies, quote concrete figures with their dates, and cite the source URL for '
        'each claim. Close with the interventions the evidence backs most strongly.'
    ),
)

QUESTION = (
    'What does recent evidence say about K-12 teacher burnout and retention? Cover reported '
    'burnout rates and weekly workload, the cost and rate of early-career turnover, protective '
    'factors, and which interventions (including AI-assisted workload reduction) are best '
    'supported by the research.'
)


def main() -> None:
    result = agent.run_sync(QUESTION)
    print(result.output)


if __name__ == '__main__':
    main()
