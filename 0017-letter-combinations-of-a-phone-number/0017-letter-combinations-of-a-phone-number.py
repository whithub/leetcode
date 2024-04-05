class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []

        flip_phone_alphabet_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, current_str):
            if len(current_str) == len(digits):
                results.append(current_str)
                return

            for char in flip_phone_alphabet_map[digits[i]]:
                backtrack(i+1, current_str + char)

        if digits:
            backtrack(0,"")

        return results