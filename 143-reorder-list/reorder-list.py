# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        t = head
        while t:
            l.append(t.val)
            t = t.next
        ll = []
        i = 0
        j = len(l)-1
        while i<=j:
            if i != j:
                ll.append(l[i])
                ll.append(l[j])
            else:
                ll.append(l[i])
            i += 1
            j -= 1
        L = head
        for i in ll:
            L.val = i
            L = L.next
        return L