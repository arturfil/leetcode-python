from typing import List

class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(arr, left, right):
            if len(arr) == 2 * n:
               res.append(arr) 

            if left > 0:
                recursion(arr + "(", left-1, right)

            if right > 0 and right > left:
                recursion(arr + ")", left, right-1)

        recursion("", n, n)
        return res
