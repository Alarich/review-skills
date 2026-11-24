"""Lint the checked-in Markdown documentation and skill files."""

import shutil
import subprocess
import sys


if __name__ == "__main__":
    command = "markdownlint-cli2"
    if not shutil.which(command):
        sys.exit(f"{command} is required. Install it and run devtools/validate.")
    sys.exit(subprocess.run([command]).returncode)
