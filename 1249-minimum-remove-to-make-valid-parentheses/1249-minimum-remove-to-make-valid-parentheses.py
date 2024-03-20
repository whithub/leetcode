class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s) # ------------------------------------> "a)b(c)d"
        open_paren_idx_stack = []

        for idx, char in enumerate(s):
            if char not in '()':
                continue

            if char == '(':
                open_paren_idx_stack.append(idx)
            elif char == ')' and not open_paren_idx_stack:
                chars[idx] = '' # ----------------------------> ['a', '', 'b', '(', 'c', ')', 'd']
            else:
                open_paren_idx_stack.pop()
        
        while open_paren_idx_stack: # ------------------------> No stack for "a)b(c)d" -- [3], but then line 12 pop() it when idx/char 5/) was hit.
            chars[open_paren_idx_stack.pop()] = ''

        return ''.join(chars)


        # Option #2:
        # indices_to_remove = set()
        # parenthesis_stack = set()

        # for idx, char in enumerate(s):
        #     if char not in '()':
        #         continue # if it's not a parenthesis, skip to next char
            
        #     if char == '(':
        #         parenthesis_stack.add(idx)
        #     elif char == ')' and not parenthesis_stack:
        #         indices_to_remove.add(idx)
        #     else:
        #         parenthesis_stack.pop()

        # indices_to_remove = indices_to_remove.union(parenthesis_stack) # accounts for opening parenthesis that came after closing ones

        # answer = ""
        # if indices_to_remove:
        #     for idx, char in enumerate(s):
        #         if idx not in indices_to_remove:
        #             answer += char
        # else:
        #     answer = s

        # return answer
            