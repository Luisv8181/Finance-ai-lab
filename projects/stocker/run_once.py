"""
Stocker AI Agent — Single Run Mode
Runs the full pipeline once and exits.
Designed to be called by Windows Task Scheduler (cron-style).
"""
from collectors.market_data import MarketDataCollector
from collectors.open_search import OpenSearchCollector
from collectors.alt_data import AltDataCollector
from agent import LLMEngine
from delivery.file_output import FileDelivery
from delivery.emailer import EmailDelivery
from utils.config import Config
from utils.knowledge_base import KnowledgeBase
from utils.logger import setup_logger
import time
import re

logger = setup_logger("run_once")

def extract_tickers_from_report(report_text):
    """Uses regex to find potential ticker symbols mentioned in the AI report."""
    # Match uppercase 1-5 letter words that look like stock tickers
    candidates = re.findall(r'\b([A-Z]{1,5})\b', report_text)
    # Filter out common English words that aren't tickers
    stopwords = {"THE", "AND", "FOR", "NOT", "BUT", "ARE", "WAS", "HAS", "ITS", 
                 "ETF", "NYSE", "CEO", "CFO", "IPO", "USD", "GDP", "CPI", "SEC",
                 "KEY", "NEW", "ALL", "DAY", "LOW", "HIGH", "BUY", "SELL"}
    return [c for c in set(candidates) if c not in stopwords and len(c) >= 2]

def run_pipeline():
    logger.info("=== STOCKER AGENT FIRING ===")
    
    config = Config()
    market = MarketDataCollector(config.WATCHLIST)
    searcher = OpenSearchCollector()
    alt = AltDataCollector()
    ai = LLMEngine()
    file_sys = FileDelivery()
    email_sys = EmailDelivery()
    kb = KnowledgeBase()

    # Gather intelligence
    context = {
        "market": market.get_stock_performance(),
        "macro_news": searcher.deep_research("stock market macro news today"),
        "politician_trades": alt.get_politician_trades(),
        "trending_searches": searcher.search_news("trending stocks reddit", max_results=3),
        "knowledge_base": {
            "previously_discovered": kb.get_discovered_tickers(limit=10),
            "recent_trends": kb.get_recent_trends(limit=5)
        }
    }

    # Synthesize Report via Gemini (cloud)
    report = ai.synthesize_report(context, use_cloud=True)

    # Extract and store discovered tickers from the report
    discovered = extract_tickers_from_report(report)
    for ticker in discovered:
        if ticker not in config.WATCHLIST:
            kb.add_ticker(ticker, "Discovered in AI report", "ai_synthesis")

    # Store trend data
    kb.add_trend("Daily Market Report", f"Generated at {time.strftime('%Y-%m-%d %H:%M')}", 0.5)

    # Deliver
    filepath = file_sys.save_report(report)
    kb.log_report(filepath, config.WATCHLIST, report[:200])
    email_sys.send_email(f"Stocker AI Report - {time.strftime('%Y-%m-%d %H:%M')}", report)
    
    kb.close()
    logger.info(f"=== PIPELINE COMPLETE — Report: {filepath} ===")

if __name__ == "__main__":
    run_pipeline()
