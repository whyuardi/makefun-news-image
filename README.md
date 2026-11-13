# The World on 13 November 2026 — news-image-01

One image that sums up the world's news of Friday 13 November 2026: a
night-side globe ringed by six vignettes, each with one short bold label,
titled `13 NOV 2026`.

## The six stories (all first reported 13 November 2026)

1. **Senate summons Huang & Lutnick** — the US Senate Banking Committee
   summoned ex-Nvidia CEO Jensen Huang and Commerce Secretary Howard
   Lutnick to testify (BBC / Al Jazeera).
2. **Zelensky meets US envoys** — Zelensky met US envoys Witkoff and
   Kushner; Europe is brought into the next round of talks (BBC).
3. **Drone hits Russian warship** — a Ukrainian drone hit the Russian
   corvette Naro-Fominsk in the Gulf of Finland, the first such strike
   in open Baltic waters (BBC / Finland confirmed detecting it).
4. **Iran claims strike on US radar in Bahrain** — the IRGC said it
   struck a US early-warning radar site in Bahrain (Al Jazeera; claimed,
   hence "claims" in the label).
5. **FBI: N. Korea $400M crypto hack** — the FBI on North Korean state
   hackers taking $400m+ in crypto from 900+ victims via fake video
   calls (BBC).
6. **US: record 483,200 deportations** — the highest annual
   deportation total in ICE's 23-year history, first reported 13 Nov
   (house canonical list / rung r3). Swapped in for the Microsoft 365
   outage after story verification (2026-11-13): the outage began
   12 Nov, so it failed the date-specific criterion.

## How it was made

The illustration was generated text-free (an image model garbles words),
then the title, six labels and source line were composited with PIL
(DejaVu Sans Bold) so every word is spelled exactly and legible at
~300 px. The image is stored as single-line base64 in `entry.b64`;
`main.py` (stdlib only) decodes it to `/output/entry.png`.

## Gate figures

- Format: JPEG bytes (name stays `entry.png`), 1024 x 1024 px
- Size: 219,404 bytes (limit 1,048,576) — comp-d.jpg
- Deterministic: two runs write identical bytes

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
