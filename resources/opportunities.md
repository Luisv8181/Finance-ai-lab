# Opportunity Radar

Last manually verified: **September 16, 2026**

This page tracks ways to get closer to the people actually building financial infrastructure and AI systems: conferences, technical communities, contribution programs, training, fellowships, and public learning resources.

Always verify dates, eligibility, and registration status on the official page before making plans.

## Near-term conferences and events

### Sibos 2026 — Miami
**September 28 – October 1, 2026**  
https://www.sibos.com/

Why it matters:
- payments;
- securities;
- FX;
- trade;
- digital assets;
- market infrastructure;
- AI in financial services.

The 2026 theme is **Digital finance for AI-driven economies**.

### FINOS CDM NYC Seminar
**October 8, 2026 — New York City**  
https://www.finos.org/hosted-events

Why it matters:
- Common Domain Model;
- securities-processing lifecycle;
- standards;
- smart contracts / tokenization;
- real industry implementation discussion.

### FINOS webinar — Frontier AI and open-source security
**October 14, 2026 — Virtual**  
https://www.finos.org/hosted-events

Why it matters:
- AI changes software supply-chain risk;
- financial-services security;
- practical governance.

### Money20/20 USA
**October 18–21, 2026 — Las Vegas**  
https://us.money2020.com/

Why it matters:
- fintech;
- payments;
- fraud;
- agentic AI;
- financial services business models;
- broad industry networking.

### Open Source in Finance Forum New York
**November 4–5, 2026 — New York**  
https://www.finos.org/hosted-events/2026-11-05-osff-new-york

Why it matters:
- probably one of the best fits for this lab;
- open-source financial technology;
- developers + financial institutions;
- contribution pathways;
- AI + governance + infrastructure.

### NVIDIA GTC Washington, D.C.
**November 30 – December 3, 2026**  
https://www.nvidia.com/gtc/dc/

Why it matters:
- agentic AI;
- infrastructure;
- open models;
- developer workshops;
- AI policy/economics.

### NVIDIA GTC 2027 — San Jose
**March 2027**  
https://www.nvidia.com/gtc/

Verify the exact dates on the official site before booking; NVIDIA's pages may display different date ranges while scheduling is finalized.

## Contribution pathways

### FINOS community
https://www.finos.org/engage-with-our-community

Individual contribution does not require working for a FINOS member company.

Start with:
- community calendar;
- Slack;
- project landscape;
- good first issues;
- public working groups.

### FINOS AI
https://ai.finos.org/

Particularly relevant to this lab:
- agentic financial services;
- AI governance;
- identity/authorization;
- provenance;
- regulated-industry controls.

### FINOS Open Source Talent Acceleration
https://talent.finos.org/

Useful for:
- internships;
- upskilling;
- newcomer pathways;
- non-developer participation.

### Free course — Open Source Contribution in Finance (LFD137)
https://osr.finos.org/docs/bok/training/lfd137-contribution-in-finance

A short Linux Foundation / FINOS course about contributing safely in financial services.

### FINOS Ambassador Program
https://www.finos.org/ambassador-program

Interesting later-stage path for someone already contributing and wanting to organize, teach, write, or build community.

### Break Through Tech AI Program
https://www.breakthroughtech.org/programs/the-ai-program/

The 2026–27 cohort is currently closed, but the site says applications generally open in December. Track future cohorts if eligible.

### MLH Fellowship
https://fellowship.mlh.io/

Track future software/production-engineering fellowship cohorts and eligibility.

## Open-source places to contribute

- FINOS: https://github.com/finos
- OpenBB: https://github.com/OpenBB-finance/OpenBB
- OpenAI Agents SDK: https://github.com/openai/openai-agents-python
- LangGraph: https://github.com/langchain-ai/langgraph
- Microsoft Qlib: https://github.com/microsoft/qlib
- FinGPT: https://github.com/AI4Finance-Foundation/FinGPT

## YouTube / video learning

### Finance and markets

**Patrick Boyle**  
https://www.youtube.com/@PBoyle

Good for: market structure, macro/finance stories, derivatives context, skepticism about financial narratives.

**Aswath Damodaran**  
https://www.youtube.com/@AswathDamodaranonValuation

Good for: valuation, corporate finance, thinking explicitly about assumptions.

**MIT OpenCourseWare — Finance**
https://www.youtube.com/@mitocw

Good for: structured foundations rather than market commentary.

### AI / engineering

**Andrej Karpathy**  
https://www.youtube.com/@AndrejKarpathy

Good for: how language models actually work, implementation intuition, building from first principles.

**DeepLearning.AI**  
https://www.youtube.com/@Deeplearningai

Good for: practical AI systems, agents, model/tool patterns, interviews with researchers/builders.

**AI Engineer / Latent Space ecosystem**  
https://www.youtube.com/@aiDotEngineer

Good for: production agent systems, developer tooling, evaluations, inference, and emerging engineering practices.

### Open source + financial technology

**FINOS**
https://www.youtube.com/@FINOSFoundation

Good for: talks from engineers and institutions working on open-source financial infrastructure.

**NVIDIA**
https://www.youtube.com/@NVIDIA

Good for: infrastructure, inference, model serving, agentic systems, conference talks.

## How to use this page

Do not try to attend everything.

At each biweekly meeting choose at most:
- one event worth tracking;
- one contribution pathway;
- one talk/video;
- one action.

Examples:
- attend a free FINOS community call;
- find a FINOS good-first-issue;
- watch one OSFF talk and summarize it;
- apply to one program;
- message one speaker with a specific technical question;
- clone one open-source repo and understand one subsystem.

## Scanner

The repository includes a lightweight opportunity scanner in `scripts/opportunity_scanner.py` and a scheduled GitHub Action.

It does not “understand” opportunities like an LLM. It checks a curated set of public official pages, extracts likely relevant links, and writes a review queue to `resources/opportunities-auto.md`.

A human should review the output before treating anything as a real opportunity.
