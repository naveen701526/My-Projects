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
    
    public void average(TreeNode node, List<Double> list)
    {
        Queue<TreeNode> q = new ArrayDeque<TreeNode>();
        
        q.add(node);
        list.add((double)node.val);
        
        while(q.size() > 0)
        {
            int size = q.size();
            
            double sum = 0;
            double avg = 0;
            int len = 0;
            for(int i = 1; i <= size; i++)
            {
                TreeNode T = q.remove();
                if(T.left != null)
                {
                    sum = sum + T.left.val;
                    len++;
                    q.add(T.left);
                }
                if(T.right != null)
                {
                    sum = sum + T.right.val;
                    len++;
                    q.add(T.right);
                }
            }
            
            if(len != 0)
            {
                 avg = (double)(sum/len);
                
                list.add(avg);
            }
           
        }
    }
    
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> list = new ArrayList<Double>();
        
        average(root,list);
        return list;
    }
}
