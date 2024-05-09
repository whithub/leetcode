class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeating_chars = set()
        
        for idx, char in enumerate(s):
            if char not in repeating_chars:
                if s.count(char) == 1:
                    return idx
                else:
                    repeating_chars.add(char)

        return -1 # if this is hit, that means the string has only/all non-repeating characters.