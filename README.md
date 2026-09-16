# Finance AI Lab

A collaborative learning and building lab for three friends exploring financial technology, AI, markets, process engineering, and emerging financial infrastructure.

## Mission

Learn the financial system by building small, working software together.

Every two weeks we aim to:

1. Discuss life, work, business, and ideas.
2. Read and debate one high-quality article, paper, primary source, or GitHub project.
3. Build or improve one small piece of the shared project.
4. Capture what we learned in GitHub.

## First Project: Market Observatory

A learning-first market intelligence agent that watches selected markets and explains:

- What moved
- Why it may have moved
- Which data supports the explanation
- What macro, company, or infrastructure events matter
- What we should learn more about
- What the agent is uncertain about

This is an educational/research project, not an investment-advice system.

## Architecture

```text
Data Sources
  |-- market prices / volume
  |-- SEC filings / company data
  |-- macroeconomic data
  |-- trusted news / RSS
  |-- financial infrastructure research
        |
        v
Ingestion Layer
        |
        v
Normalized Events + Time Series
        |
        +----> Market Analytics
        |
        +----> News / Document Retrieval
        |
        +----> Agent Tools
                    |
                    v
              Market Observer
                    |
          +---------+---------+
          |                   |
          v                   v
     Daily Brief        Learning Mode
          |                   |
          +---------+---------+
                    v
              Human Review
                    |
                    v
                 GitHub
```

## Repository Structure

```text
Finance-ai-lab/
├── README.md
├── docs/
│   ├── meeting-notes/
│   ├── reading-notes/
│   ├── architecture/
│   └── concepts/
├── agent/
│   ├── prompts/
│   ├── tools/
│   └── workflows/
├── data/
│   ├── schemas/
│   └── samples/
├── analytics/
├── app/
├── tests/
├── experiments/
├── references/
│   └── github-projects.md
└── .github/
    └── ISSUE_TEMPLATE/
```

## Working Agreements

- Treat claims as hypotheses until supported by data or a primary source.
- Keep market facts separate from model-generated interpretations.
- Record source URLs and timestamps for external information.
- Prefer reproducible experiments over long debates.
- Use issues for questions and ideas, branches for experiments, and pull requests for changes worth reviewing.
- Never put API keys, credentials, account information, or confidential employer information in this repository.

## Meeting Rhythm

### Meeting A: Learn

- Life/work updates
- One reading
- 20-minute discussion
- One concept translated into plain English
- Choose the next engineering question

### Meeting B: Build

- Life/work updates
- Demo the current prototype
- Review one pull request
- Identify one failure or unknown
- Choose the next experiment

Then repeat.

## Initial Research Themes

- AI agents and agent harnesses
- Financial data infrastructure
- Market structure
- Tokenization and digital assets
- Payments and settlement
- Process engineering and automation
- AI economics and compute markets
- Risk, governance, and model reliability
- The changing role of software in financial institutions

## First Milestones

### Milestone 1: Market Dashboard

Display a small watchlist, prices, percentage moves, volume, and a timestamped data source.

### Milestone 2: Event Explainer

When a meaningful move occurs, retrieve relevant recent information and produce an evidence-backed explanation with explicit uncertainty.

### Milestone 3: Learning Mode

The agent explains financial concepts encountered in the data: yield curves, duration, market capitalization, volatility, liquidity, settlement, etc.

### Milestone 4: Research Notebook

Automatically save daily observations, questions, sources, and lessons learned into structured Markdown.

### Milestone 5: Agent Evaluation

Create a small test set for factual accuracy, source attribution, reasoning quality, and avoidance of unsupported conclusions.
