"""Flagship: an M&A due-diligence "deal desk" of specialist agents.

This example composes two harness capabilities. `SubAgents` lets one lead agent
delegate self-contained tasks to named specialist agents, each running in its
own isolated context. The You.com capabilities (`YouSearch`, `YouResearch`)
ground each specialist in current, cited web and finance sources.

The desk has three specialists, one per You.com surface, and each returns a
typed findings model rather than loose prose:

- `market_analyst`   -- `YouSearch`: surveys the target's market, product,
  customers, and competitors, with recent, high-signal web sources (aggregators
  excluded, the business press boosted). Returns `MarketFindings`.
- `finance_analyst`  -- `YouResearch.finance_research`: analyzes financial
  health, funding, valuation, and credit exposure over You.com's finance index.
  Returns `FinanceFindings`.
- `risk_analyst`     -- `YouResearch.research`: runs multi-step research into
  regulatory, legal, security, and reputational risk, pinned to primary
  regulators and courts. Returns `RiskFindings`.

The lead agent delegates one brief to each specialist, verifies the occasional
single fact with the You.com `answer` tool, then synthesizes everything into a
structured `DueDiligenceMemo`. It shows off the orchestration controls too: a
cost-aware `fast`/`deep` model menu the lead routes each delegation to,
per-specialist timeouts and call budgets, and a tree-wide `UsageLimits` cap.

Run it (from the repo root):

    pip install -r requirements.txt
    cp .env.example .env   # then paste your keys into .env
    python deal_desk.py

Keys live in `.env` (gitignored): `YDC_API_KEY` from https://api.you.com and
`OPENROUTER_API_KEY` from https://openrouter.ai. `LLM_MODEL` sets the
specialists; `LEAD_MODEL` sets the orchestrator (defaults to `LLM_MODEL`).
`FAST_MODEL` / `DEEP_MODEL` populate the routing menu (default to `LLM_MODEL` /
`LEAD_MODEL`). All accept any Pydantic AI model string.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits

from observability import configure_observability
from pydantic_ai_harness import SubAgent, SubAgents, YouResearch, YouSearch

# Load vars from .env and wire Logfire tracing before the agents run.
load_dotenv(Path(__file__).resolve().parent / '.env')
configure_observability('cookbook-deal-desk')

MODEL = os.environ.get('LLM_MODEL', 'openrouter:anthropic/claude-3.5-sonnet')
LEAD_MODEL = os.environ.get('LEAD_MODEL') or MODEL
# The routing menu: cheap breadth on `fast`, deeper synthesis on `deep`. Both
# default to the models above, so the desk runs with no extra configuration.
FAST_MODEL = os.environ.get('FAST_MODEL') or MODEL
DEEP_MODEL = os.environ.get('DEEP_MODEL') or LEAD_MODEL


class MarketFindings(BaseModel):
    """What the market analyst reports back to the lead."""

    summary: str = Field(description='Two or three sentences on the market position and momentum.')
    market_size_and_growth: list[str] = Field(description='Sizing and growth findings, each ending with a source URL.')
    competition: list[str] = Field(description='Competitive-landscape findings, each ending with a source URL.')
    demand_signals: list[str] = Field(description='Customer and demand findings, each ending with a source URL.')
    recent_news: list[str] = Field(description='Recent developments that bear on the deal, each with a source URL.')


class FinanceFindings(BaseModel):
    """What the finance analyst reports back to the lead."""

    summary: str = Field(description='Two or three sentences on financial health and the funding picture.')
    revenue_and_margins: list[str] = Field(description='Revenue, growth, and margin findings, each with a source URL.')
    funding_and_debt: list[str] = Field(description='Funding, debt, and liquidity findings, each with a source URL.')
    valuation: list[str] = Field(description='Valuation benchmarks and comparables, each with a source URL.')
    credit_exposure: list[str] = Field(description='Credit or liquidity exposure findings, each with a source URL.')


class RiskFindings(BaseModel):
    """What the risk analyst reports back to the lead."""

    summary: str = Field(description='Two or three sentences on the overall risk posture.')
    regulatory_legal: list[str] = Field(description='Regulatory, legal, and enforcement findings, each with a URL.')
    security_fraud: list[str] = Field(description='Security, fraud, and incident findings, each with a source URL.')
    reputational: list[str] = Field(description='Reputational or ESG findings, each ending with a source URL.')
    confirmed_vs_alleged: list[str] = Field(description='Which items are confirmed facts versus open allegations.')


class DueDiligenceMemo(BaseModel):
    """The synthesized output of a deal-desk run."""

    target: str = Field(description='The acquisition target as understood by the desk.')
    thesis: str = Field(description='The investment thesis the analysis was run against.')
    market: list[str] = Field(description='Market and competitive findings, each ending with its source URL.')
    financials: list[str] = Field(description='Financial and credit findings, each ending with its source URL.')
    risks: list[str] = Field(description='Regulatory, legal, security, and reputational findings, each with a URL.')
    red_flags: list[str] = Field(description='Deal-breakers or issues that would materially change the price.')
    open_questions: list[str] = Field(description='What the desk could not resolve and should confirm in diligence.')
    recommendation: str = Field(description="One of 'proceed', 'proceed with conditions', or 'pass'.")
    rationale: str = Field(description='Why the recommendation follows from the findings above.')


market_analyst = Agent(
    MODEL,
    name='market_analyst',
    description="Surveys a target's market position, product, customers, and competitors from recent web sources.",
    output_type=MarketFindings,
    # Web Search domain controls: drop low-signal aggregators, re-rank the
    # business press up (boost keeps the rest of the web, it does not exclude
    # it). include_domains would be an allowlist and cannot combine with these.
    capabilities=[
        YouSearch(
            num_results=12,
            freshness='month',
            country='us',
            exclude_domains=['reddit.com', 'quora.com', 'pinterest.com'],
            boost_domains=['reuters.com', 'bloomberg.com', 'ft.com', 'wsj.com', 'pitchbook.com'],
            max_text_chars=6_000,
        )
    ],
    instructions=(
        'You are a market analyst on an M&A deal desk. Survey the market broadly, read the most '
        'relevant sources in full, and report the market size and growth, the competitive landscape, '
        'the customer and demand picture, and any recent news that bears on the deal. Quote dated '
        'figures and cite a source URL for every claim.'
    ),
)

finance_analyst = Agent(
    MODEL,
    name='finance_analyst',
    description="Analyzes a target's financial health, funding, valuation, and credit exposure.",
    output_type=FinanceFindings,
    # `finance_research` runs on You.com's curated finance index (SEC filings,
    # earnings transcripts, analyst coverage, fundamentals, financial news), so
    # it takes no domain filters or output_schema -- the corpus is the control.
    # `deep` (a minute or two per call) is the right default for a desk read;
    # `exhaustive` is slower and costlier, for full standalone diligence.
    capabilities=[YouResearch(finance_effort='deep')],
    instructions=(
        'You are a financial analyst on an M&A deal desk. Use `finance_research` to assess the '
        "target's revenue and growth, margins and cash position, funding and debt, valuation "
        'benchmarks, and any credit or liquidity exposure. Each `finance_research` call is a full '
        'multi-step research run that takes a minute or two and is metered per call, so make one '
        'comprehensive call covering the whole brief rather than many narrow ones. Quantify with '
        'dated figures, flag where the data is stale or estimated, and cite a source URL for every number.'
    ),
)

risk_analyst = Agent(
    MODEL,
    name='risk_analyst',
    description='Runs multi-step research into regulatory, legal, security, and reputational risk.',
    output_type=RiskFindings,
    # Research supports source_control, so pin risk work to primary regulators
    # and courts. An allowlist (include_domains) is used alone here; it cannot
    # combine with boost/exclude.
    capabilities=[
        YouResearch(
            research_effort='deep',
            freshness='year',
            country='us',
            include_domains=['sec.gov', 'justice.gov', 'ftc.gov', 'courtlistener.com', 'sam.gov'],
        )
    ],
    instructions=(
        'You are a risk and compliance analyst on an M&A deal desk. Use `research` to investigate '
        'regulatory and legal exposure, litigation and enforcement history, security and fraud '
        'incidents, and reputational or ESG concerns. Each `research` call is a multi-step run, so '
        'make one comprehensive call covering the whole brief rather than many narrow ones. Separate '
        'confirmed facts from allegations, note dates, and cite a source URL for every claim.'
    ),
)

deal_desk = Agent(
    LEAD_MODEL,
    output_type=DueDiligenceMemo,
    capabilities=[
        SubAgents(
            agents=[
                # Breadth work is cheap; give it a short leash on the fast model.
                SubAgent(
                    market_analyst,
                    timeout_seconds=180,
                    max_calls=2,
                    on_failure='Market scan is unavailable; record the gap under open_questions and continue.',
                ),
                # The finance research run is the slow, expensive one: pin it to
                # the deep model, allow a single delegation, and meter it with
                # its own request budget (which counts only this child's requests).
                SubAgent(
                    finance_analyst,
                    models=['deep'],
                    timeout_seconds=360,
                    max_calls=1,
                    usage_limits=UsageLimits(request_limit=12),
                    on_failure='Finance research is unavailable; flag the missing financials under open_questions.',
                ),
                SubAgent(
                    risk_analyst,
                    timeout_seconds=300,
                    max_calls=2,
                    on_failure='Risk research is unavailable; flag the missing risk review under open_questions.',
                ),
            ],
            # A cost-aware menu the lead routes each delegation to. Keys name the
            # job, not the vendor; the lead picks per task (finance is pinned to
            # `deep` above).
            models={'fast': FAST_MODEL, 'deep': DEEP_MODEL},
            # Only the specialists above; do not auto-load agent files from disk.
            agent_folders=None,
        ),
        # The lead keeps a light research capability purely for the `answer`
        # tool: a fast, cited, single-call check on one fact. Custom guidance
        # keeps it from doing the specialists' deep work itself.
        YouResearch(
            research_effort='lite',
            guidance=(
                'You also have an `answer` tool for a fast, cited answer to one narrow question. '
                'Use it only to verify a single specific fact (a date, a figure, an entity), never '
                'for analysis. Delegate all substantive research to the specialist sub-agents.'
            ),
        ),
    ],
    instructions=(
        'You run an M&A due-diligence desk. For the given target and thesis, delegate one '
        'self-contained brief to each specialist -- market_analyst, finance_analyst, and '
        'risk_analyst -- passing everything each needs, since they do not see this conversation. '
        'Route broad, time-boxed scans to the `fast` model and deeper analysis to the `deep` model. '
        'You may use `answer` to verify a single fact the specialists left ambiguous. Then '
        'synthesize their findings into a due-diligence memo. Keep every claim traceable to a '
        'source your analysts cited, surface contradictions between them as red flags or open '
        'questions, and let the recommendation follow from the evidence rather than the thesis.'
    ),
)

# Tree-wide budget. Because SubAgents forwards the lead's usage by default, this
# caps requests across the whole desk -- except finance_analyst, which meters
# separately under its own per-delegate usage_limits.
DESK_BUDGET = UsageLimits(request_limit=80)


def run_deal_desk(target: str, thesis: str) -> DueDiligenceMemo:
    """Run the desk against one target and thesis and return the structured memo."""
    prompt = f'Target: {target}\nThesis: {thesis}\n\nProduce the due-diligence memo.'
    return deal_desk.run_sync(prompt, usage_limits=DESK_BUDGET).output


def main() -> None:
    memo = run_deal_desk(
        target='a mid-market private credit asset manager focused on asset-backed finance',
        thesis=(
            'Acquire to expand into asset-backed finance while private credit is under stress in '
            '2026, betting the target underwrites more conservatively than distressed peers.'
        ),
    )
    print(memo.model_dump_json(indent=2))


if __name__ == '__main__':
    main()
