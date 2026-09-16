# Market Watcher Architecture

## Principle

The LLM is never the system of record for a market number.

```text
Market Data Sources
        |
        v
Normalize + Validate
        |
        v
Derived Metrics
        |
        +--------------------+
        |                    |
        v                    v
News / Macro Retrieval   Raw Evidence Log
        |                    |
        +---------+----------+
                  |
                  v
            Evidence Bundle
                  |
                  v
        Explanation / Tutor
                  |
                  v
        Brief + Citations +
           Uncertainty
```

## Data contracts

Observed market datum:
- identifier;
- value;
- units;
- observation timestamp;
- retrieval timestamp;
- source;
- adjusted/unadjusted status where relevant.

External event:
- title;
- institution/publisher;
- publication timestamp;
- URL;
- retrieval timestamp;
- relevant structured facts.

## Why not multi-agent first?

Multi-agent systems can look sophisticated while making provenance, cost, and debugging worse.

Start with:
- one deterministic evidence pipeline;
- one explanation step;
- explicit evaluation fixtures.

Split roles only when a measurable bottleneck appears.

Potential later roles:
- source retriever;
- evidence critic;
- explainer;
- concept tutor;
- citation verifier.

## Evaluation fixtures

Create saved cases for:
- missing data;
- market holiday / stale close;
- contradictory headlines;
- large move with no obvious news;
- multiple simultaneous macro events;
- article published after the price movement;
- revised economic data.

The system should preserve chronology and admit uncertainty.
