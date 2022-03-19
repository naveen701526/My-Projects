class Solution {
    public List < List < Integer >> combinationSum(int[] candidates, int target) {
        List < List < Integer >> res = new ArrayList < > ();

        solve(candidates, new ArrayList < > (), res, target, 0);
        return res;

    }
    public void solve(int[] candidates, List < Integer > ans, List < List < Integer >> res, int target, int curr) {
        /** Two base condition 
         * If curr will reach to the last index
         * if target will be 0;
         */
        if (curr == candidates.length)
            return;

        if (target == 0) {
            res.add(new ArrayList(ans));
            return;
        }

        /** if curr element is <= target than we will add it and we will reduce target.
         * if curr element is > target than we simply move to curr+1.
         */
        if (candidates[curr] <= target) {
            ans.add(candidates[curr]);
            solve(candidates, ans, res, target - candidates[curr], curr);
            ans.remove(ans.size() - 1);
        }
        //Backtracking
        solve(candidates, ans, res, target, curr + 1);
    }
}