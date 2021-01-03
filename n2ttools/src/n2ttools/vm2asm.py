import sys
from typing import Generator, TextIO


def translate(f: TextIO) -> Generator[str, None, None]:
    pass


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        yield from translate(f)
