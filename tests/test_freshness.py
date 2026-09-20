from __future__ import annotations

from datetime import datetime, timezone
import math
from unittest.mock import patch, MagicMock

import pytest

from market_watcher.market_calendar import evaluate_staleness, get_market_session
from market_watcher.collectors.news import parse_publish_time, NewsEvent
from market_watcher.collectors.alt_data import AltDataCollector
from market_watcher.market_data import MarketSnapshot
from market_watcher.synthesizer import EvidenceBundle, render_evidence_report


def test_market_session_weekend() -> None:
    # 2026-09-20 is a Sunday
    sunday_dt = datetime(2026, 9, 20, 14, 0, tzinfo=timezone.utc)
    session = get_market_session(as_of=sunday_dt)
    assert session.session_type == "WEEKEND"
    assert not session.is_open
    assert session.expected_latest_date == "2026-09-18"  # Friday


def test_market_session_regular_hours() -> None:
    # 2026-09-21 is a Monday at 11:00 AM Eastern (15:00 UTC)
    monday_open = datetime(2026, 9, 21, 15, 0, tzinfo=timezone.utc)
    session = get_market_session(as_of=monday_open)
    assert session.session_type == "REGULAR"
    assert session.is_open
    assert session.expected_latest_date == "2026-09-21"


def test_staleness_detection() -> None:
    # Check on Sunday 2026-09-20
    as_of = datetime(2026, 9, 20, 14, 0, tzinfo=timezone.utc)
    
    # An observation from Friday 2026-09-18 is NOT stale on a weekend
    is_stale, reason, session = evaluate_staleness("SPY", "2026-09-18T20:00:00+00:00", as_of=as_of)
    assert not is_stale
    assert "aligns" in reason

    # An observation from Thursday 2026-09-17 IS stale on a weekend (Friday close was missed)
    is_stale, reason, session = evaluate_staleness("SPY", "2026-09-17T20:00:00+00:00", as_of=as_of)
    assert is_stale
    assert "behind expected" in reason


def test_parse_publish_time() -> None:
    # Unix epoch
    dt_epoch = parse_publish_time(1726837200)
    assert dt_epoch is not None
    assert dt_epoch.tzinfo == timezone.utc

    # ISO string with Z
    dt_iso = parse_publish_time("2026-09-20T13:00:00Z")
    assert dt_iso is not None
    assert dt_iso.year == 2026
    assert dt_iso.day == 20

    # Unparseable
    assert parse_publish_time("not-a-date") is None
    assert parse_publish_time(None) is None


def test_alt_data_never_injects_mock_data_on_failure() -> None:
    collector = AltDataCollector()
    
    # Mock a 403 Forbidden response (the exact failure that plagued old STOCKER)
    with patch("requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 403
        mock_get.return_value = mock_resp

        result = collector.fetch_politician_trades()
        assert not result.is_available
        assert result.status_code == 403
        assert result.items == []  # MUST BE EMPTY! NEVER INJECT NANCY PELOSI MOCKS!


def test_render_evidence_report() -> None:
    session = get_market_session(datetime(2026, 9, 20, 12, 0, tzinfo=timezone.utc))
    snapshot = MarketSnapshot(
        symbol="SPY",
        label="U.S. large-cap equities",
        observation_time="2026-09-18T20:00:00+00:00",
        close=580.0,
        return_1d_pct=0.5,
        return_5d_pct=1.2,
        return_20d_pct=2.5,
        ma_20=575.0,
        ma_50=565.0,
        retrieval_time="2026-09-20T12:00:00+00:00",
        session_status="WEEKEND",
        is_stale=False,
    )
    news = [
        NewsEvent(
            symbol="SPY",
            title="Markets close higher on rate cut outlook",
            publisher="Financial Times",
            publication_time="2026-09-18T21:00:00+00:00",
            url="https://example.com/news1",
            retrieval_time="2026-09-20T12:00:00+00:00",
            age_hours=39.0,
        )
    ]
    collector = AltDataCollector()
    alt_res = collector.fetch_politician_trades()

    bundle = EvidenceBundle(
        generated_at="2026-09-20T12:00:00+00:00",
        session_state=session,
        snapshots=[snapshot],
        news=news,
        alt_data=alt_res,
    )

    report = render_evidence_report(bundle)
    assert "# STOCKER / Market Watcher" in report
    assert "SPY" in report
    assert "Markets close higher" in report
    assert "Observed Market Data" in report
