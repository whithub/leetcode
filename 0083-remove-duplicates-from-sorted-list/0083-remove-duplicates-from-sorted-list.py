# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        current_node = head
        next_node = head.next

        while next_node is not None:
            if current_node.val == next_node.val:
                current_node.next = next_node = next_node.next
            else:
                current_node = next_node
                next_node = next_node.next
        
        return head
        