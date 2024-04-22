class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # iterate through words, keeping track of current idx
        # at said idx, collect the letter at said idx, for each word and compare word[idx] == built word...
        # if I get through the for loop, return True

        for idx in range(len(words)):
            row_word = words[idx]
            col_word = ""

            for word in words:
                letter = "" if idx >= len(word) else word[idx]
                # if idx >= len(word):
                #     letter = ""
                # else:
                #     letter = word[idx]

                col_word += letter

            if row_word != col_word:
                return False

        return True
