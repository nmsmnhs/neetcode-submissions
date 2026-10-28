class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[l] <= nums[r]:
                break

            if nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[mid] <= nums[r]:
                r = mid 
        pivot = l

        l = 0
        r = len(nums)-1

        if target >= nums[pivot] and target <= nums[r]:
            return binary_search(pivot,r)
        elif target <= nums[pivot-1] and target >= nums[l]:
            return binary_search(l,pivot-1)
        else:
            return -1
