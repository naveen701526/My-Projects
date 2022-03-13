class Solution {
     public int maxSubArray(int[] a) {
        if(a.length == 0) return 0;

		int curr = a[0];
		int max = a[0];

		int n = a.length;

		for(int i = 1; i < n; i++) {
			curr = Math.max(a[i], curr+a[i]);
			max = Math.max(curr, max);
		}

		return max;
    }
}
