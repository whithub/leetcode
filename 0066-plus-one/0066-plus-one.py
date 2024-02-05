class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return None

        combined_string_digits = ''.join([str(i) for i in digits])
        incremented_int = int(combined_string_digits) + 1

        integer_as_string_chars = [*str(incremented_int)]
        final_digits_list = [int(char) for char in integer_as_string_chars]
        return final_digits_list



# [] ---> None
# [2] ---> [3]
# [9] ---> [1,0]
# [9,9] ---> [1,0,0]
