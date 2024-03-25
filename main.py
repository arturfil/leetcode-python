from HashMaps.encode_decode_strings import Codec
from Strings.abbreviation import ValidWordAbbreviation
from flags import return_flags
from random_problem import choose_random

args = return_flags()

def main():
    # choose_random(args.exclude, args.category)
    c = Codec()
    # str = c.encode(["Hello", "World"])
    str = c.encode(["#"])
    print(str)

    dec = c.decode(str)
    print(dec)

if __name__ == "__main__":
    main()


