#include <stdio.h>

int main()
{
    int n, s, i, j;
    printf("Enter number of rows: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        //display space
        for (s = i; s < n; s++)
        {
            printf(" ");
        }
        //display star equal to row number
        for (j = 1; j <= (2 * i - 1); j++)
        {
            printf("*");
        }
        // next line
        printf("\n");
    }
}
