class LongestCommonSubsequence:
    def length_of_longest_common_subs(self, s: str) -> int:
        chars = {}
        result = ""
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
            result += s[i]


'''
    testing
    lng_substring = LongestCommonSubstring()
    lng_substring.length_of_longest_subs("abcabcbb")
'''
