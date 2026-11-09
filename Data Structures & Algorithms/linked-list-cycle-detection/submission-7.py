# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        double = head
        while double:
            head = head.next
            if double.next == None:
                return False
            double = double.next.next
            if head == double:
                return True
        return False