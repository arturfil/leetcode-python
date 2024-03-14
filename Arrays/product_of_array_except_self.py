from typing import List

class ProductOfArrayExceptSelf:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]

        # prefix
        carry = 1
        for i in range(len(nums)):
            res[i] = carry 
            carry *= nums[i] 

        # postfix
        carry = 1 
        for i in reversed(range(len(res))):
            res[i] *= carry 
            carry *= nums[i]

        return res

        #  1  2  3  4
        #  1  1  2  6
        # 24 12  8  6
