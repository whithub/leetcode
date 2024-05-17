class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniq_nums1 = set(nums1)
        uniq_nums2 = set(nums2)
        result = []

        for num in uniq_nums1:
            if num in uniq_nums2:
                result.append(num)

        return result