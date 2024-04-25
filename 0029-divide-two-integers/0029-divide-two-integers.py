class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = str(dividend/divisor)
        if float(ans)>=2147483648:
            return int(ans.split(".")[0])-1
        else:
            return int(ans.split(".")[0]) 