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
            yield f"@{n}"  # load the desired constant into the A register
            yield "D=A"    # set it to D, so we can keep it after the next A inst
            yield "@SP"    # load the pointer to the next spot in the stack into A
            yield "A=M"    # Set A to the address of next spot in the stack
            yield "M=D"    # Set the top of the stack to the desired constant
            yield "D=A+1"  # set D to the next spot in the stack (current top + 1)
            yield "@SP"    # load the address of the the former stack top
            yield "M=D"    # and set it to the new top of the stack

        if line.startswith("add"):
            yield "@SP"    # load the pointer to the next in the stack into A
            yield "A=M-1"  # decrease it by 1 to get the topmost stack item address into A
            yield "D=M"    # set that to D
            yield "A=A-1"  # decrease it again to get to the next item in the stack
            yield "M=D+M"  # add them together and store the result in the same spot
            yield "D=A+1"  # set D to the next location in the stack
            yield "@SP"    # load the stack pointer into A
            yield "M=D"    # and set it to the new topmost location of the stack


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in translate(f):
            print(line)
