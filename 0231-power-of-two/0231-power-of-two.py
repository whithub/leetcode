import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return (math.ceil(self.Log2(n)) == math.floor(self.Log2(n)))

    def Log2(self, num):
        if num == 0:
            return False

        return (math.log10(num) / math.log10(2))
