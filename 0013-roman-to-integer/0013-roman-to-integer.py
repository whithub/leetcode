class Solution:
    def romanToInt(self, numeral: str) -> int:
        roman_key = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        number = 0

        for i in range(len(numeral)-1):
            if roman_key[numeral[i]] < roman_key[numeral[(i+1)]]:
                number-=roman_key[numeral[i]]
            else:
                number+=roman_key[numeral[i]]
        return number+roman_key[numeral[-1]]
        