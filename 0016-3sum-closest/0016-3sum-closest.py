class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        n = len(nums)

        for idx, i in enumerate(nums):
            x = idx
            y = x + 1
            z = n - 1

            while y < z:
                total = nums[x] + nums[y] + nums[z]

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    y += 1
                else:
                    z -= 1
                
        return closest_sum