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
// start function Class1.set
(Class1.set)
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
// start pop 16 0
@SP
A=M-1
D=M
@16
M=D
@SP
M=M-1
// end pop 16 0
// start push ARG 1
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
// end push ARG 1
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
// start push constant 0
@0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 0
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
// start function Class1.get
(Class1.get)
// start push 16 0
@16
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 16 0
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
// start function Class2.set
(Class2.set)
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
// start pop 18 0
@SP
A=M-1
D=M
@18
M=D
@SP
M=M-1
// end pop 18 0
// start push ARG 1
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
// end push ARG 1
// start pop 18 1
@SP
A=M-1
D=M
@18
A=A+1
M=D
@SP
M=M-1
// end pop 18 1
// start push constant 0
@0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 0
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
// start function Class2.get
(Class2.get)
// start push 18 0
@18
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 18 0
// start push 18 1
@18
A=A+1
D=M
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push 18 1
@SP
A=M-1
D=M
A=A-1
M=M-D
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
// start push constant 8
@8
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 8
// start push constant Class1.set_return_0
@Class1.set_return_0
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Class1.set_return_0
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
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Class1.set_return_0)
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start push constant 23
@23
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 23
// start push constant 15
@15
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant 15
// start push constant Class2.set_return_1
@Class2.set_return_1
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Class2.set_return_1
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
A=A-1
D=A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Class2.set_return_1)
// start pop 5 0
@SP
A=M-1
D=M
@5
M=D
@SP
M=M-1
// end pop 5 0
// start push constant Class1.get_return_2
@Class1.get_return_2
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Class1.get_return_2
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
@Class1.get
0;JMP
(Class1.get_return_2)
// start push constant Class2.get_return_3
@Class2.get_return_3
D=A
@SP
A=M
M=D
D=A+1
@SP
M=D
// end push constant Class2.get_return_3
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
@Class2.get
0;JMP
(Class2.get_return_3)
(WHILE)
// start goto WHILE
@WHILE
0;JMP
// end goto WHILE
