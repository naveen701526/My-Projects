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
    int diameter=0;
    public int diameterOfBinaryTree(TreeNode root) {
        getDiameter(root);
        return diameter;
    }
    
    private int getDiameter(TreeNode root){
        if(root==null)
            return 0;
        int lh=getDiameter(root.left);
        int rh=getDiameter(root.right);
        diameter=Math.max(diameter, lh+rh);
        return Math.max(lh,rh)+1;
    }
}
