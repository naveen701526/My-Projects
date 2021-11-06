#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    string intToRoman(int num)
    {
        int number[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string strnumber[13] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        string ans = "";
        int i = 0;
        while (i < 13)
        {
            if (num >= number[i])
            {
                ans += strnumber[i];
                num -= number[i];
            }
            else
                i++;
        }

        return ans;
    }
};