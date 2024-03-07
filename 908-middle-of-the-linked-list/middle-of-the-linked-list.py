# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # n = len(l)
        # a = n//2
        # nl = l[a:]
        # ll = ListNode(nl[0])
        # t = ll
        # for i in nl[1:]:
        #     nn = ListNode(i)
        #     t.next = nn
        #     t = nn
        # return ll
        f,s = head,head
        if not f or  not f.next:
            return head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s