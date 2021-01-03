import pytest

from n2ttools.vm2asm import split_functions


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
