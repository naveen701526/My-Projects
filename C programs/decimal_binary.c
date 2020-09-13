#include <stdio.h>

int main()
{
    int decimal, array[10], i = 0;
    printf("Enter the decimal number: ");
    scanf("%d", &decimal);
    while (decimal)
    {
        array[i] = decimal % 2;
        i++;
        decimal = decimal / 2;
    }
    printf("Binary number is: \n");
    while (--i >= 0)
    {
        printf("%d", array[i]);
    }

    printf("\n");

    return 0;
}
