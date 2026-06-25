# Redaction and Publication Checklist

Use this checklist before publishing forensic screenshots, case notes, PCAP findings, recovered files, OSINT notes, or lab screenshots.

## Do Not Publish

| Item | Why It Should Not Be Public |
|---|---|
| Raw disk images | They may contain private data, recovered files, credentials, or personal information. |
| Raw PCAPs | They may expose internal IPs, hostnames, usernames, payloads, or malicious URLs. |
| Full chat logs | They may contain personal, sensitive, or victim-related content. |
| Recovered private files | They are evidence, not portfolio material. |
| Exact personal identifiers | Names, DOBs, phone numbers, addresses, and personal accounts should be redacted. |
| Recovered passwords | Never publish passwords, even from a lab. |
| Malware binaries | Do not distribute executable payloads. |
| Full malicious URLs | Use sanitized summaries unless there is a clear defensive reason. |
| Offensive social-engineering instructions | Reframe as defensive awareness and mitigation. |
| Full assignment pages | They may include course metadata, grading context, or unnecessary personal details. |

## Safe to Publish

| Safer Artifact | Condition |
|---|---|
| Workflow diagrams | Use self-created SVG or Mermaid diagrams. |
| Hash-validation screenshots | Crop paths and identifiers where possible. |
| Prefetch screenshots | Crop to executable evidence and remove private paths. |
| Evidence matrices | Generalize names and sensitive findings. |
| PCAP summaries | Summarize ARP/DHCP/Kerberos/HTTP workflow without raw PCAP. |
| Metadata lessons | Explain EXIF/GPS privacy without exposing personal locations. |
| Autopsy methodology | Use sanitized tables instead of raw recovered-file listings. |
| Defensive OSINT notes | Explain risk and controls, not attack instructions. |

## Public Disclaimer to Keep

> This repository is for defensive education and portfolio demonstration only. It does not contain raw disk images, raw PCAPs, recovered private data, real victim information, offensive social-engineering instructions, malware binaries, passwords, or unredacted assignment pages.

## Final Pre-Publish Review

Before pushing any new file:

- [ ] No raw disk image, PCAP, recovered file, or executable payload is included.
- [ ] No personal identifiers, DOBs, phone numbers, addresses, or private chat content appear.
- [ ] No recovered passwords, credentials, tokens, or secrets appear.
- [ ] No exact malicious URL is published unless sanitized and justified.
- [ ] No offensive social-engineering steps are included.
- [ ] No full assignment page, cover page, or grading context appears.
- [ ] Screenshots are cropped to the forensic method being demonstrated.
- [ ] Findings distinguish confirmed artifacts from hypotheses and limitations.

## Good GitHub Hygiene

- Prefer concise Markdown artifacts over raw reports.
- Use diagrams and evidence tables for portfolio clarity.
- Keep all source evidence private.
- Document limitations honestly.
- Maintain a professional DFIR tone.
