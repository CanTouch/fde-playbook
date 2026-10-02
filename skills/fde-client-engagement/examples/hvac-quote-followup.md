# Worked example: quote follow-up for a home-services contractor

This example is invented to show the method. Every number is illustrative. Replace them with a real client's measured baseline.

## The situation
A 10-person HVAC contractor in the United States. Enquiries arrive by phone, text and web form. A dispatcher writes quotes in the evening. Nobody chases quotes that go quiet.

## Interview highlights (illustrative)
- "Why do you do it this way?" Quotes are written in the evening because the dispatcher is on calls all day.
- "Who really decides?" The owner approves any quote over a set amount.
- "Which step is theater?" Re-typing every enquiry into the scheduling tool by hand.
- "What happens on an exception?" Missing photos or an unclear problem means a call back the next day.
- "How often?" About half of enquiries need a second round of questions.

## Baseline (illustrative)
| Metric | Baseline |
|---|---|
| Quotes sent per month | 40 |
| Share never followed up | 30% |
| Average days from quote to first follow-up (when it happens) | 5 |
| Dispatcher touch time per quote | 20 minutes |
| Enquiries needing a second round of questions | 50% |

## Step sort
| Step | Bucket |
|---|---|
| Re-type enquiry into the scheduling tool | Delete (create the record automatically) |
| Create a lead record when a text, call or form arrives | Plain code |
| Send an instant "got your message" reply | Plain code |
| Extract job type, urgency and missing details from the message | Agent |
| Draft the quote and reply | Agent |
| Approve the price and send | Human |
| Wake up when a quote has no reply after two days | Plain code |
| Draft the follow-up | Agent |
| Confirm a deposit | Human |

## Smallest first build
Capture, log and follow-up timers. It removes the hand re-typing and the idle days, and needs no agent judgment yet.

## Price from the baseline
Run `python scripts/recovered_revenue.py --quotes 40 --unfollowed 0.30 --reply 0.25 --close 0.40 --job-value 4000 --fee-share 0.10 --running-cost 40`.

That gives about 4,800 per month in recovered revenue and a fee near 480 per month at a 10 percent share. For a first client, the free pilot trades that fee for the baseline, the re-measure and permission to publish.

## Day-30 re-measure
Repeat the table with the same method. Show the old and new maps side by side and write the case study from `templates/case-study.md`.
