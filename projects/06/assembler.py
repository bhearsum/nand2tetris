#!/usr/bin/env python3
#
# TODO:
#  * Implement symbol parsing

import sys
from typing import Tuple, Union


COMPUTE_INSTRUCTIONS = {
    # M versions also exist for all compute instructions
    # with A in them. They are identical to the A version
    # but with 0b1000000000000 added to them.
    "0":   0b101010000000,
    "1":   0b111111000000,
    "-1":  0b111010000000,
    "D":   0b001100000000,
    "A":   0b110000000000,
    "!D":  0b001101000000,
    "!A":  0b110001000000,
    "-D":  0b001111000000,
    "-A":  0b110011000000,
    "D+1": 0b011111000000,
    "A+1": 0b110111000000,
    "D-1": 0b001110000000,
    "A-1": 0b110010000000,
    "D+A": 0b000010000000,
    "D-A": 0b010011000000,
    "A-D": 0b000111000000,
    "D&A": 0b000000000000,
    "D|A": 0b010101000000,
}
DESTS = {
    None: 0,
    "M":   0b001000,
    "D":   0b010000,
    "MD":  0b011000,
    "A":   0b100000,
    "AM":  0b101000,
    "AD":  0b110000,
    "AMD": 0b111000,
}
JUMPS = {
    None: 0,
    "JGT": 0b001,
    "JEQ": 0b010,
    "JGE": 0b011,
    "JLT": 0b100,
    "JNE": 0b101,
    "JLE": 0b110,
    "JMP": 0b111,
}


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

    if dest and dest not in DESTS:
        raise ValueError(f"Invalid dest: {dest}")

    if jump and jump not in JUMPS:
        raise ValueError(f"Invalid jump: {jump}")

    return comp, dest, jump


def c_instruction(comp: str, dest: str, jump: str) -> str:
    static = 0b1110000000000000
    a_bit = 0
    if "M" in comp:
        a_bit = 0b1000000000000
        comp = comp.replace("M", "A")

    comp_bits = COMPUTE_INSTRUCTIONS[comp]

    if dest:
        dest_bits = DESTS[dest]
    else:
        dest_bits = 0

    if jump:
        jump_bits = JUMPS[jump]
    else:
        jump_bits = 0

    inst = static | a_bit | comp_bits | dest_bits | jump_bits
    return "{:0>16b}".format(inst)


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
