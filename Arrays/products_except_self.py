from typing import List

class ProductExceptSelf:
    def productsExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))] 
        prd = 1 

        for i in range(len(nums)):
           res[i] = prd 
           prd *= nums[i] 
           print("prd", prd)

        prd = 1
        for i in range(len(nums)-1, -1, -1):
            print(nums[i])
            res[i] = res[i] * prd
            prd *= nums[i]

        print(res)