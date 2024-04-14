# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        depth = 1
            
        for item in nestedList:
            total = self.calcSum(total, depth, item)

        return total

    def calcSum(self, total: int, depth: int, item: any):
        if item.isInteger():
            total += (depth * item.getInteger())
        else:
            for el in item.getList():
                total = self.calcSum(total, depth+1, el)
        return total

    # Nested methods:
    # def depthSum(self, nestedList: List[NestedInteger]) -> int:
    #     total = 0
    #     depth = 1

    #     def calcSum(depth, item):
    #         nonlocal total

    #         if item.isInteger():
    #             total += (depth * item.getInteger())
    #         else:
    #             for el in item.getList():
    #                 calcSum(depth+1, el)
            
    #     for item in nestedList:
    #         calcSum(depth, item)

    #     return total
    