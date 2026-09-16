from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "resources" / "opportunity_sources.json"
OUTPUT_FILE = ROOT / "resources" / "opportunities-auto.md"


@dataclass(frozen=True)
class Link:
    text: str
    url: str


class LinkParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self._href: str | None = None
        self._text: list[str] = []
        self.links: list[Link] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self._href = urljoin(self.base_url, href)
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href:
            text = re.sub(r"\s+", " ", " ".join(self._text)).strip()
            if text:
                self.links.append(Link(text=text, url=self._href))
            self._href = None
            self._text = []


def fetch(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "Finance-AI-Lab-Opportunity-Radar/0.1 (+https://github.com/Luisv8181/Finance-ai-lab)"
        },
    )
    with urlopen(request, timeout=20) as response:
        content_type = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(content_type, errors="replace")


def score(text: str, keywords: list[str]) -> int:
    haystack = text.casefold()
    return sum(1 for keyword in keywords if keyword.casefold() in haystack)


def scan_source(name: str, url: str, keywords: list[str]) -> tuple[list[Link], str | None]:
    try:
        html = fetch(url)
    except Exception as exc:  # Network failures should not kill the whole radar.
        return [], f"{type(exc).__name__}: {exc}"

    parser = LinkParser(url)
    parser.feed(html)

    unique: dict[str, Link] = {}
    for link in parser.links:
        if link.url.startswith(("http://", "https://")) and score(link.text, keywords) > 0:
            unique.setdefault(link.url, link)

    ranked = sorted(
        unique.values(),
        key=lambda item: (-score(item.text, keywords), item.text.casefold()),
    )
    return ranked[:20], None


def main() -> None:
    sources = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)

    lines = [
        "# Automated Opportunity Review Queue",
        "",
        f"Generated: **{now.isoformat(timespec='seconds')}**",
        "",
        "This is a machine-generated discovery queue, not a verified opportunity list.",
        "A human should confirm dates, eligibility, cost, location, and application status on the official page.",
        "",
    ]

    for source in sources:
        name = source["name"]
        url = source["url"]
        keywords = source["keywords"]
        links, error = scan_source(name, url, keywords)

        lines.extend([f"## {name}", "", f"Source: {url}", ""])

        if error:
            lines.extend([f"_Scanner error: {error}_", ""])
            continue

        if not links:
            lines.extend(["_No keyword-matching links found._", ""])
            continue

        for link in links:
            lines.append(f"- [{link.text}]({link.url})")
        lines.append("")

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
