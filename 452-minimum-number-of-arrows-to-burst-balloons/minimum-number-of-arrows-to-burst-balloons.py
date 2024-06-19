class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        c = 1
        end_point = points[0][1]
        for i in points[1:]:
            if i[0]>end_point:
                c += 1
                end_point = i[1]
            else:
                end_point = min(end_point,i[1])
        return c