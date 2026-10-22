import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            k = start + ((end - start)//2)
            if nums[k] > target:
                end = k-1
            elif nums[k] < target:
                start = k+1
            else:
                return k

        return -1