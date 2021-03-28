#include <stdio.h>
#include <stdlib.h>

int majority_finder(int *, int);
int majority_verifier(int *, int, int);

int main()
{
    int *ptr, n;
    printf("enter the size of array : \n");
    scanf("%d", &n);
    ptr = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("enter the %d element : ", i + 1);
        scanf("%d", ptr + i);
    }
    int majority_element = majority_finder(ptr, n);
    majority_verifier(ptr, n, majority_element) ? printf("the majority element is %d \n", majority_element) : printf("there is no majority element \n");
    return 0;
}

//function which finds the majority element
//occuring n/2 + 1 times
int majority_finder(int *ptr, int n)
{
    int majority_index = 0, count = 1;
    for (int i = 0; i < n; i++)
    {
        if (*(ptr + majority_index) == *(ptr + i))
            count++;
        else
            count--;
        if (count == 0)
        {
            majority_index = i;
            count = 1;
        }
    }
    return *(ptr + majority_index);
}

//function to figure out wheter the majority is really majority or not
int majority_verifier(int *ptr, int n, int majority_element)
{
    int count = 0;
    for (int i = 0; i < n; i++)
        if (*(ptr + i) == majority_element)
            count++;
    return (count > n / 2) ? 1 : 0;
}


// Time complexity: O(n)
// Space complexity: O(1)
