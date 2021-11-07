// Problem Statement ---> https://leetcode.com/problems/combinations/
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<vector<int>> combinations; //stores all combinations

    void func(int cur, int n, int k, vector<int> temp)
    {
        if (k == temp.size()) //base case
        {
            combinations.push_back(temp);
            return;
        }

        // running for all possible combinations
        for (int i = cur; i <= n - (k - temp.size()) + 1; i++)
        {
            temp.push_back(i);
            func(i + 1, n, k, temp); // recursive call for adding elements into each combinations.

            temp.pop_back(); //backtracking
        }

        return;
    }

    vector<vector<int>> combine(int n, int k)
    {
        vector<int> temp;
        func(1, n, k, temp); // do all required operations
        return combinations;
    }
};