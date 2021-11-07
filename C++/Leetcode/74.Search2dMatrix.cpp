// Problem Statement ---> https://leetcode.com/problems/search-a-2d-matrix/
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool binarySearchFor1d(vector<int> &matrix, int left, int right, int target)
    {
        if (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (matrix[mid] == target)
                return true;

            if (matrix[mid] > target)
            {
                return binarySearchFor1d(matrix, left, mid - 1, target);
            }

            return binarySearchFor1d(matrix, mid + 1, right, target);
        }
        return false;
    }

    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        if (m == 1 && n == 1)
        {
            if (matrix[0][0] == target)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else if (m == 1)
        {
            return binarySearchFor1d(matrix[0], 0, n - 1, target);
        }
        else if (n == 1)
        {
            int rowIdx = matrix.size() - 1;
            for (int i = 0; i < matrix.size(); i++)
            {
                if (matrix[i][0] == target)
                {
                    return true;
                }
                if (matrix[i][0] > target)
                {
                    if (i == 0)
                    {
                        return false;
                    }
                    else
                    {
                        rowIdx = i - 1;
                    }
                    break;
                }
            }
            if (matrix[rowIdx][0] == target)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            int rowIdx = matrix.size() - 1;
            for (int i = 0; i < matrix.size(); i++)
            {
                if (matrix[i][0] == target)
                {
                    return true;
                }
                if (matrix[i][0] > target)
                {
                    if (i == 0)
                    {
                        rowIdx = 0;
                    }
                    else
                    {
                        rowIdx = i - 1;
                    }
                    break;
                }
            }
            return binarySearchFor1d(matrix[rowIdx], 0, matrix[rowIdx].size() - 1, target);
        }
    }
};