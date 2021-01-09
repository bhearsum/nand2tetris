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
// start pop local 300
@SP
A=M-1
D=M
@300
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop local 300
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
// start pop argument 402
@SP
A=M-1
D=M
@402
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop argument 402
// start pop argument 401
@SP
A=M-1
D=M
@401
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop argument 401
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
// start pop this 3006
@SP
A=M-1
D=M
@3006
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop this 3006
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
// start pop that 3015
@SP
A=M-1
D=M
@3015
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop that 3015
// start pop that 3012
@SP
A=M-1
D=M
@3012
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop that 3012
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
// start pop temp 11
@SP
A=M-1
D=M
@11
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop temp 11
// start push local 300
@300
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push local 300
// start push that 3015
@3015
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push that 3015
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push argument 401
@401
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push argument 401
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push this 3006
@3006
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push this 3006
// start push this 3006
@3006
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push this 3006
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
// start push temp 11
@11
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push temp 11
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
