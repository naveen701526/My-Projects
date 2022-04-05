class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int r = 0;
        while(start < end){
            int diff = end - start;
            int shortest = Math.min(height[end], height[start]);
            r = Math.max(r, diff * shortest);
            if(shortest == height[end]){
                end--;
            }else{
                start++;
            }
        }
        return r;
    }
}
