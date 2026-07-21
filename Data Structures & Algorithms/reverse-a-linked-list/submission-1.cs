/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode ReverseList(ListNode head) 
    {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null)
        {
            // 1. Save the next node
            ListNode next = curr.next;

            // 2. Reverse the current node's pointer
            curr.next = prev;

            // 3. Move prev forward to current node
            prev = curr;

            // 4. Move curr forward to next node
            curr = next;
        }

        return prev;
    }
}