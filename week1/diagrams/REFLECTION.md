# Week 1 Reflection

> Fill this in after completing your architecture diagram. Be honest — this is for you, not for marks.

---

## What surprised me most about the architecture

<!-- 2–3 sentences. E.g. "I didn't realise Redis was doing so many different jobs..." -->

I was surprised by how many independent services are involved in a ride-hailing application.I never thought it uses this many services..

---

## The hardest trade-off I had to think through

<!-- E.g. Monolith vs microservices for a first version — what did you decide and why? -->

The hardest trade-off was monolith vs microservices.For a small project I would choose a monolith because it is easier to develop and debug, but large-scale systems like Uber I will go with microservices because teams can scale and deploy services independently.

---

## One question I still have

<!-- Write it down. You will likely answer it yourself by Week 9. -->

How are millions of driver location updated every minute simultaneously without overloading..?

---

## Time spent this week

5 hours

---

## Self-assessment

Rate yourself honestly (1 = still confused, 5 = could explain to someone else):

| Topic | Rating (1–5) |
|-------|-------------|
| Monolith vs microservices trade-offs | 5 |
| What each service in my diagram does | 5 |
| CAP theorem and how it applies | 4 |
| Latency / throughput / availability | 4 |
| Reading architecture diagrams | 5 |
