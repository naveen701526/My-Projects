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
    TreeNode ans=null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        helper(root,p,q);
        return this.ans;
    }
    
    public TreeNode helper(TreeNode node,TreeNode p, TreeNode q){
        if(node==null){
            return null;
        }
        
        TreeNode leftNode=helper(node.left,p,q);
        TreeNode rightNode=helper(node.right,p,q);
        if(((node==p || node==q)&&(leftNode!=null || rightNode!=null))||(leftNode!=null &&rightNode!=null)){
            this.ans=node;
            return node;
        }else if((leftNode!=null || rightNode!=null)||(node==p || node==q)){
            return node;
        }else{
            return null;
        }
    }
}
