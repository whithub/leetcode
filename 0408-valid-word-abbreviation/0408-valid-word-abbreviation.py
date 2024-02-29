class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # x is the pointer for traversing word
        # y is pointer for traversing abbr

        x, y = 0, 0
        word_len = len(word)
        abbr_len = len(abbr)
        idx_tracker = 0

        while x < word_len and y < abbr_len:
            if abbr[y].isdigit():
                if idx_tracker == 0 and int(abbr[y]) == 0: # check leading zeroes; if we hit any, ever, return False
                    return False

                idx_tracker = idx_tracker*10 + int(abbr[y]) # times 10 so that we can slowly build int substring as we iterate through abbr...
                                                            # abbr = "i12i" ---> 1st time we hit a digit (i.e. abbr[y] = 1; idx_tracker = 0) 0*10 = 0 + 1 = 1
                                                            #               |--> 2nd time (i.e. abbr[y] = 2; idx_tracker = 1) 1*10 = 10 + 2 = 12
                y += 1
            
            elif abbr[y].isalpha() and idx_tracker:
                x += idx_tracker
                idx_tracker = 0
            
            elif word[x]!=abbr[y]:
                return False
            
            else:
                x += 1
                y += 1

        # x += idx_tracker is for the edge cases where last character is a digit .. for eg '"i5a11o1"
        x += idx_tracker
        return x == word_len and y == abbr_len


# Example:
#   word = "internationalization"
#   abbr = "i12iz4n"
#   x, y = 0, 0
#   idx_tracker = 0
#
#   1. abbr[y] = 'a'
#      abbr[y].isdigit() -------------------> False
#      abbr[y].isalpha() and idx_tracker ---> False
#      word[x]!=abbr[y] --------------------> False
#
#      x += 1 ------------------------------> x = 1
#      y += 1 ------------------------------> y = 1
#   2. abbr[y] = '2'
#      abbr[y].isdigit() -------------------> True
#           idx_tracker = idx_tracker*10 + int(abbr[y]) ---> idx_tracker = 2
#                           (0 * 10)     +     2         =   2
#           y += 1 ----------------------------------------> y = 2
#           -----------------------------------------------> x = 1
#
#   3. abbr[y] = 'e'
#      abbr[y].isdigit() -------------------> False
#      abbr[y].isalpha() and idx_tracker ---> True (idx_tracker = 2)
#
#           x += idx_tracker ---> x = 3
#           idx_tracker = 0 ----> idx_tracker = 0
#           --------------------> y = 2
#
#   4. abbr[y] = 'e' -- since we didn't increase y....
#      abbr[y].isdigit() -------------------> False
#      abbr[y].isalpha() and idx_tracker ---> False (idx_tracker back at 0)
#      word[x]!=abbr[y] --------------------> False
#
#      x += 1 ------------------------------> x = 4
#      y += 1 ------------------------------> y = 3
#
#   5. x < word_len and y < abbr_len -------> False; exit while loop
#      x += idx_tracker --------------------> x += 0 => 4
#
#      x == word_len and y == abbr_len -----> False
#      4 == 5    and     3 == 3