from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import yfinance as yf


@dataclass(frozen=True)
class NewsEvent:
    symbol: str
    title: str
    publisher: str
    publication_time: str  # ISO-8601 UTC
    url: str
    retrieval_time: str    # ISO-8601 UTC
    age_hours: float


def parse_publish_time(raw_date: str | int | float | None) -> datetime | None:
    """Parse various timestamp formats (Unix epoch int/float or ISO-8601 string) into UTC datetime."""
    if raw_date is None:
        return None
    try:
        if isinstance(raw_date, (int, float)):
            return datetime.fromtimestamp(raw_date, tz=timezone.utc)
        if isinstance(raw_date, str):
            # Try ISO 8601 string
            clean_str = raw_date.replace("Z", "+00:00")
            dt = datetime.fromisoformat(clean_str)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
    except Exception:
        return None
    return None


def fetch_fresh_news(
    symbol: str,
    max_age_hours: float = 48.0,
    as_of: datetime | None = None,
) -> list[NewsEvent]:
    """Fetch recent news for a symbol with strict timestamp and freshness filtering.

    Any item without a verifiable timestamp or older than max_age_hours is excluded.
    Never invents or mocks news items.
    """
    now_utc = as_of or datetime.now(timezone.utc)
    retrieval_time = now_utc.isoformat()
    verified_events: list[NewsEvent] = []

    try:
        ticker = yf.Ticker(symbol)
        raw_news = getattr(ticker, "news", []) or []
    except Exception:
        return []

    for item in raw_news:
        content = item.get("content", {}) if isinstance(item, dict) else {}
        
        # Handle both flat and nested yfinance schemas
        title = content.get("title") or item.get("title") or ""
        publisher = ""
        provider = content.get("provider") or item.get("publisher")
        if isinstance(provider, dict):
            publisher = provider.get("displayName") or provider.get("name") or "Unknown"
        elif isinstance(provider, str):
            publisher = provider
        else:
            publisher = "Unknown"

        # Extract url
        url = ""
        canonical = content.get("canonicalUrl") or item.get("link")
        if isinstance(canonical, dict):
            url = canonical.get("url") or ""
        elif isinstance(canonical, str):
            url = canonical
        click_through = content.get("clickThroughUrl")
        if not url and isinstance(click_through, dict):
            url = click_through.get("url") or ""

        # Extract publish date
        pub_raw = content.get("pubDate") or item.get("providerPublishTime")
        pub_dt = parse_publish_time(pub_raw)

        # STALENESS & INTEGRITY FILTER:
        # 1. Require title and url
        if not title.strip() or not url.strip():
            continue

        # 2. Require valid parseable publish timestamp
        if pub_dt is None:
            continue

        age_hours = (now_utc - pub_dt).total_seconds() / 3600.0

        # 3. Reject future timestamps (drift > 1 hour) or items older than max_age_hours
        if age_hours < -1.0 or age_hours > max_age_hours:
            continue

        verified_events.append(
            NewsEvent(
                symbol=symbol,
                title=title.strip(),
                publisher=publisher.strip(),
                publication_time=pub_dt.isoformat(),
                url=url.strip(),
                retrieval_time=retrieval_time,
                age_hours=round(age_hours, 2),
            )
        )

    # Sort most recent first
    verified_events.sort(key=lambda x: x.publication_time, reverse=True)
    return verified_events
