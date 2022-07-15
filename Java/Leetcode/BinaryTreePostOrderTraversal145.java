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
    List<Integer> al=new LinkedList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
        postorder(root);
        return al;
    }
    private void postorder(TreeNode root){
//         post order: left->right->root
        
//         base condition
        if(root==null){
            return ;
        }
        postorder(root.left);
        postorder(root.right);
        al.add(root.val);
    }
}
