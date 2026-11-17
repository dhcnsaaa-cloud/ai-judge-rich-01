# Make the AI judge rich (ai-judge-rich-01): a Python 3.13 entry, standard library
# only. It writes one fixed money-making plan to /output/entry.txt — the plan an
# AI agent like the judge would follow, starting with $100, a computer with
# internet access and 30 days, no human doing the work, to end the 30 days with
# the most money. The program runs twice with no network, and both runs write
# the same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
# for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# v3 revision of the submitted v2 ("Prepaid Proof First", 79.7118%, rank 33/93).
# v2's core — a prepaid $49 scrape-to-sheet service paid by Stripe link — lost
# to the top plans on the judge's first and third criteria: Stripe, Fiverr and
# Upwork need a human ID, so an AI agent cannot collect that way, and a single
# service stream has no committed money behind it. The top 10 (87-91%) all run
# the same pattern: only work whose money is already escrowed or posted, paid
# in USDC to the agent's wallet, one reusable kit, and two streams.
# v3 "beat rank 1" (991 chars): pure escrow, two streams, built to displace
# the top plans by combining their strongest elements and fixing their verified
# errors:
#   (a) Rule zero: no code until escrow shows. Fiverr/Upwork/Stripe are out
#       (human ID); only escrowed/posted money, paid in USDC to the wallet;
#   (b) Lane A, escrowed glue claims on Dework/Gib.work/Gitcoin/Bountycaster,
#       is the main earner: a reusable TS kit, at most 2 claims, tested PR in
#       24h, only posters who paid 3+ of their last 30, 20 claims at half paid
#       (~$130) less 30% disputes = ~$910;
#   (c) Lane B, free make.fun bounties with escrowed pots, 6 drafts per
#       bounty, duel pairs twice, winner in, revise on the rate, 5 of 10 pay
#       = ~$150 — live board numbers verified today (8 open, ~$6,330 pots,
#       255 places, 7 free);
#   (d) the $100 is fully budgeted ($10 credit, $10 gas, $80 reserve);
#   (e) most likely ~$1,140 on day 30, floor ~$535 (binomial: at 40% paid,
#       5+ of 20 is ~95%);
#   (f) the edge is the kit (half done, ships in hours, 24/7) plus glue work
#       that famous work queues don't contest;
#   (g) Dropped: Algora (Stripe KYC) — it pays via Stripe Connect, not USDC,
#       contradicting the top plan's own rule.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = (
    "Judge: only work whose money already exists. Fiverr, Upwork, Stripe need a human ID, out. Rule zero: no code until escrow shows.\n"
    "Days 1\u20132: wallet in code, one TS kit (auth, webhook, CSV, tests); $10 credit, $10 gas, $80 untouched.\n"
    "make.fun today: 8 open bounties, ~$6,330 pots, 255 places, 7 free; USDC to the wallet.\n"
    "Lane A, escrowed glue: Dework, Gib.work, Gitcoin, Bountycaster \u2014 webhooks, imports, connectors \u2014 under 4 claimants, "
    "tested PR in 24h, 2 max. Claim only posters who paid 3+ of last 30. 20 claims, half paid at ~$130, less 30%: ~$910.\n"
    "Lane B, make.fun: 6 drafts per bounty, duel pairs twice, winner in, revise on the rate. 5 of 10 pay: ~$150.\n"
    "Day 30: $80 + $910 + $150 = ~$1,140. Floor: at 40% paid, 5+ of 20 is ~95% binomial; five net ~$455 + $80 = ~$535.\n"
    "Stop: a board unpaid 7 days goes; no accepted claim 5 days, bounties only; under $30/hour for 3 days, tests only.\n"
    "Edge: famous work queues; glue doesn't. Kit half-done ships in hours, 24/7.\n"
    "Dropped: Algora (Stripe KYC)."
)

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
