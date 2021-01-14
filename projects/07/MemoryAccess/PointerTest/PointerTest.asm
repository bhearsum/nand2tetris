// start push constant 3030
@3030
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 3030
// start pop 3 0
@SP
A=M-1
D=M
@3
M=D
@SP
M=M-1
// end pop 3 0
// start push constant 3040
@3040
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 3040
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
// start push constant 32
@32
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 32
// start pop THIS 2
@SP
A=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop THIS 2
// start push constant 46
@46
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 46
// start pop THAT 6
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
A=A+1
M=D
@SP
M=M-1
// end pop THAT 6
// start push 3 0
@3
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 3 0
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
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push THIS 2
@THIS
A=M
A=A+1
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THIS 2
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push THAT 6
@THAT
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
// end push THAT 6
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
