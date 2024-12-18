# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l = ListNode()
        dummy = l
        
        while list1 or list2:

            if list1 and list2 and list1.val >= list2.val:
                l.next = list2
                list2 = list2.next
            elif list1 and list2 and list1.val < list2.val:
                l.next = list1
                list1 = list1.next
            elif list1 and not list2:
                l.next = list1 
                list1 = list1.next
            else:
                l.next = list2
                list2 = list2.next
            
            l = l.next

        return dummy.next
            

