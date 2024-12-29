# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = []
        node = head

        while node:
            if node in node_list:
                return True
            else:
                node_list.append(node)
            node = node.next
        return False


        # node = node.next
