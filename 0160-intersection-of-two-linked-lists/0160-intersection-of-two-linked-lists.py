# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    intersection_node = None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        visited = []
        current_node_a = headA
        current_node_b = headB

        while current_node_a or current_node_b:
            if current_node_a == current_node_b:
                return current_node_a
            
            current_node_a = self.determine_intersection(current_node_a, visited)
            current_node_b = self.determine_intersection(current_node_b, visited)

            if self.intersection_node:
                return self.intersection_node
        
        return None
        

    def determine_intersection(self, node: ListNode, visited: List) -> Any:
        if node:
            if node in visited:
                self.intersection_node = node
                return node
            else:
                visited.append(node)
                return node.next