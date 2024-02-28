class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_string = ""

        while word1 and word2:
            combined_string += word1[0]
            combined_string += word2[0]

            word1 = word1[1:]
            word2 = word2[1:]

        if word1:
            combined_string += word1
        
        if word2:
            combined_string += word2

        return combined_string