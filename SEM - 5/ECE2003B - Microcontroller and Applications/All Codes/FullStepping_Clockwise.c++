
// Exp 9 Interfacing of Stepper motor with C8051F340
// Full Stepping in Clockwise Direction

/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY
*/

#include "C8051F340.h"
void delay(unsigned int Ms);
void main()
{
    char a[4]={0x02, 0x20, 0x80, 0x08};
	int i;
	P4MDOUT=0xFF;
	while(1)
	{
		for(i=0; i<4;i++)
		{
			P4=a[i];
			delay(60);
		}
	}
}
void delay(unsigned int Ms)
{
	unsigned int n;
	unsigned int j;
	for(n=0;n<Ms;n++)
	{
		for(j=0;j<65;j++);
	}
}