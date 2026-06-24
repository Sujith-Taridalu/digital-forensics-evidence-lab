#!/usr/bin/env python3
"""Extract browser history from a Firefox places.sqlite database."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path

QUERY = """
SELECT
    moz_places.url,
    moz_places.title,
    moz_historyvisits.visit_date
FROM moz_places
JOIN moz_historyvisits
    ON moz_places.id = moz_historyvisits.place_id
ORDER BY moz_historyvisits.visit_date DESC
LIMIT ?
"""


def convert_firefox_timestamp(value: int | None) -> str:
    if not value:
        return ""
    return str(value)


def export_history(database_path: Path, output_path: Path, limit: int) -> int:
    connection = sqlite3.connect(f"file:{database_path}?mode=ro", uri=True)
    try:
        rows = connection.execute(QUERY, (limit,)).fetchall()
    finally:
        connection.close()

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["url", "title", "visit_date_raw"])
        for url, title, visit_date in rows:
            writer.writerow([url, title or "", convert_firefox_timestamp(visit_date)])
    return len(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export recent Firefox history from places.sqlite."
    )
    parser.add_argument("database", type=Path, help="Path to places.sqlite")
    parser.add_argument("output", type=Path, help="CSV file to write")
    parser.add_argument("--limit", type=int, default=100, help="Number of rows to export")
    args = parser.parse_args()

    count = export_history(args.database, args.output, args.limit)
    print(f"Exported {count} browser history rows to {args.output}")


if __name__ == "__main__":
    main()