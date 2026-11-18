"""Build the frozen course prompt and append a dated evidence snapshot."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
AGENT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    evidence = args.evidence.read_text(encoding="utf-8")
    if not evidence.strip():
        parser.error("The evidence snapshot is empty.")
    subprocess.run(
        [sys.executable, str(ROOT / "tools/build_prompt.py"), "--agent", str(AGENT),
         "--case", str(args.case.resolve()), "--out", str(args.out.resolve())],
        check=True,
    )
    with args.out.open("a", encoding="utf-8") as packet:
        packet.write("\n# DATED EVIDENCE SNAPSHOT (case data)\n" + evidence)


if __name__ == "__main__":
    main()
