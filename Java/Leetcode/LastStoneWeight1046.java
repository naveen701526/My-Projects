class Solution {
    public int lastStoneWeight(int[] stones) {
        Arrays.sort(stones);
        int count = stones.length - 1;
        while (count != 0) {
            if (stones[stones.length - 1] == stones[stones.length - 2]) {
                stones[stones.length - 1] = 0;
                stones[stones.length - 2] = 0;
            }
            if (stones[stones.length - 1] != stones[stones.length - 2]) {
                stones[stones.length - 1] = stones[stones.length - 1] - stones[stones.length - 2];
                stones[stones.length - 2] = 0;
            }
            Arrays.sort(stones);
            count--;
        }
        return stones[stones.length - 1];
    }
}
