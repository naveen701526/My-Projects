class Solution {
    public int findUnsortedSubarray(int[] nums) {
        
        int[] sort=nums.clone();
        Arrays.sort(sort);
        
		int l=-1;        
		int h=-1;
        
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=sort[i]){
                l=i;
                break;
            }
        }
        
        for(int j=nums.length-1;j>=0;j--){
            if(nums[j]!=sort[j]){
                h=j;
                break;
            }
        }
        
        if(l==h) return 0;
        return h-l+1;
    }
}
