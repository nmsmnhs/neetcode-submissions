# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        first = head
        second = head.next

        while second and second.next:
            first = first.next
            second = second.next.next

        second = first.next 
        first.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        while second:
            temp = head.next
            temp2 = second.next
            head.next = second
            second.next = temp
            head = temp
            second = temp2

