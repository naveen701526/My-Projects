class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean isInc = true;
        boolean isDec = true;
        for(int i = 1; i<nums.length; i++){
            if (nums[i-1] == nums[i]){
                continue;
            }
            else if(nums[i-1]<nums[i]){
                isDec = false;
            }
            else if(nums[i-1]>nums[i]){
                isInc = false;
            }
        }
        return isInc || isDec;
    }
    
}
