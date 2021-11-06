#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &a)
    {
        int n = a.size();
        vector<vector<int>> ans;
        if (n < 3)
            return ans;
        sort(a.begin(), a.end());
        for (int i = 0; i < n; i++)
        {
            int t = -a[i];
            if (i && a[i] == a[i - 1])
                continue;
            int l = i + 1, r = n - 1;
            while (l < r)
            {
                if (a[l] + a[r] > t)
                    r--;
                else if (a[l] + a[r] < t)
                    l++;
                else
                {
                    ans.push_back({a[i], a[l], a[r]});
                    while (l < r && a[l] == a[++l])
                        ;
                    while (l < r && a[r] == a[--r])
                        ;
                }
            }
        }

        return ans;
    }
};