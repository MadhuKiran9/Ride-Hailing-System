# Week 2 Reflection

> Fill this in after your Dijkstra implementation passes verification.

---

## Did your implementation pass verification on the first try?

<!-- Yes / No. If no, what was the bug? -->
Yes

---

## What was the hardest part to implement?

<!-- Path reconstruction? The heap logic? The visited-set check? -->
Heap logic and Path reconstruction

---

## In your own words: why does Dijkstra need a min-heap?

<!-- Write 2–3 sentences as if explaining to a classmate. -->
In dijkstra everytime we need to take out a node with smallest distance, for finding the smallest number among n nodes if we follow normal checking we need to scan all nodes which would take O(n) time but in a min-heap the smallest element is always at the top and it takes O(logn) time only..

---

## Why would Dijkstra give wrong answers on a graph with negative edge weights?

<!-- Describe the scenario where it breaks. -->
Because in dijkstra we always think if one node is popped out its smallest distance is fixed which is true only when there are no negative edge weights because in dijkstra we always add a weight to the current distance but if the weight is negative it will decrease the current distance and may make it less than already fixed smallest distance for a popped out node.

---

## How does this connect to ride-hailing?

<!-- Where in the system you designed in Week 1 would Dijkstra (or a variant) run? -->
In ride-hailing we need to find shortest path from rider location to his destination in a city. We started with a graph because we can think of a city as a graph with nodes as places and edges being roads connecting them and weights being the distance between them.
---

## Time spent this week

7 hours

---

## Self-assessment

| Topic | Rating (1–5) |
|-------|-------------|
| Adjacency list vs matrix — know when to use each | 5 |
| BFS and DFS — could implement from memory | 4 |
| Dijkstra — could implement from memory | 4 |
| Min-heap / heapq — understand how it works | 5 |
| Time complexity O((V+E) log V) — understand the derivation | 5 |
