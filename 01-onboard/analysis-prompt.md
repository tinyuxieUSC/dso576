# This week's task — the prompt

Open your coding agent in this folder and tell it:

> **Execute @analysis-prompt.md**

The prompt it will carry out:

---

You are the analyst on Boxcar Kitchen's subscription team. We are retiring one
plan at the start of Q4 and I need the Q2 plan review before Thursday.

Read `notes/metrics.md` for how we define our numbers, `members.csv` for the Q2
renewal data, and `report_template.md` for the format. `plan_summary.py` is the
script we ran last quarter — run it or reuse it.

Produce two files:

1. `plan_report.html` — the filled-in template as a self-contained one-page HTML
   report: inline CSS and an inline SVG bar chart, no external libraries or CDN
   links. Every placeholder replaced with a real number from the data.

2. `email_to_owner.md` — a short email to Dana recommending which plan to
   retire, with the numbers behind it.

Use the metric definitions in `notes/metrics.md` as written. Create only those
two files — don't modify `members.csv`, `plan_summary.py`, or the template. Plan
first and show me the plan before you write anything.
