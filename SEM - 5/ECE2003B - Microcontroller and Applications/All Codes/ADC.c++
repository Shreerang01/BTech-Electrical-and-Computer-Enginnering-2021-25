// Exp - 5 ADC Interfacing with C8051F340

/*
Name: Shreerang Mhatre
Rollno: 52
Batch: A3
Class: TY
*/

#include "C8051F340.h"
#define SYSClk 12000000
sbit Buzzer= P3^3;
void delay(unsigned int Ms);
void main()
{
    XBR1= 0X40;
    P4MDOUT= 0XFF;
    www.mitwpu.edu.in
    Buzzer= 0;
    P2SKIP= 0X20;
    P2MDIN= 0XD0;
    AMX0P= 0X04;
    AMX0N= 0x1F;
    ADC0CF= (((SYSClk/3000000)-1)<<3);
    REF0CN= 0x08;
    ADC0CN= 0x80;
    AD0EN= 1;
    {
        ADC0CN =0x90;
        while (AD0BUSY == 1);
        delay(50);
        P4= ~ ADC0L;
        delay(50);
        P4= ~ ADC0H;
        delay(50);
    }
while(1);
}
void delay(unsigned int Ms)
{
    unsigned int n;
    unsigned int i;
    for (n-0; n<Ms; n++)
    {
        for (i=0; i<65; i++);
        www.mitwpu.edu.in
    }
}
