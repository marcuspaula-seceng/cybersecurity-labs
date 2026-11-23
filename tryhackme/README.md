# TryHackMe Labs

Rooms completed on TryHackMe, documented step by step with screenshots, reasoning and defensive takeaways. Flags are redacted.

## SOC Level 1 path

| Room | Category | Difficulty | Key Techniques / Topics |
|------|----------|-----------|-------------------------|
| [SOC Role in Blue Team](./soc-role-in-blue-team/) | Blue Team / SOC | Easy | Security hierarchy, CISO/Red/GRC/Blue teams, SOC L1/L2, CIRT, MSSP, incident routing |
| [Humans as Attack Vectors](./humans-as-attack-vectors/) | Social engineering | Easy | Phishing, impersonation/deepfake, fake installers, look-alike domains, security policy design |
| [Systems as Attack Vectors](./systems-as-attack-vectors/) | Vulnerability management | Easy | CVEs & patching, misconfigurations, supply chain, root-cause remediation, hardening plan |
| [SOC L1 Alert Triage](./soc-l1-alert-triage/) | Blue Team / SOC | Easy | Alert properties, SIEM queue prioritisation, ownership, TP/FP verdicts |
| [SOC L1 Alert Reporting](./soc-l1-alert-reporting/) | Blue Team / SOC | Easy | Five Ws reports, escalation to L2, communication |
| [SOC Workbooks and Lookups](./soc-workbooks-and-lookups/) | Blue Team / SOC | Easy | Identity & asset inventory, network diagrams, enrichment, workbook design |
| [SOC Metrics and Objectives](./soc-metrics-and-objectives/) | Blue Team / SOC | Easy | FPR, AER, TDR, MTTD/MTTA/MTTR, SLAs, false-positive remediation |
| [Introduction to EDR](./introduction-to-edr/) | Endpoint security | Easy | EDR vs AV, telemetry, process chains, LSASS dumping, IOC triage |
| [Introduction to SIEM](./introduction-to-siem/) | SIEM | Easy | Log sources, ingestion, correlation rules, event 4688 triage, TP verdict |
| [Splunk: The Basics](./splunk-the-basics/) | SIEM / Splunk | Easy | Forwarder/Indexer/Search Head, JSON ingestion, custom index, SPL stats |
| [Introduction to SOAR](./introduction-to-soar/) | SOAR / Automation | Easy | Alert fatigue, orchestration, playbooks, manual vs automated TI workflow |
| [Malware Classification](./malware-classification/) | Malware | Easy | Malware families by behaviour, real cases (Pegasus, Akira, Shamoon), binary vs script |
| [Intro to Malware Analysis](./intro-to-malware-analysis/) | Malware analysis | Easy | REMnux, hashes, PE sections/entropy/imports, Hybrid Analysis, anti-analysis |
| [Living Off the Land Attacks](./living-off-the-land-attacks/) | Detection / LOLBins | Easy | PowerShell IEX, certutil, mshta, rundll32, WMIC, PsExec; malicious vs benign triage |

## Events / CTF

| Room | Category | Difficulty | Key Techniques / Topics |
|------|----------|-----------|-------------------------|
| [Overheard at Breakfast](./overheard-at-breakfast/) | OSINT | Easy | Clue extraction, Gravatar email-hash pivoting (SHA-256), Base64 decoding |
