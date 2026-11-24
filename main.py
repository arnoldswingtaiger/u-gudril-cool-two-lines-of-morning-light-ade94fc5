"""Two Lines of Morning Light.

A tiny program that writes a two-line micro poem about light and
morning to /output/entry.txt. Python 3.13 standard library only:
no network, no input, no randomness.
"""

from pathlib import Path

LINES = [
    "Light climbs the windowsill like a cat come home,",
    "and the whole quiet house remembers how to breathe.",
]

POEM = "\n".join(LINES) + "\n"


def main() -> None:
    # The gate allows 1 to 120 characters; this poem is 102 including
    # the trailing newline, so it sits comfortably inside the limit.
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
