from typing import List
import heapq

class KLargestElementInArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_map, heap = {}, []

        for num in nums:
            if not num in nums_map:
                nums_map[num] = True
                heapq.heappush(heap, num)

        return heap[-k]

 
