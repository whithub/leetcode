class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = str(bin(n)).count('1')
        return bit_count