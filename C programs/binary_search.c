#include <stdio.h>
#include <stdlib.h>

//Function which will find the required element in array
//provided if the array is sorted 
int binary_search(int *, int, int, int);

int main()
{
    int *p, n, target;
    printf("enter the size: \n");
    scanf("%d", &n);
    //Allocate memory to array
    p = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("enter the number %d :", i + 1);
        scanf("%d", p + i);
    }

    printf("enter the target number : ");
    scanf("%d", &target);
    int l = 0;
    int r = n - 1;
    printf("Your number is present at : %d position\n", binary_search(p, l, r, target) + 1);
    free(p);
    return 0;
}

int binary_search(int *p, int left, int right, int target)
{
    int mid;
    while (l <= r)
    {
        //Calculating the index where the element might be present
        mid = left + right / 2;
        if (*(p + mid) == target)
            return mid;
        if (*(p + mid) < target)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}



//Time complexity of binary search is O(logn)
//Space complexity of binary search is O(1)
