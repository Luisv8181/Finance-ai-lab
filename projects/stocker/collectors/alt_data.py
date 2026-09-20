import requests
from utils.logger import setup_logger

logger = setup_logger("alt_data")

class AltDataCollector:
    """Collects alternative data like politician trades and social sentiment."""
    
    HOUSE_TRADES_URL = "https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/all_transactions.json"
    
    def get_politician_trades(self, limit=10):
        """Fetches recent house/senate stock trades from open APIs."""
        logger.info("Fetching politician trades...")
        try:
            response = requests.get(self.HOUSE_TRADES_URL, timeout=15)
            if response.status_code == 200:
                all_trades = response.json()
                # Get the most recent trades
                recent = sorted(all_trades, key=lambda x: x.get('transaction_date', ''), reverse=True)[:limit]
                trades = []
                for t in recent:
                    trades.append({
                        "politician": t.get("representative", "Unknown"),
                        "ticker": t.get("ticker", "N/A"),
                        "type": t.get("type", "Unknown"),
                        "amount": t.get("amount", "Unknown"),
                        "date": t.get("transaction_date", "Unknown"),
                        "district": t.get("district", "")
                    })
                logger.info(f"Found {len(trades)} recent politician trades")
                return trades
            else:
                logger.warning(f"HouseStockWatcher returned {response.status_code}")
                return self._fallback_trades()
        except Exception as e:
            logger.error(f"Error fetching politician trades: {e}")
            return self._fallback_trades()

    def _fallback_trades(self):
        """Fallback data if the API is unavailable."""
        return [{"ticker": "NANC", "politician": "Nancy Pelosi", "type": "Purchase", "amount": "$500k-1M"}]

    def get_sentiment(self, ticker):
        """Placeholder for social media sentiment analysis."""
        logger.info(f"Analyzing sentiment for {ticker}")
        return "Positive"

if __name__ == "__main__":
    collector = AltDataCollector()
    trades = collector.get_politician_trades()
    for t in trades:
        print(f"{t['politician']}: {t['type']} {t['ticker']} ({t['amount']})")
