// Exp - 8 Implement UART with C8051F340
/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY

Tranmission program:
*/

#include"c8051f340.h"
#define sysclk 12000000
#define BR_UART0 9600

void main()
{
	char ch[]=("SUGANDH");
	int i;
	OSCICN = 0X80;
	XBR0=0X01;
	XBR1=0X40;
	P0MDOUT=0X10;
	SCON0=0X00;
	CKCON=0X01;
	TH1=256-(sysclk/BR_UART0/2/4);
	TH1=TL1;
	TMOD=0x20;
	TR1=1;
	while(1)
	{
		for(i=0;ch[i]!='\0';i++)
		{
			SBUF0=ch[i];
			while(TI0==0);
		}
	}
}
