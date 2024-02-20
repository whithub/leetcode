class Solution:
    def isHappy(self, n: int) -> bool:
        visited_sums = []
        sum = n

        while sum != 1:
            digits = [int(d) for d in str(sum)]
            total = 0

            for i in digits:
                total += i*i
            
            if total in visited_sums:
                return False
            
            visited_sums.append(total)
            sum = total
        
        return sum