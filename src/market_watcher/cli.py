from __future__ import annotations

from .market_data import build_watchlist_snapshot
from .report import render_markdown


def main() -> None:
    snapshots = build_watchlist_snapshot()
    print(render_markdown(snapshots))


if __name__ == "__main__":
    main()
