class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 31ms runtime:
        # last_word = s.split()[-1]
        # return len(last_word)

        # 26ms runtime:
        words = s.split()
        return  len(words[-1])
        