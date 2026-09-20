import schedule
import time
from collectors.market_data import MarketDataCollector
from collectors.open_search import OpenSearchCollector
from collectors.alt_data import AltDataCollector
from agent import LLMEngine
from delivery.file_output import FileDelivery
from delivery.emailer import EmailDelivery
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("main")

def run_pipeline():
    logger.info("Starting Stocker Pipeline...")
    
    # 1. Initialize components
    config = Config()
    market = MarketDataCollector(config.WATCHLIST)
    searcher = OpenSearchCollector()
    alt = AltDataCollector()
    ai = LLMEngine()
    file_sys = FileDelivery()
    email_sys = EmailDelivery()

    # 2. Gather data
    context = {
        "market": market.get_stock_performance(),
        "macro_news": searcher.deep_research("stock market macro news"),
        "politician_trades": alt.get_politician_trades(),
        "trending_searches": searcher.search_news("trending stocks reddit", max_results=3)
    }

    # 3. Synthesize Report
    # Note: Using cloud fallback logic if local Gemma 4 fails or user prefers
    report = ai.synthesize_report(context, use_cloud=True) # Defaulting to Gemini for best quality if key is present

    # 4. Deliver
    filepath = file_sys.save_report(report)
    email_sys.send_email(f"Daily Stocker AI Report - {time.strftime('%Y-%m-%d')}", report)
    
    logger.info("Pipeline completed.")

def main():
    logger.info("Stocker AI Agent is awake.")
    
    # Schedule for 9:30 AM and 4:30 PM
    # Note: These are in 24h format
    schedule.every().day.at("09:30").do(run_pipeline)
    schedule.every().day.at("16:30").do(run_pipeline)
    
    # For testing: run once immediately
    logger.info("Running initial test cycle...")
    run_pipeline()
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
