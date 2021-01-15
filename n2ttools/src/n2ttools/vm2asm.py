import sys
from typing import Dict, Generator, TextIO, Tuple

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

PTR_SEGMENTS: Tuple[str, str, str, str] = ("argument", "local", "this", "that")

# Function name -> (number of args, number of locals)
FUNCTIONS: Dict[str, Tuple[int, int]] = {}


def push(location: str, is_ptr: bool, offset: int = 0) -> Generator[str, None, None]:
    if location == "constant":
        yield f"// start push constant {offset}"
        yield f"@{offset}"  # load the desired constant into the A register
        yield "D=A"  # set it to D, so we can keep it after the next A inst
        yield "@SP"  # load the pointer to the next spot in the stack into A
        yield "A=M"  # Set A to the address of next spot in the stack
        yield "M=D"  # Set the top of the stack to the desired constant
        yield "D=A+1"  # set D to the next spot in the stack (current top + 1)
        yield "@SP"  # load the address of the the former stack top
        yield "M=D"  # and set it to the new top of the stack
        yield f"// end push constant {offset}"
    else:
        # the segment may be a resolvable symbol
        location = SEGMENT_SYMBOLS.get(location, location)

        yield f"// start push {location} {offset}"
        yield f"@{location}"
        # the caller may want us to treat the location as a pointer
        if is_ptr:
            yield "A=M"
        # Get to the right offset
        for i in range(offset):
            yield "A=A+1"
        yield "D=M"
        yield "@SP"
        yield "A=M"
        yield "M=D"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"
        yield f"// end push {location} {offset}"


def pop(location: str, is_ptr: bool, offset: int = 0) -> Generator[str, None, None]:
    location = SEGMENT_SYMBOLS.get(location, location)

    yield f"// start pop {location} {offset}"
    yield "@SP"
    yield "A=M-1"
    yield "D=M"
    yield f"@{location}"
    if is_ptr:
        yield "A=M"
    for i in range(offset):
        yield "A=A+1"
    yield "M=D"
    yield "@SP"
    yield "M=M-1"
    yield f"// end pop {location} {offset}"


def translate_instruction(inst: str, label_count: int) -> Generator[str, None, int]:
    if inst.startswith("label"):
        _, label = inst.split(" ")
        yield f"({label})"

    if inst.startswith("goto"):
        _, label = inst.split(" ")
        yield f"// start goto {label}"
        yield f"@{label}"
        yield "0;JMP"
        yield f"// end goto {label}"

    if inst.startswith("if-goto"):
        _, label = inst.split(" ")
        yield f"// start if-goto {label}"
        yield "@SP"
        yield "AM=M-1"
        yield "D=M"
        yield f"@{label}"
        yield "D;JNE"
        yield f"// end if-goto {label}"

    # TODO: this should be part of dealing with a call, not a return
    if inst.startswith("return"):
        # pop an item off the stack (this is the return value)
        yield from pop("R13", is_ptr=False)
        # pop the next item to get the return address
        yield from pop("R14", is_ptr=False)
        # push the return value back on the stack
        yield from push("R13", is_ptr=False)
        # jump to the return address
        yield "@R14"
        yield "0;JMP"

    if inst.startswith("push"):
        _, segment, n = inst.split()
        yield from push(segment, is_ptr=segment in PTR_SEGMENTS, offset=int(n))

    if inst.startswith("pop"):
        _, segment, n = inst.split()
        yield from pop(segment, is_ptr=segment in PTR_SEGMENTS, offset=int(n))

    if inst.startswith("add"):
        yield "@SP"  # load the pointer to the next in the stack into A
        yield "A=M-1"  # decrease it by 1 to get the topmost stack item address into A
        yield "D=M"  # set that to D
        yield "A=A-1"  # decrease it again to get to the next item in the stack
        yield "M=D+M"  # add them together and store the result in the same spot
        yield "D=A+1"  # set D to the next location in the stack
        yield "@SP"  # load the stack pointer into A
        yield "M=D"  # and set it to the new topmost location of the stack

    if inst.startswith("sub"):
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "M=M-D"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"

    if inst.startswith("neg"):
        yield "@SP"
        yield "A=M-1"
        yield "M=-M"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"

    if inst.startswith("eq"):
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

    if inst.startswith("gt"):
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

    if inst.startswith("lt"):
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

    if inst.startswith("and"):
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "M=D&M"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"

    if inst.startswith("or"):
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "M=D|M"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"

    if inst.startswith("not"):
        yield "@SP"
        yield "A=M-1"
        yield "M=!M"
        yield "D=A+1"
        yield "@SP"
        yield "M=D"

    return label_count


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

    current_function = ""
    function_args = 0
    function_locals = 0

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()

        if line.startswith("function"):
            _, name, n = line.split(" ")
            current_function = name
            function_args = int(n)
            # No allocation or return address handling happens here
            # we're just translating the body of the function into
            # ASM, and storing data that's necessary for `call` to
            # work.
            yield f"// start function {name}"
            yield f"({name})"

        if current_function:
            if " local " in line:
                function_locals = max(function_locals, int(line.split(" ")[-1]))

            if line.startswith("return"):
                FUNCTIONS[current_function] = (function_args, function_locals)

            current_function = ""

        label_count = yield from translate_instruction(line, label_count)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in translate(f):
            print(line)
