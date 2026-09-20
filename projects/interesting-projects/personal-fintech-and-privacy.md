# Personal FinTech & Local-First Privacy Projects

These projects demonstrate how to build transparent, user-sovereign financial management tools that protect user data without locking users into proprietary banking platforms.

---

### 1. Actual Budget
- **Repository**: [https://github.com/actualbudget/actual](https://github.com/actualbudget/actual)
- **What it is**: 100% free and open-source local-first personal finance system built on zero-based budgeting principles.
- **Key Architectural Patterns to Study**:
  - **Local-First Architecture**: Operates on SQLite locally with optional end-to-end encrypted synchronization.
  - **CRDTs (Conflict-Free Replicated Data Types)**: Enables multi-device offline editing without server reconciliation lockups.
- **Takeaway for Finance AI Lab**:
  - Validates the thesis behind **Money Pulse**: financial software is faster, more private, and more trustworthy when it runs locally first.

---

### 2. Maybe Finance
- **Repository**: [https://github.com/maybe-finance/maybe](https://github.com/maybe-finance/maybe)
- **What it is**: Personal balance sheet and wealth tracking platform that went open-source, built in Ruby on Rails and modern frontend components.
- **Key Architectural Patterns to Study**:
  - **Net Worth & Asset Modeling**: Clean aggregation of investment accounts, real estate, debts, and liquid cash.
  - **Scenario Simulation**: Modeling life events (home purchases, career changes, early retirement).
- **Takeaway for Finance AI Lab**:
  - Great reference for extending Money Pulse from monthly cash-flow into multi-year net worth resilience.

---

### 3. Firefly III
- **Repository**: [https://github.com/firefly-iii/firefly-iii](https://github.com/firefly-iii/firefly-iii)
- **What it is**: A self-hosted personal finance manager utilizing strict double-entry bookkeeping.
- **Key Architectural Patterns to Study**:
  - **Double-Entry Discipline**: Money is never created or destroyed; it moves strictly between asset, expense, revenue, and liability accounts.
  - **Rule-Based Categorization**: Deterministic regex and merchant matching before any AI layer is introduced.
- **Takeaway for Finance AI Lab**:
  - Demonstrates why strict transaction accounting rules are superior to naive heuristic guesses.
