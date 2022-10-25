from typing import List

class MaximumSubArray:
    def max_sub_array(self, nums: List[int]) -> int:
        current, max_val = 0, nums[0]
        for i in range(len(nums)):
            current = max(nums[i] + current, nums[i])
            max_val = max(max_val, current)
        
        return max_val