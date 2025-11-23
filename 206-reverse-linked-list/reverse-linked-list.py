# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        solution_node = None
        node = head
        while node != None:
            solution_node = ListNode(val = node.val, next= solution_node)
            node = node.next
        return solution_node        