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
     public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<>();
        
       Inorder_Traversal(root,list);
        
        return list;
    }
    
    public void Inorder_Traversal(TreeNode root, List<Integer> list) {
        if(root==null)  // base case
            return;
        
		// Inorder Traversal => left -> root -> right
		
        Inorder_Traversal(root.left,list);
        list.add(root.val);
        Inorder_Traversal(root.right,list);
    }
}
