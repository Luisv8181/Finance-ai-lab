# Open Finance Terminal / AI Terminal

An open-source, AI-native financial terminal for learning, research, and experimentation.

This project is inspired by the workflow class of institutional terminals, not a clone of any proprietary terminal or data product. It uses open/public data where possible and provider adapters for optional licensed data.

## Why this exists

The Finance AI Lab already has Market Watcher, which focuses on teaching from a deterministic cross-asset evidence bundle. Open Finance Terminal expands that idea into a terminal-style research environment:

- market data
- macroeconomic data
- filings and company research
- news/events
- charts and tables
- source provenance
- AI-assisted research
- reproducible analysis
- optional local-model operation

Core principle:

> Data first, interpretation second, narrative last.

## Proposed architecture

Sources -> adapters -> normalize/validate -> evidence store -> analytics/retrieval -> AI research agent -> terminal UI

## Data strategy

Use public/open sources for the learning baseline. Candidate sources include:

- SEC EDGAR APIs for company facts and filings.
- FRED / ALFRED for macroeconomic time series.
- OpenBB ODP as an optional normalization/integration layer.
- Optional market-data providers through explicit adapters.

SEC documents and FRED data should remain source-linked and timestamped. Commercial or licensed feeds must be used according to their terms.

## AI design

The AI layer should never be the system of record for numbers.

Every material answer should be able to expose:

1. claim;
2. source;
3. observation/publication timestamp;
4. transformation or calculation;
5. model interpretation;
6. uncertainty.

Example commands:

- /quote NVDA
- /deep NVDA
- /compare NVDA AMD AVGO
- /macro inflation
- /filings MSFT
- /why SPY moved
- /chart QQQ 1y

## Local-first mode

A later milestone should support local models through Ollama or another compatible runtime.

## Relationship to Market Watcher

Market Watcher = evidence-grounded teaching engine.

Open Finance Terminal = terminal-style research environment.

Market Watcher can become the first reliable analytical module inside the terminal rather than being discarded.

## Non-goals

- autonomous trading;
- brokerage execution;
- buy/sell recommendations;
- copying proprietary Bloomberg/Reuters datasets;
- pretending coincident news caused a market move;
- opaque AI answers without evidence.

## MVP sequence

1. Terminal shell + command router.
2. Deterministic quote/search commands.
3. SEC and FRED source adapters.
4. Evidence/provenance schema.
5. Charts/tables.
6. AI research agent over structured evidence.
7. Citation verifier.
8. Local-model adapter.
9. Saved research workspaces.
10. MCP/tool interface.

## External references

OpenBB's Open Data Platform is useful to study because it exposes financial data across Python, REST, CLI, and MCP surfaces and is designed for analysts, quants, and AI agents.

OpenBB custom-agent examples are also useful references for building cited, tool-using financial agents.
