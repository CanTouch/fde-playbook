# The method

Tags: **[Source]** is from Vas's talk and slides. **[Adapted]** was added for this repo.

## Core claim [Source]
Applied AI fails when it starts with a tool. The client describes a short process. The real one is longer and has loops. Start with the process and end with measured numbers.

## Stage 1: Map the real process
Three sources, in this order [Source]:
1. **People (the human API).** Start with the head of one department and work down to the people who do the work. Details usually live with long-tenured staff, not in written procedures.
2. **Systems of record.** Live access to the CRM or ERP for 3 to 4 weeks to track inputs, changes and handoffs.
3. **Documents.** SharePoint, Drive, Notion, Slack, Teams, email, spreadsheets, current or stale.

Interview questions [Source]: why do you do it this way, who really decides, which step is theater, which step is legitimate, what happens on an exception, how often do exceptions happen.

[Adapted] Ask for the last three real cases and walk each one step by step. Stories surface exceptions. "What is your process?" gets the brochure.

## Stage 2: Measure time, pick one owner
- Touch time is minutes of real work. Elapsed time is how long the item exists. The gap is usually the problem. [Source]
- Count idle days as a metric. [Source]
- Name one owner for the process and one sponsor with budget. [Adapted from the source's "clear owners" step]

## Stage 3: Sort every step [Source]
Delete, plain code, agent, human decides. The agent prepares and a person decides. See `templates/step-sort.md`.

## Stage 4: Baseline before building [Source]
Measure steps, loops, cycle time, exception rate and cost before you build. See `templates/baseline.csv`.

## Stage 5: Build inside the client's tools [Source]
- Work in their system of record. Route approvals through the messaging tool they already use.
- Prefer background agents to chat sidekicks. The talk cites 10 to 20 percent faster output for copilots and 70 to 80 percent for background agents.
- Benchmark several models per step, including cheaper and open ones.
- Build once and deploy everywhere by grouping clients by software stack.

[Adapted] Small business: if there is no system of record, install one. A database, spreadsheet or the CRM they already pay for is enough.

## Stage 6: Prove it [Source]
Re-measure the same metrics the same way and redraw the map. Enterprise audits at 3 and 6 months. [Adapted] Small business: day 30 and day 90.

## Stage 7: Sell the outcome [Source]
Sell to the person who owns the number. CFO: cost, margin, accuracy, close time. Sales lead: quotes and cycle time. People lead: hiring speed, onboarding, leverage. IT lead: output and working inside current systems. Frame the result as reallocating people. See `references/objections.md`.

## Stage 8: Price it
See `references/pricing.md`.

## Practice routine [Source]
Monday: list every app that holds your data and the routing rules. Tuesday: audit 20 tasks from last week. Wednesday: write one process step by step. Thursday: sort it into the four buckets. Friday: reach out to small businesses and offer to map and automate one workflow.

## Case figures from the talk [Source]
Illustrations of the pattern. Do not promise them.
- Sales quote at a $5B software company: documented as 5 steps, actually 20 steps with 7 loops. 61 percent of requests loop back to step 1, legal sends 12 percent back, 30 percent repeat approval.
- Accounts payable: 17 steps to 7, cycle time 24 days to 6, loops 6 to 1, straight-through 18 percent to 87 percent, cost per invoice $31 to $6.
- Accounting firm with 60 staff: documented as 6 steps, actually 14, with a 70 percent re-ask loop in collections and a 35 percent partner send-back.
