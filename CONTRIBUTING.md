# Contributing

The lab should be easy to contribute to without becoming a free-for-all.

## Default human workflow

1. Pick or create an issue.
2. Create a branch such as `feature/market-snapshot` or `docs/meeting-02`.
3. Work manually or with your coding agent.
4. Open a pull request.
5. Ask another person to review anything non-trivial.
6. Merge after the change is understandable and testable.

Tiny documentation fixes may go directly to `main`.

## Using AI coding agents

Agents are encouraged, but the human remains responsible for what gets merged.

Tell your agent to read `AGENTS.md` first.

A good agent contribution should explain:
- what issue it is solving;
- assumptions it made;
- why the implementation is no more complex than necessary;
- tests it ran;
- what is still uncertain.

See `docs/AI_AGENT_ONBOARDING.md` for copy-paste setup prompts.

## Pull-request review questions

Before merging, ask:

- Are facts separate from interpretations?
- Are current claims sourced?
- Can another person reproduce the important calculations?
- Did we add complexity because it was necessary, or because an agent could?
- Does this accidentally behave like a trading recommendation?
- Did any employer-confidential information enter the repo?
- Did the human reviewer actually inspect agent-written code?

## Failed experiments

Failed experiments are allowed and useful.

If something fails, capture:
- hypothesis;
- approach;
- evidence;
- failure mode;
- what you would try next.

A documented failure is more valuable than an unexplained abandoned branch.
