class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # find smallest non-zero num
        #   - sep non-zero elements in it's own list..
        #   - find min number in that list
        #   - subtract min val from all non-zero numbers
        #   - add new zero values to the zero group
        #   - repeat if non-zero numbers still exist
        #   - exit when non-zero list is empty
        # keep track of iterations...
        # return iteration count at end

        zero_nums = [num for num in nums if num == 0]       # [0]
        non_zero_nums = [num for num in nums if num != 0]   # [1,5,3,5]
        iteration_count = 0

        while non_zero_nums:
            iteration_count += 1
            min_val = min(non_zero_nums)
            for num in non_zero_nums.copy():
                reduced_num = num - min_val
                if reduced_num == 0:
                    non_zero_nums.remove(num)
                    zero_nums.append(reduced_num)
                else:
                    non_zero_nums.remove(num)
                    non_zero_nums.append(reduced_num)
        
        return iteration_count

