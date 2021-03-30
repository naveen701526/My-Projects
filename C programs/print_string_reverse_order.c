#include <stdio.h>
#include <string.h>
 
void main()
{
   char str1[100], tmp;
   int l, lind, rind,i;

       printf("\n\nPrint a string in reverse order:\n ");
       printf("-------------------------------------\n");

   printf("Input a string to reverse : ");
   scanf("%s", str1);
   l = strlen(str1);

   lind = 0;
   rind = l-1;
    
for(i=lind;i<rind;i++)
       {
       tmp = str1[i];
       str1[i] = str1[rind];
       str1[rind] = tmp;
       rind--;
   }
 
   printf("Reversed string is: %s\n\n", str1);
}
