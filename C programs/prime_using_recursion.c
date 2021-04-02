#include <stdio.h>

// declaring the recursive function
int isPrime(int, int);

int main()
{
    int num, prime;
    printf("Enter a positive number to check if Prime: ");
    scanf("%d", &num);
    prime = isPrime(num, num / 2);
    if (prime == 1)
    {
        printf("\n\n%d is a prime number\n\n", num);
    }
    else
    {
        printf("\n\n%d is a Composite number\n\n", num);
    }
    return 0;
}

// function definition
int isPrime(int n, int i)
{
    if (i == 1)
        return 1; // return statement terminates the recursive funtion
    else
    {
        if (n % i == 0)
            return 0;
        else
            isPrime(n, i - 1); // recursive call not using return statement
    }
}
