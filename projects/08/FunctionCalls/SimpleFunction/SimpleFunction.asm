// start function SimpleFunction.test
(SimpleFunction.test)
// start push LCL 0
@LCL
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push LCL 0
// start push LCL 1
@LCL
A=M
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push LCL 1
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
@SP
A=M-1
M=!M
D=A+1
@SP
M=D
// start push ARG 0
@ARG
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push ARG 0
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push ARG 1
@ARG
A=M
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push ARG 1
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start pop R13 0
@SP
A=M-1
D=M
@R13
M=D
@SP
M=M-1
// end pop R13 0
// start pop THAT 0
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1
// end pop THAT 0
// start pop THIS 0
@SP
A=M-1
D=M
@THIS
M=D
@SP
M=M-1
// end pop THIS 0
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
M=D
@SP
M=M-1
// end pop ARG 0
// start pop LCL 0
@SP
A=M-1
D=M
@LCL
M=D
@SP
M=M-1
// end pop LCL 0
// start pop R14 0
@SP
A=M-1
D=M
@R14
M=D
@SP
M=M-1
// end pop R14 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start push R13 0
@R13
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push R13 0
@R14
A=M
0;JMP
