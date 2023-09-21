from typing import List

class MissingNumber:
    def missingNUmber(self, nums: List[int]) -> int:
        sum, org = 0, 0

        for i in range(0, len(nums)+1):
            org += i

        for i in nums:
            sum += i

        return org - sum 
