/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> postorder(Node root) {
        Stack<Node> st = new Stack<>();
        List<Integer> post = new LinkedList<>();
        if(root == null){
            return post;
        } 
        
        st.push(root);
        
        while(st.size() > 0){
              //rem
            Node rem = st.pop();
            
            //add to list
            post.add(0,rem.val);
            
            //add children in reverse
            for(int i = 0; i < rem.children.size(); i++){
                st.push(rem.children.get(i));
            }
        }
        
        return post;
    }
}
