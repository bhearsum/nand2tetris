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

# Function name -> (number of args, number of locals)
FuncDef = Dict[str, Tuple[int, int]]


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


def translate_instruction(
    inst: str, label_count: int, functions: FuncDef, current_function: str = ""
) -> Generator[str, None, int]:
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

    # TODO: i think nested calls are not working?
    if inst.startswith("return"):
        # pop an item off the stack (this is the return value)
        yield from pop("R13", is_ptr=False)
        # then restore the previous that, this, local, and arg pointers,
        # which are next on the stack
        for ptr in ("THAT", "THIS", "ARG", "LCL"):
            yield from pop(ptr, is_ptr=False)
        # next is the return address
        yield from pop("R14", is_ptr=False)
        # pop local args away from the stack
        # TODO: we don't actually care about these values
        # so we could adjust the SP address instead
        for i in range(functions[current_function][1] - 1):
            yield from pop("temp", is_ptr=False)
        # and then we have to pop away args, like we did for locals
        # we also don't care about them
        for i in range(functions[current_function][0] - 1):
            yield from pop("temp", is_ptr=False)
        # then push the return value back onto the stack
        yield from push("R13", is_ptr=False)
        # and jump to the return address
        yield "@R14"
        yield "A=M"
        yield "0;JMP"

    if inst.startswith("call"):
        _, name, n_args = inst.split()
        # push the return address onto the stack
        yield from push(f"{name}_return_{label_count}", is_ptr=False)
        for ptr in ("LCL", "ARG", "THIS", "THAT"):
            yield from push(ptr, is_ptr=False)
        # adjust ARG for the called function, which are behind
        # the the return address, new LCL, et. al in the stack
        yield "@SP"
        for i in range(functions[name][0] + 1 + 5):
            yield "A=A-1"
        yield "D=A"
        yield "@ARG"
        yield "A=D"
        # and adjust LCL
        yield "@SP"
        yield "D=A"
        yield "@LCL"
        yield "A=D"
        # declare the return address label
        yield f"({name}_return_{label_count})"
        label_count += 1

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


def translate(f: TextIO, functions: FuncDef) -> Generator[str, None, None]:
    label_count = 0
    current_function = ""

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()

        if line.startswith("function"):
            _, name, n = line.split(" ")
            current_function = name
            # No allocation or return address handling happens here
            # we're just translating the body of the function into
            # ASM, and storing data that's necessary for `call` to
            # work.
            yield f"// start function {name}"
            yield f"({name})"

        label_count = yield from translate_instruction(line, label_count, functions, current_function)


def parse_functions(f: TextIO) -> FuncDef:
    functions: FuncDef = {}
    current_function = ""
    function_args = 0
    function_locals = 0

    for line in f.read().splitlines():
        line = line.split("/")[0].strip()

        if line.startswith("function"):
            if current_function:
                functions[current_function] = (function_args, function_locals)

            _, name, n = line.split(" ")
            current_function = name
            function_args = int(n)

        if current_function:
            if " local " in line:
                function_locals = max(function_locals, int(line.split(" ")[-1]) + 1)

    if current_function:
        functions[current_function] = (function_args, function_locals)

    return functions


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

    functions: FuncDef = {}

    for fn in sys.argv[1:]:
        with open(fn) as f:
            functions.update(parse_functions(f))

    for line in init():
        print(line)

    for fn in sys.argv[1:]:
        with open(fn) as f:
            for line in translate(f, functions):
                print(line)
