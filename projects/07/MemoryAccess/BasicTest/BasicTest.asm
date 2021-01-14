// start push constant 10
@10
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 10
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
// start push constant 21
@21
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 21
// start push constant 22
@22
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 22
// start pop ARG 2
@SP
A=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop ARG 2
// start pop ARG 1
@SP
A=M-1
D=M
@ARG
A=M
A=A+1
M=D
@SP
M=M-1
// end pop ARG 1
// start push constant 36
@36
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 36
// start pop THIS 6
@SP
A=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop THIS 6
// start push constant 42
@42
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 42
// start push constant 45
@45
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 45
// start pop THAT 5
@SP
A=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop THAT 5
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
// start push constant 510
@510
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 510
// start pop 5 6
@SP
A=M-1
D=M
@5
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop 5 6
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
// start push THAT 5
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THAT 5
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
// start push THIS 6
@THIS
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THIS 6
// start push THIS 6
@THIS
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THIS 6
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
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push 5 6
@5
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 5 6
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
