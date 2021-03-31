#include <stdio.h>
#include <stdlib.h>
//find triplet using sorting
int compareFun(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}
int findTriplet(int arr[], int size, int sum)
{
    int leftIndex, rightIndex, tripletSum;
    qsort(arr, size, sizeof(int), compareFun);
    for (int index = 0; index < size; index++)
    {
        leftIndex = index + 1;
        rightIndex = size - 1;
        while (leftIndex < rightIndex)
        {
            tripletSum = arr[index] + arr[leftIndex] + arr[rightIndex];
            if (tripletSum == sum)
            {
                printf("Triplet is %d, %d and %d\n", arr[index], arr[leftIndex],
                       arr[rightIndex]);
                return 1;
            }
            if (tripletSum < sum)
                leftIndex++;
            else
                rightIndex--;
        }
    }
    return 0;
}
int main()
{
    int *arr, size, sum;
    printf("Enter size of the array\n");
    scanf("%d", &size);
    printf("Enter elements in array\n");
    for (int index = 0; index < size; index++)
        scanf("%d", &arr[index]);
    printf("Enter the value of sum\n");
    scanf("%d", &sum);
    if (!findTriplet(arr, size, sum))
        printf("Triplet not found");
    return 0;
}
// Time complexity : O(n^2)
//  Space Complexity : O(1)
