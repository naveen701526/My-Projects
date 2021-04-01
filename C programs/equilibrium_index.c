/*Find equilibrium index in an array */
#include <stdio.h>
#include <stdlib.h>
int EquilibriumIndex(int *arr, int size)
{
    int index, leftSum = 0, sum = 0;
    //calculate sum of whole array
    for (index = 0; index < size; index++)
        sum += arr[index];
    for (index = 0; index < size; index++)
    {
        sum -= arr[index];
        if (leftSum == sum)
            return index;
        leftSum += arr[index];
    }
    return -1;
}
int main()
{
    int *arr, size;
    printf("Enter number of elements in an array\n");
    scanf("%d", &size);
    //allocate memory for array
    arr = (int *)malloc(size * sizeof(int));
    for (int index = 0; index < size; index++)
        scanf("%d", &arr[index]);
    printf("Equilibrium index = %d",
           EquilibriumIndex(arr, size));
    return 0;
}
// Time complexity : O(n)
// Space complexity : O(1)
