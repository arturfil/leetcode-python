from Arrays.product_of_array_except_self import ProductOfArrayExceptSelf
from Matrix.rotate_image import RotateImage
from flags import return_flags
from random_problem import choose_random

args = return_flags()

def main():
    choose_random(args.exclude, args.category)

if __name__ == "__main__":
    main()


