class Solution {
int squareAdder(int n)
{
    int sum = 0;
    while (n != 0)
    {
        int lastDigit = n % 10;
        sum += pow(lastDigit, 2);
        n = n / 10;
    }
    return sum;
}

public:
bool isHappy(int n)
{
    unordered_set<int> s;
    s.insert(n);
    if (n == 1)
        return true;
    while (n != 1)
    {
        n = squareAdder(n);
        if (n == 1)
            return true;
        else if (s.find(n) != s.end())
        {
            return false;
        }
        else
        {
            s.insert(n);
        }
    }
    return false;
}
};
