class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0
        palindrome_count += len(s)

        x = 0
        y = 1
        substring = s[x]

        while x < len(s) - 1:
            substring += s[y]
            reverse_sub = substring[::-1]

            if substring == reverse_sub:
                palindrome_count += 1
            
            y += 1

            if y == len(s):
                x += 1
                y = x + 1
                substring = s[x]

        return palindrome_count