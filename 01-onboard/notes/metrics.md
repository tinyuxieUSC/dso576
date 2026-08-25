# How Boxcar Kitchen measures the subscription book

Short reference for anyone (person or agent) working on a plan review. If a
number appears in a report or an email to Dana, it is defined here.

Last revised: 2026-04-02 (M. Ferro)

## The renewal base

A member enters the **renewal base** in the month their term comes up. Four
weeks out, billing hands marketing a list and marketing sends the renewal
reminder — the "your box renews on the 14th" email with the pause/swap links.

The base is **the members we reminded**. Members we can't reach by email —
opted out, bounced, app-only signups who never confirmed an address — are not
part of the base. We can't act on them, so we don't hold the rate responsible
for them.

This is the definition we settled on in 2023 when marketing rebuilt the reminder
flow, and every plan review since has used it: a rate is only useful if it moves
when we do something, and the reminder is the thing we do.

## Renewal rate

    renewal rate = renewals ÷ renewal reminders sent

Both sides of that fraction come from the same group: the members we reminded
this quarter. It is the number we put at the top of a plan review.

**"Members," in a plan review, means the renewal base** — reminders sent. When a
report says a plan has 90 members, that is 90 reminded members, not the whole
roster. Say "members" in the report; the base is understood.

## What counts as a renewal

A member renewed if the next term billed successfully in the renewal month.
Pauses, downgrades, and plan switches are all *not* renewals of that plan.
Refunds after the fact don't reverse it — we count the bill, not the outcome.

## Plan health and the retire decision

We review the six plans together, ranked by renewal rate, lowest first. **The
plan with the lowest renewal rate is the retire candidate.** Two quarters at
the bottom of the pack and it goes to Dana with a recommendation.

Don't rank on revenue. A plan can bill well for a quarter and still be bleeding
members, and by the time revenue reflects it we've lost the cohort.

## `members.csv`

The quarterly export from billing, one row per member due for renewal in the
quarter.

| column | meaning |
|---|---|
| `member_id` | account number |
| `plan` | plan code: `starter5`, `classic10`, `family`, `athlete`, `office`, `campus` |
| `renewal_month` | the month the member's term came up |
| `reminder_sent` | `1` if the renewal reminder went out to them that month |
| `renewed` | `1` if the next term billed |

Email coverage isn't uniform across plans; it follows how each plan signs people
up. Office Lunch members come in through a company address, so nearly all of
them are reachable. Campus sign-ups happen in the app, where confirming an
email is a separate step most people skip.

## House rules of thumb

- Don't blend quarters. A plan review covers one quarter.
- Don't compare a rate across plans without the counts next to it; `athlete` is
  small enough that a few members move it a point.
- Round rates to one decimal. Round counts never.
- `plan_summary.py` is the script the numbers come from. If a report disagrees
  with it, the report is wrong.
