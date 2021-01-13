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


# Base address for various memory segments
TEMP = 5
STATIC = 16
STACK = 256
# I have no idea why these must start at these addresses, but
# if we chose other addresses, the supplied tests fail
# TODO: do we have to get these dynamically, maybe?
# seems like it, because the this/that base addresses change
# between test scripts
LOCAL = 300
ARGUMENT = 400
POINTER = 2048  # this one might be wrong still
THIS = 3030
THAT = 3040


SEGMENT_SYMBOLS: Dict[str, str] = {
    "pointer": "3",
    "temp": "5",
    "static": "16",
    "argument": "ARG",
    "local": "LCL",
    "this": "THIS",
    "that": "THAT",
}


def translate(f: TextIO) -> Generator[str, None, None]:
    label_count = 0

    # Initialize pointers to various memory segments
    # TODO: see if this is still needed after project 7
    #    yield "// begin init"
    #    yield f"@{STACK}"
    #    yield "D=A"
    #    yield "@SP"
    #    yield "M=D"
    #
    #    yield f"@{LOCAL}"
    #    yield "D=A"
    #    yield "@LCL"
    #    yield "M=D"
    #
    #    yield f"@{ARGUMENT}"
    #    yield "D=A"
    #    yield "@ARG"
    #    yield "M=D"
    #
    #    yield f"@{THIS}"
    #    yield "D=A"
    #    yield "@THIS"
    #    yield "M=D"
    #
    #    yield f"@{THAT}"
    #    yield "D=A"
    #    yield "@THAT"
    #    yield "M=D"
    #    yield "// end init"

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()

        if line.startswith("label"):
            _, label = line.split(" ")
            yield f"({label})"

        if line.startswith("goto"):
            _, label = line.split(" ")
            yield f"// start goto {label}"
            yield f"@{label}"
            yield "0;JMP"
            yield f"// end goto {label}"

        if line.startswith("if-goto"):
            _, label = line.split(" ")
            yield f"// start if-goto {label}"
            yield "@SP"
            yield "AM=M-1"
            yield "D=M"
            yield f"@{label}"
            yield "D;JNE"
            yield f"// end if-goto {label}"

        if line.startswith("push"):
            _, segment, n = line.split()
            if segment == "constant":
                yield f"// start push constant {n}"
                yield f"@{n}"  # load the desired constant into the A register
                yield "D=A"  # set it to D, so we can keep it after the next A inst
                yield "@SP"  # load the pointer to the next spot in the stack into A
                yield "A=M"  # Set A to the address of next spot in the stack
                yield "M=D"  # Set the top of the stack to the desired constant
                yield "D=A+1"  # set D to the next spot in the stack (current top + 1)
                yield "@SP"  # load the address of the the former stack top
                yield "M=D"  # and set it to the new top of the stack
                yield f"// end push constant {n}"
            else:
                sym = SEGMENT_SYMBOLS.get(segment)

                if not sym:
                    raise ValueError(f"Couldn't resolve segment: {segment}")

                yield f"// start push {segment} {n}"
                yield f"@{sym}"
                # temp and static are not pointers
                # temp, static, and pointer are not pointers to other
                # base addresses. (pointer is a 2 word segment that
                # holds the base addresses of this and that. when we're
                # pushing from pointer, we need to get those - not
                # the values stored in this or that)
                if segment not in ("temp", "static", "pointer"):
                    yield "A=M"
                # Get to the right offset
                for i in range(int(n)):
                    yield "A=A+1"
                yield "D=M"
                yield "@SP"
                yield "A=M"
                yield "M=D"
                yield "D=A+1"
                yield "@SP"
                yield "M=D"
                yield f"// end push {segment} {n}"

        if line.startswith("pop"):
            _, segment, n = line.split()

            sym = SEGMENT_SYMBOLS.get(segment)

            if not sym:
                raise ValueError(f"Couldn't resolve segment: {segment}")

            yield f"// start pop {segment} {n}"
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield f"@{sym}"
            # Get to the right offset
            # temp, static, and pointer are not pointers to other
            # base addresses. (pointer is a 2 word segment that
            # holds the base addresses of this and that. when we're
            # popping to pointer, we need to update those - not
            # the values stored in this or that)
            if segment not in ("temp", "static", "pointer"):
                yield "A=M"
            for i in range(int(n)):
                yield "A=A+1"
            yield "M=D"
            yield "@SP"
            yield "M=M-1"
            yield f"// end pop {segment} {n}"

        if line.startswith("add"):
            yield "@SP"  # load the pointer to the next in the stack into A
            yield "A=M-1"  # decrease it by 1 to get the topmost stack item address into A
            yield "D=M"  # set that to D
            yield "A=A-1"  # decrease it again to get to the next item in the stack
            yield "M=D+M"  # add them together and store the result in the same spot
            yield "D=A+1"  # set D to the next location in the stack
            yield "@SP"  # load the stack pointer into A
            yield "M=D"  # and set it to the new topmost location of the stack

        if line.startswith("sub"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "M=M-D"
            yield "D=A+1"
            yield "@SP"
            yield "M=D"

        if line.startswith("neg"):
            yield "@SP"
            yield "A=M-1"
            yield "M=-M"
            yield "D=A+1"
            yield "@SP"
            yield "M=D"

        if line.startswith("eq"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "D=D-M"
            yield "@SP"
            yield "M=M-1"
            yield "M=M-1"
            yield f"@EQUAL.{label_count}"
            yield "D;JEQ"
            yield "@SP"
            yield "A=M"
            yield "M=0"
            yield f"@END.{label_count}"
            yield "0;JMP"
            yield f"(EQUAL.{label_count})"
            yield "@SP"
            yield "A=M"
            yield "M=-1"
            yield f"(END.{label_count})"
            yield "@SP"
            yield "D=M+1"
            yield "M=D"
            label_count += 1

        if line.startswith("gt"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "D=D-M"
            yield "@SP"
            yield "M=M-1"
            yield "M=M-1"
            yield f"@EQUAL.{label_count}"
            yield "D;JLT"
            yield "@SP"
            yield "A=M"
            yield "M=0"
            yield f"@END.{label_count}"
            yield "0;JMP"
            yield f"(EQUAL.{label_count})"
            yield "@SP"
            yield "A=M"
            yield "M=-1"
            yield f"(END.{label_count})"
            yield "@SP"
            yield "D=M+1"
            yield "M=D"
            label_count += 1

        if line.startswith("lt"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "D=D-M"
            yield "@SP"
            yield "M=M-1"
            yield "M=M-1"
            yield f"@EQUAL.{label_count}"
            yield "D;JGT"
            yield "@SP"
            yield "A=M"
            yield "M=0"
            yield f"@END.{label_count}"
            yield "0;JMP"
            yield f"(EQUAL.{label_count})"
            yield "@SP"
            yield "A=M"
            yield "M=-1"
            yield f"(END.{label_count})"
            yield "@SP"
            yield "D=M+1"
            yield "M=D"
            label_count += 1

        if line.startswith("and"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "M=D&M"
            yield "D=A+1"
            yield "@SP"
            yield "M=D"

        if line.startswith("or"):
            yield "@SP"
            yield "A=M-1"
            yield "D=M"
            yield "A=A-1"
            yield "M=D|M"
            yield "D=A+1"
            yield "@SP"
            yield "M=D"

        if line.startswith("not"):
            yield "@SP"
            yield "A=M-1"
            yield "M=!M"
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
