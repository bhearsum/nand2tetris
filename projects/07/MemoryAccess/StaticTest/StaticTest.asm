// begin init
@256
D=A
@SP
M=D
@300
D=A
@LCL
M=D
@400
D=A
@ARG
M=D
@3000
D=A
@THIS
M=D
@3010
D=A
@THAT
M=D
// end init
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
// start pop static 24
@SP
A=M-1
D=M
@24
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop static 24
// start pop static 19
@SP
A=M-1
D=M
@19
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop static 19
// start pop static 17
@SP
A=M-1
D=M
@17
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop static 17
// start push static 19
@19
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push static 19
// start push static 17
@17
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push static 17
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push static 24
@24
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push static 24
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
