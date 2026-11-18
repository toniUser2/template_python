"""Run all quality checks locally - the same steps as the CI pipeline.

Usage (with activated .venv):
    python scripts/check.py
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHECKS: list[tuple[str, list[str]]] = [
    ("Lint", ["ruff", "check", "."]),
    ("Format", ["ruff", "format", "--check", "."]),
    ("Types", ["pyright"]),
    ("Tests", ["pytest"]),
    ("Build", ["build", "--outdir", "dist"]),
]


def main() -> int:
    failed: list[str] = []
    for name, args in CHECKS:
        print(f"\n===== {name}: {' '.join(args)}", flush=True)
        result = subprocess.run([sys.executable, "-m", *args], cwd=PROJECT_ROOT)
        if result.returncode != 0:
            failed.append(name)

    print("\n===== Summary")
    for name, _ in CHECKS:
        print(f"  {'FAILED' if name in failed else 'ok    '}  {name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
