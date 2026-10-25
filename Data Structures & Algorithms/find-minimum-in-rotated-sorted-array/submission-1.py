class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minNum = nums[r]

        while l <= r:
            if nums[l] <= nums[r]:
                minNum = min(minNum, nums[l])
                break

            mid = l + (r-l)//2
            minNum = min(minNum, nums[mid])

            if nums[l] <= nums [mid]:
                l = mid + 1
            if nums[mid] <= nums[r]:
                r = mid - 1
        
        return minNum
            