// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(POLL)
    @KBD
    D=M
    @DRAWBLACK
    D;JNE       // Draw black if there's a value in the keyboard register
    @DRAWWHITE
    0;JMP       // Otherwise, draw white

(DRAWBLACK)
    @R0
    M=0      // R0 tracks the current screen pixel we're at

(BLACKLOOP)
    @R0         // Go back to polling if we've reached the last pixel
    D=M
    @8192
    D=A-D
    @POLL
    D;JEQ

    @R0
    D=M
    @SCREEN
    A=A+D
    M=-1         // Otherwise draw black to the current pixel
                 // This is negative one because "1" is the value
                 // for black, and the screen's memory maps are
                 // 16-bit values, and -1's binary representation is all 1s.

    @R0
    M=M+1

    @BLACKLOOP
    0;JMP


(DRAWWHITE)
    @R0
    M=0      // R0 tracks the current screen pixel we're at

(WHITELOOP)
    @R0         // Go back to polling if we've reached the last pixel
    D=M
    @8192
    D=A-D
    @POLL
    D;JEQ

    @R0
    D=M
    @SCREEN
    A=A+D
    M=0         // Otherwise draw white to the current pixel

    @R0
    M=M+1

    @WHITELOOP
    0;JMP
