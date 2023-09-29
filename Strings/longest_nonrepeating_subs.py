class LongestNonRepeatingSubstring:
    def length_of_longest_subs(self, s: str) -> int:
            start, longest = 0, 0
            chars = {}

            for i in range(len(s)):
                if s[i] in chars and chars[i] >= start:
                    start = i + 1 
                longest = max(longest, i - start + 1)
                chars[s[i]] = i
                
            return longest
     
