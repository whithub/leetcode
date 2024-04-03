class Solution:
    def myAtoi(self, s: str) -> int:
        # trim whitespace
        s = s.lstrip()
        if not s:
            return 0

        # first char == - or + --> hold onto and apply at the end...
        first_char = s[0]
        if (first_char in ['-', '+']):
            s = s[1:]

        # iterate through remainder str, check isdigit()
        for idx, char in enumerate(s):
            if char.isdigit():
                continue
            else:
                # if not a digit or end of string, stop iteration
                s = s[:idx]
                break

        # convert str digits to int
        if s:
            num = int(s)
        else:
            num = 0

        # apply neg or pos:
        if first_char == '-':
            num *= -1

        # apply range adjustments:
        if (num >= 2**31):
            num = 2**31 - 1

        if (num <= -2**31):
            num = -2**31

        # return final number
        return num



        