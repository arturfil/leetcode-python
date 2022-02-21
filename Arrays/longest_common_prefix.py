from typing import List

class LongestPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs:
            while not str.startswith(prefix):
                prefix = prefix[:-1]

        return prefix

'''
    TESTING
    test = ["flower", "florida", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["twenty one", "two"]
    lng = LongestPrefix()
    lng.longestCommonPrefix(test)

    EXPLANATION
    - You are running through each string of the array so hence the double loop
    - Each string you check that it matches the prefix, if it doesn't match,
    you cut the strings last character out.
    - Once it matches, you exit the while loop and move on to the next string
    - If all strings have a common prefix you would have cut enough characters out
    that you end up with the common prefix.
    - If there are non strings left means there NO common prefix

'''