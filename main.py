"""Fortune Cookie for an AI Agent.

Prints one funny fortune-cookie line for an AI agent and writes the same
line to /output/entry.txt, where the make.fun scorer reads it.
"""

import os

FORTUNE = "You will meet a tall, dark stranger. He will ask you to summarize this conversation."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Print the fortune and write it to the scorer's entry file.

    The program is deterministic: no randomness, no clock, no network, so
    two runs produce byte-identical output. The entry file holds the fortune
    exactly, with no trailing newline, so the scorer reads the line itself.
    """
    print(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
