# Open Finance Terminal Architecture

## System boundary

The terminal is an orchestration layer around deterministic data and analysis systems.

Sources
  |
  +-- Market adapters
  +-- Macro adapters
  +-- Filing adapters
  +-- News/event adapters
          |
          v
   Normalize + Validate
          |
          v
   Canonical Evidence Store
          |
     +----+----+
     |         |
     v         v
 Analytics  Retrieval
     |         |
     +----+----+
          |
          v
   Evidence Bundle
          |
          v
   AI Research Agent
          |
     +----+----+
     |         |
     v         v
 citations  uncertainty
          |
          v
      Terminal UI

## Canonical evidence object

Every source observation should retain:

- source/provider;
- source URL or stable identifier;
- subject/entity;
- field;
- value;
- units/currency;
- observation timestamp;
- publication timestamp where relevant;
- retrieval timestamp;
- freshness status;
- transformation history;
- license/usage metadata where relevant.

## AI permissions

The model should not freely invent data access.

Tool permissions should be explicit:

- quote lookup;
- historical series;
- macro series;
- filing retrieval;
- news retrieval;
- deterministic calculations;
- Python/SQL analysis;
- citation lookup.

A tool call should be logged.

## Chronology protection

For causal-looking prompts such as "why did X move?":

1. establish the market observation timestamp;
2. retrieve candidate events;
3. compare event publication time with the move;
4. reject post-hoc articles as causal evidence;
5. distinguish observed fact from hypothesis.

## Evaluation

Create fixtures for:

- stale data;
- missing data;
- duplicate events;
- contradictory sources;
- revisions;
- post-hoc explanations;
- simultaneous macro events;
- incorrect ticker/entity resolution.

Track:

- factual correctness;
- source correctness;
- chronology correctness;
- calculation reproducibility;
- uncertainty calibration;
- response latency;
- tool-call efficiency.

## Relationship to OpenBB

Study OpenBB as an integration and data-platform reference, not as something to copy wholesale.

Useful concepts to investigate:

- provider abstraction;
- Python/REST/CLI/MCP surfaces;
- custom agents;
- citations;
- dashboard widgets;
- app configuration.

## Security

Never commit:

- API keys;
- tokens;
- credentials;
- private financial data;
- confidential employer data.

Keep provider credentials in environment variables or local secret stores.
