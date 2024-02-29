class Solution:
    def compress(self, chars: List[str]) -> int:
        x = 0
        y = 1
        counter = 1

        while y < len(chars):
            if chars[x] == chars[y]:
                counter += 1
                chars.pop(y)
            else:
                if counter > 1:
                    for idx, digit in enumerate(str(counter)):
                        chars.insert(x+idx+1, digit)
                    x = y + len(str(counter))
                else:
                    x = y
                y = x + 1
                counter = 1

        if counter > 1:
            for idx, el in enumerate(str(counter)):
                chars.insert(x+idx+1, el)

        return len(chars)