#include <stdio.h>

#include <stdlib.h>

//Size of the hash table
#define MAX 10000

//Function which will print the pair of elements who sum is equal to target variable
void two_sum(int *, int, int);

int main()
{
    int *ptr, n, target;
    printf("enter the size :");
    scanf("%d", &n);
    //Allocate memory for array
    ptr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("enter the %d number :", i + 1);
        scanf("%d", ptr + i);
    }
    printf("enter the target sum: ");
    scanf("%d", &target);
    two_sum(ptr, n, target);
    return 0;
}

void two_sum(int *ptr, int n, int target)
{
    int index, temp;
    int hash[MAX] = {0};
    for (index = 0; index < n; index++)
    {
        temp = target - *(ptr + index);
        if (temp >= 0 && hash[temp] == 1)
            printf("pair with given target sum %d is"
                   "(%d, %d)\n",
                   target, *(ptr + index), temp);
        hash[*(ptr + index)] = 1;
    }
}


//Time complexity: O(n)
//Space complexity: O(K) where K is range of integers


