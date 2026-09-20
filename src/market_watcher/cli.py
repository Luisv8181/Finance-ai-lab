from __future__ import annotations

import argparse
import http.server
import os
from pathlib import Path
import socketserver
import sys
import webbrowser

from .market_data import build_watchlist_snapshot
from .report import render_markdown
from .synthesizer import gather_evidence_bundle, render_evidence_report

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def run_snapshot() -> None:
    snapshots = build_watchlist_snapshot()
    print(render_markdown(snapshots))


def run_stocker() -> None:
    print("Gathering deterministic market data, fresh news, and disclosures...", file=sys.stderr)
    bundle = gather_evidence_bundle()
    print(render_evidence_report(bundle))


def run_pulse(port: int = 8000) -> None:
    # Locate projects/financial-wellness-lab
    repo_root = Path(__file__).resolve().parent.parent.parent
    wellness_dir = repo_root / "projects" / "financial-wellness-lab"
    if not wellness_dir.exists():
        print(f"Error: Could not find directory at {wellness_dir}", file=sys.stderr)
        sys.exit(1)

    os.chdir(wellness_dir)
    handler = http.server.SimpleHTTPRequestHandler
    
    # Try port, fallback to port + 1 if busy
    chosen_port = port
    httpd = None
    for p in range(port, port + 10):
        try:
            httpd = socketserver.TCPServer(("", p), handler)
            chosen_port = p
            break
        except OSError:
            continue

    if httpd is None:
        print("Error: Could not bind to an available port.", file=sys.stderr)
        sys.exit(1)

    url = f"http://localhost:{chosen_port}/index.html"
    print(f"\n=======================================================", file=sys.stderr)
    print(f"  Money Pulse — Financial Wellness Lab", file=sys.stderr)
    print(f"  Serving live at: {url}", file=sys.stderr)
    print(f"  Press Ctrl+C to stop the server.", file=sys.stderr)
    print(f"=======================================================\n", file=sys.stderr)

    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...", file=sys.stderr)
        httpd.server_close()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Market Watcher & STOCKER Market Intelligence CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("snapshot", help="Generate the basic deterministic market snapshot table")
    subparsers.add_parser("stocker", help="Generate the full STOCKER evidence-grounded intelligence report")
    subparsers.add_parser("research", help="Alias for stocker intelligence report")

    pulse_parser = subparsers.add_parser("pulse", help="Run and open the Money Pulse Financial Wellness app in browser")
    pulse_parser.add_argument("--port", type=int, default=8000, help="Port to serve Money Pulse on (default: 8000)")

    args = parser.parse_args()

    if args.command in (None, "snapshot"):
        run_snapshot()
    elif args.command in ("stocker", "research"):
        run_stocker()
    elif args.command == "pulse":
        run_pulse(port=args.port)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
