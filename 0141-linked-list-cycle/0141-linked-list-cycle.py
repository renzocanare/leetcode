# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using two pointers, one fast and one slow.
        # Fast pointer will check ahead for the end of the Linked List.
        # If there is an end, then there is no loop. Else, if it meets the slow pointer, there must be a loop.
        # Solution in O(1) space as opposed to having a "seen" set.
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        # Iterate slow by one step.
            fast = fast.next.next   # Iterate fast by two steps.
            
            if slow == fast:
                # If they meet, return True.
                return True
        
        return False