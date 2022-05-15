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
class Solution
{
int maxHeight=0, sum=0;
public int deepestLeavesSum(TreeNode root)
{
if(root.left==null && root.right==null)
return root.val;

    helper(root,0);
    return sum;
}
public void helper(TreeNode root, int height)
{
    if(root.left==null && root.right==null)
    {
        if(height<maxHeight)
            return;
        else if(height==maxHeight)
            sum+=root.val;
        else
        {
            sum=root.val;
            maxHeight=height;
        }
        return;
    }
    if(root.left!=null)
        helper(root.left, height+1);
    if(root.right!=null)
        helper(root.right, height+1);
}
}
