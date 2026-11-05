class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        count = 0
        merged = []

        while count <= (len(nums1) + len(nums2)) // 2:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] >= nums2[j]:
                    merged.append(nums2[j])
                    j += 1
                else:
                    merged.append(nums1[i])
                    i += 1
            elif i >= len(nums1):
                merged.append(nums2[j])
                j += 1
            else:
                merged.append(nums1[i])
                i += 1
            count += 1

        if (len(nums1) + len(nums2)) % 2 == 0:
            return ((merged[count-1] + merged[count -2])/2)
        else:
            return merged[count-1]

        