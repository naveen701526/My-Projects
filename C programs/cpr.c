#include <stdio.h>

int main()
{
    char *x;
    int a = 512;
    x = (char *)&a;
    x[0] = 1;
    x[1] = 2;
    printf("%d\n", a);

    return 0;
}