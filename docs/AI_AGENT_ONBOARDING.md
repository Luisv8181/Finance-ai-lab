# AI Agent Onboarding

This guide is for any member who wants ChatGPT, Codex, Claude Code, Cursor, Gemini, or another coding-agent harness to contribute to Finance AI Lab.

## 1. Get repository access

Repository:

https://github.com/Luisv8181/Finance-ai-lab

Make sure your GitHub account has the access level the repo owner intends to give you.

For local coding tools:

```bash
git clone https://github.com/Luisv8181/Finance-ai-lab.git
cd Finance-ai-lab
```

Then open the repository root in your coding-agent environment.

## 2. Connect GitHub to ChatGPT

OpenAI's current GitHub connection flow can vary slightly by product surface.

Current official guidance:

1. Open **Settings**.
2. Open **Plugins** or **Apps**, depending on the interface shown to you.
3. Find **GitHub** or a plugin that includes the GitHub app.
4. Install/connect it.
5. Sign into the GitHub account that actually has access to this repository.
6. Review the requested permissions before authorizing.
7. In a supported ChatGPT conversation, invoke it with `@GitHub` or via **+ → More** when those controls are shown.
8. Ask it to locate `Luisv8181/Finance-ai-lab`.

Official OpenAI references:
- https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
- https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt
- https://help.openai.com/en/articles/20001256/

Availability and write permissions can differ by plan, workspace, and product surface. If the agent can read but not write, use the local-clone workflow instead.

## 3. First prompt for any coding agent

Copy/paste:

> You are contributing to Luisv8181/Finance-ai-lab. Before changing anything, read README.md, AGENTS.md, CONTRIBUTING.md, and the relevant issue/project documentation. This is an educational finance + AI lab, not a trading bot. Keep observed market data, calculated metrics, and interpretation separate. Never invent current financial facts or citations. Use a branch for non-trivial work, run tests, and prepare a pull request explaining assumptions, verification, limitations, and next steps. Prefer the smallest inspectable solution over agentic complexity.

## 4. Prompt when you want the agent to choose work

> Inspect open issues in Luisv8181/Finance-ai-lab. Propose the three smallest high-value tasks that are unblocked. Do not start coding yet. For each, explain what I would learn, likely files touched, dependencies, and how we would know it works.

## 5. Prompt when you want the agent to implement an issue

> Work on issue #[NUMBER] in Luisv8181/Finance-ai-lab. Read AGENTS.md first. Create a branch named agent/[YOUR-NAME]/issue-[NUMBER]. State your plan before editing. Make the smallest coherent implementation, add tests where appropriate, run them, then open a pull request. Do not merge it.

## 6. Prompt for research rather than coding

> Treat this as a research contribution. Use primary sources where possible. Separate facts, estimates, interpretations, and open questions. Save the result as a concise Markdown note in the appropriate docs/ or references/ folder, with publication dates and source links. Do not convert contested claims into facts.

## 7. Agent autonomy levels

### Level 0 — Explain
The agent reads the repo and answers questions. No edits.

### Level 1 — Draft
The agent proposes code/docs in chat but does not write.

### Level 2 — Branch + PR
Preferred default. Agent edits on a branch and opens a PR for human review.

### Level 3 — Issue queue
The agent chooses from issues labeled as ready, opens branches/PRs, but a human still reviews and merges.

### Level 4 — Unattended merge
Not recommended for this lab at the beginning.

The goal is not maximum autonomy. The goal is maximum learning per unit of automation.

## 8. Rules for employer-adjacent discussions

Members may work in financial institutions or technology companies.

Do not put into the repository or an AI prompt:
- internal architecture;
- proprietary code;
- customer information;
- non-public incidents;
- internal roadmap details;
- private financial data;
- unpublished employer analysis.

Discuss public systems, public research, published standards, public repositories, and generalized engineering patterns.

## 9. Good first contribution

A new member should start with one of:
- improve a concept explainer;
- add a source to the reading queue;
- add a test;
- add one data-source adapter;
- document a failed experiment;
- improve the opportunity radar;
- summarize one external repository and what we should or should not borrow from it.

## 10. Bring Your Own Key (BYOK) for Gemini

To run LLM-powered market explanations and budget tutoring for free:
- See the click-by-click guide in `docs/BYOK_GUIDE.md`.
- Get a free key at [Google AI Studio](https://aistudio.google.com/).
- Never commit keys. In the CLI, store it in `.env` as `GEMINI_API_KEY=...`. In Money Pulse, store it in the in-app modal.
