# Market Watcher / Market Tutor

## Product idea

Build an agent that watches a compact cross-asset dashboard and teaches the group what changed, what may explain it, and what remains uncertain.

Core principle:

> **Data first, interpretation second, narrative last.**

## v0 — deterministic market snapshot

Start without an LLM.

The first version should:
- retrieve daily history for a small teaching watchlist;
- calculate 1-day, 5-day, and 20-day returns;
- calculate simple 20-day and 50-day moving averages;
- preserve the timestamp of the latest observation;
- render a Markdown snapshot.

Why no LLM first?

Because we cannot evaluate an explanation agent until we have a reliable evidence layer.

## v1 — evidence layer

Add:
- macro calendar/economic releases;
- trustworthy financial news;
- source URLs;
- publication/retrieval timestamps;
- duplicate-event handling;
- stale-data warnings.

## v2 — teaching agent

Given only a structured evidence bundle, produce:

1. **What happened** — observed market movements.
2. **What may matter** — sourced events and plausible relationships.
3. **What is uncertain** — competing explanations / missing evidence.
4. **Concept of the run** — duration, breadth, volatility, liquidity, etc.
5. **Questions to investigate**.

External factual claims should retain source links.

## v3 — research memory

Track:
- previous hypotheses;
- whether expected relationships held;
- group mistakes;
- recurring questions;
- changing correlations/regimes.

The goal is not predicting tomorrow's return. The goal is improving reasoning.

## Suggested initial watchlist

- SPY
- QQQ
- IWM
- TLT
- GLD
- BTC-USD
- ^VIX

This is a teaching basket, not a recommended portfolio.

## Evaluation

Score the system on:
- factual correctness;
- timestamp correctness;
- source quality;
- separation of fact and hypothesis;
- uncertainty calibration;
- teaching quality;
- stale/missing-data detection;
- reproducibility of calculations.

Do not score it on whether it predicts the next day's market direction.

## Non-goals

- autonomous trading;
- brokerage integration;
- personalized investment recommendations;
- buy/sell scoring;
- claiming causality from coincident news and price action.
