#include <stdio.h>
void main()
{
    int  j, n, sum = 0;
    printf("Enter the value of n. \n");
    scanf("%d", &n);
    printf("The first %d natural number is :\n", n);
 
    for (j = 1; j <= n; j++)
    {
        sum = sum + j;
        printf("%d ",j);    
    }
    printf("\nThe Sum is : %d\n", sum);
}
