# GitHub Projects Worth Studying

These are references, not dependencies. The point is to inspect architecture, identify useful patterns, and decide deliberately what belongs in this lab.

## Strong primary references

### OpenBB
https://github.com/OpenBB-finance/OpenBB

Study:
- financial-data provider abstractions;
- standardized data access;
- research workspace architecture;
- how agents/tools can interact with financial data.

### Microsoft Qlib
https://github.com/microsoft/qlib

Study:
- reproducible quantitative workflows;
- experiment/data/model separation;
- evaluation organization.

Important: Qlib is designed for quantitative-investment research. Borrow engineering patterns without silently turning our educational Market Tutor into a trading project.

### FinGPT
https://github.com/AI4Finance-Foundation/FinGPT

Study:
- finance-specific NLP tasks;
- financial datasets;
- evaluation ideas;
- what model specialization can and cannot solve.

A finance-tuned model does not solve current-data provenance by itself.

## Agent frameworks

### OpenAI Agents SDK — Python
https://github.com/openai/openai-agents-python

Study:
- tools;
- handoffs;
- tracing;
- guardrail patterns.

### LangGraph
https://github.com/langchain-ai/langgraph

Study:
- explicit stateful workflows;
- retries and branching;
- human approval points.

### CrewAI
https://github.com/crewAIInc/crewAI

Study:
- role/task orchestration;
- the benefits and overhead of multi-agent patterns.

### CAMEL
https://github.com/camel-ai/camel

Study:
- multi-agent research and coordination.

## Financial open-source ecosystem

### FINOS
https://github.com/finos

Use FINOS to discover:
- real financial-industry open-source projects;
- standards;
- Common Domain Model work;
- AI/governance initiatives;
- good-first-issue contribution pathways.

Community:
https://www.finos.org/engage-with-our-community

## Community financial-agent examples

These can be useful for architecture critique. Treat them as examples to inspect, not as trusted templates.

- https://github.com/yagami24/Financial-Stock-Analysis-Agent
- https://github.com/sai24k/FinanceGPT-AI-Powered-Financial-Research-Assistant-with-Multi-Agent-Architecture
- https://github.com/Deepak-gogula03/Production-Ready-Multi-Agent-Financial-AI-Assistant-using-PhiData-Groq-Llama-3.1
- https://github.com/airamare01/stock-market-garp-agent
- https://github.com/vdalhambra/financekit-mcp
- https://github.com/muskangupta1906/mcp-financial-agent-finbot

## Repository review questions

For every project, ask:

1. What data sources does it trust?
2. How are observations represented?
3. Which tasks are deterministic?
4. Which tasks are delegated to an LLM?
5. Are source URLs and timestamps preserved?
6. How does it handle stale/conflicting data?
7. What prevents hallucinated financial claims?
8. What is truly agentic versus ordinary API orchestration?
9. What are the security/permission boundaries?
10. How would we evaluate the system?
11. What could we reproduce in one meeting?
12. What would we explicitly *not* copy?

## Framework rule

Before adding a framework, answer:

- What exact problem does it solve that plain Python does not?
- Can we trace the inputs and tool calls?
- Can we test the behavior?
- What happens on partial failure?
- How are permissions constrained?
- What happens to cost and latency as agents multiply?
- Can a new member understand it in one sitting?

Default: **earn complexity**.
