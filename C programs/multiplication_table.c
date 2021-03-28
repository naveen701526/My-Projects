#include <stdio.h>
void main()
{
   int j,n;
   printf("Input the Table to be calculated : ");
   scanf("%d",&n);
   printf("\n");
   for(j=1;j<=10;j++)
   {
     printf("%d X %d = %d \n",n,j,n*j);
   }
} 
