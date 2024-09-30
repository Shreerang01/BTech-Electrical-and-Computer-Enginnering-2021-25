

// Exp - 5 DAC Interfacing with C8051F340
/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY

DAC_Square Waveform

*/

#include"c8051f340.h"
void delay(unsigned int Ms);
void main(){
	P4MDOUT=0xff;
	while(1){
		P4=~P4;
		delay(50);
	}
}
void delay(unsigned int Ms){
	unsigned int n;
	unsigned int i;
	for(n=0;n<Ms;n++){
		for(i=0;i<65;i++);
	}
}

