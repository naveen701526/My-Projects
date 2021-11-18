//Problem Statement:  https://www.codechef.com/problems/FCTRL

#include <iostream>
#include <vector>
using namespace std;

// finds the number of trailing zeroes in factorial of number
int findZeros(int n)
{
    int count = 0;
    int i = 5;
    while (n / i != 0)
    {
        count = count + n / i;
        i *= 5;
    }
    return count;
}

// driver code
int main()
{
    int t;
    cin >> t;
    vector<int> v;
    int ans;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        ans = findZeros(n);
        v.push_back(ans);
    }
    for (auto &i : v)
    {
        cout << i << endl;
    }
    return 0;
}
