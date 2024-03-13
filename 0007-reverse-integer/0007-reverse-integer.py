class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        reverse_str_num = str(x)[::-1]

        while reverse_str_num[0] == '0':
            reverse_str_num = reverse_str_num[1:]

        if x < 0:
            reverse_str_num = '-' + reverse_str_num[:-1]
        
        reverse_int = int(reverse_str_num)
        if reverse_int < (-2**31) or reverse_int > (2**31 - 1):
            return 0

        return reverse_int