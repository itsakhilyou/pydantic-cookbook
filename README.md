# You.com cookbooks for Pydantic AI Harness

Four runnable examples that ground Pydantic AI agents in current, cited sources
with the [You.com capabilities](https://github.com/pydantic/pydantic-ai-harness/tree/main/pydantic_ai_harness/youdotcom)
in `pydantic-ai-harness`. Three are minimal single-API starters, one per
You.com surface; the fourth composes all three into a multi-agent workflow.

| Cookbook | You.com surface | Capability | Topic |
| --- | --- | --- | --- |
| [`starters/healthcare_research.py`](starters/healthcare_research.py) | Research API | `YouResearch` (`research`) | Candida auris outbreak and antimicrobial resistance |
| [`starters/education_web_search.py`](starters/education_web_search.py) | Web Search API | `YouSearch` | K-12 teacher burnout and retention |
| [`starters/finance_research.py`](starters/finance_research.py) | Finance Research API | `YouResearch` (`finance_research`) | Private credit market stress |
| [`deal_desk.py`](deal_desk.py) | all three | `SubAgents` + `YouSearch` + `YouResearch` | M&A due-diligence deal desk |

## Quick start

You need two keys: a You.com API key (for search/research) and an OpenRouter
API key (for the model). The scripts read both from `.env` automatically, and
each run is traced to Logfire (see [Observability](#observability-pydantic-logfire)).

```bash
# 1. Install dependencies (creates nothing outside this folder).
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Add your keys.
cp .env.example .env
#   then edit .env and paste in:
#     YDC_API_KEY          (create at https://api.you.com)
#     OPENROUTER_API_KEY   (create at https://openrouter.ai/keys)

# 3. (Optional, one-time) connect Logfire so runs show up as traces.
uvx logfire --base-url='https://logfire-us.pydantic.dev' auth
uvx logfire --base-url='https://logfire-us.pydantic.dev' projects use --org itsakhil starter-project

# 4. Verify everything wires up without spending tokens.
make smoke

# 5. Run any example.
make run-health      # or run-edu, run-finance, run-deal
```

No manual `export` calls. Each script loads `.env` on import, so the
keys only have to live in one place. `.env` and `.logfire/` are gitignored.

Logfire is optional: if you skip step 3, `send_to_logfire='if-token-present'`
makes the scripts fall back to local console tracing, so they still run.

## Configuration (`.env`)

| Variable | Required | Purpose |
| --- | --- | --- |
| `YDC_API_KEY` | yes | You.com API key for `YouSearch` / `YouResearch`. |
| `OPENROUTER_API_KEY` | yes | OpenRouter key for the model calls. |
| `LLM_MODEL` | no | Model for the agents. Defaults to `openrouter:anthropic/claude-3.5-sonnet`. |
| `LEAD_MODEL` | no | Model for the `deal_desk.py` orchestrator. Defaults to `LLM_MODEL`. |
| `FAST_MODEL` | no | `deal_desk.py` routing menu: the `fast` model for broad scans. Defaults to `LLM_MODEL`. |
| `DEEP_MODEL` | no | `deal_desk.py` routing menu: the `deep` model for heavy analysis. Defaults to `LEAD_MODEL`. |

`LLM_MODEL` accepts any Pydantic AI model string, so you are not locked to
OpenRouter. OpenRouter examples:

```
LLM_MODEL=openrouter:anthropic/claude-3.5-sonnet
LLM_MODEL=openrouter:openai/gpt-4o
LLM_MODEL=openrouter:google/gemini-flash-1.5
LLM_MODEL=openrouter:openai/gpt-4o-mini   # cheaper, good for first runs
```

Direct providers work too (then use that provider's own key instead of
`OPENROUTER_API_KEY`): `anthropic:claude-sonnet-4-6`, `openai:gpt-4o`,
`google-gla:gemini-2.0-flash`.

The [Pydantic AI Gateway](https://pydantic.dev/docs/ai/overview/gateway/) is a
third option: it fronts many providers behind a single key managed through
Logfire, so you skip per-provider keys entirely. Prefix any model with
`gateway/`:

```
LLM_MODEL=gateway/anthropic:claude-sonnet-4-6
LLM_MODEL=gateway/openai:gpt-5.2
```

In short: `OPENROUTER_API_KEY` is only needed for `openrouter:...` models; a
direct provider needs that provider's own key; the gateway needs its single
gateway key (and none of the others).

For the deal desk, set a strong `LEAD_MODEL` and a cheaper `LLM_MODEL` so the
specialists survey cheaply and the orchestrator synthesizes on a stronger model.

## Test without spending tokens

`make smoke` imports every script and constructs every agent, which exercises
imports, capability wiring, and the deal-desk subagent roster without making
any network calls. Run it after install and after any edit:

```bash
make smoke
```

Expected output ends with `SMOKE OK` and lists the four agents plus the three
deal-desk subagents (`finance_analyst`, `market_analyst`, `risk_analyst`).

## Run

```bash
make run-health      # starters/healthcare_research.py
make run-edu         # starters/education_web_search.py
make run-finance      # starters/finance_research.py
make run-deal         # deal_desk.py
```

Or run a script directly: `python starters/healthcare_research.py`.

The `research`, `finance_research`, and full deal-desk runs issue live calls and
can take minutes on the higher effort levels; the default client timeout is
generous for that reason. Lower `research_effort` / `finance_effort`, or narrow
the questions, to iterate faster. For a first, cheap check, set
`LLM_MODEL=openrouter:openai/gpt-4o-mini` and run `make run-edu` (web search is
the fastest surface).

## Verified outputs

All four cookbooks were run end-to-end on 2026-08-19 with
`LLM_MODEL=openrouter:deepseek/deepseek-v4-flash-0731` (the deal desk routes
the same model through its `fast`/`deep` menu). Each exited 0 and returned a
structured, cited answer. Full outputs, including the enriched domain controls
and the healthcare `output_schema`, are saved in [`examples/`](examples/) so
you can see what a run produces without spending tokens; the excerpts below
show the shape.

| Cookbook | Surface | Wall time | Tool calls | Full output |
| --- | --- | --- | --- | --- |
| `education_web_search.py` | `YouSearch` | ~2.5 min | 11 `web_search` + 3 `get_page` | [`examples/education_web_search_output.md`](examples/education_web_search_output.md) |
| `healthcare_research.py` | `YouResearch` | ~1.5 min | 1 `research` + 1 `answer` | [`examples/healthcare_research_output.md`](examples/healthcare_research_output.md) |
| `finance_research.py` | `YouResearch` | ~4 min | 2 `finance_research` (`deep`) | [`examples/finance_research_output.md`](examples/finance_research_output.md) |
| `deal_desk.py` | all three + `SubAgents` | ~7.5 min | 26 `web_search`, 6 `get_page`, 2 `finance_research`, 1 `research`, 1 `answer` | [`examples/deal_desk_output.md`](examples/deal_desk_output.md) |

**Education** (Web Search) — the agent surveys broadly, then reads the most
relevant pages in full before synthesizing. It is the chattiest run: many
`web_search` rounds plus a few `get_page` reads, and the `boost_domains` show
up directly in the sourcing (RAND, Pew, OECD, NCES). Excerpt:

> # K-12 Teacher Burnout and Retention: Evidence Brief
>
> ## 1. Burnout rates: still elevated, and still worse than the broader workforce
>
> - 2025: 53% vs. 39% (teachers vs. the broader workforce)
> - **Pew Research Center (2024, n=2,531):** 54% of teachers say it's difficult
>   to achieve work-life balance; 84% say there isn't enough time in the regular
>   workday to get everything done.

**Healthcare** (Research) — one `research` call plus a quick `answer` check,
then the model synthesizes a cited clinical summary against the
`output_schema`. Fastest run. Excerpt:

> Here is a clinically oriented summary of the current U.S. *Candida auris*
> situation, drawn from the CDC's latest surveillance and guidance with dates
> attached.
>
> - **Clinical cases (CDC tracking page, as of March 3, 2026):** 6,304 clinical
>   cases in calendar year **2024**; the 2025 total fell to an estimated
>   **4,290** clinical cases.
> - Based on **8,033 isolates collected 2022–2023**: **>95% resistant to
>   fluconazole**, **~15% to amphotericin B**, **~1% to echinocandins**, and
>   **<1% pan-resistant**.

**Finance** (Finance Research) — two `finance_research` calls at `deep` effort,
then synthesis. The longest of the starters because each call does multi-step
source gathering server-side. Excerpt:

> # DESK NOTE — Private Credit: Entering 2026, the Silence Is the Signal
> ## The one-line call
>
> Private credit is not (yet) in a casualty-wave bankruptcy — the stress is
> being *held* inside the system through PIK amendments, distressed exchanges,
> and delayed marks. The investment question entering 2026 is not "will there be
> defaults" but "who holds the losses once marks catch up to cash-flow reality."

**Deal desk** (all three surfaces) — the lead delegates to the three
specialists, each of whom grounds its findings in a different You.com surface,
and synthesizes a typed `DueDiligenceMemo`. The `answer` tool shows up once, as
a lead-side fact check. Excerpt (from the JSON memo):

> **recommendation:** `proceed with conditions`
>
> **red_flags[0]:** No named target exists: this is a generic/hypothetical firm,
> so all target-specific economics (fee structure, FRE/EBITDA margin, advance
> rates, valuation multiples) are ESTIMATED and industry-benchmarked ...

### What the runs tell you about the two surfaces

- **`YouSearch`** trades tool-call count for control: the model drives the
  search loop, so expect many `web_search`/`get_page` round-trips and longer
  wall time, but you can tune `num_results` and `freshness` to shape it.
- **`YouResearch`** trades wall time for fewer round-trips: the API does the
  multi-step reading and synthesis server-side and hands back a cited result,
  so the model makes one or two tool calls and synthesizes. `research`/`finance_research`
  calls themselves take minutes; lower `research_effort`/`finance_effort` to
  iterate faster. Each `research`/`finance_research` call is a full multi-step
  run, so the instructions steer the agent to make one comprehensive call
  rather than fanning out many narrow ones.
- All four runs traced to Logfire under `cookbook-education`,
  `cookbook-healthcare`, `cookbook-finance`, and `cookbook-deal-desk` service
  names.

## The two capabilities

- **`YouSearch`** adds `web_search` (results with query-relevant excerpts, or
  full-page markdown) and `get_page` (the markdown of one URL). Use it to
  survey many sources and read the promising ones.
- **`YouResearch`** adds `answer` (a one-call cited answer), `research`
  (multi-step research across many sources), and `finance_research` (the
  finance-tuned counterpart). Use it when you want the API to do the reading and
  synthesis and hand back a cited result.

Both read `YDC_API_KEY` from the environment by default and return their sources
in a `Sources:` block plus `ToolReturn.metadata['sources']`, so the model can
cite them and your code can inspect them.

## The flagship: a deal desk of specialist agents

`deal_desk.py` shows the pattern the single-API starters build toward. A lead
agent holds a `SubAgents` capability naming three specialists, each equipped with
a different You.com surface and returning a typed findings model:

```python
from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits
from pydantic_ai_harness import SubAgent, SubAgents, YouResearch, YouSearch

# Web Search with domain controls: drop aggregators, boost the business press.
market_analyst = Agent(
    MODEL, name='market_analyst', output_type=MarketFindings,
    capabilities=[YouSearch(
        num_results=12, freshness='month', country='us',
        exclude_domains=['reddit.com', 'quora.com', 'pinterest.com'],
        boost_domains=['reuters.com', 'bloomberg.com', 'ft.com', 'wsj.com', 'pitchbook.com'],
    )],
)
# Finance Research runs on You.com's curated finance index -- no domain filters.
finance_analyst = Agent(
    MODEL, name='finance_analyst', output_type=FinanceFindings,
    capabilities=[YouResearch(finance_effort='deep')],
)
# Research supports source_control, so pin risk work to regulators and courts.
risk_analyst = Agent(
    MODEL, name='risk_analyst', output_type=RiskFindings,
    capabilities=[YouResearch(
        research_effort='deep', freshness='year', country='us',
        include_domains=['sec.gov', 'justice.gov', 'ftc.gov', 'courtlistener.com', 'sam.gov'],
    )],
)

deal_desk = Agent(
    LEAD_MODEL,
    output_type=DueDiligenceMemo,
    capabilities=[
        SubAgents(
            agents=[
                SubAgent(market_analyst, timeout_seconds=180, max_calls=2, on_failure='...'),
                SubAgent(finance_analyst, models=['deep'], timeout_seconds=360, max_calls=1,
                         usage_limits=UsageLimits(request_limit=12), on_failure='...'),
                SubAgent(risk_analyst, timeout_seconds=300, max_calls=2, on_failure='...'),
            ],
            models={'fast': FAST_MODEL, 'deep': DEEP_MODEL},  # cost-aware routing menu
            agent_folders=None,
        ),
        # The lead keeps a light research capability for the `answer` tool only:
        # a fast, cited, single-fact check while it synthesizes.
        YouResearch(research_effort='lite', guidance='Use `answer` only to verify one fact...'),
    ],
    instructions='Delegate one brief to each specialist, verify stray facts with answer, then synthesize a memo.',
)

memo = deal_desk.run_sync(prompt, usage_limits=UsageLimits(request_limit=80)).output
```

What the desk shows off, beyond the three You.com surfaces:

- **Domain controls** where the API supports them: the market analyst excludes
  aggregators and boosts the business press; the risk analyst pins its research
  to primary regulators and courts. The finance analyst uses no filters because
  `finance_research` already runs on a curated finance index.
- **Typed all the way down**: each specialist returns a Pydantic findings model
  (`MarketFindings`, `FinanceFindings`, `RiskFindings`) and the lead returns a
  `DueDiligenceMemo`.
- **Cost-aware routing**: a `fast`/`deep` model menu the lead picks from per
  delegation, with the expensive finance run pinned to `deep`.
- **Orchestration budgets**: per-specialist `timeout_seconds`, `max_calls`, and
  `on_failure` steering, plus a tree-wide `UsageLimits` on the run.
- **The `answer` tool** on the lead for fast, cited, single-fact checks during
  synthesis -- the one You.com surface the starters do not exercise.

Swap the specialists, their You.com configuration, the routing menu, or the
output models to retarget the desk at another kind of investigation.

## Folder layout

```
pydantic-cookbook/
  .env.example      # template; copy to .env and fill in keys
  .env              # your real keys (gitignored)
  .gitignore        # .env, .logfire/, __pycache__/, .venv/
  requirements.txt  # pydantic-ai, pydantic-ai-harness[youdotcom], python-dotenv, logfire[system-metrics]
  Makefile          # install, smoke, run-* targets
  README.md         # this file
  observability.py  # shared Logfire setup (configure + instrument_pydantic_ai + system metrics)
  deal_desk.py      # flagship multi-agent orchestrator
  starters/
    healthcare_research.py
    education_web_search.py
    finance_research.py
  examples/         # saved full outputs from verified runs (see "Verified outputs")
    education_web_search_output.md
    healthcare_research_output.md
    finance_research_output.md
    deal_desk_output.md
  .logfire/         # local Logfire credentials (gitignored; created by `logfire auth`)
```

## Observability (Pydantic Logfire)

Every script calls `configure_observability('<service-name>')` (in
`observability.py`) before its agent runs, so each run is a trace in Logfire:
the agent run, each model call with token usage and cost, every tool call
(`web_search`, `get_page`, `research`, `finance_research`) with its arguments,
and retries. Pydantic AI emits native OpenTelemetry spans, so the Agents view,
tokens, cost, and tools all populate.

**One-time setup** (creates `.logfire/logfire_credentials.json`):

```bash
uvx logfire --base-url='https://logfire-us.pydantic.dev' auth
uvx logfire --base-url='https://logfire-us.pydantic.dev' projects use --org itsakhil starter-project
uvx logfire --base-url='https://logfire-us.pydantic.dev' whoami   # should print the project URL
```

Then `make run-edu` and open the
[Live view](https://logfire-us.pydantic.dev/itsakhil/starter-project) -- within
seconds you'll see a `cookbook-education` trace. Filter by `service.name` to
isolate one cookbook (`cookbook-healthcare`, `cookbook-education`,
`cookbook-finance`, `cookbook-deal-desk`).

For CI or deployed runs where the credentials file is absent, set
`LOGFIRE_TOKEN` (from the project's Settings > Write tokens) instead -- the SDK
reads it from the environment. `LOGFIRE_BASE_URL` overrides the region (default
US; `https://logfire-eu.pydantic.dev` for EU).

**Content capture is OFF by default.** Timing, token usage, cost, tool names,
and run structure are observed; prompt text and tool arguments are not. Set
`LOGFIRE_INCLUDE_CONTENT=1` to also record message and tool-argument content --
only do this if your prompts contain no sensitive data.

## The harness dependency

The You.com capabilities (`YouSearch`, `YouResearch`, `SubAgents`) ship in the
`youdotcom` extra of [pydantic-ai-harness](https://github.com/pydantic/pydantic-ai-harness)
(v0.25+), which `requirements.txt` pulls from PyPI.
