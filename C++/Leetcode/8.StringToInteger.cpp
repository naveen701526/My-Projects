#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int myAtoi(string s)
    {
        int sign = 1;
        long int num = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (isalpha(s[i]) || s[i] == '.' || s[i] == ',') //if an alphabet or special character is present at the first then                                                        its not a valid string
            {
                return 0;
            }
            if (i < s.length() - 1 && s[i] == '-' && s[i + 1] >= 48 && s[i + 1] <= 57) // '-' signifies that that number is negative and a                                                                     number is present after the minus sign
            {
                sign = -1;
            }

            if (s[i] >= 48 && s[i] <= 57) //AS soon as the first number is found we start generating the number unless we                                           encounter some other character
            {
                int k = i;
                while (s[k] >= 48 && s[k] <= 57)
                {
                    if (num > INT_MAX) //if num exceeds the maximun limit of 2^31 at any time
                        break;
                    num = num * 10 + (s[k] - 48);

                    k++;
                }

                num *= sign; //generating number with the sign
                if (num < INT_MIN)
                    num = INT_MIN; //if number overflows then we assign it to lower bound of int data type
                if (num > INT_MAX)
                    num = INT_MAX; //if number overflows then we assign it to upper bound of int data type
                return num;
            }
            if (i < s.length() - 1 && (s[i] == '+' || s[i] == '-') && s[i + 1] < 48 || s[i + 1] > 57)
            {
                return 0; //if a + or minus is detected and the next character is not a number
            }
        }
        return 0;
    }
};