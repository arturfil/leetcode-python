import re # regular expression module


class IsPalindrome:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        left, right = 0, len(s)-1

        while left <= right:
            if s[left] != s[right]:
                return False

        return True
