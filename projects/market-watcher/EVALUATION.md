# Market Watcher Evaluation

The Market Watcher should be evaluated as a research assistant and teacher, not as a predictor.

## Evaluation ladder

### Level 1 — Data integrity

- instrument identifier is correct;
- numeric values are correct;
- units are correct;
- timestamp is present;
- retrieval time is present;
- source is recorded.

### Level 2 — Derived calculations

- 1-day return is reproducible;
- 5-day return is reproducible;
- 20-day return is reproducible;
- moving averages are reproducible;
- missing/stale data is flagged.

### Level 3 — Evidence grounding

Given a fixed evidence bundle, the agent should:

- identify supported facts;
- avoid unsupported facts;
- preserve publication chronology;
- distinguish evidence from hypothesis;
- cite the supplied sources.

### Level 4 — Teaching quality

The agent should:

- explain one financial concept clearly;
- connect the concept to the observed data;
- identify what is uncertain;
- suggest a useful next question.

## Test case format

```yaml
id: example-001
question: "Why did the assets move differently?"
observations:
  - instrument: SPY
    return_1d: 0.012
sources:
  - source_id: source-001
    published_at: "2026-01-01T14:00:00Z"
    facts:
      - "Example factual event"
expected:
  must_include:
    - observed return
  must_distinguish:
    - fact
    - hypothesis
  must_not_claim:
    - unsupported causality
```

## Failure categories

- fabricated number;
- fabricated source;
- wrong timestamp;
- chronology error;
- unsupported causal claim;
- omitted uncertainty;
- overconfident teaching;
- stale-data failure;
- calculation mismatch.

## Evaluation philosophy

A fluent answer is not automatically a good answer.

When the system cannot establish a reliable explanation, the correct behavior may be:

> "We can verify that X happened. We have evidence for Y. We do not have enough evidence to conclude that Y caused X."

That behavior should be considered a feature, not a failure.
