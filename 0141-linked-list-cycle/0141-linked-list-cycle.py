# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node = head
        while node:
            if not node.next:
                return False
            if node.val >= -10**5 and node.val <= 10**5:
                node.val = -10**6
                node = node.next
            else:
                return True
        return False
        