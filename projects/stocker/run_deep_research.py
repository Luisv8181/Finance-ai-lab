"""
Stocker AI Agent — Weekly Deep Research Mode
Performs extended research on sectors, trends, and emerging tickers.
Scheduled to run weekly (e.g., Sunday evening).
"""
from collectors.open_search import OpenSearchCollector
from agent import LLMEngine
from delivery.file_output import FileDelivery
from delivery.emailer import EmailDelivery
from utils.config import Config
from utils.knowledge_base import KnowledgeBase
from utils.logger import setup_logger
import time
import json

logger = setup_logger("deep_research")

RESEARCH_TOPICS = [
    "emerging market sectors 2026",
    "AI stocks to watch",
    "undervalued small cap stocks",
    "upcoming IPOs",
    "Federal Reserve interest rate outlook",
    "geopolitical risks to stock market",
    "cryptocurrency regulation impact on stocks",
    "green energy stocks momentum"
]

def run_deep_research():
    logger.info("=== WEEKLY DEEP RESEARCH START ===")
    
    searcher = OpenSearchCollector()
    ai = LLMEngine()
    file_sys = FileDelivery()
    email_sys = EmailDelivery()
    kb = KnowledgeBase()

    # Gather deep research on all topics
    all_research = {}
    for topic in RESEARCH_TOPICS:
        logger.info(f"Researching: {topic}")
        results = searcher.deep_research(topic)
        all_research[topic] = results
        # Store each topic as a trend
        summary = "; ".join([r.get("title", "") for r in results[:3]]) if results else "No results"
        kb.add_trend(topic, summary, 0.7)

    # Build deep research context
    context = {
        "mode": "WEEKLY_DEEP_RESEARCH",
        "research_topics": all_research,
        "current_watchlist": Config.WATCHLIST,
        "previously_discovered": kb.get_discovered_tickers(limit=20),
    }

    # Use Gemini for complex synthesis
    prompt_override = f"""
    You are the Stocker AI Agent in DEEP RESEARCH mode. 
    Analyze the following research data and produce a comprehensive WEEKLY INTELLIGENCE BRIEFING.
    
    Sections:
    1. Macro Outlook (economic environment summary)
    2. Sector Spotlight (which sectors are heating up or cooling down)
    3. New Ticker Discoveries (specific stocks worth adding to the watchlist, with reasoning)
    4. Risk Assessment (geopolitical, regulatory, or market risks)
    5. Actionable Recommendations (what to watch next week)
    
    Research Data:
    {json.dumps(context, indent=2, default=str)}
    
    Format: Markdown. Tone: Analytical, forward-looking.
    """

    report = ai.run_gemini(prompt_override)

    # Deliver as a special weekly report
    filepath = file_sys.save_report(f"# 📊 WEEKLY INTELLIGENCE BRIEFING\n\n{report}")
    kb.log_report(filepath, Config.WATCHLIST, "Weekly deep research")
    email_sys.send_email(f"Stocker WEEKLY Briefing - {time.strftime('%Y-%m-%d')}", report)

    kb.close()
    logger.info("=== WEEKLY DEEP RESEARCH COMPLETE ===")

if __name__ == "__main__":
    run_deep_research()
