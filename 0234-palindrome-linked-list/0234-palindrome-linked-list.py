# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def recursive(node:Optional[ListNode], values:list):
            if not node:
                return values
            values.append(node.val)
            return recursive(node.next, values)
        
        values = []        
        values = recursive(head, values)
        print(values)
        if values == list(reversed(values)):
            return True
        else:
            return False
        