from collections import Counter
import collections 


class FirstUniqueChar:
    def firstUniqChar(self, s: str) -> int:
        map = collections.Counter(s)

        for i in range(len(s)):
            if map[s[i]] == 1:
                return i 

        return -1
    
