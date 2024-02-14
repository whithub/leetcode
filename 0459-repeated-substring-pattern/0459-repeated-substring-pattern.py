class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        # in order to be a repeating pattern, the pattern need to be within `s` at least twice -- i.e. len(s)//2
        # create a range from 1 --> len(s)//2, rotating the first letter to last position and check if result == s
        for k in range(1, len(s)//2 +1): # plus 1 since default nature of range() is to exclude the last number
            if s == s[k:] + s[:k]:
                return True
        return False

        # ex: "abcdabcd"
        #      range => 1,2,3,4
        #      k=1   => bcdabcda => x
        #      k=2   => cdabcdab => x 
        #      k=3   => dabcdabc => x 
        #      k=4   => abcdabcd => √ (result == s within)

        # ex: "zxczxczxczxczxc"
        #      range => 1,2,3,4,5,6,7
        #      k=1   => xczxczxczxczxcz => x
        #      k=2   => czxczxczxczxczx => x 
        #      k=3   => zxczxczxczxczxc => √ (result == s within)
        #  able to find it before reaching end of range; i.e. pattern repeats more than twice
