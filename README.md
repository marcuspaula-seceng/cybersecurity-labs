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
| [Overheard at Breakfast](./tryhackme/overheard-at-breakfast/) | OSINT | Easy | Gravatar email-hash pivoting (SHA-256), Base64 decoding |
| [SOC Role in Blue Team](./tryhackme/soc-role-in-blue-team/) | Blue Team / SOC | Easy | Security hierarchy, SOC L1/L2, CIRT, GRC, MSSP, incident routing |
| [Humans as Attack Vectors](./tryhackme/humans-as-attack-vectors/) | Social Engineering | Easy | Phishing, impersonation/deepfake, look-alike domains, security policy |
| [Systems as Attack Vectors](./tryhackme/systems-as-attack-vectors/) | Vulnerability Mgmt | Easy | CVE patching, misconfigurations, supply chain, remediation plan |
| [SOC L1 Alert Triage](./tryhackme/soc-l1-alert-triage/) | Vulnerability Mgmt | Easy | Alert triage, SIEM queue, TP/FP verdicts |
| [SOC L1 Alert Reporting](./tryhackme/soc-l1-alert-reporting/) | Vulnerability Mgmt | Easy | Five Ws reports, L2 escalation |
| [SOC Workbooks and Lookups](./tryhackme/soc-workbooks-and-lookups/) | Vulnerability Mgmt | Easy | Enrichment, identity/asset inventory, workbooks |
| [SOC Metrics and Objectives](./tryhackme/soc-metrics-and-objectives/) | Vulnerability Mgmt | Easy | MTTD/MTTA/MTTR, FPR, SLAs |

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
