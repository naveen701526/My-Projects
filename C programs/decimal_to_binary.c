/*C program to convert number from decimal to binary*/

#include <stdio.h>

int main()
{
    int number, cnt, i;
    int bin[32];

    printf("Enter decimal number: ");
    scanf("%d", &number);

    cnt = 0; /*initialize index to zero*/
    while (number > 0)
    {
        bin[cnt] = number % 2;
        number = number / 2;
        cnt++;
    }

    /*print value in reverse order*/
    printf("Binary value is: ");
    for (i = (cnt - 1); i >= 0; i--)
        printf("%d", bin[i]);

    return 0;
}
