from __future__ import annotations

import math

from .market_data import MarketSnapshot


def _number(value: float, digits: int = 2) -> str:
    if math.isnan(value):
        return "n/a"
    return f"{value:,.{digits}f}"


def _pct(value: float) -> str:
    if math.isnan(value):
        return "n/a"
    return f"{value:+.2f}%"


def render_markdown(snapshots: list[MarketSnapshot]) -> str:
    lines = [
        "# Market Watcher — Deterministic Snapshot",
        "",
        "Observed market data only. No causal narrative is generated in v0.",
        "",
        "| Symbol | Lens | Close | 1D | 5D | 20D | MA20 | MA50 | Latest observation |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]

    for item in snapshots:
        lines.append(
            "| "
            + " | ".join(
                [
                    item.symbol,
                    item.label,
                    _number(item.close),
                    _pct(item.return_1d_pct),
                    _pct(item.return_5d_pct),
                    _pct(item.return_20d_pct),
                    _number(item.ma_20),
                    _number(item.ma_50),
                    item.observation_time,
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "Source for v0: Yahoo Finance via yfinance.",
            "",
            "Prototype limitation: this source is convenient for learning but is not a guaranteed real-time or institutional-grade market-data feed.",
        ]
    )
    return "\n".join(lines)
