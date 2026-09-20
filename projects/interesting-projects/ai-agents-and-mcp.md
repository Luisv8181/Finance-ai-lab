# AI Agents & Model Context Protocol (MCP) Harnesses

These repositories explore how AI agents interact with financial tools, how to enforce guardrails, and how to avoid agent bloat.

---

### 1. Model Context Protocol (MCP) Financial Servers
- **References**:
  - [Model Context Protocol Specification](https://modelcontextprotocol.io/)
  - [financekit-mcp](https://github.com/vdalhambra/financekit-mcp)
  - [financial-datasets-mcp](https://github.com/financial-datasets/mcp-server)
- **What it is**: An open standard developed by Anthropic allowing AI models to interact with local and remote data tools securely.
- **Key Architectural Patterns to Study**:
  - **Standardized Client-Server Boundary**: Models do not need custom Python wrapper libraries for every API; they query standardized MCP tool schemas.
  - **Permission Scoping**: Strict control over what resources an agent can read vs. write.
- **Takeaway for Finance AI Lab**:
  - Build an MCP adapter for `market_watcher` so Claude Code, Cursor, Codex, and Gemini can query our verified snapshots via native MCP tools.

---

### 2. OpenAI Agents SDK (Python)
- **Repository**: [https://github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- **What it is**: Lightweight multi-agent orchestration framework emphasizing tracing, function calling, handoffs, and guardrails.
- **Key Architectural Patterns to Study**:
  - **Handoffs**: Clear delegation between specialized agents (e.g. data retriever -> evidence critic -> explainer).
  - **Tracing & Observability**: Complete visibility into token costs, latency, and prompt payloads.
- **Takeaway for Finance AI Lab**:
  - A clean, inspectable pattern to study when moving from single-agent scripts to multi-role evaluation harnesses.

---

### 3. FinGPT (AI4Finance Foundation)
- **Repository**: [https://github.com/AI4Finance-Foundation/FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)
- **What it is**: Open-source financial LLMs and fine-tuning datasets for sentiment analysis, financial relation extraction, and robo-advising experiments.
- **Key Architectural Patterns to Study**:
  - **Low-Rank Adaptation (LoRA)** on open models (Llama, Gemma).
  - Multi-source financial sentiment data feeds.
- **Critical Caution**:
  - Fine-tuning does not solve numeric hallucination. A fine-tuned model must still be bound to an external deterministic system of record.
