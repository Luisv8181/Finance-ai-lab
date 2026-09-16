# Market Observatory Architecture

## Product principle

The Observatory is a learning system first and an automation system second.

It should distinguish three layers:

1. **Observation** - deterministic data retrieved from a named source.
2. **Interpretation** - model-generated explanation grounded in retrieved evidence.
3. **Learning** - concepts, questions, and follow-up research generated from the observation.

## Initial flow

```text
Market/API data ──┐
                  ├──> Normalizer ──> Observation Store
News/documents ───┘                         |
                                           v
                                  Event / Move Detector
                                           |
                         ┌─────────────────┴─────────────────┐
                         v                                   v
                 Evidence Retrieval                   Market Analytics
                         |                                   |
                         └─────────────────┬─────────────────┘
                                           v
                                    Explanation Agent
                                           |
                              ┌────────────┼────────────┐
                              v            v            v
                           Summary      Evidence     Questions
                              |            |            |
                              └────────────┴────────────┘
                                           v
                                      Human Review
                                           |
                                           v
                                      GitHub Notes
```

## Design rules

- Every observation gets a timestamp and source.
- Market data should be handled deterministically where possible.
- The LLM should not invent prices, events, sources, or causal explanations.
- Causal language should distinguish correlation, plausible explanation, and verified event.
- The agent should expose uncertainty rather than hide it.
- No automated trading or portfolio actions in the initial project.

## Suggested first watchlist

Start small. Example categories rather than a permanent list:

- Broad U.S. equity index
- Technology-heavy equity index
- 2-year Treasury yield
- 10-year Treasury yield
- U.S. dollar index
- Crude oil
- Gold
- Bitcoin

The group should choose the actual instruments and document why.

## Future capabilities

- SEC filing retrieval
- Earnings/event detection
- Macro calendar
- Sector comparison
- Yield-curve visualization
- Financial concept tutor
- Historical event replay
- Agent evaluation suite
- MCP-based tool access
- Multi-agent research experiments
