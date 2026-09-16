# GitHub Projects to Study

These are reference implementations, not dependencies. The goal is to inspect architecture, identify useful patterns, and decide what we would build differently.

## Financial agents

- https://github.com/yagami24/Financial-Stock-Analysis-Agent
- https://github.com/sai24k/FinanceGPT-AI-Powered-Financial-Research-Assistant-with-Multi-Agent-Architecture
- https://github.com/Deepak-gogula03/Production-Ready-Multi-Agent-Financial-AI-Assistant-using-PhiData-Groq-Llama-3.1
- https://github.com/airamare01/stock-market-garp-agent

## Finance + MCP

- https://github.com/vdalhambra/financekit-mcp
- https://github.com/muskangupta1906/mcp-financial-agent-finbot
- https://github.com/AryaSingh2001/financial-analyst-mcp1

## Research collections

- https://github.com/ohselab/awesome-ai-trading-research
- https://github.com/OctagonAI/octagon-a2a-agents

## Questions to ask when reviewing a repository

1. What data sources does it trust?
2. How does it represent financial observations?
3. Which tasks are deterministic and which are delegated to an LLM?
4. How are sources and timestamps preserved?
5. How does it handle stale or conflicting data?
6. What prevents hallucinated financial claims?
7. What is actually agentic versus ordinary API orchestration?
8. What would we keep, remove, or redesign?
9. Could we reproduce the core idea in one meeting?
10. What can we learn from the project's failures as well as its features?
