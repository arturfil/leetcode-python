from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i

'''
    TESTING
    target = 9
    nums = [2,7,11,15]
    two = TwoSum()
    two.twoSum(nums, target)

    EXPLANATION
    - You want to create a dictionary which in python would be the same as a hashmap.
    - If you have NOT seen the number minus the target (the other number that adds up),
      then you add the number as a key and the index as a value
    - Once you iterate throuh the List or Array at some point, you will see the other 
      value needed and where "if complement in hashmap" will be true, then you
      return that current number's index and the reciprocal "hashmap[ complement ]" which 
      will give the value of the index
'''