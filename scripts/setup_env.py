"""Create the virtual environment and install the project in editable mode.

Usage (from anywhere):
    python scripts/setup_env.py
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = PROJECT_ROOT / ".venv"


def venv_python() -> Path:
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def run(*args: str | Path) -> None:
    print(">", " ".join(str(a) for a in args))
    subprocess.run([str(a) for a in args], cwd=PROJECT_ROOT, check=True)


def main() -> None:
    if VENV_DIR.exists():
        print(f"venv already exists: {VENV_DIR}")
    else:
        run(sys.executable, "-m", "venv", VENV_DIR)

    python = venv_python()
    run(python, "-m", "pip", "install", "--upgrade", "pip")
    run(python, "-m", "pip", "install", "-e", ".[dev]")

    print("\nDone. Activate the environment with:")
    if sys.platform == "win32":
        print(r"  .\.venv\Scripts\Activate.ps1")
    else:
        print("  source .venv/bin/activate")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(f"\nSetup failed (exit code {exc.returncode}).")
