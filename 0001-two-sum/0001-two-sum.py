class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums) - 1):
            b = len(nums) - 1

            while a < b:
                if nums[a] + nums[b] == target:
                    return [a, b]
                b -= 1


        # Option #2: slightly less clean
        # n = len(nums)

        # for x in range(n):
        #     y = x + 1
            
        #     while y < n:
        #         total = nums[x] + nums[y]

        #         if total == target:
        #             return [x,y]
        #         y += 1


        # Option #3: no for loop, defining x & y explicitly
        # x = 0
        # y = 1

        # while x < len(nums)-1:
        #     if nums[x] + nums[y] == target:
        #         return [x, y]
        #     else:
        #         y += 1
            
        #     if y == len(nums):
        #         x += 1
        #         y = x + 1