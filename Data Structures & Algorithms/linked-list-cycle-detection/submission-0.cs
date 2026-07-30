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
    public bool HasCycle(ListNode head)
    {
        var dict = new Dictionary<ListNode, int>();
        
        // keep getting next node while it's not null
        while (head != null)
        {
            // if next is not null and points to a node that we've already seen return true
            if (dict.ContainsKey(head))
                return true;

            // add ref/ID/hash to hashmap
            dict.Add(head, 0);

            head = head.next;
        }        

        return false;
    }
}
