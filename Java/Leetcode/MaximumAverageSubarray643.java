class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double s=0.0;
        for(int i=0;i<k;i++)
            s+=(double)nums[i];
        double max=s/k;       
        for(int i=k;i<nums.length;i++)
        {
            s=s+nums[i]-nums[i-k];            
            max=Math.max(s/k,max);
        }
        return max;
    }
}
