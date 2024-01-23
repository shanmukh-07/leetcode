# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # def fun(l):
        #     if not l:
        #         return None
        #     head = Node(l[0])
        #     c = head
        #     for i in l[1:]:
        #         nn = Node(i)
        #         c.next = nn
        #         c = nn
        #     return head
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        # n = len(l)
        # a = k%n
        # a1 = l[(n-a):]
        # a2 = l[:(n-a)]
        # ll = a1+a2
        # fun(ll)
        if not head or k == 0:
            return head
        c = head
        l = 0
        while c:
            l+=1
            c = c.next
        if k == l:
            return head
        k =  k % l
        if k == 0:
            return head
        g = l - k
        fst = head
        for i in range(g-1):
            fst = fst.next
        nextFirst = fst.next
        fst.next = None
        if l == 1:
            return head
        t = nextFirst
        while t.next:
            t = t.next
        t.next = head
        return nextFirst