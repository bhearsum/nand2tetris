import sys
from typing import Dict, Generator, Iterator, TextIO, Tuple, Union

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


def push_constant(val: Union[str, int]) -> Generator[str, None, None]:
    yield f"// start push constant {val}"
    yield f"@{val}"  # load the desired constant into the A register
    yield "D=A"  # set it to D, so we can keep it after the next A inst
    yield "@SP"  # load the pointer to the next spot in the stack into A
    yield "A=M"  # Set A to the address of next spot in the stack
    yield "M=D"  # Set the top of the stack to the desired constant
    yield "D=A+1"  # set D to the next spot in the stack (current top + 1)
    yield "@SP"  # load the address of the the former stack top
    yield "M=D"  # and set it to the new top of the stack
    yield f"// end push constant {val}"


def push(location: str, is_ptr: bool, offset: int = 0) -> Generator[str, None, None]:
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


def call(name: str, n_args: int, n_label: int) -> Generator[str, None, None]:
    return_label = f"{name}_return_{n_label}"
    yield from push_constant(return_label)
    # store the pointers for the current function on the stack
    for ptr in ("LCL", "ARG", "THIS", "THAT"):
        yield from push(ptr, is_ptr=False)
    # adjust ARG for the called function, which are behind
    # the return address, new LCL, et. al in the stack
    yield "@SP"
    yield "A=M"
    for i in range(int(n_args) + 5):
        yield "A=A-1"
    yield "D=A"
    yield "@ARG"
    yield "M=D"
    # adjust LCL to the new tip of the stack
    yield "@SP"
    yield "D=M"
    yield "@LCL"
    yield "M=D"
    # jump to the function
    yield f"@{name}"
    yield "0;JMP"
    # and declare the return address label
    yield f"({return_label})"


def translate_instruction(inst: str, label_numbers: Iterator[int]) -> Generator[str, None, None]:
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

    if inst.startswith("push"):
        _, segment, n = inst.split()
        if segment == "constant":
            yield from push_constant(n)
        else:
            yield from push(segment, is_ptr=segment in PTR_SEGMENTS, offset=int(n))

    if inst.startswith("pop"):
        _, segment, n = inst.split()
        if segment == "constant":
            yield from push_constant(n)
        else:
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
        n_label = next(label_numbers)
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "D=D-M"
        yield "@SP"
        yield "M=M-1"
        yield "M=M-1"
        yield f"@EQUAL.{n_label}"
        yield "D;JEQ"
        yield "@SP"
        yield "A=M"
        yield "M=0"
        yield f"@END.{n_label}"
        yield "0;JMP"
        yield f"(EQUAL.{n_label})"
        yield "@SP"
        yield "A=M"
        yield "M=-1"
        yield f"(END.{n_label})"
        yield "@SP"
        yield "D=M+1"
        yield "M=D"

    if inst.startswith("gt"):
        n_label = next(label_numbers)
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "D=D-M"
        yield "@SP"
        yield "M=M-1"
        yield "M=M-1"
        yield f"@EQUAL.{n_label}"
        yield "D;JLT"
        yield "@SP"
        yield "A=M"
        yield "M=0"
        yield f"@END.{n_label}"
        yield "0;JMP"
        yield f"(EQUAL.{n_label})"
        yield "@SP"
        yield "A=M"
        yield "M=-1"
        yield f"(END.{n_label})"
        yield "@SP"
        yield "D=M+1"
        yield "M=D"

    if inst.startswith("lt"):
        n_label = next(label_numbers)
        yield "@SP"
        yield "A=M-1"
        yield "D=M"
        yield "A=A-1"
        yield "D=D-M"
        yield "@SP"
        yield "M=M-1"
        yield "M=M-1"
        yield f"@EQUAL.{n_label}"
        yield "D;JGT"
        yield "@SP"
        yield "A=M"
        yield "M=0"
        yield f"@END.{n_label}"
        yield "0;JMP"
        yield f"(EQUAL.{n_label})"
        yield "@SP"
        yield "A=M"
        yield "M=-1"
        yield f"(END.{n_label})"
        yield "@SP"
        yield "D=M+1"
        yield "M=D"

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


def translate(f: TextIO, label_numbers: Iterator[int]) -> Generator[str, None, None]:
    n_statics = 0

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()
        if "push static" in line or "pop static" in line:
            n_statics = max(n_statics, int(line.split()[2]) + 1)

        if line.startswith("function"):
            _, name, n_locals = line.split(" ")
            # No allocation or return address handling happens here
            # we're just declaring a label for the function and
            # initializing any local variables it has, and then
            # continuing the loop to translate the body of the function
            # setting up it's stack is handled by a `call` instruction
            # returning handling is handled by a return `return`
            # instruction
            yield f"// start function {name}"
            yield f"({name})"
            for i in range(int(n_locals)):
                yield from push_constant(0)

        if line.startswith("return"):
            # pop an item off the stack (this is the return value)
            # put it in the bottom most part of the caller's stack
            # FRAME (R13) = LCL
            yield "@LCL"
            yield "D=M"
            yield "@R13"
            yield "M=D"
            # RET (R14) = FRAME - 5
            for i in range(5):
                yield "D=D-1"
            yield "A=D"
            yield "D=M"
            yield "@R14"
            yield "M=D"
            # *ARG = pop()
            yield from pop("argument", is_ptr=True)
            # SP = ARG+1
            yield "@ARG"
            yield "D=M+1"
            yield "@SP"
            yield "M=D"
            # THAT = *FRAME - 1, etc.
            yield "@R13"
            yield "A=M-1"
            yield "D=M"
            yield "@THAT"
            yield "M=D"

            yield "@R13"
            yield "A=M-1"
            yield "A=A-1"
            yield "D=M"
            yield "@THIS"
            yield "M=D"

            yield "@R13"
            yield "A=M-1"
            yield "A=A-1"
            yield "A=A-1"
            yield "D=M"
            yield "@ARG"
            yield "M=D"

            yield "@R13"
            yield "A=M-1"
            yield "A=A-1"
            yield "A=A-1"
            yield "A=A-1"
            yield "D=M"
            yield "@LCL"
            yield "M=D"

            # return to caller
            yield "@R14"
            yield "A=M"
            yield "0;JMP"

        if line.startswith("call"):
            _, name, n_args = line.split()
            # push the return address onto the stack
            yield from call(name, int(n_args), next(label_numbers))

        yield from translate_instruction(line, label_numbers)

    # I really don't like modifying this global variable, but
    # I haven't found a cleaner way to update the base addreses
    # for the static segment.
    SEGMENT_SYMBOLS["static"] = str(int(SEGMENT_SYMBOLS["static"]) + n_statics)


def init() -> Generator[str, None, None]:
    yield "// begin init"
    yield "@256"
    yield "D=A"
    yield "@SP"
    yield "M=D"
    # TODO: Calling Sys.init like this means the stack pointer moves
    # to 261 before any real code runs. Things appear to work fine
    # if simply jump to Sys.init directly, without letting `call`
    # adjust the stack pointer. This is left as is because the
    # nand2tetris tests fail if jump directly
    # yield "@Sys.init"
    # yield "0;JMP"
    yield from call("Sys.init", 0, 0)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate [file_to_translate ...]")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    # Init happens here because we may be translating multiple files
    # and we only want to initialize once
    for line in init():
        print(line)

    label_numbers = iter(range(100000))

    for fn in sys.argv[1:]:
        with open(fn) as f:
            for line in translate(f, label_numbers):
                print(line)
