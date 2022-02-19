
hashmap = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
class RomanToInteger:
    def romanToInteger(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i + 1]]:
                sum += hashmap[s[i + 1]] - hashmap[s[i]]
                i += 2
            else:
                sum += hashmap[s[i]]
                i += 1
            
        return sum

'''
    TESTING
    # test = "MCMXCIV"
    test = "LVIII"
    roman = RomanToInteger();
    print(roman.romanToInteger(test))

    EXPLANATION
    - You are going to iterate through the loop and in the case that 
    the string value is less than the next value i.e. IX -> 9, in roman
    you would add 10 then substract the one so it would fall in the first
    if case.
    - Since you account for two numbers you increment "i" by 2
'''
