# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.result = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.result.append(i.getInteger())
            else:
                self.flatten(i.getList())

    def next(self) -> int:
        num = self.result.pop(0)
        return num

    def hasNext(self) -> bool:
        return len(self.result) > 0

# Attempt #1 -- except input: [[[[]]],[]] would output: [[]] or [null] or [None] ...       
#   def __init__(self, nestedList: [NestedInteger]):
#     self.nestedList = nestedList
#     self.subList = []

#   def next(self) -> int:
#     while self.subList:
#         el = self.subList.pop(0)

#         if el.isInteger():
#             return el.getInteger()
#         elif el.getList():
#             self.subList += el.getList()

#   def hasNext(self) -> bool:
#     while self.nestedList:
#         el = self.nestedList.pop(0)

#         if el.isInteger():
#             self.subList.append(el)
#             return True
#         elif el.getList():
#             self.subList += el.getList()
#             return True

#     while self.subList:
#       return True

#     return False

    

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())