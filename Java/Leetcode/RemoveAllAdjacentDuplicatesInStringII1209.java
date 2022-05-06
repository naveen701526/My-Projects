class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<CharCounter> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!stack.isEmpty() && c == stack.peek().c) {
                if (stack.peek().count == k - 1) {
                    stack.pop();
                } else {
                    stack.peek().count++;
                }
            } else {
                stack.push(new CharCounter(c));
            }
        }
        StringBuilder res = new StringBuilder();
        for (CharCounter charCount : stack) {
            res.append(charCount);
        }
        return res.toString();
    }
}


class CharCounter {
    char c;
    int count;
    
    CharCounter(char c) {
        this.c = c;
        this.count = 1;
    }
    
    @Override
    public String toString() {
        return Character.toString(c).repeat(count);
    }
}
