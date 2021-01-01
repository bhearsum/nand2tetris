#!/usr/bin/env python3

import pprint
import sys
from typing import Dict, Tuple, Union


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
SYMBOL_TABLE: Dict[str, int] = {
    "R0":     0,
    "SP":     0,
    "R1":     1,
    "LCL":    1,
    "R2":     2,
    "ARG":    2,
    "R3":     3,
    "THIS":   3,
    "R4":     4,
    "THAT":   4,
    "R5":     5,
    "R6":     6,
    "R7":     7,
    "R8":     8,
    "R9":     9,
    "R10":    10,
    "R11":    11,
    "R12":    12,
    "R13":    13,
    "R14":    14,
    "R15":    15,
    "SCREEN": 0x4000,
    "KBD":    0x6000,
}
JUMP_TABLE: Dict[str, int] = {}
memory_addresses = iter(range(0, 0x3FFF))


def is_int(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


# We might need to do this in two passes:
# 1) go over all instructions and keep symbols in them, while
#    noting which explicit memory addresses are used
# 2) resolve symbols - allocating free memory addresses for them
#    at the same time
def resolve_symbol(sym: str) -> int:
    if sym in JUMP_TABLE:
        return JUMP_TABLE[sym]

    if sym in SYMBOL_TABLE:
        return SYMBOL_TABLE[sym]

    if is_int(sym):
        return int(sym)

    next_addr = next(memory_addresses)
    while next_addr in SYMBOL_TABLE.values():
        next_addr = next(memory_addresses)

    SYMBOL_TABLE[sym] = next_addr

    return SYMBOL_TABLE[sym]


def a_instruction(addr: str) -> str:
    return "{:0>16b}".format(resolve_symbol(addr))


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


def c_instruction(comp: str, dest: Union[str, None], jump: Union[str, None]) -> str:
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


def stage1(asm: str) -> str:
    """Strips away comments and blank lines and adds
    jump labels to lookup table."""

    preprocessed_asm = []
    lineno = 0
    for line in asm.splitlines():
        if "/" in line:
            line, _ = line.split("/", 1)
        else:
            line = line
        line = line.strip()

        if not line:
            continue

        if line.startswith("("):
            label = line.strip("()")
            JUMP_TABLE[label] = lineno
        else:
            lineno += 1

        preprocessed_asm.append(line)

    return "\n".join(preprocessed_asm)


def stage2(asm: str) -> None:
    for line in asm.splitlines():
        # Get rid of comments
        # TODO: do we need to deal with block comments?
        if "/" in line:
            instruction, _ = line.split("/", 1)
        else:
            instruction = line
        instruction = instruction.strip()

        # Skip blank lines, comment lines, or jump labels
        if not instruction or instruction.startswith("("):
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


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} file_to_assemble")
        print()
        print("Output will be written to stdout")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        stage1_output = stage1(f.read())

    stage2(stage1_output)

    print("SYMBOL TABLE:", file=sys.stderr)
    print(pprint.pformat(SYMBOL_TABLE), file=sys.stderr)
    print("JUMP TABLE:", file=sys.stderr)
    print(pprint.pformat(JUMP_TABLE), file=sys.stderr)
