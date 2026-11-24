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

## Hack The Box Academy

Step-by-step progress tracker: [hackthebox/academy](./hackthebox/academy/) - *Operating System Fundamentals* path (Linux Fundamentals done, Windows Fundamentals 46.67% in progress, MacOS/Android to do).

---

## TryHackMe Labs

Step-by-step write-ups with screenshots ([index](./tryhackme/)). Flags are redacted.

| Room | Category | Difficulty | Key Techniques |
|------|----------|-----------|----------------|
| [SOC Role in Blue Team](./tryhackme/soc-role-in-blue-team/) | Blue Team / SOC | Medium | Security hierarchy, CISO/Red/GRC/Blue teams, SOC L1/L2, CIRT, MSSP, incident routing |
| [Humans as Attack Vectors](./tryhackme/humans-as-attack-vectors/) | Social engineering | Medium | Phishing, impersonation/deepfake, fake installers, look-alike domains, security policy design |
| [Systems as Attack Vectors](./tryhackme/systems-as-attack-vectors/) | Vulnerability management | Medium | CVEs & patching, misconfigurations, supply chain, root-cause remediation, hardening plan |
| [SOC L1 Alert Triage](./tryhackme/soc-l1-alert-triage/) | Blue Team / SOC | Medium | Alert properties, SIEM queue prioritisation, ownership, TP/FP verdicts |
| [SOC L1 Alert Reporting](./tryhackme/soc-l1-alert-reporting/) | Blue Team / SOC | Medium | Five Ws reports, escalation to L2, communication |
| [SOC Workbooks and Lookups](./tryhackme/soc-workbooks-and-lookups/) | Blue Team / SOC | Medium | Identity & asset inventory, network diagrams, enrichment, workbook design |
| [SOC Metrics and Objectives](./tryhackme/soc-metrics-and-objectives/) | Blue Team / SOC | Medium | FPR, AER, TDR, MTTD/MTTA/MTTR, SLAs, false-positive remediation |
| [Introduction to EDR](./tryhackme/introduction-to-edr/) | Endpoint security | Medium | EDR vs AV, telemetry, process chains, LSASS dumping, IOC triage |
| [Introduction to SIEM](./tryhackme/introduction-to-siem/) | SIEM | Medium | Log sources, ingestion, correlation rules, event 4688 triage, TP verdict |
| [Splunk: The Basics](./tryhackme/splunk-the-basics/) | SIEM / Splunk | Medium | Forwarder/Indexer/Search Head, JSON ingestion, custom index, SPL stats |
| [Introduction to SOAR](./tryhackme/introduction-to-soar/) | SOAR / Automation | Medium | Alert fatigue, orchestration, playbooks, manual vs automated TI workflow |
| [Malware Classification](./tryhackme/malware-classification/) | Malware | Medium | Malware families by behaviour, real cases (Pegasus, Akira, Shamoon), binary vs script |
| [Intro to Malware Analysis](./tryhackme/intro-to-malware-analysis/) | Malware analysis | Medium | REMnux, hashes, PE sections/entropy/imports, Hybrid Analysis, anti-analysis |
| [Living Off the Land Attacks](./tryhackme/living-off-the-land-attacks/) | Detection / LOLBins | Medium | PowerShell IEX, certutil, mshta, rundll32, WMIC, PsExec; malicious vs benign triage |
| [Shadow Trace](./tryhackme/shadow-trace/) | Malware triage (challenge) | Medium | sigcheck/strings IOC extraction, Base64 & char-code decoding, alert correlation |
| [Pyramid of Pain](./tryhackme/pyramid-of-pain/) | Threat intel framework | Medium | Hash→IP→Domain→Artifacts→Tools→TTPs, Any.run/VT reports, fuzzy hashing |
| [Cyber Kill Chain](./tryhackme/cyber-kill-chain/) | Threat modelling | Medium | 7 phases, macros, watering hole, DNS tunneling; Target 2013 breach mapped |
| [Unified Kill Chain](./tryhackme/unified-kill-chain/) | Threat modelling | Medium | 18 phases In/Through/Out, mapping SOC alerts to phases |
| [MITRE](./tryhackme/mitre/) | Threat intel framework | Medium | ATT&CK groups (Mustang Panda, APT33), DET IDs, CAR, D3FEND, ATLAS, AADAPT |
| [Summit](./tryhackme/summit/) | Detection engineering (challenge) | Medium | Hash/IP/DNS blocks, Sigma rules for registry, beaconing and TTPs |
| [Eviction](./tryhackme/eviction/) | Threat intelligence / ATT&CK Navigator | Medium | Mapping APT28 TTPs to hunting hypotheses across the kill chain |
| [Phishing Analysis Fundamentals](./tryhackme/phishing-analysis-fundamentals/) | Phishing / email analysis | Medium | Header triage with grep, Base64 attachment decoding, brand-spoofing IOCs |
| [Phishing Emails in Action](./tryhackme/phishing-emails-in-action/) | Phishing / email analysis | Medium | Six real samples: spoofing, URL shorteners, tracking pixels, credential harvesting, malicious attachments |
| [Phishing Analysis Tools](./tryhackme/phishing-analysis-tools/) | Phishing / sandboxing | Medium | Header analysers, reputation tools, PhishTool, ANY.RUN (CVE-2017-11882) |
| [Phishing Prevention](./tryhackme/phishing-prevention/) | Email security / Wireshark | Medium | SPF/DKIM/DMARC, S/MIME, SMTP response codes, attachment hunting in a pcap |
| [The Greenholt Phish](./tryhackme/the-greenholt-phish/) | Phishing / email triage | Medium | Reply-To mismatch, SPF/DMARC, WHOIS, attachment carving, magic bytes (RAR as CAB) |
| [Snapped Phish-ing Line](./tryhackme/snapped-phishing-line/) | Phishing / threat-actor pivot | Medium | HTML attachment carving, phishing-kit pivot via open directory, credential log, collector email, IR actions |
| [Network Traffic Basics](./tryhackme/network-traffic-basics/) | Network traffic analysis | Medium | Logs vs PCAP vs flow, DNS tunneling, fragmentation, TCP sequence, tap placement |
| [Wireshark: The Basics](./tryhackme/wireshark-the-basics/) | Network traffic analysis | Medium | Capture properties, packet dissection, Expert Info, display filters, Follow Stream, Export Objects |
| [Wireshark: Packet Operations](./tryhackme/wireshark-packet-operations/) | Network traffic analysis | Medium | Conversations/Endpoints/GeoIP, protocol stats, display filters, contains/matches/in, profiles |
| [Wireshark: Traffic Analysis](./tryhackme/wireshark-traffic-analysis/) | Network traffic analysis | Medium | Nmap/ARP-MITM detection, DHCP/NetBIOS/Kerberos, ICMP/DNS tunnelling, FTP, Log4j, TLS decryption, firewall rules |
| [Overheard at Breakfast](./tryhackme/overheard-at-breakfast/) | OSINT | Medium | Clue extraction, Gravatar email-hash pivoting (SHA-256), Base64 decoding |
| [Handbook for the Recently Compromised](./tryhackme/handbook-for-the-recently-compromised/) | Windows forensics / EVTX | Medium | Sysmon + PowerShell 4104 timeline, mshta → certutil LOLBin, scheduled-task persistence, Base64 payload |

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
