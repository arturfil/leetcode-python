from typing import List

class ProductOfArrayExceptSelf():
    def product_except_self(self, nums: List[int]) -> List[int]:
        res, carry = [], 1
        
        for i in range(0, len(nums)):
            res.append(nums[i])
            res[i] = carry
            carry *= nums[i]
        
        carry = 1
        for i in range(len(res)-1, -1, -1):
            res[i] *= carry
            carry *= nums[i]
        
        return res


        #  1  2  3  4
        #  1  1  2  6
        # 24 12  8  6