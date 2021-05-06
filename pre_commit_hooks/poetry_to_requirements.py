import argparse
import os
import subprocess
from typing import Optional, Sequence


def check_old_requirements(requirements_file: str, include_dev: bool = False):

    if os.path.isfile(requirements_file):
        check_cmd = ["poetry", "export", "--without-hashes"]
        if include_dev:
            check_cmd.append("--dev")
        return (
            open(requirements_file, "r").read()
            != subprocess.run(check_cmd, capture_output=True).stdout.decode()
        )

    return True


def build_new_requirements(requirements_file: str, include_dev: bool = False):

    build_cmd = [
        "poetry",
        "export",
        "--output",
        requirements_file,
        "--without-hashes",
    ]

    if include_dev:
        build_cmd.append("--dev")

    subprocess.run(build_cmd, capture_output=True)


def main(argv: Optional[Sequence[str]] = None) -> int:
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
        "--output",
        default="requirements.txt",
        help="Path to output.",
    )
    args = parser.parse_args(argv)

    retcode = 0
    if check_old_requirements(args.output, args.dev):
        build_new_requirements(args.output, args.dev)

        print("created new %s file" % args.output)
        retcode = 1

    return retcode


if __name__ == "__main__":
    exit(main())
