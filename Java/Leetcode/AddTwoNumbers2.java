/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         ListNode curr = new ListNode(0);
        ListNode ans = curr;
        int carry = 0;
        while(l1 != null || l2 != null && curr != null){
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int val = x + y + carry;
            carry = 0;
            if(val > 9) {
                curr.next = new ListNode((val + carry) % 10);
                carry =1;
            } else {
                curr.next = new ListNode(val);
            }
            curr = curr.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        if(carry >0) curr.next = new ListNode(carry);
        return ans.next;
    }
}
