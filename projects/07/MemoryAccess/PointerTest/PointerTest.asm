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
// start pop pointer 0
@SP
A=M-1
D=M
@3
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop pointer 0
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
// start pop pointer 1
@SP
A=M-1
D=M
@3
A=A+1
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop pointer 1
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
// start pop this 2
@SP
A=M-1
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop this 2
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
// start pop that 6
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
A=M
D=A-1
@SP
M=D
// end pop that 6
// start push pointer 0
@3
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push pointer 0
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
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push this 2
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
// end push this 2
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push that 6
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
// end push that 6
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
