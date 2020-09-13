#include <stdio.h>
#include <math.h>

int main()
{
    int num, i, flag = 0, num1;
    printf("ENter the number: \n");
    scanf("%d", &num);
    num1 = num;
    for (i = 2; i <= floor(sqrt(num1)); i++)
    {
        if (num % i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {

        printf("This number is not prime. \n");
    }
    else
    {
        printf("This is a prime number. \n");
    }

    return 0;
}