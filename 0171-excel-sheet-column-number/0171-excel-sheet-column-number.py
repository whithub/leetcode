import string

class Solution:
    alphabet = string.ascii_uppercase

    def titleToNumber(self, columnTitle: str) -> int:           # AVB
        reverseColumnTitle = columnTitle[::-1]                  # BVA
        colNum = 0
        alphabetLength = len(self.alphabet)

        for idx, char in enumerate(reverseColumnTitle):         # 0, B        | 1, V                | 2, A
            charIdx = self.alphabet.find(char) + 1              # 2           | 22                  | 1

            if idx == 0:
                colNum += charIdx                               # colNum = 2
            else:
                colNumForChar = charIdx                         #             | charIdx = 22        | charIdx = 1
                for i in range(idx):                            #             | idx = 1             | idx = 2
                    colNumForChar *= alphabetLength             #             | 1 time (22*26) 572  | 2 times (1*26 = 26 ... 26*26 = 676) 676 

                colNum += colNumForChar                         #             | 574 (2 + 572)       | 1250 (574 + 676)

        return colNum                                           # 1250
            
