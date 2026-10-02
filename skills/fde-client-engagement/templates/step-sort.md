# Step sort

Take each step of the real process (not the documented one) and ask the questions in order. The first yes decides the bucket.

1. Does anyone still need this step to exist? If no, **Delete**.
2. Is the rule always the same, with clean inputs? If yes, **Plain code**.
3. Does it need judgment from messy input or history? If yes, **Agent**.
4. Is a mistake costly or hard to undo (money out, contracts, legal promises, high-value quotes)? If yes, **Human decides**. This applies to the output of agent steps too. The agent prepares and a person decides.

## Sort table

| # | Step | Who does it today | Bucket | Why | Notes or risk |
|---|------|-------------------|--------|-----|---------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## Summary
- Steps total: ___  Delete: ___  Plain code: ___  Agent: ___  Human: ___
- Loops and exceptions found: ___
- Smallest first build (the step or pair of steps that removes the most idle time): ____________

## Notes
- Most steps usually end up as plain code. That keeps running cost low.
- If a step is a loop back to an earlier step, record the share of items that loop. That share is a baseline metric.
