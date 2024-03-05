# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        values = []

        node = head
        while node:
            values.append(node.val)
            node = node.next

        while values:
            twin_a_val = values.pop(0)
            twin_b_val = values.pop(-1)

            total = twin_a_val + twin_b_val

            if total > max_sum:
                max_sum = total
        
        return max_sum
        