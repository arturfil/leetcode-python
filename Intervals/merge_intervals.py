from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort ascending by first value
        res = [intervals[0]]
        
        for interval in intervals:
            last = res[-1]
            if last[1] < interval[0]:
                res.append(interval)
            else:
                last[1] = max(last[1], interval[1])
        
        return res
          
