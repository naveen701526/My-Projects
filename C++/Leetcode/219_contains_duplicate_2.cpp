class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> result;
        for(int i=0;i<nums.size();i++)
        {
            if(result.find(nums[i])!=result.end())
            {
                if(abs(result[nums[i]]-i)<=k)
                {
                    return true;
                }
            }
            result[nums[i]]=i; //if the diff is not <=K we will assign the new index to the map(result here)
        }
        return false;
    }
};
