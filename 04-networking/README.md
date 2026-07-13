# 🌐 04 — Networking

This folder collects **common networking knowledge for cybersecurity**. Almost
every security topic — attacks, defenses, monitoring, incident response — sits on
top of how networks actually move data around. You can't secure, exploit, or
investigate something you don't understand, so these notes build that foundation
first.

## What this folder covers

- **Core networking concepts** — how devices find and talk to each other (IP, MAC,
  DNS, ports, protocols, the OSI/TCP-IP models).
- **The "why it matters for security" angle** — for each concept, where it shows up
  in attacks and defenses (e.g. why DNS is a common exfiltration channel, why NAT
  hides internal hosts, why ports map to services you can scan).
- **Real-world examples** — plain-English analogies and "what actually happens when
  you load a website" style walkthroughs, so the theory sticks.

Much of this is inspired by **CompTIA Network+ (Net+)** fundamentals, framed toward
security rather than pure network administration.

## Files in this folder

| File | What's inside |
|------|---------------|
| [`GeneralKnowledge.md`](GeneralKnowledge.md) | Foundational networking terms & concepts, each with an explanation, why it matters for security, and a real-life example. |

> 📌 More topic-specific notes (protocols deep-dives, subnetting practice, packet
> analysis, common attacks) will be added as separate files over time.
