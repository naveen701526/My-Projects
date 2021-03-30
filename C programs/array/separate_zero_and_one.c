#include <stdio.h>
#include <stdlib.h>
void seperate0and1(int arr[], int size)
{
int leftIndex = 0, rightIndex = size-1;
while( leftIndex < rightIndex)
{
while((arr[leftIndex] == 0) && (leftIndex < rightIndex))
leftIndex++;
while((arr[rightIndex] == 1) && (rightIndex > leftIndex))
rightIndex--;
if(leftIndex < rightIndex)
{
arr[leftIndex++] = 0;
arr[rightIndex--] = 1;
}
}
}
void printArray(int arr[], int size)
{
for(int index = 0; index < size; index++)
printf("%d\t", arr[index]);
}
int main()
{
int *arr, size;
printf("Enter size of the array\n");
scanf("%d", &size);
printf("Enter elements in array\n");
for(int index = 0; index < size; index++)
scanf("%d", &arr[index]);
seperate0and1(arr, size);
printArray(arr, size);
return 0;
}
// Time complexity: O(n)
// Space Complexity: O(1)
