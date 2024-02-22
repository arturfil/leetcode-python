from typing import List

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}

        for string in strs:
            sorted_string = ''.join(sorted(string)) # sort 

            if sorted_string not in strs_table: # add to table if not sorted
                strs_table[sorted_string] = [] # add a new list if not there

            strs_table[sorted_string].append(string) # append sorted string and anagram string

        print([x for x in strs_table.values()])
        return [x for x in strs_table.values()] # return the list of values
