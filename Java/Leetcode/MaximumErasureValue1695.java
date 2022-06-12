class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        Map<Integer, Integer> loc = new HashMap<>();
        loc.put(nums[0], 0);
        int start = 0;
        int max = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            sum[i] = sum[i - 1] + num;
            if (loc.containsKey(num)) {
                start = Math.max(start, loc.get(num) + 1);
            }
            loc.put(num, i);
            max = Math.max(max, start == 0 ? sum[i] : sum[i] - sum[start - 1]);
        }
        return max;
    }
}
