class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count = {}

        for letter in s:
            if letter in letter_count:
                letter_count[letter] = letter_count[letter] + 1
            else:
                letter_count[letter] = 1
        
        copy_letter_count = letter_count.copy()
        for k,v in copy_letter_count.items():
            if v % 2 == 0: # even
                letter_count.pop(k)

        if letter_count:
            return len(s) - len(letter_count) + 1
        else:
            return len(s)

        # Option B
        # ss = set()
        # for letter in s:
        #     if letter not in ss:
        #         ss.add(letter)
        #     else:
        #         ss.remove(letter)
        # if len(ss) != 0:
        #     return len(s) - len(ss) + 1
        # else:
        #     return len(s)
