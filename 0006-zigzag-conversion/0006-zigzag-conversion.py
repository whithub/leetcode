class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = ""
        s_length = len(s)
        diff = numRows*2-2

        for row in range(numRows):
            index = row
            while index < s_length:
                answer += s[index]
                if row not in [0, numRows-1]:
                    diagonal_diff = diff-2 * row
                    second_idx = index + diagonal_diff
                    if second_idx < s_length:
                        answer += s[second_idx]
                index += diff

        return answer
        