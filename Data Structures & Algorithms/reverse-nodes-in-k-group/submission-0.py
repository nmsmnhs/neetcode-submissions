# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while count < k and cur:
            cur = cur.next
            count += 1

        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                dummy = head.next
                head.next = cur
                cur = head
                head = dummy
                count -= 1
            head = cur
            
        return head