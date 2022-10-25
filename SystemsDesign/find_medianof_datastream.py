from heapq import heappush, heappushpop
from bisect import bisect_left

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

# Time O(N) + O(logN) = O(N)
class MedianFinderAlt:
    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        if not self.store:
            self.store.append(num)
        else:
            idx = bisect_left(self.store, num)
            self.store.insert(idx, num)
    
    def findMedian(self) -> float:
        n = len(self.store)-1
        if n % 2 == 0:
            return self.store[n//2]
        else:
            res = (self.store[n//2] + self.store[n//2 + 1])/2.0
            return res