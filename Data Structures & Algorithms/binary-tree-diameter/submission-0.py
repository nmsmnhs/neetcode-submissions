# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        
        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            
            res = max(res, dfs(cur.left) + dfs(cur.right))
            return 1 + max(dfs(cur.left), dfs(cur.right))

        dfs(root)
        return res

        