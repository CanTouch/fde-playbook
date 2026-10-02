---
name: fde-client-engagement
description: Run a forward-deployed-engineer style AI project for a client. Covers the discovery interview, baseline metrics, four-bucket step sort, outcome pitch, pricing from the baseline and a dated plan, for small businesses and enterprises.
---

# FDE client engagement

Use this skill when someone is about to build an AI agent or automation inside a real business process and wants to do it the forward deployed engineer way: map the real process, measure it, build inside the client's tools, and prove the result with numbers.

The method is adapted from Vas of Varick Agents (Greg Isenberg's Startup Ideas Podcast). See `references/method.md` for the stages and what is adapted.

## 1. Establish the situation
Ask only for what is missing, in one short message:
- Client type and size (1-50 people, or enterprise) and the trade or function.
- The one process in scope.
- Who owns that process and who sponsors the project.
- Stage: before the first call, after the call, building, or measuring.

## 2. Run the stages in order
Read the matching file when you reach the stage.

| Stage | What to do | File |
|---|---|---|
| Discovery | Run or prepare the 20 minute call and the six interview questions | `templates/discovery-call.md` |
| Map and measure | Three real cases, systems, documents. Separate elapsed time from touch time | `references/method.md` |
| Sort | Delete, plain code, agent or human for every step | `templates/step-sort.md` |
| Baseline | Fill the table and have the owner confirm it | `templates/baseline.csv` |
| Outreach | First message and follow-ups | `templates/outreach.md` |
| Pitch | Sell the outcome to whoever owns the number | `references/objections.md` |
| Price | Free first project, fixed fee, then value-based | `references/pricing.md`, `scripts/recovered_revenue.py` |
| Plan | 30-day small business plan or 8-week enterprise plan | `templates/engagement-plan.md` |
| Prove | Re-measure and write the case study | `templates/case-study.md` |

A worked example is in `examples/hvac-quote-followup.md`.

## 3. Output rules
- Never invent client numbers. Mark every assumption and every illustrative figure.
- Prefer real timestamps and exports over owner estimates. Use the owner's answer to decide where to look.
- The agent prepares and a person decides anything involving money, contracts or promises.
- Build inside the tools the client already uses. If they have no system of record, add one.
- One process, one owner. Do not take on several processes at once.
- Case-study figures from the source material show a pattern. Do not promise them to a client.
- The retainer guidance and the 30-day small-business plan are adaptations, not part of the source. Say so if asked.

## 4. When asked for a deliverable
Produce it from the template, filled with the client's own details: a call sheet, a step map with bucket sort, a baseline table, a pitch for the buyer's role, a dated plan, or a case study. Keep client names out of anything meant to be shared, and describe the client by trade and region.
