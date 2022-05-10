class Solution {
   public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> combinations = new ArrayList<>();
        backtracking(combinations, new ArrayList<>(), k, n, 1);
        return combinations;
    }

    private void backtracking(List<List<Integer>> result, List<Integer> current, int k, int n, int start) {
        if (current.size() == k && n == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i <= 9; i++) {
            current.add(i);
            backtracking(result, current, k, n - i , i + 1);
            current.remove(current.size() - 1);
        }
    }
}
