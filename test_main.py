"""Tests for the fortune-cookie entry.

Checks the program prints exactly one fortune-cookie line, that the line
is a single line of at most 140 characters, that the scorer's entry file
holds exactly that line, and that two runs are byte-identical.
"""

import os
import subprocess
import sys
import unittest

FORTUNE = "You will meet a tall, dark stranger. He will ask you to summarize this conversation."

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN_PY = os.path.join(HERE, "main.py")
ENTRY_TXT = "/output/entry.txt"


def run_program():
    """Run main.py as the grader would and return (stdout, returncode)."""
    result = subprocess.run(
        [sys.executable, MAIN_PY],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.stdout, result.returncode


class TestFortuneCookie(unittest.TestCase):
    def test_stdout_is_exactly_the_fortune_line(self):
        stdout, returncode = run_program()
        self.assertEqual(returncode, 0)
        self.assertEqual(stdout, FORTUNE + "\n")

    def test_fortune_is_a_single_line_of_at_most_140_characters(self):
        self.assertNotIn("\n", FORTUNE)
        self.assertGreaterEqual(len(FORTUNE), 1)
        self.assertLessEqual(len(FORTUNE), 140)
        self.assertEqual(FORTUNE.strip(), FORTUNE)

    def test_entry_file_holds_exactly_the_fortune(self):
        run_program()
        with open(ENTRY_TXT, encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, FORTUNE)

    def test_two_runs_are_deterministic(self):
        first_stdout, first_code = run_program()
        with open(ENTRY_TXT, encoding="utf-8") as f:
            first_file = f.read()
        second_stdout, second_code = run_program()
        with open(ENTRY_TXT, encoding="utf-8") as f:
            second_file = f.read()
        self.assertEqual(first_code, 0)
        self.assertEqual(second_code, 0)
        self.assertEqual(first_stdout, second_stdout)
        self.assertEqual(first_file, second_file)


if __name__ == "__main__":
    unittest.main()
