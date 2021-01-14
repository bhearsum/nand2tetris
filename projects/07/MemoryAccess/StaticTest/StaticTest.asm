// start push constant 111
@111
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 111
// start push constant 333
@333
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 333
// start push constant 888
@888
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 888
// start pop 16 8
@SP
A=M-1
D=M
@16
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop 16 8
// start pop 16 3
@SP
A=M-1
D=M
@16
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop 16 3
// start pop 16 1
@SP
A=M-1
D=M
@16
A=A+1
M=D
@SP
M=M-1
// end pop 16 1
// start push 16 3
@16
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
// end push 16 3
// start push 16 1
@16
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 16 1
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push 16 8
@16
A=A+1
A=A+1
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
// end push 16 8
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
