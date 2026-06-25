# Week 3 Reflection

> Fill this in after your A* implementation produces a correct route.

---

## How many nodes did A* explore vs Dijkstra on your city query?

A* explored: 243 
Dijkstra explored: 1535 
Saving: 84%

---

## In your own words: why did A* explore fewer nodes?

<!-- 2–3 sentences. Relate it to the heuristic. -->

Dijkstra gives no priority to destination it goes uniformly while searching but A* changes the priority of heap by adding a function which favours the nodes nearer to destination so destination node popped out faster than by dijkstra.

---

## What would happen if your heuristic overestimated the true distance?

<!-- Would A* still find the optimal path? Why / why not? -->

Then it will mislead and take a wrong route thinking the optimal route is not shortest.

---

## What is the Haversine formula actually calculating?

<!-- Not the code — describe it geometrically in plain English. -->

Shortest distance between two points on surface of a sphere.

---

## What did you find surprising about the OSMnx road graph?

<!-- E.g. number of nodes, one-way streets, missing roads, anything. -->

Missing roads and one-way streets.

---

## How does this connect to the ride-hailing system from Week 1?

<!-- Which service in your architecture diagram uses this? -->

Given latitudes, longitudes of riders location and destination, the mapping/routing service uses A* to find shortest path between them.

---

## Time spent this week

9 hours

---

## Self-assessment

| Topic | Rating (1–5) |
|-------|-------------|
| A* algorithm — could implement from memory | 4 |
| Admissible heuristic — understand the requirement | 5 |
| Haversine formula — understand what it computes | 5 |
| OSMnx — comfortable loading a graph and querying it | 3 |
| Bidirectional A* / contraction hierarchies — conceptual understanding | 4 |
