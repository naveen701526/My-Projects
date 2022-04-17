class Solution {
    public TreeNode increasingBST(TreeNode root) {
        ArrayList<Integer> al = new ArrayList<>();
        inorder(root, al);
        return buildTree(al);
    }
    
    private TreeNode buildTree(ArrayList<Integer> al){
        if(al.size() == 0) return null;
        TreeNode root = new TreeNode(al.remove(0));
        root.right = buildTree(al);
        return root;
    }
    
    private void inorder(TreeNode root, ArrayList<Integer> al){
        if(root == null) return;
        inorder(root.left, al);
        al.add(root.val);
        inorder(root.right, al);
    }
}
