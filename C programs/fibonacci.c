#include<stdio.h>    
int main()    
{    
 int n1,n2,n3,i,number;    
 printf("Enter the number of elements:");    
 scanf("%d",&number);    
 printf("Enter First number and Second number :");
 scanf("%d%d", &n1,&n2);
 printf("%d %d", n1, n2);
 for(i=2;i<number;++i)//loop starts from 2 because n1 and n2 are already printed    
 {    
  n3=n1+n2;    
  printf(" %d",n3);    
  n1=n2;    
  n2=n3;    
 }  
  return 0;  
 }    
