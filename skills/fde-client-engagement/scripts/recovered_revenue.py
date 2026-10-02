#!/usr/bin/env python3
"""Estimate monthly and yearly revenue recovered by following up quotes nobody chased.

Recovered revenue per month =
    quotes_per_month x share_never_followed_up x reply_rate x close_rate x job_value

Use the client's measured numbers. Example values in the README are illustrative only.

Usage:
    python recovered_revenue.py --quotes 40 --unfollowed 0.30 --reply 0.25 --close 0.40 --job-value 4000
    python recovered_revenue.py --quotes 40 --unfollowed 0.30 --reply 0.25 --close 0.40 --job-value 4000 --fee-share 0.10 --running-cost 40
"""
import argparse
import sys


def share(value, name):
    if not 0 <= value <= 1:
        sys.exit(f"{name} must be between 0 and 1 (for example 0.30 for 30 percent), got {value}")
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--quotes", type=float, required=True, help="quotes sent per month")
    p.add_argument("--unfollowed", type=float, required=True, help="share never followed up, 0 to 1")
    p.add_argument("--reply", type=float, required=True, help="share of chased quotes that reply, 0 to 1")
    p.add_argument("--close", type=float, required=True, help="share of replies that close, 0 to 1")
    p.add_argument("--job-value", type=float, required=True, help="average job value in your currency")
    p.add_argument("--fee-share", type=float, default=0.10, help="your fee as a share of recovered revenue, default 0.10")
    p.add_argument("--running-cost", type=float, default=0.0, help="monthly running cost in the same currency")
    a = p.parse_args()

    unfollowed = share(a.unfollowed, "--unfollowed")
    reply = share(a.reply, "--reply")
    close = share(a.close, "--close")
    fee_share = share(a.fee_share, "--fee-share")
    if a.quotes < 0 or a.job_value < 0 or a.running_cost < 0:
        sys.exit("--quotes, --job-value and --running-cost must not be negative")

    unchased = a.quotes * unfollowed
    replies = unchased * reply
    jobs = replies * close
    monthly = jobs * a.job_value
    fee = monthly * fee_share

    print(f"Quotes never followed up per month : {unchased:,.1f}")
    print(f"Replies after a follow-up          : {replies:,.1f}")
    print(f"Extra jobs closed per month        : {jobs:,.2f}")
    print(f"Recovered revenue per month        : {monthly:,.0f}")
    print(f"Recovered revenue per year         : {monthly * 12:,.0f}")
    print(f"Fee at {fee_share:.0%} of recovered revenue    : {fee:,.0f} per month")
    if a.running_cost:
        print(f"Running cost per month             : {a.running_cost:,.0f}")
        print(f"Fee minus running cost             : {fee - a.running_cost:,.0f} per month")
        if fee < a.running_cost * 2:
            print("Warning: the fee is under twice the running cost. Raise the fee or reduce the scope.")
    print("Every figure above depends on the inputs. Replace illustrative inputs with the client's measured baseline.")


if __name__ == "__main__":
    main()
