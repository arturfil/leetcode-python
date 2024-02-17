class LongestCommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        # Create 2D grid
        dp = [[0 for col in range(len2 + 1)] for row in range(len1 + 1)] # leave as is, it's easy to understand row and col

        for row in reversed(range(len1)):
            for col in reversed(range(len2)):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1]) # max from diagonal

        return dp[0][0] # return max wlen from table
