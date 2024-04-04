# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # return original/new head -- dummy pointer...
        # iterate through entire LL:
        #   curr_node & next_node
        #   if next_node match val, curr_node.next = next_node.next -- curr_node = next_node.next & next_node = curr_node.next

        while head and head.val == val:
            head = head.next

        curr_node = head

        while curr_node:
            next_node = curr_node.next

            while next_node and next_node.val == val:
                next_node = next_node.next
            
            curr_node.next = next_node
            curr_node = next_node
        
        return head

        