#!/usr/bin/env python3
"""Summarize executed-program signals from a text export of Prefetch findings."""

from __future__ import annotations

import argparse
import re
from collections import Counter

PREFETCH_NAME = re.compile(r"\b([A-Z0-9_.-]+)\.EXE\b", re.IGNORECASE)


def summarize_prefetch_text(path: str) -> Counter:
    counter: Counter[str] = Counter()
    with open(path, "r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            for match in PREFETCH_NAME.findall(line):
                counter[match.upper()] += 1
    return counter


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Count executable references in a Prefetch note or export."
    )
    parser.add_argument("input_file", help="Text file containing Prefetch findings")
    parser.add_argument(
        "--top",
        type=int,
        default=15,
        help="Number of executable names to display",
    )
    args = parser.parse_args()

    counts = summarize_prefetch_text(args.input_file)
    if not counts:
        print("No executable references found.")
        return

    for name, count in counts.most_common(args.top):
        print(f"{name}: {count}")


if __name__ == "__main__":
    main()