/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        
        TreeNode node=find(original,cloned,target);
        return node;
    }
    
    private TreeNode find(TreeNode original, TreeNode cloned, TreeNode target) {
        if (original==null) {
            return null;
        }
        
        if (original==target) {
            return cloned;
        }
        
        TreeNode left=find(original.left,cloned.left,target);
        TreeNode right=find(original.right,cloned.right,target);
        
        if (left!=null) {
            return left;
        }
        
        return right;
    }
}
