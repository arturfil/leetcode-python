from typing import List


class InsertIntervals:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       res = [] 

       for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                start = min(newInterval[0], interval[0])
                end = max(newInterval[1], interval[1])
                newInterval = [start,end]
                
       res.append(newInterval)    
       return res 
