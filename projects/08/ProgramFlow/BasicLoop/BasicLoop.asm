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
// start pop LCL 0
@SP
A=M-1
D=M
@LCL
A=M
M=D
@SP
M=M-1
// end pop LCL 0
(LOOP_START)
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
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop LCL 0
@SP
A=M-1
D=M
@LCL
A=M
M=D
@SP
M=M-1
// end pop LCL 0
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
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// end pop ARG 0
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
// start if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
// end if-goto LOOP_START
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
