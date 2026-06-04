"""Offline Dydak deadline parser for the archived Canvas sync project."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


@dataclass(frozen=True)
class Deadline:
    title: str
    due_date: str


class StrongTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_strong = False
        self.items: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "strong":
            self._in_strong = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "strong":
            self._in_strong = False

    def handle_data(self, data: str) -> None:
        if self._in_strong and data.strip():
            self.items.append(data.strip())


def parse_deadlines(html: str) -> list[Deadline]:
    parser = StrongTextParser()
    parser.feed(html)
    deadlines: list[Deadline] = []

    for line in parser.items:
        date_match = re.search(r"on (\d{1,2}/\d{1,2}/\d{2})", line)
        title_match = re.search(r"\.\s*(.*?)\s*M:", line)
        if not date_match or not title_match:
            continue
        due_date = dt.datetime.strptime(date_match.group(1), "%m/%d/%y").strftime("%Y-%m-%d")
        deadlines.append(Deadline(title=title_match.group(1), due_date=due_date))

    return deadlines


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse Dydak deadline HTML without Canvas login or API calls.")
    parser.add_argument("--fixture", type=Path, default=Path("fixtures/dydak_deadlines.html"))
    parser.add_argument("--live", action="store_true", help="Always refused in this archive.")
    args = parser.parse_args()

    if args.live:
        raise SystemExit("Live Canvas sync is disabled in this archive. Use the offline parser fixture.")

    deadlines = parse_deadlines(args.fixture.read_text(encoding="utf-8"))
    for item in deadlines:
        print(f"{item.due_date}: {item.title}")
    print(f"parsed_deadlines={len(deadlines)} network_calls=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
