class Solution:
    def longestPalindrome(self, s: str) -> str:
        reverse_s = s[::-1]
        substring = ""
        palindrome = "" 

        for letter in s:
            substring += letter

            while (substring not in reverse_s):
                substring = substring[1:]
            else:
                if (substring == substring[::-1] and len(palindrome) < len(substring)):
                    palindrome = substring
        
        return palindrome