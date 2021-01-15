// begin init
@256
D=A
@SP
M=A
@Sys.init
0;JMP
// start function Main.fibonacci
(Main.fibonacci)
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
D=D-M
@SP
M=M-1
M=M-1
@EQUAL.0
D;JGT
@SP
A=M
M=0
@END.0
0;JMP
(EQUAL.0)
@SP
A=M
M=-1
(END.0)
@SP
D=M+1
M=D
// start if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
// end if-goto IF_TRUE
// start goto IF_FALSE
@IF_FALSE
0;JMP
// end goto IF_FALSE
(IF_TRUE)
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
(IF_FALSE)
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
// start push Main.fibonacci_return_1 0
@Main.fibonacci_return_1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push Main.fibonacci_return_1 0
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
(Main.fibonacci_return_1)
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
// start push Main.fibonacci_return_2 0
@Main.fibonacci_return_2
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push Main.fibonacci_return_2 0
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
(Main.fibonacci_return_2)
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
// start function Sys.init
(Sys.init)
// start push constant 4
@4
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 4
// start push Main.fibonacci_return_0 0
@Main.fibonacci_return_0
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push Main.fibonacci_return_0 0
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
(Main.fibonacci_return_0)
(WHILE)
// start goto WHILE
@WHILE
0;JMP
// end goto WHILE
