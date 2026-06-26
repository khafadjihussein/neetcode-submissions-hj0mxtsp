# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        """have a pointer at head, and a pointer at head.next, 
        make head.next point to none, make the pointer at head.next 
        the new head, make that point to none, repeat until theres no 
        head.next.next"""
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
            

        