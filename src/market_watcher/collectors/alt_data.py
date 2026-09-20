from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import logging
from typing import Any
import requests

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class AltDataResult:
    source_name: str
    is_available: bool
    status_code: int | None
    error_message: str | None
    retrieval_time: str
    items: list[dict[str, Any]]


class AltDataCollector:
    """Alternative data collector with strict honesty: fails gracefully with zero mock fallbacks."""

    HOUSE_TRADES_URL = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"

    def __init__(self, timeout_seconds: float = 8.0):
        self.timeout_seconds = timeout_seconds

    def fetch_politician_trades(self, limit: int = 10) -> AltDataResult:
        """Attempt to fetch recent disclosures.
        
        If the endpoint is unreachable or forbidden (HTTP 403), returns an explicit
        is_available=False result. NEVER invents mock fallback trades.
        """
        now_utc = datetime.now(timezone.utc).isoformat()
        try:
            response = requests.get(self.HOUSE_TRADES_URL, timeout=self.timeout_seconds)
            if response.status_code == 200:
                all_trades = response.json()
                if not isinstance(all_trades, list):
                    return AltDataResult(
                        source_name="HouseStockWatcher",
                        is_available=False,
                        status_code=response.status_code,
                        error_message="Unexpected payload schema (not a list)",
                        retrieval_time=now_utc,
                        items=[],
                    )

                recent = sorted(
                    all_trades,
                    key=lambda x: x.get("transaction_date", "") if isinstance(x, dict) else "",
                    reverse=True,
                )[:limit]

                trades: list[dict[str, Any]] = []
                for t in recent:
                    if isinstance(t, dict):
                        trades.append({
                            "representative": t.get("representative", "Unknown"),
                            "ticker": t.get("ticker", "N/A"),
                            "type": t.get("type", "Unknown"),
                            "amount": t.get("amount", "Unknown"),
                            "transaction_date": t.get("transaction_date", "Unknown"),
                            "district": t.get("district", ""),
                        })

                return AltDataResult(
                    source_name="HouseStockWatcher",
                    is_available=True,
                    status_code=200,
                    error_message=None,
                    retrieval_time=now_utc,
                    items=trades,
                )
            else:
                logger.warning("HouseStockWatcher returned HTTP %s", response.status_code)
                return AltDataResult(
                    source_name="HouseStockWatcher",
                    is_available=False,
                    status_code=response.status_code,
                    error_message=f"Endpoint returned HTTP {response.status_code}",
                    retrieval_time=now_utc,
                    items=[],
                )
        except Exception as exc:
            logger.warning("Error querying HouseStockWatcher: %s", exc)
            return AltDataResult(
                source_name="HouseStockWatcher",
                is_available=False,
                status_code=None,
                error_message=str(exc),
                retrieval_time=now_utc,
                items=[],
            )
