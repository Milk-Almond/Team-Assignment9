"""Build the common test packets from local clones of the five candidates."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

AGENT = Path(__file__).resolve().parents[2]
ROOT = AGENT.parents[1]
CANDIDATES = (
    ("yanisimova", "b62cf4880dee65fd313970ead50cceac3fcd59d5",
     "MASY1800_ET_Agent_Scaffold_v1_0-2/agents/landscape_agent"),
    ("Harry-max264", "d99088ce9b86897f147fc47669994d04222febaf", "agents/landscape_agent"),
    ("mp7240-sudo", "2e0f238a31e7a862d333d0418bee80380bb9e6ff", "agents/landscape_agent"),
    ("sawulya", "725f4027e183582621d14be4b3c7fe5e949a998f",
     "MASY1800_ET_Agent_Scaffold_v1_0 3/agents/landscape_agent"),
    ("yicrry777", "40d11aa9f5699742f9f70cb635d207d79d143907", "agents/gpu_landscape_agent"),
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("clones", nargs=5, type=Path,
                        help="Candidate clone paths in the order listed in submission-review.md")
    parser.add_argument("--out", type=Path, default=ROOT / "work/common")
    args = parser.parse_args()
    evidence = (AGENT / "evidence/source-register.md").read_text(encoding="utf-8")
    for (name, expected, relative), clone in zip(CANDIDATES, args.clones):
        commit = subprocess.check_output(
            ["git", "-C", str(clone), "rev-parse", "HEAD"], text=True
        ).strip()
        if commit != expected:
            parser.error(f"{name} must be checked out at {expected}, got {commit}")
        for case in ("primary", "contrast_1"):
            output = args.out.resolve() / name / f"{case}.txt"
            subprocess.run([
                sys.executable, str(ROOT / "tools/build_prompt.py"),
                "--agent", str((clone / relative).resolve()),
                "--case", str(AGENT / "cases" / f"{case}.json"),
                "--out", str(output),
            ], check=True, stdout=subprocess.DEVNULL)
            with output.open("a", encoding="utf-8") as packet:
                packet.write("\n# DATED EVIDENCE SNAPSHOT (case data)\n" + evidence)
            print(hashlib.sha256(output.read_bytes()).hexdigest(), f"{name}/{case}.txt")


if __name__ == "__main__":
    main()
