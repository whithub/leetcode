class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or target <= nums[0]:
            return 0
        if len(nums) == 1:
            return 1

        for idx in range(len(nums)-1):
            a = nums[idx]
            b = nums[idx+1]

            if a == target:
                return idx
            if target <= b:
                return idx + 1

        return len(nums)