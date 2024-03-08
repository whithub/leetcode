class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # iterate through nums
        # apply quadratic formula -- update in place?
        # return sorted new values

        for idx, num in enumerate(nums):
            new_val = (a * (num*num)) + (b * num) + c
            nums[idx] = new_val

        nums.sort()

        return nums
