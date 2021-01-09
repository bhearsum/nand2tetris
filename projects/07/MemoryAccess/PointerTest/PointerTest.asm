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
@3030
D=A
@THIS
M=D
@3040
D=A
@THAT
M=D
// end init
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
// start pop pointer 2048
@SP
A=M-1
D=M
@2048
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop pointer 2048
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
// start pop pointer 2049
@SP
A=M-1
D=M
@2049
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop pointer 2049
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
// start pop this 3032
@SP
A=M-1
D=M
@3032
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop this 3032
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
// start pop that 3046
@SP
A=M-1
D=M
@3046
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop that 3046
// start push pointer 2048
@2048
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push pointer 2048
// start push pointer 2049
@2049
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push pointer 2049
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push this 3032
@3032
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push this 3032
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push that 3046
@3046
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push that 3046
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
