class Solution {
    List<List<Integer>> result;
    public List<List<Integer>> permuteUnique(int[] nums) {
        result = new ArrayList<>();
        backTracking(result, nums, 0);
        return result;
    }
    
    void backTracking(List<List<Integer>> result, int[] nums, int start){
        if(start == nums.length){
            result.add(toList(nums));
            return;
        }

        for(int i = start; i < nums.length; i++){
            if(i != start && !canPermutate(nums, start, i))
                continue;
            swap(nums, i, start);
            backTracking(result, nums, start+1);
            swap(nums, i, start);
        }
    }
    
    boolean canPermutate(int[] nums, int start, int curr){
        for(int i = start; i < curr; i++){
            if(nums[i] == nums[curr])
                return false;
        }
        return true;
    }
    
    List<Integer> toList(int[] nums){
        List<Integer> list = new ArrayList<>();
        for(int ele : nums)
            list.add(ele);
        return list;
    }
    
    void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
