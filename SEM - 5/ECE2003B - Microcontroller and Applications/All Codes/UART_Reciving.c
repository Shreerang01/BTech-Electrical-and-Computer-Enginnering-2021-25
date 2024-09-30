// Exp - 8 Implement UART with C8051F340
/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY

Reciving Program:

*/

#include"c8051f340.h"
#define sysclk 12000000
#define BR_UART0 9600
sbit BUZZER=P3^3;

void main()
{
	OSCICN = 0X83;
	XBR0=0X01;
	XBR1=0X40;
	P3MDOUT=0X08;
	BUZZER=1;
	P0MDIN=0X20;
	P4MDOUT=0xFF;
	SCON0=0X10;
	CKCON=0X01;
	TH1=256-(sysclk/BR_UART0/2/4);
	TH1=TL1;
	TMOD=0x20;
	TR1=1;
	while(RI0==0)
	{
		P4=~SBUF0;
		RI0=0;
	}
}
