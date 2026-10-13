class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) > 1:
            left = 0
            right = len(heights) - 1
            most = 0
            while left != right:
                current = min(heights[left], heights[right]) * (right-left)
                most = max(most, current)
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1
            return most
        return 0