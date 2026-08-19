"""Shared Pydantic Logfire setup for the cookbooks.

Each cookbook script calls `configure_observability('<service-name>')` right
after loading `.env`, before it builds its agent. That wires:

- `logfire.configure()` -- connects to the Logfire project. For local dev it
  reads `.logfire/logfire_credentials.json` automatically (created by
  `uvx logfire ... auth` + `projects use`). For CI or deployed runs, set
  `LOGFIRE_TOKEN` instead.
- `logfire.instrument_pydantic_ai()` -- Pydantic AI emits native OpenTelemetry
  spans, so this records every agent run, model call, tool call, and retry as a
  trace in Logfire (Agents view, tokens, cost, tools).
- `logfire.instrument_system_metrics()` -- CPU/memory/disk/process metrics.

Content capture (prompt and tool-argument text) is OFF by default. Timing,
token usage, cost, tool names, and run structure are still observed. Set
`LOGFIRE_INCLUDE_CONTENT=1` to also capture message and tool-argument content
(only do this if your prompts contain no sensitive data).

This never fails when credentials are missing: `send_to_logfire='if-token-present'`
makes Logfire fall back to local console output, so imports and tests stay green
on a machine that has not run `logfire auth`.
"""

from __future__ import annotations

import os

import logfire

# US Logfire region. Override with LOGFIRE_BASE_URL for the EU region
# (https://logfire-eu.pydantic.dev) or a self-hosted endpoint.
LOGFIRE_BASE_URL = os.environ.get('LOGFIRE_BASE_URL', 'https://logfire-us.pydantic.dev')

# Instrumentation must run exactly once per process (the Pydantic AI guide
# warns against re-instrumenting). Each cookbook script is its own process in
# real use, but tests and `make smoke` import several in one process, so guard.
_instrumented = False


def configure_observability(service_name: str) -> None:
    """Configure Logfire tracing for one cookbook service.

    Args:
        service_name: Short, stable name for this script's traces in Logfire
            (e.g. `'cookbook-healthcare'`), so runs are filterable in the Live view.
    """
    global _instrumented  # noqa: PLW0603
    logfire.configure(
        service_name=service_name,
        send_to_logfire='if-token-present',
        advanced=logfire.AdvancedOptions(base_url=LOGFIRE_BASE_URL),
    )
    if _instrumented:
        return
    logfire.instrument_pydantic_ai(include_content=os.environ.get('LOGFIRE_INCLUDE_CONTENT') == '1')
    logfire.instrument_system_metrics()
    _instrumented = True
