# Cybersecurity Labs

> **Marcus Paula** | Security and infrastructure study notes

Study write-ups of HackTheBox exercises and offensive techniques, with mappings to defensive controls. These notes do not establish enterprise deployment, measured risk reduction or a competition ranking.

---

## Operational Relevance

Understanding attacker techniques informs better defensive decisions.
Each lab connects techniques to potential defensive applications:

| Area | Potential application |
|-----|-------------|
| **Risk Exposure Index** | Identifying misconfiguration patterns (SUDO, NFS, wildcard injection) before attackers do |
| **Security Incident Rate** | Recognising lateral movement TTPs used in real incidents (MITRE ATT&CK) |
| **Change Success Rate** | Exploit path awareness drives safer change management and hardening procedures |
| **Automation Rate** | Candidate detection ideas to validate in an isolated lab |

---

## Learning Scope

The write-ups below cover Linux exploitation paths and defensive lessons. Competition results and professional certifications are omitted until their supporting records are verified.

---

## HackTheBox Writeups

| Machine | Difficulty | OS | Key Techniques |
|---------|-----------|-----|----------------|
| [Joker](./hackthebox/joker/) | Hard | Linux | TFTP, Squid proxy, Werkzeug RCE, sudoedit CVE-2015-5602, tar wildcard |
| [Falafel](./hackthebox/falafel/) | Hard | Linux | Blind SQLi, PHP type juggling, wget truncation, framebuffer, debugfs |
| [Jail](./hackthebox/jail/) | Insane | Linux | Stack BOF, NFS UID spoofing, rvim escape, RSA Wiener attack |
| [Calamity](./hackthebox/calamity/) | Hard | Linux | PHP eval RCE, audio steganography, ret2mprotect ROP chain |

---

## TryHackMe Labs

Step-by-step write-ups with screenshots ([index](./tryhackme/)). Flags are redacted.

| Room | Category | Difficulty | Key Techniques |
|------|----------|-----------|----------------|
| [SOC Role in Blue Team](./tryhackme/soc-role-in-blue-team/) | Blue Team / SOC | Easy | Security hierarchy, CISO/Red/GRC/Blue teams, SOC L1/L2, CIRT, MSSP, incident routing |
| [Humans as Attack Vectors](./tryhackme/humans-as-attack-vectors/) | Social engineering | Easy | Phishing, impersonation/deepfake, fake installers, look-alike domains, security policy design |
| [Systems as Attack Vectors](./tryhackme/systems-as-attack-vectors/) | Vulnerability management | Easy | CVEs & patching, misconfigurations, supply chain, root-cause remediation, hardening plan |
| [SOC L1 Alert Triage](./tryhackme/soc-l1-alert-triage/) | Blue Team / SOC | Easy | Alert properties, SIEM queue prioritisation, ownership, TP/FP verdicts |
| [SOC L1 Alert Reporting](./tryhackme/soc-l1-alert-reporting/) | Blue Team / SOC | Easy | Five Ws reports, escalation to L2, communication |
| [SOC Workbooks and Lookups](./tryhackme/soc-workbooks-and-lookups/) | Blue Team / SOC | Easy | Identity & asset inventory, network diagrams, enrichment, workbook design |
| [SOC Metrics and Objectives](./tryhackme/soc-metrics-and-objectives/) | Blue Team / SOC | Easy | FPR, AER, TDR, MTTD/MTTA/MTTR, SLAs, false-positive remediation |
| [Introduction to EDR](./tryhackme/introduction-to-edr/) | Endpoint security | Easy | EDR vs AV, telemetry, process chains, LSASS dumping, IOC triage |
| [Introduction to SIEM](./tryhackme/introduction-to-siem/) | SIEM | Easy | Log sources, ingestion, correlation rules, event 4688 triage, TP verdict |
| [Splunk: The Basics](./tryhackme/splunk-the-basics/) | SIEM / Splunk | Easy | Forwarder/Indexer/Search Head, JSON ingestion, custom index, SPL stats |
| [Introduction to SOAR](./tryhackme/introduction-to-soar/) | SOAR / Automation | Easy | Alert fatigue, orchestration, playbooks, manual vs automated TI workflow |
| [Malware Classification](./tryhackme/malware-classification/) | Malware | Easy | Malware families by behaviour, real cases (Pegasus, Akira, Shamoon), binary vs script |
| [Intro to Malware Analysis](./tryhackme/intro-to-malware-analysis/) | Malware analysis | Easy | REMnux, hashes, PE sections/entropy/imports, Hybrid Analysis, anti-analysis |
| [Living Off the Land Attacks](./tryhackme/living-off-the-land-attacks/) | Detection / LOLBins | Easy | PowerShell IEX, certutil, mshta, rundll32, WMIC, PsExec; malicious vs benign triage |
| [Shadow Trace](./tryhackme/shadow-trace/) | Malware triage (challenge) | Easy | sigcheck/strings IOC extraction, Base64 & char-code decoding, alert correlation |
| [Overheard at Breakfast](./tryhackme/overheard-at-breakfast/) | OSINT | Easy | Clue extraction, Gravatar email-hash pivoting (SHA-256), Base64 decoding |

---

## Techniques Mapped to MITRE ATT&CK

| Technique | ATT&CK ID | Seen In |
|-----------|-----------|---------|
| Sudo exploitation | T1548.003 | Joker, Jail |
| Wildcard injection via cron | T1053.003 | Joker |
| NFS share abuse | T1039 | Jail |
| Web shell upload | T1505.003 | Falafel, Calamity |
| Credential access via config files | T1552.001 | Falafel, Joker |
| Steganography | T1027.003 | Calamity |
| Buffer overflow | T1203 | Jail, Calamity |

---

## Related Study Topics

MITRE ATT&CK mapping, forensic methodology and network security. These topics are learning areas, not claims of a completed professional award.

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Marcus_Paula-0077B5?style=flat-square&logo=linkedin)](https://linkedin.com/in/marcuspaula)
[![GitHub](https://img.shields.io/badge/GitHub-marcuspaula--seceng-181717?style=flat-square&logo=github)](https://github.com/marcuspaula-seceng)


---

## Classification

**Study Notes** — part of the [`marcuspaula-security-portfolio`](https://github.com/marcuspaula-seceng/marcuspaula-security-portfolio) hub.

This repository contains study write-ups with embedded command and code examples. It is not a packaged or validated engineering project, and does not establish production execution.
