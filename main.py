from Matrix.rotate_image import RotateImage
from flags import return_flags
from random_problem import choose_random

args = return_flags()

def main():
    # choose_random(args.exclude, args.category)
    matrix = [[1,2,3], [4,5,6], [7,8,9]]

    m = RotateImage()
    m.rotate(matrix)

    for i in range(len(matrix[0])):
        print(matrix[i])


if __name__ == "__main__":
    main()


