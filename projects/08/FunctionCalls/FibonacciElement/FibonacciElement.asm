// begin init
@256
D=A
@SP
M=D
// start push constant Sys.init_return_0
@Sys.init_return_0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Sys.init_return_0
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
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init_return_0)
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
@LCL
D=M
@R13
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@R14
M=D
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// end pop ARG 0
@ARG
D=M+1
@SP
M=D
@R13
A=M-1
D=M
@THAT
M=D
@R13
A=M-1
A=A-1
D=M
@THIS
M=D
@R13
A=M-1
A=A-1
A=A-1
D=M
@ARG
M=D
@R13
A=M-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
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
// start push constant Main.fibonacci_return_1
@Main.fibonacci_return_1
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Main.fibonacci_return_1
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
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
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
// start push constant Main.fibonacci_return_2
@Main.fibonacci_return_2
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Main.fibonacci_return_2
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
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci_return_2)
@SP
A=M-1
D=M
A=A-1
M=D+M
D=A+1
@SP
M=D
@LCL
D=M
@R13
M=D
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@R14
M=D
// start pop ARG 0
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
// end pop ARG 0
@ARG
D=M+1
@SP
M=D
@R13
A=M-1
D=M
@THAT
M=D
@R13
A=M-1
A=A-1
D=M
@THIS
M=D
@R13
A=M-1
A=A-1
A=A-1
D=M
@ARG
M=D
@R13
A=M-1
A=A-1
A=A-1
A=A-1
D=M
@LCL
M=D
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
// start push constant Main.fibonacci_return_0
@Main.fibonacci_return_0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Main.fibonacci_return_0
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
A=M
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci_return_0)
(WHILE)
// start goto WHILE
@WHILE
0;JMP
// end goto WHILE
