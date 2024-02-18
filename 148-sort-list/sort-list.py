# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        if not l:return None
        head = ListNode(l[0])
        t = head
        for i in l[1:]:
            nn = ListNode(i)
            t.next = nn
            t = nn
        return head