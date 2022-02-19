# from Arrays import two_sum
from HashMaps.two_sum import TwoSum

def main():
    target = 9
    nums = [2,7,11,15]
    two = TwoSum()
    two.twoSum(nums, target)

if __name__ == "__main__":
    main()