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
// start pop 3 1
@SP
A=M-1
D=M
@3
A=A+1
M=D
@SP
M=M-1
// end pop 3 1
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
// start pop THAT 0
@SP
A=M-1
D=M
@THAT
A=M
M=D
@SP
M=M-1
// end pop THAT 0
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
// start pop THAT 1
@SP
A=M-1
D=M
@THAT
A=M
A=A+1
M=D
@SP
M=M-1
// end pop THAT 1
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
(MAIN_LOOP_START)
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
// start if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
// end if-goto COMPUTE_ELEMENT
// start goto END_PROGRAM
@END_PROGRAM
0;JMP
// end goto END_PROGRAM
(COMPUTE_ELEMENT)
// start push THAT 0
@THAT
A=M
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THAT 0
// start push THAT 1
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
// end push THAT 1
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop THAT 2
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
// end pop THAT 2
// start push 3 1
@3
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 3 1
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
// start pop 3 1
@SP
A=M-1
D=M
@3
A=A+1
M=D
@SP
M=M-1
// end pop 3 1
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
// start goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
// end goto MAIN_LOOP_START
(END_PROGRAM)
