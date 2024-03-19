class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 1:
            return 1
        d = Counter(tasks)
        l = list(d.values())
        t = max(l)
        tm = (t-1)*(n+1) + 1
        for i in range(len(l)):
            if l[i] == t:
                tm += 1
        return max(tm-1,len(tasks))