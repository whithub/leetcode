# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (high + low) // 2

        while low <= high:
            result = guess(mid)

            if result == 1:
                low = mid + 1
                mid = (high + low) // 2 # 7
            elif result == -1:
                high = mid - 1
                mid = (high + low) // 2
            elif result == 0:
                return mid

