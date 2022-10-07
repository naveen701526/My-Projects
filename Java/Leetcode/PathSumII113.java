/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
public List<List<Integer>> pathSum(TreeNode root, int sum) {
    List<List<Integer>> res = new ArrayList();
    helper(res, new ArrayList<Integer>(), root, 0, sum);
    return res;
}
private void helper(List<List<Integer>> res, ArrayList<Integer> sub, TreeNode root, int cur, int sum) {
    if (root == null) return;
    sub.add(root.val);
    helper(res, sub, root.left, cur + root.val, sum);
    if (root.left == null && root.right == null && cur + root.val == sum) {
        res.add(new ArrayList<Integer>(sub));
    }
    helper(res, sub, root.right, cur + root.val, sum);
    sub.remove(sub.size() - 1);
}
}
