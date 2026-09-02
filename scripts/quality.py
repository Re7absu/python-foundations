import subprocess
import sys

commands = [
    ["uv", "run", "black", "."],
    ["uv", "run", "ruff", "check", "."],
    ["uv", "run", "mypy", "--strict", "."],
]

for command in commands:
    result = subprocess.run(command)

    if result.returncode != 0:
        sys.exit(result.returncode)
