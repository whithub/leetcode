class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_total = 0

        for idx in range(len(nums)):
            running_total += nums[idx]
            nums[idx] = running_total

        return nums
