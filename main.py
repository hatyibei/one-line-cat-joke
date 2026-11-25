"""Entry for The One-Line Cat Joke That Lands: writes the cat joke to /output/entry.txt."""

import os

TEXT = "My cat isn't being rude when she knocks things off the table — she's quality-testing gravity, and it has passed every audit for nine years."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
