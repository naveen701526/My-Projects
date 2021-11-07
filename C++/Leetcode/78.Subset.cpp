// Problem Statement ---> https://leetcode.com/problems/subsets/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<vector<int>> v;
    void recur(vector<int> &nums, int i, vector<int> vec)
    {
        if (i == nums.size())
        {
            v.push_back(vec);
            return;
        }
        vector<int> v1 = vec;
        vector<int> v2 = vec;
        v1.push_back(nums[i]);
        recur(nums, i + 1, v1);
        recur(nums, i + 1, v2);
    }
    vector<vector<int>> subsets(vector<int> &nums)
    {

        int n = nums.size();
        vector<int> vec;
        recur(nums, 0, vec);
        return v;
    }
};