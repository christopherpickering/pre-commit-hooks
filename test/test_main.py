"""Test poetry to requirements."""

import os
import subprocess
import unittest
from pathlib import Path

from pre_commit_hooks.poetry_to_requirements import (
    build_new_requirements,
    check_old_requirements,
    main,
)


class CliTest(unittest.TestCase):
    def test_cli(self):
        project_root = "test/existing_requirements/"
        requirements_file = "requirements.txt"

        # verify cli
        exit_code = main(["--output", requirements_file, "--input", project_root])

        # should exit 1 when file is created
        self.assertEqual(1, exit_code)

        # check again and should exit 0 as file already exists.
        exit_code = main(["--output", requirements_file, "--input", project_root])
        self.assertEqual(0, exit_code)

        # remove the file
        os.remove(project_root + requirements_file)


class FunctionTest(unittest.TestCase):
    def test_check_old_requirements(self):
        project_root = "test/existing_requirements/"
        requirements_file = "requirements.txt"
        x = check_old_requirements(requirements_file, False, project_root)

        # should return true as file does not yet exist
        self.assertEqual(x, True)

    def test_build_new_requirements(self):
        project_root = "test/existing_requirements/"
        requirements_file = "requirements.txt"
        build_new_requirements(requirements_file, False, project_root)

        # verify file was created
        self.assertEqual((Path(project_root) / requirements_file).is_file(), True)

        # verify that file is found
        x = check_old_requirements(requirements_file, False, project_root)

        # remove the file
        os.remove(project_root + requirements_file)

        # should return false as file exists and should not change
        self.assertEqual(x, False)

    def test_build_new_requirements_top_level(self):
        project_root = "test/top_level_pyproject/"
        requirements_file = "requirements.txt"
        build_new_requirements(requirements_file, False, project_root)

        # verify file was created
        self.assertEqual((Path(project_root) / requirements_file).is_file(), True)

        # remove the file
        os.remove(project_root + requirements_file)

    def test_build_new_requirements_nested(self):
        project_root = "test/nested_pyproject/app_one/"
        requirements_file = "requirements.txt"
        build_new_requirements(requirements_file, False, project_root)

        # verify file was created
        self.assertEqual((Path(project_root) / requirements_file).is_file(), True)

        # remove the file
        os.remove(project_root + requirements_file)


if __name__ == "__main__":
    unittest.main()
