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
    public ListNode rotateRight(ListNode head, int k) {
        if (k <= 0 || head == null || head.next == null) {
            return head;
        }
        ListNode temp=head;
        int length=1;
        while(temp.next!=null){
            temp=temp.next;
            length++;
        }
        temp.next=head;
        int mod=k%length;
        int loop=length-mod;
        ListNode dummy=head;
         for (int i = 0; i < loop - 1; i++) {
            dummy=dummy.next;
        }
        head=dummy.next;
        dummy.next=null;
        return head;
    }
}
