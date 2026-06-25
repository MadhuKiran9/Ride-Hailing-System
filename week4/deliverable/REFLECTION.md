# Week 4 Reflection

> Fill this in after your nearby-drivers service hits the under-50ms target.

---

## Which approach did you use? Why?

<!-- Redis GEOSEARCH / your own H3 k-ring / your own geohash prefix -->

I used H3 k-ring lookup. H3 avoids geohash boundary problems and makes it easy to search nearby cells using k-ring.

---

## What was your measured query time?

Average over 100 runs: 13 ms

---

## In your own words: why does bucketing beat scanning all drivers?


<!-- 2–3 sentences -->

Instead of checking all 10,000 drivers, H3 first finds a small set of nearby cells. Then only drivers inside those cells are checked, which makes the search much faster.

---

## Describe the boundary edge case in your own words

<!-- What goes wrong if you only search the exact matching cell, with no neighbours? -->

A driver can be very close to the rider but be located in a neighbouring cell. If we only search the rider's cell, that nearby driver might be missed.

---

## Why does Uber use hexagons instead of squares for H3?

<!-- Explain the equidistant-neighbour property -->

Every hexagon has 6 neighbours at roughly equal distance. This makes neighbour searches more consistent compared to squares.

---

## What resolution / precision did you choose, and why?

<!-- Too coarse = too many candidates to rank. Too fine = might miss nearby drivers
in an adjacent cell. What tradeoff did you land on? -->

I used resolution 7. It is detailed enough to reduce the number of candidates while still covering nearby drivers in neighbouring cells.

---

## How does this connect to the dispatch service in your Week 1 architecture?

The dispatch service needs to find nearby drivers for a rider request. H3 helps quickly find those nearby drivers before matching them. 

---

## Time spent this week

9 hours

---

## Self-assessment

| Topic | Rating (1–5) |
|-------|-------------|
| Geohash encoding and prefix search | 4 |
| The boundary-straddling edge case and its fix | 4 |
| Quadtrees / R-trees — conceptual understanding | 4 |
| H3 hexagons — why they're used and how k-ring works | 5 |
| Could explain "why not just scan all drivers" to a non-technical person | 5 |
