class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if empty string, return 0
        # if string length == 1, return 1
        if len(s) <= 1:
            return len(s)

        longest_substring = ""
        substring = ""
        # iterate through string, slowly building a substring
        for char in s:
            # if substring already contains next char:
            if char in substring:

        #       if longest_substring length <= substring length:
                if len(longest_substring) < len(substring):
        #           make longest_substring = substring
                    longest_substring = substring
                    
        #       then edit substring: while new char is not in substring, remove first char in substring and tack on the next char in string
                while char in substring:
                    substring = substring[1:]
                else:
                    substring += char
            else:
                substring += char

        # account for string that has no repeating chars
        if len(longest_substring) < len(substring):
            longest_substring = substring

        return len(longest_substring)
