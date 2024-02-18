import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        pattern = r"[^a-zA-Z0-9\s]"
        regex_str = re.sub(pattern, '', s)
        formatted_str = regex_str.replace(" ", "").lower()

        return formatted_str == formatted_str[::-1]
        # if I couldn't do the above:
        # str_copy = formatted_str
        # for i in range(len(str_copy)//2):
        #     a,b = formatted_str[0], formatted_str[-1]

        #     if a == b:
        #         formatted_str = formatted_str[1:-1]
        #     else:
        #         return False
        
        # return True