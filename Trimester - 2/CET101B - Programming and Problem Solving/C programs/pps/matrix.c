// program to find average marks obtained by
//class of 10 students in a test.

#include<stdio.h>
int main()
{

int avg,sum =0;
int i;

int marks[10]; // Array declaration

for (i=0;i<=9;i++)
{
  printf("Enter Marks :");
  scanf("%d", &marks[i]); // store data in array
}

for(i=0;i<=9;i++)
sum=sum+marks[i]; //read data from an Array

avg=sum/10;

printf("average marks=%d\n",avg);

  return 0;
}