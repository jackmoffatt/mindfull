---
name: claude-gpt-debate
description: Get a second opinion from OpenAI's GPT on an idea or decision, let Claude and GPT debate where they disagree, and report the common ground. Use when the user asks to "ask GPT", "get ChatGPT's view", "have Claude and GPT debate", "find common ground", or wants two AI opinions on a business, product, naming or design decision.
---

# Claude + GPT debate

Goal: two independent opinions, an honest debate on the disagreements, and a clear common-ground answer the user can act on.

## Before you start
- Tell the user, in one line, that the topic will be sent to OpenAI. Never send secrets, API keys, passwords, or the user's personal details (name, email, location). Describe the idea, not the person.
- The script is `scripts/ask_gpt.py` in this skill's folder. Pipe the prompt on stdin. Set `OPENAI_MODEL` to change the model.

## Steps
1. **Frame it.** Write the question in 2-4 sentences with the context GPT needs (what the product is, who it's for, the decision to make).
2. **Claude answers first, alone.** Write your own position and top 3 reasons before seeing GPT's, so neither anchors the other.
3. **GPT answers alone.** Send GPT only the framed question (not your answer). Ask for a clear position plus its top 3 reasons.
4. **Compare.** List where you agree and where you disagree.
5. **Debate the disagreements (max 2 rounds).** For each disagreement, send GPT your argument and ask it to either concede, hold its ground with a reason, or propose a middle option. Reconsider honestly yourself too; change your view when GPT has the better argument.
6. **Report to the user** in this visual, skimmable format (the user prefers short visual layouts over long text):

| | |
|---|---|
| **Both agree** | bullets |
| **Still disagree** | Claude says X / GPT says Y, one line each |
| **Common ground** | the combined recommendation |
| **Your call** | the one decision only the user can make |

Keep each cell to short bullets. Quote GPT faithfully; don't soften or strengthen what it said.

## If the call fails
- 401/403: the OpenAI key isn't set up. Ask for it with the request_credential tool for host `api.openai.com` (never ask the user to paste a key in chat).
- Blocked host: the environment's network must allow `api.openai.com`.
- Model not found: set `OPENAI_MODEL` to a model the account has.
