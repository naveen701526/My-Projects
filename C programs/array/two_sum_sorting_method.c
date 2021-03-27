// Find the pair whose sum is X
#include <stdio.h>
#include <stdlib.h>
int cmpfunc (const void * a, const void * b)
{
return ( *(int*)a - *(int*)b );
}
int findPairs(int *arr, int size, int sum)
{
int left, right;
//sort the array using quicksort (built function)
qsort(arr, size, sizeof(int), cmpfunc);
left = 0;
right = size - 1;
while(left < right)
{
if(arr[left] + arr[right] == sum)
return 1;
else if (arr[left] + arr[right] < sum)
left++;
else
right--;
}
return 0;
}
int main()
{
int size, index, sum, *arr;
printf("Enter number of Elements in an array \n");
scanf("%d", &size);
//allocate memory for array
arr = (int *) malloc(sizeof(int) * size);
printf("Enter elements to array\n");
for(index = 0; index < size; index++)
scanf("%d", &arr[index]);
printf("Enter sum value");
scanf("%d", &sum);
if(findPairs(arr, size, sum))
printf("\nThe pairs of elements whose sum is = %d found in an array", sum);
else
printf("The pairs of elements whose sum is = %d not found in an array", sum);
return 0;
}
// Time complexity: O(nlogn)
// Space complexity: O(1)
