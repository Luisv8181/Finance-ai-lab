from duckduckgo_search import DDGS
from utils.logger import setup_logger

logger = setup_logger("search")

class OpenSearchCollector:
    """
    Search collector that uses DuckDuckGo as a default open-source backend.
    Can be extended to support a Vane/Perplexica API endpoint once provided.
    """
    def __init__(self, vane_backend=None):
        self.vane_backend = vane_backend

    def search_news(self, query, max_results=5):
        """Performs a search for news related to a ticker or macro event."""
        logger.info(f"Searching for: {query}")
        try:
            with DDGS() as ddgs:
                results = [r for r in ddgs.text(query, max_results=max_results)]
                return results
        except Exception as e:
            logger.error(f"Search error for {query}: {e}")
            return []

    def deep_research(self, topic):
        """Simulates Vane's deep research by combining multiple search queries."""
        # Future: implement direct Vane/Perplexica API calls here
        logger.info(f"Performing deep research on {topic}")
        queries = [topic, f"{topic} market impact", f"{topic} latest developments"]
        all_results = []
        for q in queries:
            all_results.extend(self.search_news(q, max_results=3))
        return all_results

if __name__ == "__main__":
    searcher = OpenSearchCollector()
    print(searcher.search_news("NVDA stock news"))
