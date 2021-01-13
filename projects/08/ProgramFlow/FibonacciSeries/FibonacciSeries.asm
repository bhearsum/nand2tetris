// start push argument 1
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
// end push argument 1
// start pop pointer 1
@SP
A=M-1
D=M
@3
A=A+1
M=D
@SP
M=M-1
// end pop pointer 1
// start push constant 0
@0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 0
// start pop that 0
@SP
A=M-1
D=M
@THAT
A=M
M=D
@SP
M=M-1
// end pop that 0
// start push constant 1
@1
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 1
// start pop that 1
@SP
A=M-1
D=M
@THAT
A=M
A=A+1
M=D
@SP
M=M-1
// end pop that 1
// start push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push argument 0
// start push constant 2
@2
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 2
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start pop argument 0
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// end pop argument 0
(MAIN_LOOP_START)
// start push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push argument 0
// start if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
// end if-goto COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// start push that 0
@THAT
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push that 0
// start push that 1
@THAT
A=M
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push that 1
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop that 2
@SP
A=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop that 2
// start push pointer 1
@3
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push pointer 1
// start push constant 1
@1
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 1
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop pointer 1
@SP
A=M-1
D=M
@3
A=A+1
M=D
@SP
M=M-1
// end pop pointer 1
// start push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push argument 0
// start push constant 1
@1
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 1
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start pop argument 0
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// end pop argument 0
(END_PROGRAM)
