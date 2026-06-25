# Evidence Gallery

This gallery contains public-safe screenshots and notes extracted from the original forensic report. The goal is to show evidence-handling and artifact-review methodology without publishing raw disk images, private recovered files, full chat logs, or unredacted report pages.

## Evidence Integrity

### MD5 Validation

![MD5 integrity validation](screenshots/md5-integrity-validation.svg)

This screenshot documents the integrity-check step that helped establish the disk image as a valid and unchanged evidence source before deeper review.

## Filesystem and User Artifact Review

### Prefetch Execution Traces

![Prefetch execution traces](screenshots/prefetch-execution-traces.svg)

Prefetch artifacts helped identify which applications had actually executed, including tools relevant to communication, browsing, and possible concealment behavior.

### Documents and Downloads

User-folder review notes captured how documents, compressed archives, downloads, and image files were enumerated and compared against other artifact sources. These are summarized in the repo instead of shown as full screenshots because raw directory listings may expose private names and recovered file details.

## Communication and Artifact Correlation

### Local Chat / Cache Artifact Review

The original report reviewed cache/log material stored in JSON format and converted it to a readable format for analysis. The repo summarizes this as communication-artifact review rather than publishing raw chat content.

## Browser and SQLite Evidence

Firefox `places.sqlite` history was reviewed to correlate web activity with local files and application execution. This supports the investigative narrative but should be published only as a sanitized table or workflow note.

## Data-Hiding Indicators

Steganography and encryption-related indicators were documented in the report. The evidence gallery treats these as leads requiring correlation and follow-up, not as standalone proof.

## Autopsy and USB Lab Evidence

Autopsy lab work showed extension mismatch review, deleted-file listing, USB filesystem interpretation, and artifact-context analysis. The public repo uses summaries and safe tables because raw Autopsy pages can expose sensitive file paths or recovered filenames.

## PCAP Evidence

The PCAP lab covered ARP, DHCP, Kerberos, HTTP executable download identification, SHA256 hashing, and malware-enrichment interpretation. The repo does not publish the raw PCAP or executable file.

## Screenshot Safety Note

Do not upload full report pages. Some source pages include personal/case details, full directory listings, GPS metadata, deleted-file names, account names, or potentially malicious URL/hash material. Use [`screenshot-guide.md`](screenshot-guide.md) and [`redaction-and-publication-checklist.md`](redaction-and-publication-checklist.md) before adding new images.
