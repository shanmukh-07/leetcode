class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        ll = []
        for i in range(l):
            s = 0
            for j in range(l):
                if boxes[j] == '1':
                    s += abs(j-i)
            ll.append(s)
        return ll