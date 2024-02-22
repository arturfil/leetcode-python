from typing import List

class MaximizeGreatness:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        greatness = 0
        for i in range(len(nums)):
            if nums[i] > nums[greatness]:
                greatness += 1
        return greatness


     
