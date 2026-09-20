# Market Infrastructure & Data Projects

These projects demonstrate how to build clean, reproducible financial data pipelines, data provider abstraction layers, and institutional data representations.

---

### 1. OpenBB Platform
- **Repository**: [https://github.com/OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)
- **What it is**: The leading open-source investment research software platform, providing a unified Python SDK and terminal for equity, fixed income, crypto, and macro data.
- **Key Architectural Patterns to Study**:
  - **Provider Abstraction Layer**: Standardizes different data providers (Yahoo, Polygon, FRED, SEC EDGAR, FMP) behind a uniform data contract.
  - **Tool & Agent Integration**: How OpenBB exports functions as LLM tool definitions (functions/schemas).
- **Takeaway for Finance AI Lab**:
  - Borrow their data contract patterns for `market_watcher` so we can easily swap providers without changing analytical logic.

---

### 2. FINOS Common Domain Model (CDM)
- **Organization**: [FINOS (Fintech Open Source Foundation)](https://www.finos.org/)
- **Repository**: [https://github.com/finos/common-domain-model](https://github.com/finos/common-domain-model)
- **What it is**: An industry-standardized digital representation of financial events and transactions across trades, collateral, and clearing (ISDA, ICMA, ISLA).
- **Key Architectural Patterns to Study**:
  - **Trade State Lifecycle**: How a financial product moves from pre-trade to execution, clearing, settlement, and lifecycle events.
  - **Type Safety**: Unambiguous data definitions that prevent multi-party reconciliation discrepancies.
- **Takeaway for Finance AI Lab**:
  - Helps the team understand the actual plumbing between broker-dealers, clearing corporations (DTCC), and custodians.

---

### 3. Microsoft Qlib
- **Repository**: [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib)
- **What it is**: An AI-oriented quantitative investment platform emphasizing reproducible data pipelines and model backtesting.
- **Key Architectural Patterns to Study**:
  - **Strict Separation**: Clean boundaries between raw data, derived features, and model inference.
  - **Evaluation Fixtures**: Structured benchmarking against fixed historical baselines.
- **Takeaway for Finance AI Lab**:
  - Educational reference for how to test calculation logic and feature engineering reproducibly.

---

### 4. SEC EDGAR Python Tools (edgar / sec-edgar-downloader)
- **Repositories**: [https://github.com/dgunning/edgartools](https://github.com/dgunning/edgartools)
- **What it is**: Fast, structured parsing of SEC filings (10-K, 10-Q, 8-K, Form 4 insider transactions).
- **Key Architectural Patterns to Study**:
  - Direct access to primary regulatory filings rather than third-party summaries.
  - XBRL parsing and table extraction.
- **Takeaway for Finance AI Lab**:
  - Potential verified data source for corporate disclosures and insider transactions to replace unreliable third-party endpoints.
