
// Exp - 7 Generation of PWM using C8051F340 to control speed of DC motor
/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY

*/

#include "c8051f340.h"
#define SYSCLK 3000000
void main(){
	PCA0L=0x10;
	OSCICN=0x83;
	CLKSEL=0x00;
	XBR1=0x41;
	P2MDOUT=0x08;
	P0SKIP=0xff;
	P1SKIP=0xff;
	P2SKIP=0x07;
	while(1){
		PCA0MD=0x02;
		PCA0CPM0=0x42;
		PCA0CPH0=(256-(256*0.75));
		CR=1;
	}
}
