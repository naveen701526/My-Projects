class Solution {
   
      public List<List<Integer>> shiftGrid(int[][] grid, int k) {
		int m = grid.length;
		int n = grid[0].length;
		int a = m * n;

		k %= a;
		if (k > 0) {
			int[] two2One = new int[a];
			for (int i = 0; i < m; i++) {
				System.arraycopy(grid[i], 0, two2One, i * n, n);
			}

			int[] t = new int[k];
			System.arraycopy(two2One, a - k, t, 0, k);
			System.arraycopy(two2One, 0, two2One, k, a - k);
			System.arraycopy(t, 0, two2One, 0, k);

			for (int i = 0; i < m; i++) {
				System.arraycopy(two2One, i * n, grid[i], 0, n);
			}
		}

		return (List)Arrays.asList(grid);
	}
}
