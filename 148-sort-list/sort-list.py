# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        l =[]
        while t:
            l.append(t.val)
            t = t.next
        l.sort()
        c = head
        for i in l:
            c.val = i
            c = c.next
        return head