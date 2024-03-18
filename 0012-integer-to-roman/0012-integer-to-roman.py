class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals_map = {
            1000: 'M', 900: 'CM',
            500: 'D',  400: 'CD',
            100: 'C',  90: 'XC',
            50: 'L',   40: 'XL',
            10: 'X',   9: 'IX',
            5: 'V',    4: 'IV',
            1: 'I'
        }

        ans = ""
        
        for digit, roman_num in roman_numerals_map.items():
            while digit <= num:
                ans += roman_num
                num -= digit

        return ans
