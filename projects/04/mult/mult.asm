// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @R2
    M=0
(LOOP)
    // end if R1 is zero
    @R1
    D=M
    @DONE
    D;JEQ

    // increase R2 by R0 value
    @R0
    D=M
    @R2
    M=M+D

    // decrease R1 by 1
    @R1
    M=M-1

    // loop
    @LOOP
    D;JMP
    
(DONE)
