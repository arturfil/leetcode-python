from typing import Counter, List
import heapq

class TopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map, heap = {}, []

        for num in nums:
            if num in map: 
                map[num] += 1
            else: 
                map[num] = 1

        for key, val in map.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
