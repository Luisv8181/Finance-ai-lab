# Finance AI Lab

A biweekly learning-and-building lab for three friends exploring **financial technology, markets, AI, process engineering, and emerging financial infrastructure**.

The lab is part discussion group, part research notebook, and part tiny engineering team.

## Start here

**For tonight — September 16, 2026**
- [Kickoff agenda](meetings/2026-09-16-kickoff.md)
- [Orientation and recurring meeting format](docs/orientation.md)
- [Reading queue](docs/reading-queue.md)
- [Market Watcher project](projects/market-watcher/README.md)

**For each person's AI coding agent**
- [AI agent + GitHub onboarding](docs/AI_AGENT_ONBOARDING.md)
- [Standing instructions for agents](AGENTS.md)
- [Contribution workflow](CONTRIBUTING.md)

**For getting deeper into the space**
- [Conferences, pathways, communities, and videos](resources/opportunities.md)
- [Automatically refreshed opportunity review queue](resources/opportunities-auto.md)
- [GitHub projects worth studying](references/github-projects.md)

## Mission

Learn how modern finance and AI systems actually work by discussing primary sources and building small, inspectable software together.

Every two weeks:

1. Share meaningful life, career, and business updates.
2. Build a compact market mental model.
3. Discuss one strong reading.
4. Examine one failed assumption or “blooper.”
5. Build or improve one artifact.
6. Capture decisions, questions, and next actions in GitHub.

## Flagship project: Market Watcher / Market Tutor

A learning-first market intelligence system that eventually should answer:

- What moved?
- How do we know?
- What might explain it?
- Which explanations are weak?
- What financial concept does this illustrate?
- What should we investigate next?
- What is the system uncertain about?

The design rule is:

> **Data first, interpretation second, narrative last.**

This is an educational/research project, not an investment-advice or automated-trading system.

See:
- [Project brief](projects/market-watcher/README.md)
- [Architecture](projects/market-watcher/ARCHITECTURE.md)

## Current v0

The initial Python prototype builds a deterministic cross-asset snapshot before any LLM is added.

Default teaching basket:
- SPY
- QQQ
- IWM
- TLT
- GLD
- BTC-USD
- ^VIX

It calculates:
- latest close;
- 1-day return;
- 5-day return;
- 20-day return;
- 20-day moving average;
- 50-day moving average;
- latest observation timestamp.

### Run it

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate

pip install -e ".[dev]"
market-watcher
pytest
```

The v0 prototype uses Yahoo Finance through `yfinance` for learning/prototyping. That is not a production-grade or guaranteed real-time institutional market-data source.

## Opportunity Radar

The repository has two opportunity pages:

- `resources/opportunities.md` — human-curated, manually verified resources.
- `resources/opportunities-auto.md` — a machine-generated review queue.

A scheduled GitHub Action runs every Monday and scans a curated group of official pages for likely conferences, programs, contribution pathways, and events.

The scanner is intentionally simple. It discovers candidates; humans verify them.

## Repository map

```text
Finance-ai-lab/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── docs/
│   ├── AI_AGENT_ONBOARDING.md
│   ├── orientation.md
│   └── reading-queue.md
├── meetings/
│   ├── TEMPLATE.md
│   └── 2026-09-16-kickoff.md
├── projects/
│   └── market-watcher/
│       ├── README.md
│       └── ARCHITECTURE.md
├── resources/
│   ├── opportunities.md
│   ├── opportunities-auto.md
│   └── opportunity_sources.json
├── references/
│   └── github-projects.md
├── scripts/
│   └── opportunity_scanner.py
├── src/
│   └── market_watcher/
├── tests/
└── .github/
    ├── pull_request_template.md
    ├── ISSUE_TEMPLATE/
    └── workflows/
        └── opportunity-radar.yml
```

## Working agreements

- Treat claims as hypotheses until supported by data or a strong source.
- Keep observed market facts separate from model interpretations.
- Record source URLs and timestamps for current external information.
- Prefer reproducible experiments over long debates.
- Use issues for questions/tasks, branches for non-trivial work, and PRs for review.
- Coding agents can write code; humans own what gets merged.
- Never put API keys, credentials, private financial information, or confidential employer material in this repository.

## Six-month north-star question

> What can the three of us understand, explain, or build in six months that none of us could do today?
