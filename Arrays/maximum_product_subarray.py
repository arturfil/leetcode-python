from typing import List


class MaxProductSubArray:
    def maxProduct(self, nums: List[int]) -> int:
        tot, max_p, min_p = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, max_p * num, min_p * num)
            min_p = min(num, max_p * num, min_p * num)
            max_p = temp_max
            tot = max(max_p, tot)

        return tot