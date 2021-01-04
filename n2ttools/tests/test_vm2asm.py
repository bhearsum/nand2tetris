import pytest
from io import StringIO

from n2ttools.vm2asm import split_functions, translate


@pytest.mark.parametrize(
    "vmcode,funcnames",
    [
        (
            """
            function mult 2
                push constant 0
                pop local 0
                push argument 1
                return
            """,
            ("mult",),
        ),
        (
            """
            function mult 2
                push constant 0
                pop local 0
                push argument 1
                return
            function div 2
                push constant 0
                pop local 0
                return
            """,
            ("mult", "div"),
        ),
        (
            """
            function mult 2
                push constant 0
                pop local 0
                push argument 1
                pop local 1
            label loop
                push constant 0
                pop local 1
                Eq
                if-goto end
                goto loop
            label end
                return
            """,
            ("mult",),
        ),
        (
            """
            function mult 2
                push constant 0
                pop local 0
                push argument 1
                pop local 1
            label mult.loop
                push constant 0
                pop local 1
                Eq
                if-goto mult.end
                goto mult.loop
            label mult.end
                return
            function div 2
                push constant 0
                pop local 0
                push argument 1
                pop local 1
            label div.loop
                push constant 0
                pop local 1
                Eq
                if-goto div.end
                goto div.loop
            label div.end
                return
            """,
            ("mult", "div"),
        ),
    ],
)
def test_split_functions(vmcode, funcnames):
    fns = split_functions(vmcode)
    assert set(fns.keys()) == set(funcnames)


@pytest.mark.parametrize(
    "vmcode,asmcode",
    [
        (
            """
push argument 0
            """,
            """
@ARG
D=M
@SP
M=D
D=A+1
@0
M=D
            """,
        ),
        (
            """
push argument 1
            """,
            """
@ARG
A=A+1
D=M
@SP
M=D
D=A+1
@0
M=D
            """,
        ),
        (
            """
push static 0
            """,
            """
            """,
        ),
        (
            """
push static 1
            """,
            """
            """,
        ),
        (
            """
push constant 0
            """,
            """
@256
D=A
@0
M=D
@0
D=A
@SP
M=D
D=A+1
@0
M=D
            """,
        ),
        (
            """
push this 0
            """,
            """
            """,
        ),
        (
            """
push this 1
            """,
            """
            """,
        ),
        (
            """
push that 0
            """,
            """
            """,
        ),
        (
            """
push that 1
            """,
            """
            """,
        ),
        (
            """
push pointer 0
            """,
            """
            """,
        ),
        (
            """
push pointer 1
            """,
            """
            """,
        ),
        (
            """
push temp 0
            """,
            """
            """,
        ),
        (
            """
push temp 1
            """,
            """
            """,
        ),
        (
            """
add
            """,
            """
@256
D=A
@0
M=D
@SP
A=A-1
D=M
A=A-1
M=D+M
D=A+1
@0
M=D
            """,
        ),
    ]
)
def test_translate(vmcode, asmcode):
    translated_asm = ""
    for line in translate(StringIO(vmcode)):
        translated_asm += f"{line}\n"
    assert translated_asm.strip() == asmcode.strip()
