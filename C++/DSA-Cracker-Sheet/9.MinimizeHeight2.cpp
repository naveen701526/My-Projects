// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++

class Solution
{
public:
    int getMinDiff(int arr[], int n, int k)
    {
        sort(arr, arr + n);
        int least = arr[0] + k;
        int highest = arr[n - 1] - k;
        int ans = arr[n - 1] - arr[0];
        for (int i = 0; i < n - 1; i++)
        {
            int minVal = min(least, arr[i + 1] - k);
            int maxVal = max(highest, arr[i] + k);
            if (minVal < 0)
                continue;
            ans = min(maxVal - minVal, ans);
        }
        return ans;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k;
        cin >> k;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.getMinDiff(arr, n, k);
        cout << ans << "\n";
    }
    return 0;
} // } Driver Code Ends