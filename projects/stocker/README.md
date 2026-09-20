# STOCKER — Autonomous Market Intelligence Agent (Historical & Reference)

STOCKER was the original automated market intelligence agent that operated locally on Windows from **April 13, 2026 through September 1, 2026**, generating 92 scheduled market briefings and research dossiers.

It was decommissioned on **September 2, 2026** for a complete operating audit and is preserved here in **Finance AI Lab** as both a functional reference and a primary case study in financial AI systems engineering.

---

## 🏛️ What Worked Well

1. **Automation Reliability**:
   - Automated via Windows Task Scheduler (`Stocker_MarketOpen`, `Stocker_MarketClose`, `Stocker_WeeklyResearch`).
   - Daily and weekly HTML/Markdown reports delivered reliably to email via SMTP (`delivery/emailer.py`).
2. **Local Web Dashboard**:
   - Standalone browser dashboard (`dashboard/index.html`, `dashboard/app.js`, `dashboard/style.css`) powered by Python's built-in `server.py` to view reports, watchlists, and sentiment.
3. **Local Knowledge Base**:
   - SQLite-backed store (`utils/stocker_kb.db` + `utils/knowledge_base.py`) logging historical discoveries, ticker notes, and report history across 4.5 months.

---

## 🔍 Forensic Audit: What Degraded & Core Lessons

During its 92-report lifetime, the system experienced progressive data integrity degradation:

1. **The Silent Mock Fallback Loop**:
   - In `collectors/alt_data.py`, when the HouseStockWatcher Amazon S3 bucket returned HTTP 403 Forbidden, the code had a fallback method:
     ```python
     def _fallback_trades(self):
         return [{"ticker": "NANC", "politician": "Nancy Pelosi", "type": "Purchase", "amount": "$500k-1M"}]
     ```
   - Because of this silent fallback, the LLM accepted the synthetic trade as a real event, repeatedly generating narratives about Nancy Pelosi buying NANC in almost every run.
   - **Lesson**: *Never inject synthetic mock data into real analysis pipelines. When an external data provider fails, fail explicitly and report `[UNAVAILABLE]`.*

2. **Market Open Bar Latency**:
   - Running at 9:30 AM Eastern meant that the 1-day bar had either just opened (yielding identical open and close prices, or 0% return) or was still showing yesterday's close.
   - **Lesson**: *The pipeline must be market-calendar aware. It must detect `PRE_MARKET`, `REGULAR`, `AFTER_HOURS`, and `WEEKEND/HOLIDAY` sessions.*

3. **Unbounded Web Search Queries**:
   - Queries via DuckDuckGo without publication date restrictions (`timelimit`) caused older articles from months prior to be retrieved and framed by the prompt as today's breaking drivers.
   - **Lesson**: *All news inputs must carry verified ISO-8601 timestamps and pass a strict freshness window ($\le 48\text{h}$).*

---

## 🚀 The Revival in `market_watcher`

The strengths of STOCKER have been revived, modernized, and hardened inside `src/market_watcher/`:

| Feature | Original STOCKER | Modernized Market Watcher (`src/market_watcher/`) |
|---|---|---|
| **Market Data** | Raw 1-day bars | Full calendar awareness (`market_calendar.py`), 20MA/50MA, and staleness audits |
| **Alternative Data** | Injected fake Nancy Pelosi mock on 403 | Honest failure handling: reports `[UNAVAILABLE]` with zero fake data |
| **News Retrieval** | Unbounded DDG search | Verified UTC publish dates with $\le 48\text{h}$ freshness filter |
| **AI Synthesis** | Unconstrained report generation | Grounded **Evidence Critic & Narrative Buster** evaluating chronology and market beta |
| **Model Support** | Hardcoded older models | Bring Your Own Key (BYOK) Google AI Studio with modern `gemini-flash-latest` support |

---

## 📂 Preserved Directory Layout

- `agent.py`: Original LLM synthesis script (Ollama Gemma + Google Gemini)
- `main.py`: Pipeline coordinator
- `dashboard/`: Local web dashboard interface
- `delivery/`: Emailer and file output handlers
- `collectors/`: Original market, alt data, and open search collectors
- `reports/`: Complete archive of 92 historical reports generated between April and September 2026
- `utils/`: Config, logger, and SQLite knowledge base
