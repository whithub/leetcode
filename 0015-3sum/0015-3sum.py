class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = set()

        n = len(nums)

        for x in range(n - 2):
            y = x + 1
            z = n - 1

            while y < z:
                subset = (nums[x], nums[y], nums[z])
                total = sum(subset)
                if total == 0:
                    results.add(subset)
                    y += 1
                elif total > 0:
                    z -= 1
                else:
                    y += 1

        return results


        # Option #2:
        # results = []

        # x = 0
        # y = 1
        # z = 2
        # while x < len(nums) - 2:
        #     a, b, c = nums[x], nums[y], nums[z]
        #     if a + b + c == 0:
        #         sub_arr = [a,b,c]
        #         sub_arr.sort()

        #         if sub_arr not in results:
        #             results.append(sub_arr)

        #     if z == len(nums) - 1:
        #         y += 1
        #         z = y + 1
        #     elif z < len(nums) - 1:
        #         z += 1
        #     if y == len(nums) - 1:
        #         x += 1
        #         y = x + 1
        #         z = y + 1

        # return results