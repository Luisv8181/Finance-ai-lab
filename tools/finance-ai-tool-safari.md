# Finance AI Tool Safari

Purpose: install a small set of real finance/AI tools and learn by running the same research questions through different architectures.

This is a learning lab, not a recommendation to use any tool for investment decisions.

## The five tools to explore

| Tool | What it teaches | Start here | Local install |
|---|---|---|---|
| OpenBB | Financial data platform, terminal workflows, AI/MCP integration | https://github.com/OpenBB-finance/OpenBB | `pip install openbb` |
| Microsoft Qlib | AI-oriented quantitative research, data, modeling, backtesting | https://github.com/microsoft/qlib | `pip install pyqlib` |
| FinRL | Financial reinforcement learning and the boundary between research and trading agents | https://github.com/AI4Finance-Foundation/FinRL | clone repo; follow environment setup |
| QuantConnect LEAN | Event-driven research/backtesting engine and algorithm lifecycle | https://github.com/QuantConnect/Lean | `pip install lean` |
| FINOS AI Governance MCP Server | Governance, controls, and machine-readable AI policy interfaces | https://github.com/finos/aigf-mcp-server | clone repo; use its documented venv setup |

### Priority order

1. OpenBB — directly relevant to the Open Finance Terminal.
2. FINOS AIGF MCP — directly relevant to trustworthy agent/tool boundaries.
3. Qlib — understand AI-native quant research.
4. LEAN — understand what happens when research becomes executable strategy logic.
5. FinRL — understand reinforcement-learning approaches without confusing a research framework with a reliable trading system.

OpenBB currently positions its platform as an open data platform for analysts, quants, and AI agents, while FINOS is developing open governance and agentic financial-services specifications. Qlib covers an end-to-end quantitative research pipeline, and LEAN provides an event-driven open-source algorithmic trading engine. FinRL's original repository is explicitly positioned as an educational/research framework, with FinRL-X as its newer production-oriented direction. These distinctions are useful to preserve in our lab notes.

## First experiment: one question, five architectures

Use the same question where each tool supports it:

> Compare SPY and QQQ over the last 20 trading days. What changed, what evidence supports the explanation, and what would invalidate the explanation?

Record:

- data source;
- timestamp;
- transformation/calculation;
- model/algorithm used;
- citations/evidence;
- assumptions;
- failure modes;
- what the tool does automatically;
- what still requires human verification.

Do not compare outputs by "which answer sounds smartest." Compare the underlying evidence path.

## Experiments

### Experiment A — Data terminal

OpenBB:
- retrieve a quote;
- retrieve historical data;
- inspect available news/economic data;
- expose the result through a CLI or API;
- identify exactly where timestamps and provider metadata appear.

Lesson: a terminal is a data and workflow system before it is an AI interface.

### Experiment B — AI quant research

Qlib:
- load a supported dataset;
- run one baseline model;
- inspect feature construction;
- run a simple backtest;
- identify where leakage, survivorship bias, or overfitting could enter.

Lesson: "AI found a signal" is not the same thing as "the signal is valid."

### Experiment C — Execution architecture

LEAN:
- create a tiny local project;
- run a deterministic strategy;
- inspect orders, fills, portfolio state, and results;
- compare the research code with the execution lifecycle.

Lesson: once software can act, permissions, state, timing, and auditability become first-class concerns.

### Experiment D — Agent governance

FINOS AIGF MCP:
- inspect the governance framework exposed through MCP;
- map policy -> tool permission -> runtime observation;
- identify what an AI finance agent should be allowed to read, calculate, write, or execute.

Lesson: governance can become software infrastructure rather than a PDF reviewed after the fact.

### Experiment E — Reinforcement learning

FinRL:
- reproduce one educational example;
- inspect the environment, reward function, state, and action space;
- identify where the simulated environment differs from real markets.

Lesson: an agent optimizing a reward function is not automatically learning the thing humans actually care about.

## What I want us to notice

### 1. AI is not the whole stack

The interesting architecture is:

source data -> normalization -> evidence -> tools -> analysis -> agent -> human decision/action

If the evidence layer is weak, a stronger model does not fix the underlying problem.

### 2. The tool boundary becomes part of the model

An AI that can only read data is fundamentally different from one that can calculate, write files, place orders, alter portfolios, or call external systems.

For every tool, ask:

- What can the agent see?
- What can it calculate?
- What can it change?
- What can it execute?
- What gets logged?
- What requires human approval?

### 3. Chronology matters

For market explanations, publication time must be separated from event time and retrieval time. A news article published after a price move cannot be treated as evidence that caused the move.

### 4. "Agentic" should mean more than chat

An agent should have a bounded workflow, explicit tools, observable intermediate steps, and a defined failure state.

### 5. Backtests are experiments, not proof

A backtest can demonstrate behavior under a specified historical dataset and simulator. It does not establish future performance.

### 6. Open source does not mean open data

The software can be open source while its data providers, exchange feeds, or proprietary datasets remain licensed. Do not commit restricted datasets or API credentials to this repository.

## Suggested lab folder

As we test each tool, create:

`experiments/<tool-name>/README.md`

Each README should contain:

1. Goal
2. Installation
3. Minimal example
4. Input data
5. Output
6. Evidence/provenance
7. Failure modes
8. What we learned
9. What we would steal for Open Finance Terminal
10. What we would explicitly avoid

## Safety / research boundary

No brokerage credentials, private financial information, employer data, or production trading connections belong in these experiments.

Keep live execution disabled unless the group explicitly creates a separate, reviewed experiment with clear controls.

## Why these tools belong together

They cover different layers rather than competing for the same job:

OpenBB = data/research interface

Qlib = quantitative AI research

FinRL = reinforcement-learning research

LEAN = algorithm lifecycle/execution engine

FINOS AIGF = governance/control layer

That gives the Finance AI Lab a useful miniature map of the financial AI stack.
