class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()

        mid = len(combined) // 2
        if len(combined) % 2 == 0:
            a = mid - 1
            b = mid
            return (combined[a] + combined[b]) / 2
        else:
            return combined[mid]
            