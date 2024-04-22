from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.cnt = 0

    def push(self, x: int) -> None:
        self.stack.add((self.cnt, x))
        self.values.add((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int:
        idx, val = self.stack.pop()
        self.values.remove((val, idx))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        val, idx = self.values.pop()
        self.stack.remove((idx, val))
        return val



# Time Limit Exceeded Attempt:
# class MaxStack:
#     def __init__(self):
#         self.stack = []
#         self.max_stack = []
        
#     def push(self, x: int) -> None:
#         self.stack.append(x)

#         if not self.max_stack or x >= self.max_stack[-1]:
#             self.max_stack.append(x)

#     def pop(self) -> int:
#         if self.stack:
#             if self.max_stack and self.max_stack[-1] == self.stack[-1]:
#                 self.max_stack.pop()
#             return self.stack.pop()
#         else:
#             return -1

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
#         else:
#             return -1

#     def peekMax(self) -> int:
#         if self.max_stack:
#             return self.max_stack[-1]
#         else:
#             return -1

#     def popMax(self) -> int:
#         temp = []

#         if self.stack and self.max_stack:
#             while self.stack[-1] != self.max_stack[-1]:
#                 num = self.stack.pop()
#                 temp.append(num)

#             max_num = self.stack.pop()
#             self.max_stack.pop()

#             while temp:
#                 num = temp.pop()
#                 self.push(num)

#             return max_num
#         else:
#             return -1
        
        


# # Your MaxStack object will be instantiated and called as such:
# # obj = MaxStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.peekMax()
# # param_5 = obj.popMax()