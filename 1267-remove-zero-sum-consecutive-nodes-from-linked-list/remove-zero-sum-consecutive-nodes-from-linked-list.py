# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        ps = 0
        psd = {}
        c = d
        while c:
            ps += c.val
            psd[ps] = c
            c = c.next
        c = d
        ps = 0
        while c:
            ps += c.val
            if ps in psd:
                c.next = psd[ps].next
            c = c.next
        return d.next