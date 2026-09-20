# Stocker AI Agent Implementation Plan

This plan outlines the architecture for a Python-based intelligent agent that runs locally to fetch, summarize, and report on stock market activity, tailored to your tracked stocks and discovering new opportunities.

## User Review Required
> [!IMPORTANT]
> **Dual LLM Architecture:** We will implement both **Gemma 4** (running locally via Ollama) and **Google Gemini** (via your provided API key). Use Gemma 4 for routine processing and Gemini for complex synthesis or when local resources are constrained.
>
> **Search Infrastructure:** We will integrate **Vane (formerly Perplexica)**. This open-source answering engine will serve as our primary source for cited, real-time internet research.
>
> **Secrets Management:** We will move the key from `api-key` into a `.env` file along with SMTP settings for secure access.

## Proposed Architecture

1. **Automation Core (`main.py`)**: A Python script utilizing the `schedule` library to run the agent pipeline continuously in the background (9:30 AM and 4:30 PM).
2. **Data Collectors (`collectors/`)**:
   - `market_data.py`: Uses `yfinance` to grab daily performance for your target stocks.
   - `vane_search.py`: [NEW] Interfaces with **Vane** to perform "Deep Research" on macro events and company specific news.
   - `alt_data.py`: Fetches politician trades and samples social media sentiment.
3. **Dual AI Synthesizer (`agent.py`)**:
   - **Local Engine**: Uses `Ollama` to run **Gemma 4** for high-performance reasoning without API costs.
   - **Cloud Engine**: Uses `google-generativeai` with your API key for advanced multimodal analysis or fallback.
   - **Knowledge Building**: Analyzes search results to identify *new* companies, sectors, or trends to watch.
4. **Delivery System (`delivery/`)**:
   - `file_output.py`: Saves reports as `.md` or `.pdf` in the `stocker/` folder.
   - `emailer.py`: Sends the daily report to your inbox via SMTP.

## Verification Plan

### Manual Verification
- Dry-run the agent using both Gemma 4 and Gemini to compare output quality.
- Verify Vane Search retrieves accurate, cited news.
- Verify email delivery and file storage.

### Automated Tests
- Test cases for switching between Local and API models.
- Validation scripts for Vane Search API connectivity.
