from Strings.longest_common_subsequence import LongestCommonSubsequence
from SystemsDesign.word_dictionary import WordDictionary
from flags import return_flags

from random_problem import choose_random 

args = return_flags()

def main():
    wd = WordDictionary()
    wd.addWord("cat")
    wd.addWord("hat")
    wd.addWord("bat")

    wd.addWord("doll")
    wd.addWord("matt")
    wd.addWord("crow")

    # wd.search("cat")
    wd.search("cats")

if __name__ == "__main__":
    main()


'''
    TODO:
        - Palindromic Substrings
        - LongestCommonSubsequence
        - RotateImage
        - MaxSubArray
'''
