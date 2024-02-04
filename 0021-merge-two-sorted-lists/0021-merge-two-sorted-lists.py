# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Normal solution:
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         # Return lists if either are empty.
#         if list1 is None:
#             return list2
#         elif list2 is None:
#             return list1
        
#         # Set head.
#         head = None
#         if list1.val <= list2.val:
#             head = list1
#             list1 = list1.next
#         else:
#             head = list2
#             list2 = list2.next
        
#         # "head is a reference to the first node in your merged list, and tail is also a reference to this same node. 
#         # They are not pointing to each other, but rather they are both pointing to the same location 
#         # in memory (the first node of your merged list)."
        
#         # Set tail.
#         tail = head
        
#         # Traverse linked list.
#         while (list1 is not None) and (list2 is not None):
#             temp = None # Temp to store next object.
#             if list1.val <= list2.val:
#                 temp = list1
#                 list1 = list1.next
#             else:
#                 temp = list2
#                 list2 = list2.next
            
#             tail.next = temp
#             tail = temp
        
#         # Fill in either remainder of list1 or list2.
#         if list1 is not None:
#             tail.next = list1
            
#         if list2 is not None:
#             tail.next = list2
        
#         return head

# Merge in-place (recursively) solution:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(list1, list2):
            # Return lists if either are empty.
            if list1 is None:
                return list2
            elif list2 is None:
                return list1
            
            if list1.val <= list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
            
        merged = merge(list1, list2)
        return merged