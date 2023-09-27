from typing import List

class KClosestPoint:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances, res = [], []

        for point in points:
            temp = point[0] ** 2 + point[1] ** 2
            distances.append([temp, point])

        distances.sort(key = lambda p: p[0])

        for i in range(k):
           res.append(distances[i][1]) 

        return res 

