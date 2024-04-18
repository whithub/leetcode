class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        maxElement = max(nums)
        minElement = min(nums)

        farthestMaxIndex = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == maxElement:
                farthestMaxIndex = i
                break
        
        nearestMinIndex = 0
        for i in range(len(nums)):
            if nums[i] == minElement:
                nearestMinIndex = i
                break

        swaps = (len(nums) - 1 - farthestMaxIndex) + (nearestMinIndex)

        if nearestMinIndex > farthestMaxIndex:
            swaps -=1

        return swaps

        
        
        # Less Clean:
        # swaps = 0
        # smallest_num_and_idx = (nums[0], 0)
        # largest_num_and_idx  = (nums[0], 0)

        # for x in range(len(nums)-1):
        #     y = x + 1
        #     num1 = nums[x]
        #     num2 = nums[y]
        #     smallest_num_and_idx = min(smallest_num_and_idx, (num1, x), (num2, y))
        #     largest_num_and_idx  = max(largest_num_and_idx, (num1, x), (num2, y))
             
        # idx_of_smallest = smallest_num_and_idx[1]
        # idx_of_largest = largest_num_and_idx[1]

        # swaps_for_smallest = idx_of_smallest
        # swaps_for_largest = len(nums) - 1 - idx_of_largest

        # swaps = swaps_for_smallest + swaps_for_largest

        # if idx_of_smallest > idx_of_largest:
        #     swaps -= 1

        # return swaps