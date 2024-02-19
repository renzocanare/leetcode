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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode head = null;
        
        // Return either lists if one of them is NULL.
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        }
        
        // Set either list1 or list2 as the head.
        if (list1.val <= list2.val) {
            head = list1;
            list1 = list1.next;
        } else {
            head = list2;
            list2 = list2.next;
        }
        
        // Set tail.
        ListNode tail = head;
        
        // Iterate through lists.
        while (list1 != null && list2 != null) {
            ListNode tmp = null;
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;   // Move tail pointer forward.
        }
        
        // Link remaining lists.
        if (list1 != null) {
            tail.next = list1;
        } else if (list2 != null) {
            tail.next = list2;
        }
            
        return head;
    }
}