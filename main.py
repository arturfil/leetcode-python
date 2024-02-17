from Strings.longest_common_subsequence import LongestCommonSubsequence
from flags import return_flags

from random_problem import choose_random 

args = return_flags()

def main():

    # choose_random(args.exclude, args.category) 
    LCS = LongestCommonSubsequence()
    res = LCS.longestCommonSubsequence("abaabcra", "abca")
    print(res)

if __name__ == "__main__":
    main()


'''
    TODO:
        - Palindromic Substrings
        - LongestCommonSubsequence
        - RotateImage
        - MaxSubArray
'''
