# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(cur):
            if not cur:
                return [True, 0]

            if (dfs(cur.left)[0] and dfs(cur.right)[0]) and abs(dfs(cur.left)[1] - dfs(cur.right)[1]) <= 1:
                balanced = True
            else:
                balanced = False

            return [balanced, 1 + max(dfs(cur.left)[1], dfs(cur.right)[1])]

        return dfs(root)[0]