# Eazybizman content strategy - weekly rotation

This is the repeatable plan the Wren agent follows to build each Saturday's
batch of images + captions. It replaces the "cover all four pain points
shallowly every week" approach from the 2026-09-04 batch with a themed-week
rotation: one pain point is the target each week, explored in depth across a
fixed set of angles, so four weeks together cover the whole product without
any single week feeling like a repeat of the last.

Never invent a customer quote, a stat, or a claim beyond the four documented
pain points and the Estimate -> Quote -> Deliver -> Get Paid pipeline. That
constraint applies to every week's copy, regardless of theme or angle.

## Platforms: every post goes on all 3 connected channels

Every post in every batch ships to all three connected channels - LinkedIn,
Facebook, and Instagram. Don't omit a channel for an individual slot; the
per-post `Platform(s):` field in each batch's captions file should always
list all three, and the scheduling step should reject (or fix) any batch
where a post is missing one.

## Cadence: 9 pieces a week = 8 static posts + 1 Reel (revised 2026-10-10)

Buffer's free plan holds **10 scheduled posts per channel**. Each week is
therefore **9 pieces in total, and the weekly Reel is one of the 9**: 8 static
posts + 1 video. Never schedule 9 static posts plus a video.

Every post goes to all three channels (LinkedIn, Facebook, Instagram) and the
week runs Monday to Sunday. The operator schedules the following week on the
Saturday evening, so this routine drafts on or before Saturday.

| Day | Slot(s) | Time (Australia/Melbourne) |
|---|---|---|
| Monday | 1 | 9:00 AM |
| Tuesday | 2 | 9:00 AM |
| Wednesday | 3 + the weekly Reel | 9:00 AM; Reel at 5:00 PM |
| Thursday | 4 and 5 (problem -> solution pivot) | 9:00 AM; 5:00 PM |
| Friday | 6 | 9:00 AM |
| Saturday | 7 | 9:00 AM |
| Sunday | 8 (closing call-to-action) | 9:00 AM |

The Reel is made and scheduled in the operator's Saturday-evening interactive
session (it needs image/video tooling and the operator's narration). This
routine only drafts the 8 static captions and a one-line Reel caption idea;
it does NOT create the Reel and the scheduling step must not treat a missing
Reel as an error.

The captions file for each batch (`drafts/YYYY-MM-DD-next-8-posts.md`) records
the day and time for every image so scheduling into Buffer is a direct
lookup, not a judgment call. Always produce exactly 8 static posts per batch.

## The 4-week rotation

The four pain points map 1:1 onto the four pipeline stages, so the rotation
doubles as a walk through the pipeline:

| Week | Target pain point | Pipeline stage |
|---|---|---|
| 1 | Lost margin - the estimate is never checked against real costs | Estimate |
| 2 | Slow quoting - jobs get re-priced from scratch instead of reusing assemblies | Quote |
| 3 | Field data lost - hours/materials/site photos don't make it back to the office | Deliver |
| 4 | Cash-flow drag - deposits/progress claims/invoices chased by hand | Get Paid |

After week 4, repeat from week 1. `rotation-state.json` in this folder
tracks which week ran last (theme, batch number range, next theme due) so
the next scheduled run can advance automatically without re-deriving it.

## The 8-slot weekly template

Every themed week fills the same 8 static slots (plus the Reel), so the
*format* is constant and the *topic* is what rotates.

| # | Slot | Day | Description |
|---|---|---|---|
| 1 | Problem - blunt statement | Mon | "Sound familiar?" style, one-line gut punch |
| 2 | Problem - relatable scenario | Tue | A specific moment in the workday where the pain shows up |
| 3 | Problem - persona angle | Wed | The same pain point as seen by a different person on the job (owner vs. crew vs. office admin) |
| 4 | Problem - cost of inaction | Thu 9:00 AM | What keeps costing you by *not* fixing this - framed conceptually, never with an invented number |
| 5 | Solution - direct contrast | Thu 5:00 PM | "With Eazybizman" answer to slot 1's statement |
| 6 | Solution - outcome-framed | Fri | What changes for you day-to-day once this is fixed |
| 7 | Solution - before/after | Sat | A split framing: before vs. after adopting the fix |
| 8 | Pipeline recap + CTA | Sun | One concrete "how it works" sentence, zooms into this week's stage within the full pipeline, closes with "Book a demo" phrased around this week's pain point |

The old "how it works" slot was folded into slot 8 so the week fits 8 static
posts + the Reel.

## Visual style

All images stay in the existing navy (#1B2340) / orange (#EE6C10) flat card
template established in `01_intro.png` - `10_cta_demo.png`: eyebrow label +
underline, bold headline, logo footer. Persona, before/after, and the
combined pipeline+CTA slots reuse the same template with light layout
variation (a two-column split for before/after, a compact icon strip above
the headline for the closer) rather than introducing new colors or a
different visual language.

## Numbering and files

Each week's batch continues the running numbering from the previous batch
(next batch is `57_` - `64_`, 8 images) and ships with its own
`drafts/YYYY-MM-DD-next-8-posts.md` captions file with day and time columns. Each batch is opened as its own PR - the human
merge is still the only thing that lets a batch reach Buffer.
