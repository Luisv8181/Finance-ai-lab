from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Mapping

import pandas as pd
import yfinance as yf


DEFAULT_WATCHLIST: dict[str, str] = {
    "SPY": "U.S. large-cap equities",
    "QQQ": "Nasdaq-100 / growth equities",
    "IWM": "U.S. small-cap equities",
    "TLT": "Long-duration U.S. Treasuries proxy",
    "GLD": "Gold proxy",
    "BTC-USD": "Bitcoin / crypto risk lens",
    "^VIX": "S&P 500 implied volatility",
}


from .market_calendar import evaluate_staleness


@dataclass(frozen=True)
class MarketSnapshot:
    symbol: str
    label: str
    observation_time: str
    close: float
    return_1d_pct: float
    return_5d_pct: float
    return_20d_pct: float
    ma_20: float
    ma_50: float
    retrieval_time: str = ""
    session_status: str = "UNKNOWN"
    is_stale: bool = False
    staleness_note: str = ""


def period_return_pct(close: pd.Series, periods: int) -> float:
    """Return percent change over N trading observations."""
    clean = close.dropna()
    if periods < 1:
        raise ValueError("periods must be >= 1")
    if len(clean) <= periods:
        return math.nan

    previous = float(clean.iloc[-(periods + 1)])
    current = float(clean.iloc[-1])
    if previous == 0:
        return math.nan

    return ((current / previous) - 1.0) * 100.0


def moving_average(close: pd.Series, window: int) -> float:
    """Return simple moving average over the latest N observations."""
    clean = close.dropna()
    if window < 1:
        raise ValueError("window must be >= 1")
    if len(clean) < window:
        return math.nan
    return float(clean.iloc[-window:].mean())


def fetch_history(symbol: str, period: str = "6mo") -> pd.DataFrame:
    """Fetch daily history for a symbol.

    yfinance is used only as a convenient educational prototype source.
    """
    history = yf.Ticker(symbol).history(
        period=period,
        interval="1d",
        auto_adjust=False,
        actions=False,
    )
    if history.empty:
        raise ValueError(f"No market history returned for {symbol}")
    if "Close" not in history.columns:
        raise ValueError(f"Close column missing for {symbol}")
    return history


def build_snapshot(symbol: str, label: str) -> MarketSnapshot:
    retrieval_time = pd.Timestamp.now(tz="UTC").isoformat()
    history = fetch_history(symbol)
    close = history["Close"].dropna()

    if close.empty:
        raise ValueError(f"No closing prices returned for {symbol}")

    observation = close.index[-1]
    observation_time = pd.Timestamp(observation).isoformat()
    is_stale, staleness_note, session = evaluate_staleness(symbol, observation_time)

    return MarketSnapshot(
        symbol=symbol,
        label=label,
        observation_time=observation_time,
        close=float(close.iloc[-1]),
        return_1d_pct=period_return_pct(close, 1),
        return_5d_pct=period_return_pct(close, 5),
        return_20d_pct=period_return_pct(close, 20),
        ma_20=moving_average(close, 20),
        ma_50=moving_average(close, 50),
        retrieval_time=retrieval_time,
        session_status=session.session_type,
        is_stale=is_stale,
        staleness_note=staleness_note,
    )


def build_watchlist_snapshot(
    watchlist: Mapping[str, str] = DEFAULT_WATCHLIST,
) -> list[MarketSnapshot]:
    snapshots: list[MarketSnapshot] = []
    for symbol, label in watchlist.items():
        snapshots.append(build_snapshot(symbol, label))
    return snapshots
