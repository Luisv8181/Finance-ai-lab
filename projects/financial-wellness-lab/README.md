# Financial Wellness Lab — Money Pulse

Money Pulse is the Finance AI Lab's first consumer-fintech / financial-wellness experiment.

It is intentionally a **prototype**, not a finished budgeting product.

## What it demonstrates

Instead of presenting a budget as a spreadsheet, the interface treats monthly finances as a system:

- **Essentials** — recurring costs that keep life operating.
- **Lifestyle** — discretionary quality-of-life spending.
- **Future** — savings, investing, debt payoff, and other forward-looking allocations.
- **Breathing room** — unassigned monthly cash after the current plan.

The prototype updates live as assumptions change.

## Features in v0

- Editable monthly take-home income.
- Editable planned savings/investing.
- Editable emergency-fund balance.
- Add and remove monthly expense flows.
- Three-bucket visual money map.
- Circular "Money Pulse" allocation visualization.
- Monthly cash-flow margin.
- Savings/future-building rate.
- Essential-cost load.
- Emergency-runway estimate.
- Deterministic prototype wellness score.
- Deterministic observations/insights.
- Income-shock stress test.
- One-click scenario experiments.
- Browser-local persistence through `localStorage`.

No account connection, financial credentials, external API, or backend is used.

## Run it

The easiest route:

1. Download or clone the repository.
2. Open `projects/financial-wellness-lab/index.html` in a modern browser.

No package installation is required.

## Why this belongs in Finance AI Lab

The lab should not only study institutional financial infrastructure.

Consumer financial wellness raises equally interesting fintech questions:

- How should software represent a person's financial life?
- Which metrics are genuinely useful versus merely familiar?
- How do we help people reason about trade-offs without turning heuristics into false precision?
- How should budgeting handle uncertainty rather than only a static monthly average?
- How should an AI assistant explain a budget without becoming overconfident or prescriptive?
- What information should remain local/private?
- What does a useful "financial wellness" model measure?
- How could transaction classification work?
- What can be automated safely?

## Design principle

> A financial interface should help the user understand structure and sensitivity, not merely record transactions.

## Important limitation

The current wellness score is an intentionally transparent heuristic.

It considers:
- monthly margin;
- future-building rate;
- essential-cost load;
- emergency runway.

It is **not** a validated measure of financial health and should not be presented as one.

A useful future experiment would be to replace a single score with an explainable multidimensional model.

## Potential roadmap

### v1 — Better budgeting model

- irregular/annual expenses;
- pay-period view;
- recurring vs variable classification;
- sinking funds;
- debt balances/APRs;
- goals and timelines;
- household/shared-expense mode;
- cash-flow calendar.

### v2 — Transaction sandbox

Import a local CSV and experiment with:
- categorization;
- merchant normalization;
- recurring-payment detection;
- anomaly detection;
- duplicate detection.

Keep the first version local-first.

### v3 — AI financial explainer

Given structured, user-approved data, let an assistant answer questions such as:

- What changed this month?
- Which recurring costs increased?
- Which expenses are driving the largest change in available cash?
- Which assumptions make the plan fragile?
- What does this financial term mean?

The assistant should distinguish:
- facts;
- calculations;
- heuristics;
- user preferences;
- educational explanations.

### v4 — Scenario engine

Model questions such as:
- What if rent rises?
- What if income drops for two months?
- What if a debt is paid off?
- What if savings increase?
- What changes when two people combine some household costs?

### v5 — Privacy / fintech architecture

Explore:
- local-first storage;
- encrypted data;
- bank-data providers;
- OAuth;
- consent;
- permissions;
- data minimization;
- auditability;
- deletion/export.

## Questions for the group

1. Is "breathing room" a better mental model than "money left over"?
2. Should savings and debt payoff belong in the same future-building bucket?
3. Is one wellness score useful or misleading?
4. What belongs in essentials when different people define necessity differently?
5. Should a future AI explain options or actively suggest actions?
6. Which insights should require a human-defined goal before appearing?
7. How should a budget represent uncertainty?
8. How much financial data should ever leave the user's device?
