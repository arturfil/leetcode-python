class ValidParenthesis:
    # test2 = "([]){}"
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}","(":")","[":"]"}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                return False
        return len(stack) == 0
    
'''
    TESTING
    test = "(){}[]"
    test2 = "([]){}"
    test3 = "{)"
    vp = ValidParenthesis()
    print(vp.isValid(test2))

    EXPLANATION
    - Essentially here we are creating two datastructures:
    one hashmap (dictionary) and a stack (list, array, w/e)
    - With these we are going to put the valid parenthesis in the hashmap
    and we are going to use the list (array) as a stack.
    - Every time we see an oppening parenthesis (there has to be a pair), we
    place the reciprocal in the stack, when we encounter the actual closing one,
    we pop() the closing parenthesis from the stack.
    - If we repeat this process we should end up with an empty stack therefore,
    we return true if the stack's length is 0 otherwise false.
'''