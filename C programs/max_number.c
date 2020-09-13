#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr1, *ptr, n, j = 0, maximum = 0;
    printf("Enter the size of input: ");
    scanf("%d", &n);

    ptr1 = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the %d number:", i + 1);
        scanf("%d", ptr1 + i);
    }

    ptr = ptr1;
    while (j < n - 1)
    {
        if (*(ptr + j) > *(ptr + j + 1))
        {
            maximum = *(ptr + j);
        }
        j++;
        ptr++;
    }

    if (!maximum)
    {
        maximum = *(ptr1 + j);
    }

    printf("The maximum is %d .", maximum);
    free(ptr1);

    return 0;
}