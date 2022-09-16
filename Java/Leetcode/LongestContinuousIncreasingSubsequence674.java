class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int ans=0, count=0;
        for (int i=0;i<nums.length;++i) {
            if (i>0 && nums[i-1]> nums[i]) 
                count=i;
            ans=Math.max(ans,i-count+1);
        }
        return ans;
    }
}
