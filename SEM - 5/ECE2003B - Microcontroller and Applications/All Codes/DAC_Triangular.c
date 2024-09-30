
// Exp - 5 DAC Interfacing with C8051F340
/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY

DAC_Triangular Waveform

*/

#include"c8051f340.h"
void main(){
	int i;
	P4MDOUT=0xff;
	while(1){
		for(i=0; i<=254;i++){
			P4=i;
		}
		for(i=255; i>=1; i--){
			P4=i;
		}
	}
}