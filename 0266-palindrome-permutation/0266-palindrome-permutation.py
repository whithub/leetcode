class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_number_chars = set()

        for char in s:
            if char in odd_number_chars:
                odd_number_chars.remove(char)
            else:
                odd_number_chars.add(char)

        if len(odd_number_chars) == 0:
            return True
        if (len(s) == (len(s) - len(odd_number_chars) + 1)):
            return True
        
        return False



        # characters = list(s)
        # # ['c', 'a', 'r', 'e', 'r', 'a', 'c']
        # uniq_chars = set(characters)
        # # {'a', 'c', 'e', 'r'}

        # character_frequency = {}
        # for char in uniq_chars:
        #     character_frequency[char] = characters.count(char)
        #     # character_frequency = {'a': 2, 'c': 2, 'e': 1, 'r': 2}

        # is_even_length = len(s) % 2 == 0

        # if is_even_length:
        #     return all((x % 2 == 0) for x in character_frequency.values())
        #     # allowed_char_freq = int(len(s) / len(uniq_chars))
        #     # all(x == allowed_char_freq for x in character_frequency.values())
        # else:
        #     odd_frequency = []
        #     even_frequency = []
        #     for k,v in character_frequency.items():
        #         if (v % 2 == 0):
        #             even_frequency.append(k)
        #         else:
        #             odd_frequency.append(k)
        #     return len(odd_frequency) == 1