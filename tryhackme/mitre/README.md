# MITRE — ATT&CK, CAR, D3FEND, ATLAS & AADAPT

| Item | Detail |
|------|--------|
| Platform | TryHackMe — SOC Level 1 path (Cyber Defence Frameworks) |
| Room | [MITRE](https://tryhackme.com/room/mitre) |
| Category | Threat intelligence · Frameworks |
| Difficulty | Easy |
| Date | 23 Nov 2026 |
| Status | ✅ Completed — 8/8 tasks |

> **Goal:** navigate the MITRE ecosystem as a SOC analyst — use ATT&CK to profile threat groups, CAR for detection analytics, D3FEND for countermeasures, and ATLAS/AADAPT for AI and blockchain threats.

---

## How I answered each question (method)

All answers were researched directly on the official MITRE sites:

| Framework | Where I looked |
|-----------|----------------|
| ATT&CK Enterprise matrix | attack.mitre.org → Tactics/Techniques |
| Group profile | attack.mitre.org/groups/G0129 (Mustang Panda), APT33 |
| Detection strategies | Technique page → *Detection Strategies* (DET IDs) |
| CAR | car.mitre.org/analytics/CAR-2019-07-001 |
| D3FEND | d3fend.mitre.org → User Behavior Analysis |
| AADAPT / ATLAS | aadapt.mitre.org, atlas.mitre.org |

## 1. ATT&CK framework

- **Phishing** (T1566) sits under the **Initial Access** tactic.
- **Create Account** = **T1136** (Persistence).

## 2. ATT&CK in operation — Mustang Panda (G0129)

- Based in **China**.
- Delivered *web bugs* to profile targets → **T1598.003** (Phishing for Information: Spearphishing Link).
- Access Token Manipulation via **Cobalt Strike**.

## 3. ATT&CK for threat intelligence — aviation sector

| Step | Finding |
|------|---------|
| Group targeting aviation since 2013 | **APT33** |
| Sub-technique of concern for Office 365 users | **Cloud Accounts** (T1078.004) |
| Tool linked to APT33 for it | **Ruler** |
| Mitigation: remove inactive/unused accounts | **User Account Management** (M1018) |
| Detection strategy | **DET0546** – Detection of abused or compromised cloud accounts |

This is the core TI workflow: *sector → group → techniques → tools → mitigations → detections*.

## 4. CAR (Cyber Analytics Repository)

**CAR-2019-07-001 — Access Permission Modification** → tactic **Defense Evasion**, analytic type **Situational Awareness**.

## 5. D3FEND

Under *User Behavior Analysis*, **User Geolocation Logon Pattern Analysis** analyses the location of logon attempts; its digital artifact is **Network Traffic**.

## 6. Other MITRE projects

| Project | Purpose | Answer |
|---------|---------|--------|
| **AADAPT** | Adversary tactics against digital-asset/blockchain systems | *Scrape Blockchain Data* = **ADT3025** |
| **ATLAS** | Adversarial threats to AI/ML systems | *LLM Prompt Obfuscation* (AML.T0068) → **Defense Evasion** |
| Caldera / Emulation Library | Automated adversary emulation | — |

---

## Key takeaways

1. ATT&CK is the shared language: every alert, report and detection rule should reference a technique ID.
2. Group pages turn "who targets my sector?" into a concrete list of techniques to detect.
3. ATT&CK says *what* attackers do, CAR says *how to detect it*, D3FEND says *how to counter it*.
4. Answer-format tip: when a technique has sub-techniques, always check whether the question expects the sub-technique ID (T1598 **.003**).
