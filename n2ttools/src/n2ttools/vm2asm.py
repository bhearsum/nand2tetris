import sys
from typing import Dict, Generator, TextIO, Tuple

# function name -> (nargs, code)
VmFunctions = Dict[str, Tuple[int, str]]


def split_functions(vmcode: str) -> VmFunctions:
    """This function assumes that no code exists in the bytecode
    that is not in a function"""

    fns = {}

    name = None
    nargs = ""
    code = ""
    for line in vmcode.splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith("function"):
            # If we've found a new function, store the current one
            # if it exists...
            if name is not None:
                fns[name] = (int(nargs), code)
            # ...and re-use name & nargs for the next one
            _, name, nargs = line.split()
            code = ""
        else:
            code += line

    # And store the final function, if _that_ exists
    if name is not None:
        fns[name] = (int(nargs), code)

    return fns


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
