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
    private boolean res = true;
    public boolean isBalanced(TreeNode root) {
        if(root==null) return true;
        int leftH = height(root.left);
        int rightH = height(root.right);
        if(Math.abs(leftH-rightH)>1) res = false;
        isBalanced(root.left);
        isBalanced(root.right);
        return res;
    }
    int height(TreeNode root){
        if(root==null) return 0;
        return 1+Math.max(height(root.left), height(root.right));
    }
}
