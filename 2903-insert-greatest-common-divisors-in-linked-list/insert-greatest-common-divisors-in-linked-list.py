# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            if node.next == None:
                return head
            aux = node.next
            node.next = ListNode(math.gcd(node.val,node.next.val),aux)
            node = aux