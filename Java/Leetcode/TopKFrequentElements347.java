class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int num: nums) {
            max = Math.max(max, num);
            min = Math.min(min, num);
        }
        int[] map = new int[max - min + 1];
        for (int num: nums) {
            map[num - min]++;
        }
        PriorityQueue <Integer> q = new PriorityQueue<>((Integer a, Integer b) -> map[a] - map[b]);
        for (int i = 0; i <= max - min; i++) {
            if (map[i] > 0) {
                q.add(i);
            }
            if (q.size() > k) {
                q.poll();
            }
        }
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = q.poll() + min;
        }
        return result;
    }
}
