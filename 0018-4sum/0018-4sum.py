class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        uniq_combos = set()

        for w in range(n-3):
            x = w + 1
            y = x + 1
            z = n - 1

            while x < y and y < z:
                total = nums[w] + nums[x] + nums[y] + nums[z]

                if total == target:
                    uniq_combos.add((nums[w], nums[x], nums[y], nums[z]))

                if total <= target:
                    y += 1
                if total > target:
                    z -= 1
            
                if y == z:
                    x += 1
                    y = x + 1
                    z = n - 1

        results = []

        for combo in uniq_combos:
            results.append(list(combo))

        return results
