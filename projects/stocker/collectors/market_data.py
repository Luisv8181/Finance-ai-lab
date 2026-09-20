import yfinance as yf
from utils.logger import setup_logger

logger = setup_logger("market_data")

class MarketDataCollector:
    def __init__(self, tickers):
        self.tickers = tickers

    def get_stock_performance(self):
        """Fetches daily performance for the watchlist."""
        data = {}
        for ticker in self.tickers:
            try:
                logger.info(f"Fetching data for {ticker}")
                stock = yf.Ticker(ticker)
                hist = stock.history(period="1d")
                if not hist.empty:
                    close_price = hist['Close'].iloc[-1]
                    open_price = hist['Open'].iloc[-1]
                    percent_change = ((close_price - open_price) / open_price) * 100
                    data[ticker] = {
                        "price": round(close_price, 2),
                        "change": round(percent_change, 2),
                        "volume": int(hist['Volume'].iloc[-1])
                    }
                else:
                    logger.warning(f"No data found for {ticker}")
            except Exception as e:
                logger.error(f"Error fetching {ticker}: {e}")
        return data

if __name__ == "__main__":
    collector = MarketDataCollector(["AAPL", "TSLA"])
    print(collector.get_stock_performance())
