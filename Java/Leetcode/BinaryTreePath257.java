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
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        getPaths(root, result, "");
        return result;
    }
    private void getPaths(TreeNode root, List<String> result, String path) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            result.add(path + root.val);
            return;
        }
        getPaths(root.left, result, path + root.val + "->");
        getPaths(root.right, result, path + root.val + "->");
    }
}
