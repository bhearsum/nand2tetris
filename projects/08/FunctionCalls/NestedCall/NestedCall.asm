// begin init
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// start function Sys.init
(Sys.init)
// start push constant 4000
@4000
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 4000
// start pop 3 0
@SP
A=M-1
D=M
@3
M=D
@SP
M=M-1
// end pop 3 0
// start push constant 5000
@5000
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 5000
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
// start push Sys.main_return_0 0
@Sys.main_return_0
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push Sys.main_return_0 0
// start push LCL 0
@LCL
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push LCL 0
// start push ARG 0
@ARG
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push ARG 0
// start push THIS 0
@THIS
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THIS 0
// start push THAT 0
@THAT
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THAT 0
@SP
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
A=D
@SP
D=A
@LCL
A=D
(Sys.main_return_0)
// start pop 5 1
@SP
A=M-1
D=M
@5
A=A+1
M=D
@SP
M=M-1
// end pop 5 1
(LOOP)
// start goto LOOP
@LOOP
0;JMP
// end goto LOOP
// start function Sys.main
(Sys.main)
// start push constant 4001
@4001
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 4001
// start pop 3 0
@SP
A=M-1
D=M
@3
M=D
@SP
M=M-1
// end pop 3 0
// start push constant 5001
@5001
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 5001
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
// start push constant 200
@200
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 200
// start pop LCL 1
@SP
A=M-1
D=M
@LCL
A=M
A=A+1
M=D
@SP
M=M-1
// end pop LCL 1
// start push constant 40
@40
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 40
// start pop LCL 2
@SP
A=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop LCL 2
// start push constant 6
@6
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 6
// start pop LCL 3
@SP
A=M-1
D=M
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
@SP
M=M-1
// end pop LCL 3
// start push constant 123
@123
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 123
// start push Sys.add12_return_1 0
@Sys.add12_return_1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push Sys.add12_return_1 0
// start push LCL 0
@LCL
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push LCL 0
// start push ARG 0
@ARG
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push ARG 0
// start push THIS 0
@THIS
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THIS 0
// start push THAT 0
@THAT
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push THAT 0
@SP
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
A=D
@SP
D=A
@LCL
A=D
(Sys.add12_return_1)
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
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
// start push LCL 1
@LCL
A=M
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push LCL 1
// start push LCL 2
@LCL
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
// end push LCL 2
// start push LCL 3
@LCL
A=M
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
// end push LCL 3
// start push LCL 4
@LCL
A=M
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
// end push LCL 4
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
M=D+M
D=A+1
@SP
M=D
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
M=D+M
D=A+1
@SP
M=D
// start pop R13 0
@SP
A=M-1
D=M
@R13
M=D
@SP
M=M-1
// end pop R13 0
// start pop THAT 0
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1
// end pop THAT 0
// start pop THIS 0
@SP
A=M-1
D=M
@THIS
M=D
@SP
M=M-1
// end pop THIS 0
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
M=D
@SP
M=M-1
// end pop ARG 0
// start pop LCL 0
@SP
A=M-1
D=M
@LCL
M=D
@SP
M=M-1
// end pop LCL 0
// start pop R14 0
@SP
A=M-1
D=M
@R14
M=D
@SP
M=M-1
// end pop R14 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start push R13 0
@R13
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push R13 0
@R14
A=M
0;JMP
// start function Sys.add12
(Sys.add12)
// start push constant 4002
@4002
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 4002
// start pop 3 0
@SP
A=M-1
D=M
@3
M=D
@SP
M=M-1
// end pop 3 0
// start push constant 5002
@5002
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 5002
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
// start push constant 12
@12
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 12
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
// start pop R13 0
@SP
A=M-1
D=M
@R13
M=D
@SP
M=M-1
// end pop R13 0
// start pop THAT 0
@SP
A=M-1
D=M
@THAT
M=D
@SP
M=M-1
// end pop THAT 0
// start pop THIS 0
@SP
A=M-1
D=M
@THIS
M=D
@SP
M=M-1
// end pop THIS 0
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
M=D
@SP
M=M-1
// end pop ARG 0
// start pop LCL 0
@SP
A=M-1
D=M
@LCL
M=D
@SP
M=M-1
// end pop LCL 0
// start pop R14 0
@SP
A=M-1
D=M
@R14
M=D
@SP
M=M-1
// end pop R14 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start push R13 0
@R13
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push R13 0
@R14
A=M
0;JMP
