class Solution:
    def reverseBits(self, n: int) -> int:
                            #=> Input: 00000010100101000001111010011100
        n = format(n, 'b')  #=> 10100101000001111010011100
        n = n.zfill(32)     #=> 00000010100101000001111010011100
        reverse = n[::-1]   #=> 00111001011110000010100101000000

        return int(reverse, 2)