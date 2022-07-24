class Solution {
    
    class Stack {
	
	Node top;
	
	class Node{
		int data;
		Node(int data){
			this.data = data;
		}
		Node next;
	}
	public void add(int data) {
		// add to top
		Node node = new Node(data);
		if(null == top) {
			top = node;
		}else {
			node.next = top;
			top = node;
		}
	}
	public Node remove() {
		if(null == top) {
			return null;
		}else {
			Node current = top;
			top = current.next;
			return current;
		}
	}
	public boolean isEmpty() {
		return null == top? true: false;
	}	

}
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        
        int[] result = new int[nums1.length];
        Stack s = new Stack();
        Stack s2 = new Stack();
        for(int n:nums2){
            s.add(n);
        }
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        while(!s.isEmpty()){
            Solution.Stack.Node current = s.remove();
            s2.add(current.data);
            map.put(current.data,getNextGreaterElement(s2,current.data));
        }
        for(int i=0;i<nums1.length;i++){
            result[i] =  map.getOrDefault(nums1[i],-1);
        }
        return result;
    
    }
    public int getNextGreaterElement(Stack s, int data){
        if(s.top == null) {
        	return -1;
        }
        Solution.Stack.Node temp = s.top.next;
         while(null != temp){
            if(temp.data>data){
                return temp.data;
            }
            temp = temp.next;
        }
        return -1;
    }
}
