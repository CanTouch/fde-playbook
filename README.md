# FDE Playbook

A Claude skill and a reading guide for running forward-deployed-engineer style AI projects: find the real process, measure it, build inside the client's tools, and prove the result with numbers. It works for a one-person shop serving small businesses and for a team inside a large enterprise.

## What is in here
```
skills/fde-client-engagement/   The skill
  SKILL.md                      Entry point Claude reads
  templates/                    Discovery call sheet, step sort, baseline table, outreach, plans, case study
  references/                   Method, pricing, objections, glossary
  scripts/recovered_revenue.py  Revenue-recovered and fee calculator
  examples/                     A worked example with invented numbers
docs/
  playbook.html                 Long-form guide with diagrams (open in a browser)
  flow.html                     Flowchart of the whole engagement
```

## Use it
**With Claude Code or another agent that reads skills:** copy `skills/fde-client-engagement` into your skills folder, then start a conversation such as:

> New client: an 8-person HVAC contractor. Quotes go cold after the first call. Prepare my discovery call and the baseline table.

**Without an agent:** open `templates/` and fill in the files by hand.

**The calculator:**
```
python skills/fde-client-engagement/scripts/recovered_revenue.py --quotes 40 --unfollowed 0.30 --reply 0.25 --close 0.40 --job-value 4000 --fee-share 0.10
```
The example inputs are illustrative. Use a client's measured baseline.

## The method in eight lines
1. Map the real process with interviews, systems and documents.
2. Measure elapsed time against touch time. Name one owner.
3. Sort every step: delete, plain code, agent or human.
4. Baseline before you build.
5. Build inside the client's own tools. The agent prepares and a person decides.
6. Re-measure the same way and redraw the map.
7. Sell the outcome to whoever owns the number.
8. Price from the measured result.

## Credit and limits
The method comes from Vas of Varick Agents, as presented on Greg Isenberg's Startup Ideas Podcast and in his slides. This repository is an independent adaptation and is not affiliated with or endorsed by Vas, Varick Agents or Greg Isenberg. Watch the original for the full context.

Each file marks what is taken from the source and what is added here. The 30-day small-business plan, the objections, the outreach messages, the price arithmetic and the calculator are additions.

The case-study figures in the source are vendor examples. They show a pattern. Do not promise them to a client. The example in `examples/` uses invented numbers.

Check local law before cold outreach (email consent, SMS and WhatsApp opt-in, data protection) and before processing a client's customer data.

## License
MIT. See `LICENSE`.
