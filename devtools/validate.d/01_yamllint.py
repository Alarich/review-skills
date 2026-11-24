"""Lint repository YAML and YAML front matter in each skill."""

from pathlib import Path
import shutil
import subprocess
import sys


def main():
    if not shutil.which("yamllint"):
        sys.exit("yamllint is required. Install it and run devtools/validate.")

    command = ["yamllint", "--strict"]
    failed = subprocess.run([*command, "."]).returncode != 0

    for skill in sorted(Path("skills").glob("*/SKILL.md")):
        opening, _, body = skill.read_text(encoding="utf-8").partition("\n")
        front_matter, closing, _ = body.partition("\n---\n")
        if opening != "---" or not closing or not front_matter.strip():
            print(f"{skill}: missing YAML front matter", file=sys.stderr)
            failed = True
            continue

        result = subprocess.run(
            [*command, "-"], input=front_matter + "\n", text=True,
            capture_output=True,
        )
        if result.returncode:
            print(f"{skill} (YAML front matter):", file=sys.stderr)
            print(result.stdout + result.stderr, end="", file=sys.stderr)
            failed = True

    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
