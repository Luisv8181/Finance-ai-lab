# Six-Month Roadmap

This is a default path, not a syllabus. Change topics when the world gives the group something more interesting.

Assume one meeting every two weeks.

## Meeting 01 — Tokenization becomes infrastructure

**Learn**
- securities settlement;
- custody vs asset representation;
- tokenization;
- collateral mobility.

**Read**
DTCC July 15, 2026 tokenization production update.

**Build**
Define Market Watcher v0 and run the deterministic cross-asset snapshot.

**Question**
What changes when an asset becomes programmable, and what stubbornly remains the same?

---

## Meeting 02 — How markets actually clear and settle

**Learn**
- trade date vs settlement date;
- clearing;
- central counterparties;
- netting;
- settlement risk;
- T+1.

**Build**
Create an evidence/data schema:
- observed market fact;
- derived metric;
- external event;
- source;
- timestamp.

**Blooper theme**
“Faster is always better.”

---

## Meeting 03 — Agent architecture without agent theater

**Learn**
- tools;
- state;
- context;
- retrieval;
- permissions;
- traces;
- human approval;
- why multiple agents can make systems worse.

**Inspect**
OpenAI Agents SDK and LangGraph.

**Build**
Add one evidence-grounded explanation step to a saved market fixture before using live news.

**Question**
What does an agent do here that a normal function cannot?

---

## Meeting 04 — Rates are the price of time

**Learn**
- Treasury curve;
- yield vs price;
- duration;
- real vs nominal rates;
- rate expectations;
- why rates propagate across assets.

**Build**
Add Treasury yields / curve representation to the dashboard.

**Teaching mode**
Have the system explain duration from that day's evidence.

---

## Meeting 05 — Process engineering before AI

**Learn**
Map a real process as:
- trigger;
- inputs;
- transformation;
- decision;
- exception;
- output;
- owner;
- control.

**Read**
A real AI/process-engineering case study.

**Build**
Choose one non-confidential repetitive workflow and create an automation opportunity map before writing code.

**Question**
Where is the actual bottleneck?

---

## Meeting 06 — Money is getting new wrappers

**Learn**
Compare:
- bank deposits;
- central-bank money;
- stablecoins;
- tokenized deposits;
- tokenized money-market funds.

**Build**
Create a concept map showing issuer, claim, settlement asset, redemption path, and major risks.

**Blooper theme**
“Everything on a blockchain is the same kind of money.”

---

## Meeting 07 — Evaluation is the product

**Learn**
- deterministic tests;
- LLM evaluations;
- citation verification;
- hallucination;
- calibration;
- golden datasets;
- regression testing.

**Build**
Create 10 difficult Market Tutor fixtures:
- stale close;
- missing data;
- contradictory news;
- post-hoc headline;
- revised macro data;
- no obvious catalyst.

**Question**
How do we know the agent got better?

---

## Meeting 08 — The economics of AI

**Learn**
- tokens;
- inference;
- context length;
- caching;
- model routing;
- latency;
- cost per successful task;
- human review cost.

**Build**
Instrument one agent workflow for:
- model calls;
- tokens;
- latency;
- success/failure;
- estimated cost.

**Question**
What should become cheaper, and what becomes the new bottleneck?

---

## Meeting 09 — Open source inside finance

**Learn**
- why regulated firms contribute to open source;
- shared standards;
- Common Domain Model;
- supply-chain risk;
- governance.

**Community**
Attend or watch a FINOS event/session.

**Build**
Each member reviews one FINOS project and identifies:
- problem;
- users;
- architecture;
- possible contribution;
- good-first-issue candidate.

---

## Meeting 10 — Market narratives vs evidence

**Learn**
- correlation vs causation;
- event timing;
- reflexivity;
- positioning;
- narrative formation;
- why markets can move without a clean story.

**Build**
Add chronology checks to the explanation agent.

The system should flag an article published after the relevant move instead of treating it as a cause.

---

## Meeting 11 — Turn the prototype into a product

**Learn**
- user;
- job to be done;
- scope;
- UX;
- reliability;
- distribution;
- maintenance burden.

**Build**
Choose a simple interface:
- CLI;
- email-style brief;
- small dashboard;
- Slack/Discord summary.

**Question**
Who is this genuinely useful for besides us?

---

## Meeting 12 — Demo day + retrospective

Each person explains:
1. one finance concept they did not understand six months ago;
2. one AI engineering concept they can now implement;
3. one assumption they changed;
4. one repository contribution they own.

Demo the Market Tutor.

Then decide whether the next six months should emphasize:
- market infrastructure;
- AI/process automation;
- quantitative research;
- product/startup experiments;
- open-source contribution;
- another flagship build.
