#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    long long maxSubarraySum(int arr[], int n)
    {

        // Your code here
        int allNegative = 0;
        for (int i = 0; i < n; i++)
            if (arr[i] < 0)
                allNegative += 1;
        if (allNegative == n)
            return findMin(arr, n);
        long long maxsofar = 0;
        int currentsum = 0;
        for (int i = 0; i < n; i++)
        {

            if (currentsum + arr[i] > maxsofar)
            {
                maxsofar = currentsum + arr[i];
                currentsum += arr[i];
            }
            else
            {
                if (currentsum + arr[i] < 0)
                {
                    currentsum = 0;
                }
                else
                {

                    currentsum += arr[i];
                }
            }
        }
        return maxsofar;
    }

private:
    long long findMin(int arr[], int len)
    {

        int max = -32766;
        for (int i = 0; i < len; i++)
        {
            if (arr[i] > max)
            {
                max = arr[i];
            }
        }
        return max;
    }
};

// { Driver Code Starts.

int main()
{
    int t, n;

    cin >> t;   //input testcases
    while (t--) //while testcases exist
    {

        cin >> n; //input size of array

        int a[n];

        for (int i = 0; i < n; i++)
            cin >> a[i]; //inputting elements of array

        Solution ob;

        cout << ob.maxSubarraySum(a, n) << endl;
    }
}
// } Driver Code Ends