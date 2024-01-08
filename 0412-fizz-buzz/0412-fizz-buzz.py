class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        my_list = list(range(1, n+1))
        for i in my_list:
            if (i % 3 == 0) and (i % 5 == 0):
                answer.append("FizzBuzz")
            elif (i % 3 == 0):
                answer.append("Fizz")
            elif (i % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return(answer)
        