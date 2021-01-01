import unittest

from n2ttools.assembler import parse_c_instruction


class AssemblerTests(unittest.TestCase):
    def test_c_instruction_all_parts(self):
        comp, dest, jump = parse_c_instruction("D=A+1;JGT")
        assert comp == "A+1"
        assert dest == "D"
        assert jump == "JGT"

    def test_c_instruction_no_jump(self):
        comp, dest, jump = parse_c_instruction("D=A+1")
        assert comp == "A+1"
        assert dest == "D"
        assert jump is None

    def test_c_instruction_no_dest(self):
        comp, dest, jump = parse_c_instruction("A+1;JGT")
        assert comp == "A+1"
        assert dest is None
        assert jump == "JGT"

    def test_c_instruction_no_jump_no_dest(self):
        comp, dest, jump = parse_c_instruction("A+1")
        assert comp == "A+1"
        assert dest is None
        assert jump is None

    def test_c_instruction_invalid_dest(self):
        try:
            parse_c_instruction("C=A+1")
        except ValueError as e:
            assert e.args[0] == "Invalid dest: C"
        else:
            assert False, "ValueError should've been raised"

    def test_c_instruction_invalid_jump(self):
        try:
            parse_c_instruction("D=A+1;JAG")
        except ValueError as e:
            assert e.args[0] == "Invalid jump: JAG"
        else:
            assert False, "ValueError should've been raised"


if __name__ == "__main__":
    unittest.main()
