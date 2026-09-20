import sqlite3
import os
import json
from datetime import datetime
from utils.logger import setup_logger

logger = setup_logger("knowledge_base")

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stocker_kb.db")

class KnowledgeBase:
    """Persistent knowledge base for discovered trends, tickers, and insights."""
    
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self._init_tables()

    def _init_tables(self):
        cursor = self.conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS discovered_tickers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT UNIQUE,
                reason TEXT,
                source TEXT,
                discovered_at TEXT,
                score REAL DEFAULT 0.0
            );
            CREATE TABLE IF NOT EXISTS trends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT,
                summary TEXT,
                discovered_at TEXT,
                relevance_score REAL DEFAULT 0.0
            );
            CREATE TABLE IF NOT EXISTS report_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                generated_at TEXT,
                watchlist TEXT,
                summary TEXT
            );
        """)
        self.conn.commit()

    def add_ticker(self, ticker, reason, source="ai_discovery"):
        try:
            self.conn.execute(
                "INSERT OR IGNORE INTO discovered_tickers (ticker, reason, source, discovered_at) VALUES (?, ?, ?, ?)",
                (ticker.upper(), reason, source, datetime.now().isoformat())
            )
            self.conn.commit()
            logger.info(f"Discovered ticker: {ticker} — {reason}")
        except Exception as e:
            logger.error(f"KB error adding ticker: {e}")

    def add_trend(self, topic, summary, relevance=0.5):
        try:
            self.conn.execute(
                "INSERT INTO trends (topic, summary, discovered_at, relevance_score) VALUES (?, ?, ?, ?)",
                (topic, summary, datetime.now().isoformat(), relevance)
            )
            self.conn.commit()
            logger.info(f"Tracked trend: {topic}")
        except Exception as e:
            logger.error(f"KB error adding trend: {e}")

    def log_report(self, filename, watchlist, summary=""):
        try:
            self.conn.execute(
                "INSERT INTO report_history (filename, generated_at, watchlist, summary) VALUES (?, ?, ?, ?)",
                (filename, datetime.now().isoformat(), json.dumps(watchlist), summary)
            )
            self.conn.commit()
        except Exception as e:
            logger.error(f"KB error logging report: {e}")

    def get_discovered_tickers(self, limit=20):
        cursor = self.conn.execute(
            "SELECT ticker, reason, discovered_at FROM discovered_tickers ORDER BY discovered_at DESC LIMIT ?", (limit,)
        )
        return cursor.fetchall()

    def get_recent_trends(self, limit=10):
        cursor = self.conn.execute(
            "SELECT topic, summary, discovered_at FROM trends ORDER BY discovered_at DESC LIMIT ?", (limit,)
        )
        return cursor.fetchall()

    def get_report_history(self, limit=20):
        cursor = self.conn.execute(
            "SELECT filename, generated_at FROM report_history ORDER BY generated_at DESC LIMIT ?", (limit,)
        )
        return cursor.fetchall()

    def close(self):
        self.conn.close()
