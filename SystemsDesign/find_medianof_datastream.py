from heapq import heappush, heappushpop
from bisect import bisect, insort

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
'''
Best, easy way. Use insertion sort to find and insert number
'''
class MedianFinderAlt:
    def __init__(self):
        self.arr = []
        self.n = 0
    
    def insertionSort(self, num: int) -> None:
        left, right = 0, len(self.arr) - 1

        while left <= right:
            middle = (left + right) // 2
            if self.arr[middle] < num:
                left = middle + 1
            else:
                right = middle - 1
        
        self.arr.insert(left, num)

    def addNum(self, num: int) -> None:
        # insort(self.arr, num)
        self.insertionSort(num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.arr[self.n // 2] + self.arr[self.n // 2 - 1]) / 2
        else:
            return self.arr[self.n // 2]
