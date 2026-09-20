from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import math
import os
from typing import Mapping

from .market_data import MarketSnapshot, build_watchlist_snapshot, DEFAULT_WATCHLIST
from .market_calendar import get_market_session, SessionState
from .collectors.news import NewsEvent, fetch_fresh_news
from .collectors.alt_data import AltDataCollector, AltDataResult


@dataclass(frozen=True)
class EvidenceBundle:
    generated_at: str
    session_state: SessionState
    snapshots: list[MarketSnapshot]
    news: list[NewsEvent]
    alt_data: AltDataResult


def gather_evidence_bundle(
    watchlist: Mapping[str, str] = DEFAULT_WATCHLIST,
    news_max_age_hours: float = 48.0,
    check_alt_data: bool = True,
) -> EvidenceBundle:
    """Gather all deterministic market observations, fresh news, and alternative data."""
    now_utc = datetime.now(timezone.utc)
    session = get_market_session(now_utc)
    snapshots = build_watchlist_snapshot(watchlist)

    # Gather fresh news for primary index symbols
    news_events: list[NewsEvent] = []
    primary_symbols = ["SPY", "QQQ", "TLT", "BTC-USD"]
    for sym in primary_symbols:
        if sym in watchlist:
            events = fetch_fresh_news(sym, max_age_hours=news_max_age_hours, as_of=now_utc)
            news_events.extend(events[:3])  # Top 3 freshest per instrument

    # Deduplicate news by URL
    seen_urls = set()
    unique_news: list[NewsEvent] = []
    for n in news_events:
        if n.url not in seen_urls:
            seen_urls.add(n.url)
            unique_news.append(n)

    alt_result = (
        AltDataCollector().fetch_politician_trades()
        if check_alt_data
        else AltDataResult("Disabled", False, None, "Check skipped", now_utc.isoformat(), [])
    )

    return EvidenceBundle(
        generated_at=now_utc.isoformat(),
        session_state=session,
        snapshots=snapshots,
        news=unique_news,
        alt_data=alt_result,
    )


def _fmt_pct(val: float) -> str:
    if math.isnan(val):
        return "n/a"
    return f"{val:+.2f}%"


def _fmt_num(val: float) -> str:
    if math.isnan(val):
        return "n/a"
    return f"{val:,.2f}"


def render_evidence_report(bundle: EvidenceBundle) -> str:
    """Render a transparent, fool-proof market intelligence report.
    
    Adheres strictly to AGENTS.md:
    - Observed data, derived metrics, and interpretations are kept strictly distinct.
    - Zero invented facts or mock fallback trades.
    - Explicit freshness audits and session state warnings.
    """
    lines: list[str] = [
        "# STOCKER / Market Watcher — Intelligence Report",
        "",
        f"**Generated (UTC)**: `{bundle.generated_at}`  ",
        f"**Market Session**: `{bundle.session_state.session_type}` (Open: `{bundle.session_state.is_open}`)  ",
        f"**Session Note**: {bundle.session_state.note}",
        "",
        "---",
        "",
        "## 1. Observed Market Data & Technical Metrics",
        "",
        "| Symbol | Lens | Close | 1D Return | 5D Return | 20D Return | 20 MA | 50 MA | Observation Time | Freshness |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]

    for s in bundle.snapshots:
        freshness_label = "[STALE]" if s.is_stale else "[Current]"
        lines.append(
            f"| {s.symbol} | {s.label} | {_fmt_num(s.close)} | {_fmt_pct(s.return_1d_pct)} | "
            f"{_fmt_pct(s.return_5d_pct)} | {_fmt_pct(s.return_20d_pct)} | {_fmt_num(s.ma_20)} | "
            f"{_fmt_num(s.ma_50)} | {s.observation_time} | {freshness_label} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 2. Fresh Verified News & Macro Events",
        "",
    ])

    if not bundle.news:
        lines.append("*No news items passed the strict freshness filter (<= 48h with verified publish timestamps).*")
    else:
        lines.append("| Ticker | Age | Headline | Publisher | Published (UTC) |")
        lines.append("|---|---:|---|---|---|")
        for n in bundle.news:
            lines.append(f"| {n.symbol} | {n.age_hours:.1f}h | [{n.title}]({n.url}) | {n.publisher} | {n.publication_time} |")

    lines.extend([
        "",
        "---",
        "",
        "## 3. Alternative Data & Disclosures",
        "",
        f"- **Source**: `{bundle.alt_data.source_name}`",
        f"- **Status**: {'[AVAILABLE]' if bundle.alt_data.is_available else '[UNAVAILABLE]'}",
    ])

    if not bundle.alt_data.is_available:
        lines.append(f"- **Diagnostic Notice**: {bundle.alt_data.error_message}")
        lines.append("- **Integrity Rule**: Per `AGENTS.md`, synthetic mock data is strictly forbidden when endpoints are unavailable.")
    else:
        lines.append(f"- **Disclosures Retrieved**: {len(bundle.alt_data.items)}")
        for item in bundle.alt_data.items[:5]:
            lines.append(
                f"  - **{item.get('representative')}** ({item.get('district', '')}): "
                f"{item.get('type')} `{item.get('ticker')}` for {item.get('amount')} "
                f"on {item.get('transaction_date')}"
            )

    lines.extend([
        "",
        "---",
        "",
        "## 4. Explanatory Hypotheses (Interpretation)",
        "",
        "> [!NOTE]",
        "> Market explanations are hypotheses unless causal evidence is unusually strong.",
        "> Observations must precede price movement to be considered causal candidates.",
        "",
    ])

    # Rule-based educational commentary grounded solely on observed data
    top_mover = max(bundle.snapshots, key=lambda x: abs(x.return_1d_pct) if not math.isnan(x.return_1d_pct) else -1)
    if not math.isnan(top_mover.return_1d_pct):
        direction = "gain" if top_mover.return_1d_pct > 0 else "decline"
        lines.append(
            f"- **Largest 1D Movement**: `{top_mover.symbol}` ({top_mover.label}) registered a {direction} of "
            f"{_fmt_pct(top_mover.return_1d_pct)}. Relative to its 20-day moving average ({_fmt_num(top_mover.ma_20)}), "
            f"it is trading {'above' if top_mover.close > top_mover.ma_20 else 'below'}."
        )

    vix = next((s for s in bundle.snapshots if s.symbol == "^VIX"), None)
    if vix and not math.isnan(vix.close):
        vol_env = "elevated implied volatility" if vix.close > 20.0 else "subdued/normal implied volatility"
        lines.append(f"- **Volatility Environment**: S&P 500 implied volatility (^VIX) is at {_fmt_num(vix.close)}, signaling {vol_env}.")

    lines.extend([
        "",
        "---",
        "",
        "## 5. Provenance & Limitations",
        "",
        "- **Data Sources**: Yahoo Finance (`yfinance`) for prices and news; HouseStockWatcher S3 for disclosures.",
        "- **Educational Purpose**: For research and educational modeling only; no automated trading or investment recommendations.",
        "- **LLM Boundary**: Numeric data is derived deterministically; LLMs are never systems of record for market numbers.",
    ])

    return "\n".join(lines)
