class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        left = 0
        maxleft = height[left]
        right = len(height) - 1
        maxright = height[right]

        total = 0

        while left < right:
            if maxleft < maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                total += maxleft - height[left]
            else:
                right -= 1
                maxright = max(maxright, height[right])
                total += maxright - height[right]

        return total
        
        

                