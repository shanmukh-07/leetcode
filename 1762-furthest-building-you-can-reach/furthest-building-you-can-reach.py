class Solution:
    import heapq
    def furthestBuilding(self, h: List[int], bri: int, lad: int) -> int:
        n = len(h)
        l = []
        for i in range(n-1):
            d = h[i+1]-h[i]
            if d > 0:
                heapq.heappush(l,d)
                if len(l) > lad:
                    bri -= heapq.heappop(l)
                if bri < 0:
                    return i
        return  n-1