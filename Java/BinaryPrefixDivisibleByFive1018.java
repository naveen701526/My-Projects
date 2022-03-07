class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> result = new ArrayList(nums.length);
        if(nums[0] == 0)
            result.add(0,true);
        else
            result.add(0,false);
        int current = nums[0];
        for(int i = 1; i<nums.length; i++)
        {
            current = current*2 + nums[i];
            if(current%5==0)
                result.add(i,true);
            else
                result.add(i,false);
            current %= 5;
        
        }
        return result;
    }
}
