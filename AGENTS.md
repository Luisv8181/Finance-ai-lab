# AGENTS.md

This file is the standing instruction set for AI coding agents working in **Finance AI Lab**.

## Mission

Help the team learn financial markets, financial infrastructure, AI engineering, process engineering, and software delivery by building transparent educational tools.

## Read first

Before making changes, read:

1. `README.md`
2. `CONTRIBUTING.md`
3. the relevant issue
4. the relevant project README
5. the most recent meeting note if the issue came from a meeting

## Non-negotiables

- This repository is for learning and research, not automated trading.
- Do not add broker execution, leverage, autonomous portfolio management, or personalized buy/sell recommendations.
- Never invent market prices, returns, dates, citations, article titles, or source content.
- Keep **observed data**, **derived metrics**, and **interpretation** distinct.
- A market explanation is a hypothesis unless the causal evidence is unusually strong.
- Preserve source URLs and timestamps for current information.
- Never commit passwords, API keys, tokens, private account information, proprietary employer data, or confidential work material.
- Prefer simple, inspectable code over impressive-looking agent complexity.

## Agent workflow

When assigned an issue:

1. Restate the objective and identify assumptions.
2. Inspect the existing repo before creating new abstractions.
3. Create a branch unless the human explicitly tells you not to.
4. Make the smallest coherent change that resolves the issue.
5. Add tests for calculation or transformation logic.
6. Run available tests and linters.
7. Open a pull request with:
   - problem;
   - approach;
   - files changed;
   - assumptions;
   - test evidence;
   - limitations;
   - suggested next step.
8. Do not merge your own PR unless a human explicitly authorizes it.

## Data rules

Every current market datum should eventually be traceable to:
- instrument / identifier;
- value;
- units;
- observation timestamp;
- retrieval timestamp;
- source.

Every retrieved event/article should eventually retain:
- title;
- publisher/institution;
- publication timestamp;
- URL;
- retrieval timestamp.

LLMs are never the system of record for numeric market data.

## AI rules

If adding an LLM:
- follow the Bring Your Own Key (BYOK) protocol in `docs/BYOK_GUIDE.md`;
- never hardcode, print, or commit API keys;
- always support graceful fallback to deterministic outputs when no key is set;
- show which evidence was supplied to the model (EvidenceBundle);
- require citations or structured source IDs in outputs;
- make uncertainty explicit;
- evaluate chronology: headlines must precede market moves to be considered causal candidates;
- create evaluation cases before adding more agents;
- do not allow the model to silently rely on remembered current-market facts.

## Definition of done

A change is done when another member can:
- understand why it exists;
- run or verify it;
- identify its sources;
- see its limitations;
- change it without depending on the original author or their AI agent.
