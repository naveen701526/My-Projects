/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    HashMap<Integer, Node> map = new HashMap<>();
    public Node connect(Node root) {
        preOrderWithHeight(root,0);
        return root;
    }
    public void preOrderWithHeight(Node root, int height){
        if(root==null)
            return;
        else
        {
            if(map.containsKey(height))
            {
                map.get(height).next = root;
                map.put(height,root);
            }
            else
                map.put(height,root);
            preOrderWithHeight(root.left,height+1);
            preOrderWithHeight(root.right,height+1);
            
        }
    }
}
