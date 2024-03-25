from typing import List

class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(brackets, left, right):
            if len(brackets) == 2 * n:
                res.append(brackets)

            # you have to add a left it still has n chars to be added
            if left > 0:                 
                recursion(brackets + "(", left - 1, right)

            # you have to add a right because there still are missing n adds
            if right > 0 and right > left: 
                recursion(brackets + ")", left, right - 1)

        recursion("", n, n)
        return res

