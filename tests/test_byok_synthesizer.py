from __future__ import annotations

from datetime import datetime, timezone
from unittest.mock import patch, MagicMock

import pytest

from market_watcher.market_calendar import get_market_session
from market_watcher.market_data import MarketSnapshot
from market_watcher.collectors.news import NewsEvent
from market_watcher.collectors.alt_data import AltDataResult
from market_watcher.synthesizer import (
    EvidenceBundle,
    get_gemini_api_key,
    critique_evidence_with_gemini,
    render_evidence_report,
)


def create_sample_bundle() -> EvidenceBundle:
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
    alt_data = AltDataResult("HouseStockWatcher", False, 403, "Forbidden", "2026-09-20T12:00:00", [])
    return EvidenceBundle(
        generated_at="2026-09-20T12:00:00+00:00",
        session_state=session,
        snapshots=[snapshot],
        news=news,
        alt_data=alt_data,
    )


def test_get_gemini_api_key_from_env() -> None:
    with patch.dict("os.environ", {"GEMINI_API_KEY": "AIzaSyTestKey123"}, clear=True):
        key = get_gemini_api_key()
        assert key == "AIzaSyTestKey123"


def test_critique_evidence_with_gemini_success() -> None:
    bundle = create_sample_bundle()
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": "### A. Chronology Critique\nThe article was published after Friday close, making it post-hoc commentary."
                        }
                    ]
                }
            }
        ]
    }

    with patch("requests.post", return_value=mock_resp) as mock_post:
        result = critique_evidence_with_gemini(bundle, "test-key-abc")
        assert "Chronology Critique" in result
        assert "post-hoc commentary" in result
        mock_post.assert_called_once()
        assert "key=test-key-abc" in mock_post.call_args[0][0]


def test_critique_evidence_with_gemini_api_error() -> None:
    bundle = create_sample_bundle()
    mock_resp = MagicMock()
    mock_resp.status_code = 400
    mock_resp.text = "Invalid API key"

    with patch("requests.post", return_value=mock_resp):
        result = critique_evidence_with_gemini(bundle, "bad-key")
        assert "HTTP 400" in result
        assert "Invalid API key" in result


def test_render_evidence_report_without_key_graceful_fallback() -> None:
    bundle = create_sample_bundle()
    with patch("market_watcher.synthesizer.get_gemini_api_key", return_value=None):
        report = render_evidence_report(bundle)
        assert "Deterministic Baseline Hypotheses" in report
        assert "BYOK Tip" in report
        assert "GEMINI_API_KEY" in report


def test_render_evidence_report_with_key_never_leaks_key() -> None:
    bundle = create_sample_bundle()
    secret_key = "AIzaSySuperSecretKeyXYZ"
    with patch("market_watcher.synthesizer.get_gemini_api_key", return_value=secret_key):
        with patch("market_watcher.synthesizer.critique_evidence_with_gemini", return_value="Verified Critique"):
            report = render_evidence_report(bundle)
            assert "Evidence Critic / Narrative Buster" in report
            assert "Verified Critique" in report
            # CRITICAL SECURITY CHECK: Raw API key must NEVER be printed into report output
            assert secret_key not in report
