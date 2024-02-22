# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_values = []
        l2_values = []
        
        while l1:
            l1_values.insert(0, l1.val)
            l1 = l1.next
        
        while l2:
            l2_values.insert(0, l2.val)
            l2 = l2.next

        stringify_l1_values = [str(i) for i in l1_values]
        stringify_l2_values = [str(i) for i in l2_values]
        
        l1_as_string = ''.join(stringify_l1_values)
        l2_as_string = ''.join(stringify_l2_values)

        l1_as_int = int(l1_as_string)
        l2_as_int = int(l2_as_string)

        sum = l1_as_int + l2_as_int
        sum_as_string = str(sum)
        sum_as_list = list(sum_as_string)

        if len(sum_as_list) < 2:
            node_val = sum_as_list[0]
            node = ListNode(int(node_val))
        else:
            x = 0
            node_val = sum_as_list[x]
            node = ListNode(int(node_val))
            x += 1

            while x < len(sum_as_list):
                prev_node_val = sum_as_list[x]
                prev_node = ListNode(int(prev_node_val), node)
                node = prev_node
                x += 1
            
        return node
