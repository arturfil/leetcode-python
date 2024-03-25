from typing import Counter, List
import heapq

class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        heap = []

        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        for key, val in map.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]
