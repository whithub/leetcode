class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize currSum and maxSum to the sum of the initial k elements
        curr_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            # Add the right-most element of the window (+= nums[i])
            # Subtract the left-most element of the window (- nums[i - k])
            max_sum = max(curr_sum, max_sum)

        return max_sum / k


    # Approach: 
    #  Sliding window approach:
    #  Initialize currSum and maxSum to the sum of the initial k elements
    #  Iterate through nums starting at k until the len(nums)... doing this b/c we initialized curr_sum and max_sum to the sum of the initial k elements
    #  Calculate a rolling curr_sum:
    #    - Add the right-most element of the window (+= nums[i])
    #    - Subtract the left-most element of the window (- nums[i - k])
    #  Find average at the end... return max_sum / k
    
    
    # ------------------------------------------------------------------------
    # Initial aproach which landed me in: Time Limit Exceeded
    #   pointer 1 (x) -- idx 0    # x = 0
    #   pointer 2 (y) -- x + k    # y = 4 -- using idx 4 b/c later when we pluck the range, it's exclusive -- i.e. sum(nums[x:y]) --> sum(nums[0:4]) --> nums at idx 0, 1, 2, 3...
    #   iterate through nums
    #   sum the numbers btwn x & y
    #   if current_avg > max_avg, then re-assign
    #     else: move sliding window and continue with for loop
    #   move sliding window until x == len(nums)-k+1 --> i.e. x = 2 (max)
    #   find average at the end... 
    #
    #
    # max_sum = float('-inf')
    #
    # for x in range(len(nums)-k+1):
    #     y = x + k
    #     curr_sum = sum(nums[x:y])
    #     max_sum = max(curr_sum, max_sum)
    #
    # return max_sum / k