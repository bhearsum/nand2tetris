#!/usr/bin/env python3

import sys
from typing import Tuple, Union


JUMPS = {
    None: None,
    "JGT": 0b001,
    "JEQ": 0b010,
    "JGE": 0b011,
    "JLT": 0b100,
    "JNE": 0b101,
    "JLE": 0b110,
    "JMP": 0b111,
}
VALID_DESTS = ("M", "D", "MD", "A", "AM", "AD", "AMD")


def a_instruction(addr: str) -> str:
    return "{:0>16b}".format(int(addr))


def parse_c_instruction(inst: str) -> Tuple[str,
                                            Union[str, None],
                                            Union[str, None]]:
    comp = None
    dest = None
    jump = None

    if "=" in inst:
        dest, inst = inst.split("=")
    if ";" in inst:
        comp, jump = inst.split(";")
    else:
        comp = inst

    if dest and dest not in VALID_DESTS:
        raise ValueError(f"Invalid dest: {dest}")

    if jump and jump not in JUMPS.keys():
        raise ValueError(f"Invalid jump: {jump}")

    return comp, dest, jump


def c_instruction(comp: str, dest: str, jump: str) -> str:
    if jump:
        jump_bits = JUMPS[jump]
    else:
        jump_bits = 0
    return "{:0>16b}".format(jump_bits)


def main(asm):
    for line in open(asm).readlines():
        # Get rid of comments
        # TODO: do we need to deal with block comments?
        if "/" in line:
            instruction, _ = line.split("/", 1)
        else:
            instruction = line
        instruction = instruction.strip()

        # Skip blank lines or comment lines
        if not instruction:
            continue

        # A instruction
        if instruction.startswith("@"):
            if len(instruction) < 2:
                print("Error: A (@) instruction has no address or symbol",
                      file=sys.stderr)
                sys.exit(1)

            _, addr = instruction.split("@", 2)
            print(a_instruction(addr))
            continue

        # C instruction
        comp, dest, jump = parse_c_instruction(instruction)
        print(c_instruction(comp, dest, jump))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_assemble")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    main(sys.argv[1])
