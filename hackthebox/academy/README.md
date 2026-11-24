# Hack The Box Academy — Learning Path Progress

> **Marcus Paula** | IT Operations Engineer → Security
> HTB Academy user: `marcusovercome` · Year: 2026

Tracker for my Hack The Box Academy studies, starting from the fundamentals. Each module lists what is **done** and the **next steps still to do**, in order.

> **Note on dates:** GitHub's commit dates do not reflect when each section was actually completed — they only show when this tracker was updated.

---

## Overview

| Item | Status |
|------|--------|
| Enrolled Skill Path | **Operating System Fundamentals** (Easy · 4 modules) — 46.7% |
| Modules completed | Learning Process ✅ · Linux Fundamentals ✅ |
| Module in progress | Windows Fundamentals — 46.67% (7 / 15 sections) |
| Weekly streak | 1 week (200 / 200 weekly goal) |

---

## Skill Path: Operating System Fundamentals

| # | Module | Progress | Status |
|---|--------|----------|--------|
| 1 | Linux Fundamentals | 100% | ✅ Completed |
| 2 | Windows Fundamentals | 46.67% | 🔄 In progress |
| 3 | MacOS Fundamentals | 0% | ⏳ To do |
| 4 | Android Fundamentals | 0% | ⏳ To do |

Other modules completed: **Learning Process** ✅

---

## Windows Fundamentals — step by step

| # | Chapter | Section | Type | Status |
|---|---------|---------|------|--------|
| 1 | Introduction | Introduction to Windows | Interactive | ⏳ To do |
| 2 | Core of the Operating System | Operating System Structure | Interactive | ⏳ To do |
| 3 | Core of the Operating System | File System | Interactive | ⏳ To do |
| 4 | Core of the Operating System | NTFS vs. Share Permissions | Interactive | ✅ Done |
| 5 | Core of the Operating System | Windows Registry | Interactive | ✅ Done |
| 6 | Working with Services & Processes | Windows Services & Processes | Interactive | ⏳ To do |
| 7 | Working with Services & Processes | Service Permissions | Theory | ✅ Done |
| 8 | Interacting with Windows | Windows Sessions | Theory | ✅ Done |
| 9 | Interacting with Windows | Interacting with the Windows Operating System | Interactive | ⏳ To do |
| 10 | Interacting with Windows | Windows Management Instrumentation (WMI) | Interactive | ⏳ To do |
| 11 | Further Windows Usage | Microsoft Management Console (MMC) | Theory | ✅ Done |
| 12 | Further Windows Usage | Windows Subsystem for Linux (WSL) | Theory | ✅ Done |
| 13 | Diving Deeper & Close Out | Desktop Experience vs. Server Core | Theory | ✅ Done |
| 14 | Diving Deeper & Close Out | Windows Security | Interactive | 🔄 In progress |
| 15 | Diving Deeper & Close Out | Skills Assessment — Windows Fundamentals | Interactive | ⏳ To do |

**Done:** 7 / 15 — all remaining sections are interactive (target machine + questions).

---

## Next steps (to do, in order)

1. **Windows Security** — finish the section in progress (UAC, ACLs, Defender, security policies).
2. **Introduction to Windows** — connect to the target via RDP, answer the OS/version questions.
3. **Operating System Structure** — boot partition layout, system folders.
4. **File System** — NTFS/FAT32, `icacls` permissions practice.
5. **Windows Services & Processes** — `services.msc`, `Get-Service`, `tasklist`, critical processes (LSASS, svchost).
6. **Interacting with the Windows Operating System** — CMD, PowerShell, execution policy, aliases.
7. **Windows Management Instrumentation (WMI)** — `wmic` / `Get-WmiObject` / `Get-CimInstance` queries.
8. **Skills Assessment — Windows Fundamentals** — final hands-on (users, groups, SMB share, permissions, services, SIDs).
9. Start **MacOS Fundamentals** (Skill Path module 3).
10. Start **Android Fundamentals** (Skill Path module 4) → completes the *Operating System Fundamentals* path.
11. Suggested next module: **Introduction to Networking** (Fundamental · Tier 0).

---

## Why this matters for operations

| Area | Practical link |
|------|----------------|
| Endpoint support | NTFS/share permissions, registry and services are daily service-desk work |
| Hardening | UAC, Defender, service permissions and least privilege |
| Detection | Knowing normal processes (LSASS, svchost) makes abnormal ones stand out in SOC triage |
| Automation | PowerShell + WMI/CIM for inventory and remediation scripts |
