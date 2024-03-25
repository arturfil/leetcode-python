from typing import List

class MissingNumber:
    def missingNUmber(self, nums: List[int]) -> int:
        idx_sum, n_sum = 0, 0 

        for i in range(len(nums)+1):
            idx_sum += i

        for num in nums:
            n_sum += num

        return idx_sum - n_sum
