#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> nums;
    int sizeOfNums;
    cin >> sizeOfNums;
    int num;
    int length = 0;
    for (int i = 0; i < sizeOfNums; i++)
    {
        cin >> num;
        nums.push_back(num);
        length += 1;
    }
    int minVal, maxVal;
    if (length % 2 == 0)
    {
        minVal = nums[0] < nums[1] ? nums[0] : nums[1];
        maxVal = nums[0] >= nums[1] ? nums[0] : nums[1];
    }
    else
    {
        minVal = nums[0];
        maxVal = nums[0];
    }
    int index = length % 2 ? 1 : 2;
    while (index < length)
    {
        if (nums[index + 1] > nums[index])
        {
            maxVal = nums[index + 1] > maxVal ? nums[index + 1] : maxVal;
            minVal = nums[index] < minVal ? nums[index] : minVal;
        }
        else
        {
            maxVal = nums[index] > maxVal ? nums[index] : maxVal;
            minVal = nums[index + 1] < minVal ? nums[index + 1] : minVal;
        }
        index += 2;
    }
    cout << "The Minimum Value is : " << minVal << endl;
    cout << "The Maximum Value is : " << maxVal << endl;
    return 0;
}