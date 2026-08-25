"""Quarterly plan review: renewal rate by plan.

Reads members.csv and prints the standard plan table, lowest renewal rate
first. Definitions are in notes/metrics.md -- this script is just that document
in code, so don't change the arithmetic here without changing that first.

    uv run python plan_summary.py

Written for the Q3 2025 review, rerun each quarter since.  -- M. Ferro
"""

import csv

DATA = "members.csv"

PLAN_NAMES = {
    "starter5": "Starter 5",
    "classic10": "Classic 10",
    "family": "Family Table",
    "athlete": "Trainer",
    "office": "Office Lunch",
    "campus": "Campus",
}


def load(path):
    """Return {plan: [members, renewals]} over the renewal base."""
    totals = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            # The base is the members we reminded (notes/metrics.md).
            if row["reminder_sent"] != "1":
                continue
            plan = row["plan"]
            if plan not in totals:
                totals[plan] = [0, 0]
            totals[plan][0] += 1
            if row["renewed"] == "1":
                totals[plan][1] += 1
    return totals


def main():
    totals = load(DATA)

    rows = []
    for plan, (members, renewals) in totals.items():
        rate = renewals / members if members else 0.0
        rows.append((plan, members, renewals, rate))
    rows.sort(key=lambda r: r[3])

    print("Plan review -- renewal rate by plan, lowest first")
    print("%-14s %9s %9s %9s" % ("plan", "members", "renewals", "rate"))
    print("-" * 44)
    for plan, members, renewals, rate in rows:
        print("%-14s %9d %9d %8.1f%%"
              % (PLAN_NAMES.get(plan, plan), members, renewals, 100 * rate))

    members = sum(r[1] for r in rows)
    renewals = sum(r[2] for r in rows)
    print("-" * 44)
    print("%-14s %9d %9d %8.1f%%"
          % ("all plans", members, renewals, 100 * renewals / members))


if __name__ == "__main__":
    main()
