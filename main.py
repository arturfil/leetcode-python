# from Arrays import two_sum
from HashMaps.roman_to_integer import RomanToInteger

def main():
    # test = "MCMXCIV"
    test = "LVIII"
    roman = RomanToInteger();
    print(roman.romanToInteger(test))

if __name__ == "__main__":
    main()