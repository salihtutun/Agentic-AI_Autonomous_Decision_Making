"""Render assets/mermaid/*.mmd to PNG with Mermaid CLI.

The .mmd files are the source. The PNG names match the notebooks.
"""

import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "mermaid"
CONFIG = SRC / "config.json"


def render(path):
    dest = HERE / f"{path.stem}.png"
    subprocess.run(
        [
            "npx.cmd",
            "--yes",
            "@mermaid-js/mermaid-cli",
            "-c",
            str(CONFIG),
            "-i",
            str(path),
            "-o",
            str(dest),
            "-b",
            "white",
            "-s",
            "2",
        ],
        check=True,
    )
    print(dest.name)


def main():
    for path in sorted(SRC.glob("*.mmd")):
        render(path)


if __name__ == "__main__":
    main()
