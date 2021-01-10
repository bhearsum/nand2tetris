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
// start pop local 0
@SP
A=M-1
D=M
@LCL
A=M
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop local 0
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
// start pop argument 2
@SP
A=M-1
D=M
@ARG
A=M
A=A+1
A=A+1
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop argument 2
// start pop argument 1
@SP
A=M-1
D=M
@ARG
A=M
A=A+1
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop argument 1
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
// start pop this 6
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
A=M
D=A-1
@SP
M=D
// end pop this 6
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
// start pop that 5
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
A=M
D=A-1
@SP
M=D
// end pop that 5
// start pop that 2
@SP
A=M-1
D=M
@THAT
A=M
A=A+1
A=A+1
M=D
@SP
A=M
D=A-1
@SP
M=D
// end pop that 2
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
// start pop temp 6
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
A=M
D=A-1
@SP
M=D
// end pop temp 6
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
// start push that 5
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
// end push that 5
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start push argument 1
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
// end push argument 1
@SP
A=M-1
D=M
A=A-1
M=M-D
D=A+1
@SP
M=D
// start push this 6
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
// end push this 6
// start push this 6
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
// end push this 6
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
// start push temp 6
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
// end push temp 6
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
