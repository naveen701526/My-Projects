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
    private TreeNode first = null;
    private TreeNode second = null;
    private TreeNode pre = null;
    
    public void recoverTree(TreeNode root) {
        if(root==null) return;

        //find swapped nodes
        inorder(root);
        
        //swap the nodes
        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }
    
    private void inorder(TreeNode root){
        if(root==null) return;
        inorder(root.left);
        
        //find the first node which is at wrong position
        if(first==null && (pre==null ||pre.val>=root.val)){
            first = pre;
        }
        
        //find the second node which is at wrong position
        if(first!=null && pre.val>=root.val){
            second = root;
        }
        
        //store previus node to compare
        pre = root;
        inorder(root.right);
    }
}
