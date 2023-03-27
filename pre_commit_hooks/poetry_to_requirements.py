"""Converts Poetry pyproject.toml requirements into a requirements.txt file."""

import argparse
import subprocess
from pathlib import Path
from typing import Optional, Sequence


def check_old_requirements(
    requirements_file: str, include_dev: bool = False, project_root="."
):
    """Check for an old requirements.txt file."""
    requirements_path = Path(project_root) / requirements_file

    if requirements_path.is_file():
        check_cmd = ["poetry", "export", "--without-hashes"]
        if include_dev:
            check_cmd.append("--dev")

        return (
            requirements_path.read_text(encoding="utf8").splitlines()
            != subprocess.run(check_cmd, capture_output=True, cwd=project_root)
            .stdout.decode()
            .splitlines()
        )

    return True


def build_new_requirements(
    requirements_file: str, include_dev: bool = False, project_root="."
):
    """Export poetry requirements to a requirements file."""
    build_cmd = [
        "poetry",
        "export",
        "--output",
        requirements_file,
        "--without-hashes",
    ]

    if include_dev:
        build_cmd.append("--dev")

    subprocess.run(build_cmd, capture_output=True, cwd=project_root)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """CLI program to run."""
    parser = argparse.ArgumentParser(
        "Convert Poetry to requirements.txt",
    )
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Filenames pre-commit believes are changed.",
    )
    parser.add_argument(
        "--dev",
        default="False",
        action="store_true",
        help="Include dev requirements in export.",
    )
    parser.add_argument(
        "--input",
        default=".",
        help="Path to project root.",
    )
    parser.add_argument(
        "--output",
        default="requirements.txt",
        help="Path to output.",
    )
    args = parser.parse_args(argv)

    retcode = 0
    if check_old_requirements(args.output, args.dev, args.input):
        print("rebuilding")
        build_new_requirements(args.output, args.dev, args.input)

        print(f"created new {args.output} file")
        retcode = 1

    return retcode


if __name__ == "__main__":
    exit(main())
