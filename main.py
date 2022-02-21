# from Arrays import two_sum
from Arrays.longest_common_prefix import LongestPrefix
from Stacks.valid_parenthesis import ValidParenthesis

def main():
    test = "(){}[]"
    test2 = "([]){}"
    test3 = "{)"
    vp = ValidParenthesis()
    print(vp.isValid(test2))

if __name__ == "__main__":
    main()