from typing import List

class VerifyingAlienDictionary:
    def isAlientSorted(self, words: List[str], order: str) -> bool:
        map = {}
        # map = {k : i for i, k in enumerate(order)}
        
        for i, val in enumerate(order):
            map[val] = i

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(w2): return False # if j >= the whole length of the word 2 return false

                if w1[j] != w2[j]:
                    if map[w2[j]] < map[w1[j]]: return False # this means not in order
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True
                        
