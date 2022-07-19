class Solution {
    public int majorityElement(int[] nums) {
        int me = nums[0]; //max element
        int count = 1;
        
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] == me) {
                count++;
            } else {
                count--;
            }
            
            if(count == 0) {
                me = nums[i];
                count = 1;
            }
        }
        
        return me;
    }
}
