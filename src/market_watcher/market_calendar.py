from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, time, timezone
from zoneinfo import ZoneInfo

EASTERN = ZoneInfo("America/New_York")


@dataclass(frozen=True)
class SessionState:
    session_type: str  # "REGULAR", "PRE_MARKET", "AFTER_HOURS", "WEEKEND", "CLOSED"
    is_open: bool
    expected_latest_date: str  # YYYY-MM-DD
    note: str


def get_market_session(as_of: datetime | None = None, is_crypto: bool = False) -> SessionState:
    """Determine US equities market session state for a given timestamp."""
    now_utc = as_of or datetime.now(timezone.utc)
    if is_crypto:
        today_utc = now_utc.strftime("%Y-%m-%d")
        return SessionState(
            session_type="24_7_CONTINUOUS",
            is_open=True,
            expected_latest_date=today_utc,
            note="Crypto markets trade continuously 24/7.",
        )

    now_et = now_utc.astimezone(EASTERN)
    weekday = now_et.weekday()  # 0=Monday, 6=Sunday
    current_time = now_et.time()

    market_open = time(9, 30)
    market_close = time(16, 0)
    pre_market = time(4, 0)
    post_market = time(20, 0)

    # Weekend check
    if weekday == 5:  # Saturday
        # Expected latest session is Friday
        friday = now_et.date().fromordinal(now_et.date().toordinal() - 1)
        return SessionState(
            session_type="WEEKEND",
            is_open=False,
            expected_latest_date=friday.strftime("%Y-%m-%d"),
            note="Saturday — markets closed. Expected data is Friday close.",
        )
    elif weekday == 6:  # Sunday
        # Expected latest session is Friday
        friday = now_et.date().fromordinal(now_et.date().toordinal() - 2)
        return SessionState(
            session_type="WEEKEND",
            is_open=False,
            expected_latest_date=friday.strftime("%Y-%m-%d"),
            note="Sunday — markets closed. Expected data is Friday close.",
        )

    # Weekday check
    today_str = now_et.strftime("%Y-%m-%d")
    yesterday = now_et.date().fromordinal(now_et.date().toordinal() - (3 if weekday == 0 else 1))
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    if current_time < pre_market:
        return SessionState(
            session_type="CLOSED",
            is_open=False,
            expected_latest_date=yesterday_str,
            note="Overnight — before pre-market. Expected data is previous close.",
        )
    elif current_time < market_open:
        return SessionState(
            session_type="PRE_MARKET",
            is_open=False,
            expected_latest_date=yesterday_str,
            note="Pre-market session. Regular market has not opened yet; intraday bars unformed.",
        )
    elif current_time <= market_close:
        return SessionState(
            session_type="REGULAR",
            is_open=True,
            expected_latest_date=today_str,
            note="Regular market trading hours (9:30 AM - 4:00 PM ET).",
        )
    elif current_time <= post_market:
        return SessionState(
            session_type="AFTER_HOURS",
            is_open=False,
            expected_latest_date=today_str,
            note="After-hours session. Official regular close should be available.",
        )
    else:
        return SessionState(
            session_type="CLOSED",
            is_open=False,
            expected_latest_date=today_str,
            note="Evening closed. Expected data is today's close.",
        )


def evaluate_staleness(
    symbol: str,
    observation_iso: str,
    as_of: datetime | None = None,
) -> tuple[bool, str, SessionState]:
    """Check if market observation timestamp matches expected market session.

    Returns (is_stale, reason, session_state).
    """
    is_crypto = "BTC" in symbol.upper() or "ETH" in symbol.upper() or "-USD" in symbol.upper()
    now_utc = as_of or datetime.now(timezone.utc)
    session = get_market_session(now_utc, is_crypto=is_crypto)

    try:
        obs_dt = datetime.fromisoformat(observation_iso)
        obs_date_str = obs_dt.strftime("%Y-%m-%d")
    except Exception:
        return True, f"Unparseable observation timestamp: {observation_iso}", session

    if is_crypto:
        obs_aware = obs_dt if obs_dt.tzinfo is not None else obs_dt.replace(tzinfo=timezone.utc)
        age_hours = (now_utc - obs_aware).total_seconds() / 3600.0
        if age_hours > 36.0:
            return True, f"Crypto observation is {age_hours:.1f}h old (expected <= 24h).", session
        return False, f"Fresh crypto observation ({age_hours:.1f}h old).", session

    # For equities
    if obs_date_str < session.expected_latest_date:
        return (
            True,
            f"Observation date ({obs_date_str}) is behind expected latest session date ({session.expected_latest_date}).",
            session,
        )

    return False, f"Observation aligns with expected session ({session.session_type}).", session
