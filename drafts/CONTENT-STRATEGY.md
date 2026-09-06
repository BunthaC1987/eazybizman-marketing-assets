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

## Cadence: 9 posts, Monday through Sunday

Batches run on a **9-post cadence**, not 10. When this routine runs on a
Saturday, Buffer already has a post queued for the very next day (Sunday)
left over from the prior batch, so only 9 new posts are needed to fully
staff the upcoming Monday-Sunday week. Since 9 doesn't divide evenly across
7 days, two days carry a double post:

| Day | Slot(s) |
|---|---|
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4, 5 (problem -> solution pivot) |
| Friday | 6 |
| Saturday | 7 |
| Sunday | 8, 9 (closing double post) |

The captions file for each batch (`drafts/YYYY-MM-DD-next-N-posts.md`)
records the day assignment for every image so scheduling into Buffer is a
direct lookup, not a judgment call.

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

## The 9-slot weekly template

Every themed week fills the same 9 slots, so the *format* is constant and
the *topic* is what rotates. This is what gives each week internal cohesion
instead of the grab-bag mix used in the very first (2026-09-04) batch.

| # | Slot | Day | Description |
|---|---|---|---|
| 1 | Problem - blunt statement | Mon | "Sound familiar?" style, one-line gut punch |
| 2 | Problem - relatable scenario | Tue | A specific moment in the workday where the pain shows up |
| 3 | Problem - persona angle | Wed | The same pain point as seen by a different person on the job (owner vs. crew vs. office admin) |
| 4 | Problem - cost of inaction | Thu | What keeps costing you by *not* fixing this - framed conceptually, never with an invented number |
| 5 | Solution - direct contrast | Thu | "With Eazybizman" answer to slot 1's statement |
| 6 | Solution - outcome-framed | Fri | What changes for you day-to-day once this is fixed |
| 7 | Solution - before/after | Sat | A split framing: before vs. after adopting the fix |
| 8 | Solution - how it works | Sun | One concrete mechanic, explained in a single sentence |
| 9 | Pipeline recap + CTA | Sun | Zooms into this week's stage within the full pipeline, closes with "Book a demo" phrased around this week's pain point |

Slots 9 combines what used to be two separate images (a pipeline recap and a
generic CTA) into one closing card, so the problem/solution depth (4 + 4)
stays intact within a 9-image budget.

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
(e.g. week 1 of this rotation is `21_` - `29_`, week 2 is `30_` - `38_`,
etc.) and ships with its own `drafts/YYYY-MM-DD-next-9-posts.md` captions
file with a day column. Each batch is opened as its own PR - the human
merge is still the only thing that lets a batch reach Buffer.
