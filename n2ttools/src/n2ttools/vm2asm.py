import sys
from typing import Dict, Generator, TextIO, Tuple

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

# Function name -> number of locals
FuncDef = Dict[str, int]


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
    functions: FuncDef = {}
    current_function = ""

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()

        if line.startswith("function"):
            _, name, n_locals = line.split(" ")
            functions[name] = int(n_locals)
            current_function = name
            # No allocation or return address handling happens here
            # we're just translating the body of the function into
            # ASM, and storing data that's necessary for `call` to
            # work.
            yield f"// start function {name}"
            yield f"({name})"
            for i in range(int(n_locals)):
                yield from push("constant", False, 0)

        if line.startswith("return"):
            # pop an item off the stack (this is the return value)
            # put it in the bottom most part of the caller's stack
#            yield from pop("argument", is_ptr=True)
#            # pop local args away from the stack
#            # TODO: we don't actually care about these values
#            # so we could adjust the SP address instead
#            for i in range(functions[current_function] - 1):
#                yield from pop("R14", is_ptr=False)
#            # reset the stack pointer to the right location for the caller
#            yield "@ARG"
#            yield "D=M+1"
#            yield "@SP"
#            yield "A=D"
#            # then restore the previous that, this, local, and arg pointers,
#            # which are next on the stack
#            for ptr in ("THAT", "THIS", "ARG", "LCL"):
#                yield from pop(ptr, is_ptr=False)
#            # next is the return address
#            yield from pop("R13", is_ptr=False)
#            # and jump to the return address
#            yield "@R13"
#            yield "A=M"
#            yield "0;JMP"
            # this logic is totally fucked. call logic is fine (or not)
            # FRAME (R13) = LCL - GOOD
            yield "@LCL"
            yield "D=M"
            yield "@R13"
            yield "M=D"
            # RET (R14) = FRAME - 5 - GOOD
            for i in range(5):
                yield "D=D-1"
            yield "A=D"
            yield "D=M"
            yield "@R14"
            yield "M=D"
            # *ARG = pop() - GOOD
            yield from pop("argument", is_ptr=True)
            # SP = ARG+1 - GOOD
            yield "@ARG"
            yield "D=M+1"
            yield "@SP"
            yield "M=D"
            # THAT = *FRAME - 1, etc. - GOOD i think?
            yield "@R13"
            yield "D=M-1"
            yield "@THAT"
            yield "M=D"
            yield "D=D-1"
            yield "@THIS"
            yield "M=D"
            yield "D=D-1"
            yield "@ARG"
            yield "M=D"
            yield "D=D-1"
            yield "@LCL"
            yield "M=D"
            # return to caller
            yield "@R14"
            yield "A=M"
            yield "0;JMP"
            current_function = ""

        if line.startswith("call"):
            _, name, n_args = line.split()
            # push the return address onto the stack
            yield from push("constant", False, f"{name}_return_{label_count}")
            # TODO: it looks like this and that are pushed wrong
            # we get absolutel values instead of addresses in the stack
            # should pointer 0/1 get pushed instead?
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
            # and adjust LCL
            yield "@SP"
            yield "D=M"
            yield "@LCL"
            yield "M=D"
            # and jump to the function
            yield f"@{name}"
            yield "0;JMP"
            # declare the return address label
            yield f"({name}_return_{label_count})"
            label_count += 1

        label_count = yield from translate_instruction(line, label_count)


def init() -> Generator[str, None, None]:
    yield "// begin init"
    yield "@256"
    yield "D=A"
    yield "@SP"
    yield "M=D"
    yield "@Sys.init"
    yield "0;JMP"


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_translate [file_to_translate ...]")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    for line in init():
        print(line)

    for fn in sys.argv[1:]:
        with open(fn) as f:
            for line in translate(f):
                print(line)
