class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.buildParenthesisStr(0, 0, '', n, result)

        return result

    def buildParenthesisStr(self, left: int, right: int, s: str, n: int, result: list):
        if len(s) == n * 2:
            result.append(s)
            return 
        
        if left < n:
            self.buildParenthesisStr(left + 1, right, s + '(', n, result)
        
        if right < left:
            self.buildParenthesisStr(left, right + 1, s + ')', n, result)


    # Cleaner:
    # def generateParenthesis(self, n: int) -> List[str]:

    #     def buildParenthesisStr(left: int, right: int, s: str):
    #         if len(s) == n * 2:
    #             result.append(s)
    #             return 
            
    #         if left < n:
    #             buildParenthesisStr(left + 1, right, s + '(')
            
    #         if right < left:
    #             buildParenthesisStr(left, right + 1, s + ')')

    #     result = []
    #     buildParenthesisStr(0, 0, '')

    #     return result

