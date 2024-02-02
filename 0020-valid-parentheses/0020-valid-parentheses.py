class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        for char in s:
            if char in ['(', '{', '[']:
                bracket_stack.append(char)
            elif len(bracket_stack) > 0:
                if char == ')' and bracket_stack[-1] == '(':
                    bracket_stack.pop(-1)
                elif char == '}' and bracket_stack[-1] == '{':
                    bracket_stack.pop(-1)
                elif char == ']' and bracket_stack[-1] == '[':
                    bracket_stack.pop(-1)
                else:
                    return False
            else:
                return False
        
        if len(bracket_stack) > 0:
            return False

        return True