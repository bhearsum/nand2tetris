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
    # Initialize the stack pointer
    yield "@256"
    yield "D=A"
    yield "@SP"
    yield "M=D"

    for line in f.read().splitlines():
        if line.startswith("push"):
            _, segment, n = line.split()
            # TODO: update these comments, fuck the tests
            yield f"@{n}"  # load the desired constant into the A register
            yield "D=A"    # set it to D, so we can keep it after the next inst
            yield "@SP"    # load the pointer to the next spot in the stack into A
            yield "A=M"
            yield "M=D"    # set it to the desired constant value
            yield "D=A+1"  # set D to the next spot in the stack
            yield "@SP"     # load 0 (the address of SP) into A
            yield "M=D"    # and set it to the new top of the stack

        if line.startswith("add"):
            yield "@SP"    # pop the topmost stack item and store it in D
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "M=D+M"
            yield "D=A+1"
            yield "@SP"
            yield "M=D"


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in translate(f):
            print(line)
