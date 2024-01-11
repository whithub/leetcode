class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

        # # option 2:
        # x_string = str(x)
        # reverse_x = ""

        # for i in range(len(x_string)-1, -1, -1):
        #     reverse_x += x_string[i]

        # return reverse_x == x_string
