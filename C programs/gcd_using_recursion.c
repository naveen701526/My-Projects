#include <stdio.h>

int gcd(int c, int d) // function definition
{
    if (d == 0)
        return c;
    else
        return gcd(d, c % d);
}

int main()
{
    int a, b;
    printf("Enter 2 numbers: \n\n");
    scanf("%d%d", &a, &b);
    printf("\n\nGreatest Common Divisor is: %d", gcd(a, b)); // function calling
    return 0;
}
