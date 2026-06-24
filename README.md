# Digital Forensics Evidence Lab

## Overview

This repository documents a digital forensics investigation workflow built around the analysis of a seized disk image in a criminal investigation scenario. It emphasizes evidence integrity, artifact correlation, timeline reconstruction, and clear reporting suitable for case-oriented forensic work.

## Objectives

- validate forensic evidence integrity
- review key user and system artifacts
- reconstruct activity across communications, files, and browsing history
- identify evidence of concealment, coordination, or suspicious intent
- present findings in a clear and defensible case summary

## Project Highlights

- Verified evidence integrity using hash validation
- Examined a forensic image in read-only mode
- Reviewed Prefetch artifacts, Discord cache content, browser history, downloaded files, and user directories
- Correlated communication records with on-disk artifacts and suspicious tools
- Documented suspected use of steganography and encrypted volumes
- Produced a case-style narrative with findings, limitations, and next investigative steps

## Investigation Workflow

1. Validate the seized image and preserve read-only handling.
2. Review recently executed applications and user activity traces.
3. Extract and interpret communication artifacts from local cache data.
4. Examine files, downloads, and browser history for corroborating evidence.
5. Build a timeline across communications, applications, and files.
6. Summarize findings, limitations, and follow-up actions.

## Key Findings

- Artifacts suggested the use of Discord for suspicious coordination and file exchange.
- Evidence pointed to the presence of steganography tooling and encrypted storage mechanisms.
- Browser and filesystem artifacts reinforced the operational narrative built from communication logs.
- The report linked user behavior, files of interest, and application usage into a coherent case story.

## Skills Demonstrated

`Digital Forensics` `Evidence Handling` `Artifact Analysis` `Timeline Reconstruction` `Hash Validation` `Forensic Reporting` `SQLite/Browser History Review` `Case Documentation`

## Suggested Repository Structure

```text
.
├── README.md
├── docs/
├── evidence-notes/
├── timeline/
└── report/
```

## Notes

This repository should be framed as a forensic case study and methodology portfolio piece, with sanitized evidence descriptions and strong emphasis on analytical process.
