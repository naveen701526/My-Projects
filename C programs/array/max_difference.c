// Find the maximum difference beetween two elements such that larger element  appears after the smaller element 

#include <stdio.h>

int maximumDifference(int *arr, int size)
{
    int min_ele_so_far=arr[0];
    int maxdiff_so_far=0;
    int curr_diff,index;
    for (index=1; index < size; index++)
    {
        if (arr [index]< min_ele_so_far)
            min_ele_so_far=arr[index];
        else
        {
            curr_diff=arr[index]-min_ele_so_far;
            if(curr_diff>maxdiff_so_far)
                maxdiff_so_far=curr_diff;
        }
    }
    return maxdiff_so_far;
}
void main()
{
    int arr[]={4,3,10,2,9,1,6};
    int max_diff=maximumDifference(arr,7);
    printf("%d",max_diff);
}


// Time Complexity is O(n)
// Space Complexity is O(1)
