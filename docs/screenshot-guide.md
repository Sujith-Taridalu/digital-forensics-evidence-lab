# Screenshot and Image Guide

Use screenshots carefully. Digital-forensics screenshots can easily expose names, private file paths, recovered files, chat content, GPS data, hashes, or case details. Prefer diagrams, sanitized tables, and tightly cropped tool evidence.

## Recommended Screenshot Locations

| Screenshot File | Folder | Use In | What It Should Show |
|---|---|---|---|
| `md5-integrity-validation.svg` | `docs/screenshots/` | README, `evidence-handling.md` | Hash-validation step for the forensic image. |
| `prefetch-execution-traces.svg` | `docs/screenshots/` | README, `artifact-correlation.md` | Execution traces for tools/applications, with private paths minimized. |
| `discord-cache-json-sanitized.png` | `docs/screenshots/` | `artifact-correlation.md` | Sanitized cache/log existence only, not full chats. |
| `documents-downloads-sanitized.png` | `docs/screenshots/` | `forensic-case-study.md` | Sanitized directory listing without private victim details. |
| `autopsy-extension-mismatch.png` | `docs/screenshots/` | `autopsy-usb-analysis.md` | Extension mismatch table with sensitive paths redacted. |
| `wireshark-pcap-summary.png` | `docs/screenshots/` | `pcap-network-forensics.md` | Cropped Wireshark view showing protocol type only, not full PCAP. |
| `exif-metadata-sanitized.png` | `docs/screenshots/` | `steganography-metadata-lab.md` | Metadata categories, not private GPS data unless fictional/training-only. |

## Images From Uploaded Documents: Safe or Not?

| Source Image Type | Publish? | Reason |
|---|---|---|
| Hash validation terminal screenshot | Usually safe after crop | Good evidence-handling proof; crop path/user details if possible. |
| Prefetch listing | Usually safe after crop | Useful execution evidence; avoid full private paths. |
| Discord cache/log screenshot | Not raw | Do not publish actual chat content or personal identifiers. |
| Documents/Downloads folder screenshots | Not raw | Can reveal private file names and people; sanitize first. |
| Suitcase/evidence photo | Avoid | Adds little technical portfolio value and may look sensational. |
| Steganography histogram screenshot | Maybe | Safe if it does not expose personal browser/session details. |
| EXIF/GPS screenshot | Not raw | GPS/location data should be generalized unless it is clearly a training image. |
| Autopsy deleted-file lists | Maybe after redaction | Can expose private filenames; crop and sanitize. |
| Wireshark PCAP screenshots | Maybe after redaction | Avoid raw PCAP upload, payloads, and full malicious URLs. |

## Best Practice

For this repo, use:

- self-created SVG diagrams for workflow;
- sanitized screenshots only when they prove a forensic method;
- captions explaining what the screenshot supports;
- Markdown tables instead of raw screenshots when the screenshot contains sensitive details.

## Markdown Example

```md
![MD5 integrity validation](screenshots/md5-integrity-validation.svg)
```

## Redaction Checklist Before Uploading Any Image

- Remove personal identifiers, phone numbers, email addresses, dates of birth, and private names.
- Remove raw chat messages unless fully fictional and safe.
- Remove exact private GPS coordinates unless the dataset is clearly public/training-only.
- Remove raw malicious URLs, credentials, recovered passwords, and file payloads.
- Remove full directory paths when they identify people or private systems.
- Avoid full assignment pages or university cover pages.
- Crop tightly so the image shows the method, not the entire report.
