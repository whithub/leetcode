class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.checkSubPalindrome(s, i, j-1) or self.checkSubPalindrome(s, i + 1, j)
            
            i += 1
            j -= 1
            
        return True

    def checkSubPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

