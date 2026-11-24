# TryHackMe Labs

Rooms completed on TryHackMe, documented step by step with screenshots, reasoning and defensive takeaways. Flags are redacted.

> **About dates:** only the year (**2026**) is recorded for these labs. The dates shown on GitHub
> (commit/publish dates) reflect when the write-ups were uploaded to this repository and **do not
> correspond to the actual date each room, task or process was completed**.

## SOC Level 1 path

| Room | Category | Difficulty | Key Techniques / Topics |
|------|----------|-----------|-------------------------|
| [SOC Role in Blue Team](./soc-role-in-blue-team/) | Blue Team / SOC | Medium | Security hierarchy, CISO/Red/GRC/Blue teams, SOC L1/L2, CIRT, MSSP, incident routing |
| [Humans as Attack Vectors](./humans-as-attack-vectors/) | Social engineering | Medium | Phishing, impersonation/deepfake, fake installers, look-alike domains, security policy design |
| [Systems as Attack Vectors](./systems-as-attack-vectors/) | Vulnerability management | Medium | CVEs & patching, misconfigurations, supply chain, root-cause remediation, hardening plan |
| [SOC L1 Alert Triage](./soc-l1-alert-triage/) | Blue Team / SOC | Medium | Alert properties, SIEM queue prioritisation, ownership, TP/FP verdicts |
| [SOC L1 Alert Reporting](./soc-l1-alert-reporting/) | Blue Team / SOC | Medium | Five Ws reports, escalation to L2, communication |
| [SOC Workbooks and Lookups](./soc-workbooks-and-lookups/) | Blue Team / SOC | Medium | Identity & asset inventory, network diagrams, enrichment, workbook design |
| [SOC Metrics and Objectives](./soc-metrics-and-objectives/) | Blue Team / SOC | Medium | FPR, AER, TDR, MTTD/MTTA/MTTR, SLAs, false-positive remediation |
| [Introduction to EDR](./introduction-to-edr/) | Endpoint security | Medium | EDR vs AV, telemetry, process chains, LSASS dumping, IOC triage |
| [Introduction to SIEM](./introduction-to-siem/) | SIEM | Medium | Log sources, ingestion, correlation rules, event 4688 triage, TP verdict |
| [Splunk: The Basics](./splunk-the-basics/) | SIEM / Splunk | Medium | Forwarder/Indexer/Search Head, JSON ingestion, custom index, SPL stats |
| [Introduction to SOAR](./introduction-to-soar/) | SOAR / Automation | Medium | Alert fatigue, orchestration, playbooks, manual vs automated TI workflow |
| [Malware Classification](./malware-classification/) | Malware | Medium | Malware families by behaviour, real cases (Pegasus, Akira, Shamoon), binary vs script |
| [Intro to Malware Analysis](./intro-to-malware-analysis/) | Malware analysis | Medium | REMnux, hashes, PE sections/entropy/imports, Hybrid Analysis, anti-analysis |
| [Living Off the Land Attacks](./living-off-the-land-attacks/) | Detection / LOLBins | Medium | PowerShell IEX, certutil, mshta, rundll32, WMIC, PsExec; malicious vs benign triage |
| [Shadow Trace](./shadow-trace/) | Malware triage (challenge) | Medium | sigcheck/strings IOC extraction, Base64 & char-code decoding, alert correlation |
| [Pyramid of Pain](./pyramid-of-pain/) | Threat intel framework | Medium | Hash→IP→Domain→Artifacts→Tools→TTPs, Any.run/VT reports, fuzzy hashing |
| [Cyber Kill Chain](./cyber-kill-chain/) | Threat modelling | Medium | 7 phases, macros, watering hole, DNS tunneling; Target 2013 breach mapped |
| [Unified Kill Chain](./unified-kill-chain/) | Threat modelling | Medium | 18 phases In/Through/Out, mapping SOC alerts to phases |
| [MITRE](./mitre/) | Threat intel framework | Medium | ATT&CK groups (Mustang Panda, APT33), DET IDs, CAR, D3FEND, ATLAS, AADAPT |
| [Summit](./summit/) | Detection engineering (challenge) | Medium | Hash/IP/DNS blocks, Sigma rules for registry, beaconing and TTPs |
| [Eviction](./eviction/) | Threat intelligence / ATT&CK Navigator | Medium | Mapping APT28 TTPs to hunting hypotheses across the kill chain |
| [Phishing Analysis Fundamentals](./phishing-analysis-fundamentals/) | Phishing / email analysis | Medium | Header triage with grep, Base64 attachment decoding, brand-spoofing IOCs |
| [Phishing Emails in Action](./phishing-emails-in-action/) | Phishing / email analysis | Medium | Six real samples: spoofing, URL shorteners, tracking pixels, credential harvesting, malicious attachments |
| [Phishing Analysis Tools](./phishing-analysis-tools/) | Phishing / sandboxing | Medium | Header analysers, reputation tools, PhishTool, ANY.RUN (CVE-2017-11882) |
| [Phishing Prevention](./phishing-prevention/) | Email security / Wireshark | Medium | SPF/DKIM/DMARC, S/MIME, SMTP response codes, attachment hunting in a pcap |
| [The Greenholt Phish](./the-greenholt-phish/) | Phishing / email triage | Medium | Reply-To mismatch, SPF/DMARC, WHOIS, attachment carving, magic bytes (RAR as CAB) |
| [Snapped Phish-ing Line](./snapped-phishing-line/) | Phishing / threat-actor pivot | Medium | HTML attachment carving, phishing-kit pivot via open directory, credential log, collector email, IR actions |
| [Network Traffic Basics](./network-traffic-basics/) | Network traffic analysis | Medium | Logs vs PCAP vs flow, DNS tunneling, fragmentation, TCP sequence, tap placement |
| [Wireshark: The Basics](./wireshark-the-basics/) | Network traffic analysis | Medium | Capture properties, packet dissection, Expert Info, display filters, Follow Stream, Export Objects |

## Events / CTF

| Room | Category | Difficulty | Key Techniques / Topics |
|------|----------|-----------|-------------------------|
| [Overheard at Breakfast](./overheard-at-breakfast/) | OSINT | Medium | Clue extraction, Gravatar email-hash pivoting (SHA-256), Base64 decoding |
| [Handbook for the Recently Compromised](./handbook-for-the-recently-compromised/) | Windows forensics / EVTX | Medium | Sysmon + PowerShell 4104 timeline, mshta → certutil LOLBin, scheduled-task persistence, Base64 payload |
