class Solution {
    
    public int numberOfSteps(int num) {
        int reduceCount = 0;
        
        while (num > 0) {
            num = ((num & 1) == 0) ? num >> 1 : num -1;
            reduceCount++;
        }
        
        return reduceCount;
    }
}
