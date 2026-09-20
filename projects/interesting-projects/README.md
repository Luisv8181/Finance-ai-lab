# Interesting Projects & Ecosystem Radar

This directory tracks external open-source projects, institutional prototypes, and agent harnesses worth studying for **Finance AI Lab**.

These are references to inspect for architectural patterns, data contracts, and design ideas—not blind dependencies.

---

## 🧭 Project Categories

| Category | Description | Primary Dossier |
|---|---|---|
| **Market Infrastructure & Data** | Open-source market terminals, data abstraction layers, and institutional standards. | [market-infrastructure.md](market-infrastructure.md) |
| **AI Agents & MCP Harnesses** | Model Context Protocol (MCP) servers, multi-agent frameworks, and financial research agents. | [ai-agents-and-mcp.md](ai-agents-and-mcp.md) |
| **Personal FinTech & Local-First** | Privacy-focused personal budgeting engines, local transaction parsers, and double-entry systems. | [personal-fintech-and-privacy.md](personal-fintech-and-privacy.md) |
| **Tokenization & Settlement** | Digital asset infrastructure, programmable cash, central counterparties, and settlement mechanics. | [tokenization-and-settlement.md](tokenization-and-settlement.md) |

---

## 🔍 How to Review an External Project

When exploring an external codebase or repository, answer the **Lab Evaluation Questions**:

1. **What data sources does it trust?** Is it institutional, commercial API, or screen-scraped?
2. **Where is the system of record?** Are numbers calculated deterministically or hallucinated by an LLM?
3. **How does it handle staleness and market hours?** Does it recognize weekends, holidays, and bar latency?
4. **What are the privacy and credential boundaries?** Does it use BYOK, local storage, or send credentials to third parties?
5. **What can we reproduce in one meeting?** What is the smallest high-value pattern we can borrow?
6. **What should we explicitly NOT copy?** Avoid bloated agent orchestrations, synthetic fallback mocks, or unverified trading hype.
