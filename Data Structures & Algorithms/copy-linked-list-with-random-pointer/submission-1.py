"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        hsh = {None:None}

        while cur:
            copy = Node(cur.val)
            hsh[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = hsh[cur]
            copy.next = hsh[cur.next]
            copy.random = hsh[cur.random]
            cur = cur.next

        return hsh[head]