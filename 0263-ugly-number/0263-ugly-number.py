class Solution:
    def isUgly(self, n: int) -> bool:
        prime_nums = [5,3,2]
        if n <= 0:
            return False
        if n == 1 or (n in prime_nums):
            return True

        numbers = prime_nums.copy()

        while numbers:
            division_result = n / numbers[0]

            if division_result.is_integer():
                n = division_result
            else:
                numbers.pop(0)
            
            if n in prime_nums:
                return True
        
        return False
        