# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        a = head
        length = 1
        while a.next != None :
            length +=1
            a=a.next
        a = head
        
        for i in range(length/2) :
            a = a.next 
        return a
        