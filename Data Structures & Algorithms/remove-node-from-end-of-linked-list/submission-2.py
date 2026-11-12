# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        count = 0
        cur = head

        while cur:
            count += 1
            cur = cur.next

        cur = ListNode()
        cur.next = head
        dummy = cur

        while (count - n) > 0:
            cur = cur.next
            count -= 1

        cur.next = cur.next.next

        return dummy.next