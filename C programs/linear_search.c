#include <stdio.h>
#include <stdlib.h>

int linear_search(int *, int, int);

int main()
{
    int *p, n, target;
    printf("enter the size: \n");
    scanf("%d", &n);

    p = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("enter the number %d :", i + 1);
        scanf("%d", p + i);
    }

    printf("enter the target number : ");
    scanf("%d", &target);
    printf("Your number is present at : %d position\n", linear_search(p, n, target) + 1);
    free(p);
    return 0;
}

int linear_search(int *p, int n, int target)
{
    for (int i = 0; i < n; i++)
    {
        if (*(p + i) == target)
        {
            return i;
        }
    }

    return -1;
}