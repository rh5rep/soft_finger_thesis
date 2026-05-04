from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def launcher_command() -> list[str]:
    app_path = Path(__file__).with_name("streamlit_app.py")
    return [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app_path),
        "--browser.gatherUsageStats=false",
    ]


def main() -> int:
    return subprocess.call(launcher_command())


if __name__ == "__main__":
    raise SystemExit(main())
