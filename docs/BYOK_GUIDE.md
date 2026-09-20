# Bring Your Own Key (BYOK) Guide

This guide explains how any human member or coding agent in **Finance AI Lab** can use Google Gemini models for free using **Google AI Studio**.

---

## Why Bring Your Own Key (BYOK)?

1. **Zero Shared Costs**: No group credit card or shared billing account needed.
2. **Generous Free Tier**: Google AI Studio provides free access to `gemini-2.5-flash` with substantial daily rate limits.
3. **Privacy & Security**: Keys and personal data are never committed to GitHub or sent to an intermediary server.
   - In the **Python CLI**, your key stays on your local machine in `.env` (which is git-ignored).
   - In **Money Pulse**, your key stays in your browser's `localStorage`.

---

## 👤 For Humans: Click-by-Click Setup

### Step 1: Get Your Free API Key (30 Seconds)
1. Open your browser and navigate to **[https://aistudio.google.com/](https://aistudio.google.com/)**.
2. Sign in with any personal Google account.
3. In the left navigation menu, click **"Get API key"** (or click the blue **"Get API key"** button at the top).
4. Click **"Create API key"**.
   - If prompted to choose a Google Cloud project, select your default project or create a quick free one.
5. Click **"Copy"** next to your new API key (it begins with `AIzaSy...`).
6. Store it in a secure password manager.

---

### Step 2: Use Your Key

#### Option A: In the Terminal (`market-watcher stocker`)
1. Open the repository root in your terminal or editor (`finance-lab`).
2. Create a file named `.env` (note the leading dot):
   ```env
   GEMINI_API_KEY=AIzaSyYourKeyHere
   ```
3. Run the stocker intelligence report:
   ```bash
   market-watcher stocker
   ```
   *The system will automatically detect your key, enrich the report with the **Evidence Critic / Narrative Buster**, and critique financial headlines against market chronology.*

#### Option B: In the Browser (Money Pulse Budget Tool)
1. Run `market-watcher pulse` or open `projects/financial-wellness-lab/index.html` in your web browser.
2. In the top navigation bar, click **"🤖 AI Explainer (BYOK)"**.
3. Paste your Google AI Studio API key into the input field and click **"Save Key"**.
4. Click any scenario button (e.g. *"Analyze Budget Health"*, *"Stress-test a \$300 rent hike"*, or *"How to reach a 6-month runway"*).
5. Gemini will analyze your current numbers live in your browser.

---

## 🤖 For AI Coding Agents: Agent Protocol

When building or updating features that use LLMs:

1. **Never Hardcode Secrets**: Never embed API keys, secrets, or bearer tokens in code, tests, or commit messages.
2. **Environment Contract**:
   - Always look for `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) from `os.environ` or `.env`.
   - Never print the raw key to logs, stdout, stderr, or reports.
3. **Graceful Degradation**:
   - If an API key is missing or invalid, the system must not crash.
   - Fall back to the clean, deterministic rule-based analysis with a clear diagnostic notice (`[BYOK Notice: No GEMINI_API_KEY detected; using deterministic analysis]`).
4. **Strict Grounding Boundary**:
   - The LLM must be supplied with an `EvidenceBundle` containing verified prices, timestamps, and sources.
   - Forbid the model from inventing prices, percentages, dates, or citations.
   - Require the model to classify market explanations as **hypotheses**, evaluating chronology (did the headline precede the price drop?) and index correlation.
