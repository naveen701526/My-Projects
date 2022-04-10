class Solution {
    public int calPoints(String[] ops) {
        Deque<Integer> stack = new LinkedList<>();
        for(String val:ops) {
            if("+".equals(val)) {
                int op1 = stack.pop();
                int op2 = op1 + stack.peek();
                stack.push(op1);
                stack.push(op2);
            } else if("C".equals(val)) {
                stack.pop();
            } else if("D".equals(val)) {
                stack.push(2*stack.peek());
            } else {
                stack.push(Integer.parseInt(val));
            }
        }
        int res=0;
        while(!stack.isEmpty()) {
            res+=stack.pop();
        }
        return res;
    }
}
