import asyncio
import socket
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional

TIMEOUT = 1
CONCURRENCY = 500

COMMON_SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MS RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}


# ---------------- CORE SCANNER ----------------

async def scan_port(ip: str, port: int, sem: asyncio.Semaphore) -> Optional[Dict]:
    async with sem:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(ip, port),
                timeout=TIMEOUT
            )

            banner = ""
            try:
                writer.write(b"\r\n")
                await writer.drain()
                data = await asyncio.wait_for(reader.read(200), timeout=0.5)
                banner = data.decode(errors="ignore").strip()
            except Exception:
                banner = ""

            writer.close()
            try:
                await writer.wait_closed()
            except Exception:
                pass

            return {
                "port": port,
                "service": COMMON_SERVICE_MAP.get(port, "Unknown"),
                "banner": banner[:120]
            }

        except Exception:
            return None


async def run_scan(target: str, start: int, end: int, quiet: bool = False) -> List[Dict]:
    ip = socket.gethostbyname(target)
    sem = asyncio.Semaphore(CONCURRENCY)

    if not quiet:
        print("=" * 70)
        print("ASYNC ULTRA-FAST PORT SCANNER")
        print("=" * 70)
        print("Target:", target, ip)
        print("Range :", start, end)
        print("Start :", datetime.now())
        print("=" * 70)

    tasks = [scan_port(ip, p, sem) for p in range(start, end + 1)]
    results: List[Dict] = []

    for coro in asyncio.as_completed(tasks):
        r = await coro
        if r:
            if not quiet:
                print(f"[OPEN] {r['port']}")
            results.append(r)

    return results


# ---------------- REPORT EXPORT ----------------

def export_reports(results: List[Dict], prefix="async_results"):
    with open(f"{prefix}.json", "w") as f:
        json.dump(results, f, indent=2)

    with open(f"{prefix}.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["port", "service", "banner"])
        writer.writeheader()
        writer.writerows(results)


# ---------------- CLI ----------------

def create_arg_parser():
    import argparse

    parser = argparse.ArgumentParser(
        description="Async ultra-fast TCP port scanner (educational use only)"
    )

    # target optional → prevents SystemExit in no-arg runs
    parser.add_argument("target", nargs="?", default="localhost")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=1024)
    parser.add_argument("--quiet", action="store_true")

    return parser


def main_cli():
    parser = create_arg_parser()
    args = parser.parse_args()

    if args.start < 1 or args.end > 65535 or args.start > args.end:
        raise SystemExit("Invalid port range")

    results = asyncio.run(run_scan(args.target, args.start, args.end, args.quiet))

    if not args.quiet:
        print("\nOPEN PORT TABLE")
        print("-" * 70)
        for r in sorted(results, key=lambda x: x["port"]):
            print(f"{r['port']:<8}{r['service']:<15}{r['banner'][:40]}")

    export_reports(results)

    if not args.quiet:
        print("Reports saved.")
        print("End:", datetime.now())


if __name__ == "__main__":
    main_cli()
