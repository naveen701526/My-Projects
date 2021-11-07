// Problem Statement ---> https://leetcode.com/problems/sort-colors/
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void sortColors(vector<int> &nums)
    {
        int p = 0;
        int l = 0;
        int h = nums.size() - 1;

        while (p <= h)
        {
            if (nums[h] == 2)
                h--;
            else if (nums[p] == 0)
            {
                swap(nums[p], nums[l]);
                if (nums[p] == nums[l])
                    p++;
                l++;
            }
            else if (nums[p] == 1)
                p++;
            else
            {
                swap(nums[p], nums[h]);
                if (nums[h] == nums[p])
                    p++;
                h--;
            }
        }
    }
};