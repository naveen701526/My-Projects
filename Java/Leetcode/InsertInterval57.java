class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> list = new ArrayList<>();

        int[] temp = newInterval;

        for (int[] interval : intervals) {
            if (temp[1] < interval[0]) {
                // temp, interval
                list.add(temp);
                temp = interval;
            } else if (interval[1] < temp[0]) {
                // interval, temp
                list.add(interval);
            } else {
                // overlapping
                temp = new int[]{
                    Math.min(temp[0], interval[0]),
                    Math.max(temp[1], interval[1])
                };
            }
        }
        list.add(temp);

        return list.toArray(new int[list.size()][2]);
    }
}
