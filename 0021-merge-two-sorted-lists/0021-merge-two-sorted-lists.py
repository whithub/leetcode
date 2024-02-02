# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = final_list = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                current.next = list1
                list1, current = list1.next, list1
            else:
                current.next = list2
                list2, current = list2.next, list2
                
        if list1 or list2:
            current.next = list1 if list1 else list2

        return final_list.next
        # final_list = ListNode{
        #     val: 0,
        #     next: ListNode{
        #         val: 1, -----------------------------------> 1
        #         next: ListNode{
        #             val: 1, -------------------------------> 1
        #             next: ListNode{
        #                 val: 2, ---------------------------> 2
        #                 next: ListNode{
        #                     val: 3, -----------------------> 3
        #                     next: ListNode{
        #                         val: 4, -------------------> 4
        #                         next: ListNode{
        #                             val: 4, ---------------> 4
        #                             next: None
        #                         }
        #                     }
        #                 }
        #             }
        #         }
        #     }
        # }
