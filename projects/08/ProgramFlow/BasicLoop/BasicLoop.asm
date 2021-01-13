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
// start pop local 0
@SP
A=M-1
D=M
@LCL
A=M
M=D
@SP
M=M-1
// end pop local 0
(LOOP_START)
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
// start push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push local 0
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop local 0
@SP
A=M-1
D=M
@LCL
A=M
M=D
@SP
M=M-1
// end pop local 0
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
// start if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
// start push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push local 0
