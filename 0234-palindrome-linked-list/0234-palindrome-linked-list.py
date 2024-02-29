# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_vals = []

        while head:
            node_vals.append(head.val)
            head = head.next

        return node_vals == node_vals[::-1]
