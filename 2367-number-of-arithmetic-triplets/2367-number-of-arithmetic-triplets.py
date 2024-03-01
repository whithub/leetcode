class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result_count = 0
        a = 0
        b = 1

        while a < len(nums)-2:
            if nums[b] - nums[a] == diff:
                sub_arr = nums[b+1:]
                c = 0
                while c < len(sub_arr):
                    if sub_arr[c] - nums[b] == diff:
                        result_count += 1
                        c = len(sub_arr)
                    else:
                        c += 1

            if nums[b] - nums[a] >= diff or b == len(nums) - 2:
                a += 1
                b = a + 1
            else:
                b += 1

        return result_count