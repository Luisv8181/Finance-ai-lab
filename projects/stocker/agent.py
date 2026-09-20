import google.generativeai as genai
import requests
import json
from duckduckgo_search import DDGS
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger("agent")

class LLMEngine:
    def __init__(self):
        self.config = Config()
        # Setup Gemini
        if self.config.GOOGLE_API_KEY:
            genai.configure(api_key=self.config.GOOGLE_API_KEY)
            # Using Gemini 2.5 Flash for high efficiency and availability
            self.gemini_model = genai.GenerativeModel('models/gemini-2.5-flash')
        else:
            self.gemini_model = None
            logger.warning("Google API Key not found. Gemini fallback disabled.")

    def run_gemma(self, prompt):
        """Runs the local Gemma 4 model via Ollama."""
        logger.info("Generating with Local Gemma 4...")
        try:
            url = "http://localhost:11434/api/generate"
            payload = {
                "model": "gemma 4", # User specified Gemma 4
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(url, json=payload, timeout=60)
            if response.status_code == 200:
                return response.json().get("response", "")
            return "Error: Ollama not reachable or error in response."
        except Exception as e:
            logger.error(f"Gemma error: {e}")
            return f"Error: {e}"

    def run_gemini(self, prompt):
        """Runs the Google Gemini model via API."""
        if not self.gemini_model:
            return "Gemini not configured."
        logger.info("Generating with Google Gemini...")
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return f"Error: {e}"

    def synthesize_report(self, context, use_cloud=False):
        """Synthesizes the gathered context into a structured report."""
        prompt = f"""
        You are the Stocker AI Agent. Analyze the following data and generate a comprehensive daily stock report.
        Include Sections:
        1. Market Overview (Macros & World Events)
        2. Watchlist Performance (Price & Change)
        3. Alternative Insights (Politician Trades & Sentiment)
        4. Knowledge Discovery (Suggest new tickers/trends found in search)
        5. Educational Insight (A quick concept or link)

        Context Data:
        {json.dumps(context, indent=2)}

        Format: Markdown. Tone: Professional, actionable, and data-driven.
        """
        if use_cloud:
            return self.run_gemini(prompt)
        else:
            return self.run_gemma(prompt)
