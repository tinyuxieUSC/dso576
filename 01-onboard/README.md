# Boxcar Kitchen — subscription team

**Boxcar Kitchen** is a meal-prep delivery service in Frogtown that drops
chilled boxes across east LA three mornings a week. Six plans, about 3,000
active members, one small team. This is the subscription team's working repo,
and the DSO-576 Module 1 repo.

You are the analyst on the subscription team. Boxcar is carrying one plan too
many — six plans means six menus, six pack lines, six promo calendars — and Dana
(the owner) has decided **one plan gets retired at the start of Q4.** Your job
this week is the Q2 plan review that tells her which one.

## What's in this repo

| File | What it is |
|---|---|
| `README.md` | This file. |
| `analysis-prompt.md` | This week's task, written as a prompt. Tell your agent: *"Execute @analysis-prompt.md"* |
| `members.csv` | The data: one row per member whose subscription came up for renewal in Q2 2026 (April–June). Columns: `member_id`, `plan`, `renewal_month`, `reminder_sent`, `renewed`. |
| `notes/metrics.md` | The team's metric definitions — what a renewal rate is here, and what the columns mean. |
| `plan_summary.py` | The script the last analyst ran each quarter. Plain Python, no pandas. Run it with `uv run python plan_summary.py`. |
| `report_template.md` | The standard one-page plan review. Same shape every quarter. |
| `AGENTS.md` | The house rules a coding agent follows in this repo. |
| `plan_memo.md` | The template for what you hand in. Fill it in and upload it to Brightspace. |
| `tutor.md` | Instructions your own agent can read to tutor you for Quiz 1. |

## The plans

| Code | Plan | Who it's for |
|---|---|---|
| `starter5` | Starter 5 | Five meals a week, the entry plan |
| `classic10` | Classic 10 | Ten meals a week, the core plan |
| `family` | Family Table | Four-serving dinners, biggest box |
| `athlete` | Trainer | High-protein, sold through gyms |
| `office` | Office Lunch | Workplace delivery, billed to the company |
| `campus` | Campus | Discounted student plan, sign-up is in the app |

## Working here

This repo is public and read-only to you: you clone it once, work on your own
machine, and never push. Your handout has the clone commands and this week's
steps.

Nothing is handed in through GitHub. The one thing you submit for this module is
**`plan_memo.md`**, filled in and uploaded to **Brightspace** before Quiz 1.

To practice for the quiz, tell your agent: *"Read tutor.md and tutor me."*
