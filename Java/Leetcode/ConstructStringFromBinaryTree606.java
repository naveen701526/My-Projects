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
    public String tree2str(TreeNode root) {
        StringBuilder answer = new StringBuilder();
        treeToString(root, answer);
        return answer.toString();
    }
    
    private void treeToString(TreeNode node, StringBuilder result) {
        if(node == null) {
            return;
        }
        result.append(node.val);
        if(node.left != null) {
            result.append("(");
            treeToString(node.left, result);
            result.append(")");
        }
        if(node.right != null) {
            if(node.left == null) {
                result.append("()");
            }
            result.append("(");
            treeToString(node.right, result);
            result.append(")");
        }
    }
}
