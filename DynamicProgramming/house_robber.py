from typing import List

class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0

        for n in nums:
            temp = max(n + prev_max, curr_max)
            prev_max = curr_max
            curr_max = temp

        return curr_max

