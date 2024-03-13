class LongestSubstringWithoutRepeatingChars:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            - Guess the algorithm? Seems like a sliding window
            - point at a character, loop through the string in that char and 
            check the lenght of the string until you find again the character
            len = max(max, end - start)
        '''
        seen = {}
        start, char_len = 0, 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1

            seen[s[i]] = i
            char_len = max(char_len, i - start + 1)

        return char_len
     
    def slidingWindow(self, s: str) -> int:
        ch_set = set()
        left, res = 0, 0

        for i in range(len(s)):
            while s[i] in ch_set:
                ch_set.remove(s[left])
                left += 1
                ch_set.add(s[i])
                res = max(res, i - left + 1)

        return res
