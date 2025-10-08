# Week 5 – Network Connectivity Monitoring

## Objective

Expand your system monitor by adding **network availability checks**.  
You will now log not only CPU/memory/disk usage, but also **whether the system can reach the internet**.

---

## Tasks

1. Use `subprocess` to ping `8.8.8.8` (Google DNS).
2. Record the result:
   - `Ping_Status`: either `"UP"` or `"DOWN"`
   - `Ping_ms`: ping response time in milliseconds (or `-1` if failed)
3. Combine this with your previous log fields:
   - Timestamp, CPU, Memory, Disk, Ping_Status, Ping_ms
4. Append 5 log entries with a 10-second delay between each.

---

## Example `log.csv` output
Timestamp,CPU,Memory,Disk,Ping_Status,Ping_ms
2025-09-21 14:00:01,18.2,40.3,58.7,UP,21.3
2025-09-21 14:00:11,20.4,42.5,58.9,UP,22.1
2025-09-21 14:00:21,21.1,43.8,59.0,DOWN,-1
…
---

## Submission Checklist

- [ ] `main.py` contains ping function and parsing logic  
- [ ] `log.csv` contains 5 entries including ping status  
- [ ] Screenshot of either terminal or CSV file  
- [ ] Code pushed to GitHub repo

---

## Copilot Prompt (for help)

> “Ping 8.8.8.8 in Python and extract the response time using subprocess”

---

Let your instructor know if you're using Windows – ping syntax may differ!
