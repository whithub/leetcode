# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        visited = []
        current_node = head

        # iterate through linked list; if no cycle I will eventually hit a None node, if cycle, I should hit the return True and exit conditional...
        while(current_node is not None):
            # adding entire node obj to visited as I go
            visited.append(current_node)

            # at each visit, check if node.next is in visited
            #   if so, a cycle exists
            if(current_node.next in visited):
                return True
            
            #   if not, set current_node to next and continue checking...
            current_node = current_node.next

        # if I make it through the whole linked list, no cycle detected
        return False

        