class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int evenIndex = 0;
        int oddIndex = 1;
        int n = nums.length;
        while(evenIndex<n && oddIndex<n){
            while(evenIndex<n && nums[evenIndex]%2==0)
                evenIndex+=2;
            while(oddIndex<n && nums[oddIndex]%2==1)
                oddIndex+=2;
            if(evenIndex<n && oddIndex<n){
                nums[evenIndex] = nums[evenIndex] + nums[oddIndex];
                nums[oddIndex] = nums[evenIndex] - nums[oddIndex];
                nums[evenIndex] = nums[evenIndex] - nums[oddIndex];
                
            }
            
        }
        return nums;
    }
}
